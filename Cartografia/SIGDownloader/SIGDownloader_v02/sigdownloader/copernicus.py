import shutil,subprocess,sys
from .util import arquivo_valido,registro

def executar(repo,lg,cfg):
 p=repo/'06_COPERNICUS';p.mkdir(parents=True,exist_ok=True)
 itens=[('Copernicus — correntes','cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m',['uo','vo'],p/'correntes_superficie_2025.nc'),('Copernicus — temperatura','cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m',['thetao'],p/'temperatura_superficie_2025.nc')]
 cmds=[];regs=[]
 for nome,ds,vars,d in itens:
  vv=' '.join('--variable '+v for v in vars)
  cmd=f'copernicusmarine subset --dataset-id "{ds}" {vv} --minimum-longitude {cfg.OESTE} --maximum-longitude {cfg.LESTE} --minimum-latitude {cfg.SUL} --maximum-latitude {cfg.NORTE} --start-datetime "{cfg.DATA_INICIAL}T00:00:00" --end-datetime "{cfg.DATA_FINAL}T23:59:59" --minimum-depth {cfg.PROFUNDIDADE_MIN} --maximum-depth {cfg.PROFUNDIDADE_MAX} --output-directory "{p}" --output-filename "{d.name}" --overwrite';cmds.append(cmd)
  pode=cfg.EXECUTAR_COPERNICUS and (3,10)<=sys.version_info[:2]<=(3,13) and shutil.which('copernicusmarine')
  if arquivo_valido(d):st='concluído'
  elif pode:st='concluído' if subprocess.run(cmd,shell=True).returncode==0 and arquivo_valido(d) else 'falhou'
  else:st='preparado'
  regs.append(registro(nome,st,d,observacao='requer login e Python 3.10–3.13' if st=='preparado' else ''))
 (p/'comandos_copernicus.txt').write_text('\n\n'.join(cmds)+'\n',encoding='utf-8')
 (p/'LEIA-ME.txt').write_text('Instale em Python 3.13: py -3.13 -m pip install copernicusmarine\nFaça: copernicusmarine login\nExecute comandos_copernicus.txt ou ative EXECUTAR_COPERNICUS.\n',encoding='utf-8')
 return regs
