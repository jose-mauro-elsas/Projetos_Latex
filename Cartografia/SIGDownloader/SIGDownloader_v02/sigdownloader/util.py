import csv, hashlib, logging, time, zipfile
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
AGENTE='SIGDownloader/0.2'; TIMEOUT=(30,180); CHUNK=1024*1024

def criar_logger(repo):
    repo.mkdir(parents=True, exist_ok=True); lg=logging.getLogger('sigdownloader'); lg.setLevel(logging.INFO)
    if not lg.handlers:
        fh=logging.FileHandler(repo/'sigdownloader.log',encoding='utf-8'); fh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        sh=logging.StreamHandler(); sh.setFormatter(logging.Formatter('%(message)s')); lg.addHandler(fh); lg.addHandler(sh)
    return lg

def sha256(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(CHUNK),b''): h.update(b)
    return h.hexdigest()

def arquivo_valido(p):
    if not p.exists() or p.stat().st_size<1000:return False
    if p.suffix.lower()=='.zip':
        try:
            with zipfile.ZipFile(p) as z:return z.testzip() is None and bool(z.namelist())
        except zipfile.BadZipFile:return False
    return True

def baixar(url,destino,logger,tentativas=2):
    destino.parent.mkdir(parents=True,exist_ok=True)
    if arquivo_valido(destino):logger.info(f'JÁ EXISTE: {destino}');return True
    parcial=destino.with_suffix(destino.suffix+'.part')
    for n in range(1,tentativas+1):
        logger.info(f'{destino.name} — tentativa {n}/{tentativas}')
        try:
            inicio=parcial.stat().st_size if parcial.exists() else 0; h={'User-Agent':AGENTE}
            if inicio:h['Range']=f'bytes={inicio}-'
            with requests.get(url,stream=True,timeout=TIMEOUT,headers=h,allow_redirects=True) as r:
                r.raise_for_status(); modo='ab' if inicio and r.status_code==206 else 'wb'
                with parcial.open(modo) as f:
                    for b in r.iter_content(CHUNK):
                        if b:f.write(b)
            parcial.replace(destino)
            if not arquivo_valido(destino):raise RuntimeError('arquivo falhou na validação')
            logger.info(f'CONCLUÍDO: {destino}');return True
        except Exception as e:
            logger.warning(f'FALHA: {e}'); destino.unlink(missing_ok=True)
            if n<tentativas:time.sleep(5)
    return False

def links_da_pagina(url):
    r=requests.get(url,timeout=TIMEOUT,headers={'User-Agent':AGENTE});r.raise_for_status();s=BeautifulSoup(r.text,'html.parser')
    return [(' '.join(a.get_text(' ',strip=True).split()),urljoin(r.url,a['href'])) for a in s.find_all('a',href=True)]

def registro(item,status,caminho=None,url='',observacao=''):
    return {'item':item,'status':status,'arquivo':str(caminho) if caminho else '', 'url':url or '', 'tamanho_bytes':caminho.stat().st_size if caminho and caminho.exists() else '', 'sha256':sha256(caminho) if caminho and arquivo_valido(caminho) else '', 'observacao':observacao}

def registrar_csv(repo,linhas):
    campos=['item','status','arquivo','url','tamanho_bytes','sha256','observacao']
    with (repo/'catalogo_downloads.csv').open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=campos,delimiter=';');w.writeheader();w.writerows(linhas)
