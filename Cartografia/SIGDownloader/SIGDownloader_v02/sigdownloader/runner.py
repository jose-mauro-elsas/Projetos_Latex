from datetime import datetime
import config as cfg
from .util import criar_logger,registrar_csv
from .fontes import basicos,bc250,populacao,sgb,gebco
from .copernicus import executar as cop

def executar():
 repo=cfg.REPOSITORIO;lg=criar_logger(repo);lg.info('='*72);lg.info(f'SIGDownloader v0.2 — {datetime.now():%d/%m/%Y %H:%M:%S}');lg.info(f'Repositório: {repo}');lg.info('='*72)
 r=basicos(repo,lg);r.append(bc250(repo,lg));r.append(populacao(repo,lg,cfg.URL_POPULACAO));r.append(sgb(repo,lg,cfg.URL_SGB));r.append(gebco(repo,lg,cfg.URL_GEBCO));r.extend(cop(repo,lg,cfg));registrar_csv(repo,r)
 lg.info('-'*72);lg.info(f'Concluídos: {sum(x["status"]=="concluído" for x in r)}/{len(r)}');lg.info(f'Catálogo: {repo/"catalogo_downloads.csv"}')
