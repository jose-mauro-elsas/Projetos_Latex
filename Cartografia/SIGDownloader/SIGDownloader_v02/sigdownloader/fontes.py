from .util import baixar,links_da_pagina,registro
IBGE=[
('Limite do Brasil','https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR/BR_Pais_2025.zip','01_IBGE/Malhas/BR_Pais.zip'),
('Unidades da Federação','https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR/BR_UF_2025.zip','01_IBGE/Malhas/BR_UF.zip'),
('Municípios do Brasil','https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR/BR_Municipios_2025.zip','01_IBGE/Malhas/BR_Municipios.zip')]
BC250='https://geoftp.ibge.gov.br/cartas_e_mapas/bases_cartograficas_continuas/bc250/versao2025/geopackage/'
POP='https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html'
SGB='https://geosgb.sgb.gov.br/downloads/'

def basicos(repo,lg):
 r=[]
 for n,u,p in IBGE:
  d=repo/p;ok=baixar(u,d,lg);r.append(registro(n,'concluído' if ok else 'falhou',d,u))
 return r

def bc250(repo,lg):
 d=repo/'02_IBGE_BC250/BC250_2025_GPKG.zip'
 try:
  c=[u for t,u in links_da_pagina(BC250) if u.lower().endswith('.zip') and 'gpkg' in u.lower()]
  u=c[-1];ok=baixar(u,d,lg);return registro('BC250 nacional','concluído' if ok else 'falhou',d,u)
 except Exception as e:return registro('BC250 nacional','falhou',d,observacao=str(e))

def populacao(repo,lg,override=None):
 d=repo/'01_IBGE/Populacao/estimativas_populacao_municipios_2025.xls'
 try:
  u=override
  if not u:
   c=[u for t,u in links_da_pagina(POP) if ('2025' in (t+' '+u)) and u.lower().split('?')[0].endswith(('.xls','.xlsx'))]
   if not c:c=[u for t,u in links_da_pagina(POP) if u.lower().split('?')[0].endswith(('.xls','.xlsx'))]
   u=c[-1]; d=d.with_suffix('.xlsx' if '.xlsx' in u.lower().split('?')[0] else '.xls')
  ok=baixar(u,d,lg);return registro('População municipal 2025','concluído' if ok else 'falhou',d,u)
 except Exception as e:return registro('População municipal 2025','falhou',d,observacao=str(e))

def sgb(repo,lg,override=None):
 d=repo/'04_SGB/Geologia/Mapa_Geologico_Brasil_SGB.zip'
 try:
  u=override
  if not u:
   c=[]
   for t,x in links_da_pagina(SGB):
    a=(t+' '+x).lower()
    if x.lower().split('?')[0].endswith('.zip') and any(k in a for k in ('brasil','litoestr','integr')):c.append(x)
   if not c:raise RuntimeError('link direto não exposto pelo GeoSGB')
   u=c[-1]
  ok=baixar(u,d,lg);return registro('Mapa geológico do Brasil','concluído' if ok else 'falhou',d,u)
 except Exception as e:
  d.parent.mkdir(parents=True,exist_ok=True);(d.parent/'LEIA-ME.txt').write_text('Abra https://geosgb.sgb.gov.br/downloads/ > Integração Geológica Regional > Brasil. Copie a URL do ZIP para URL_SGB em config.py.\n',encoding='utf-8')
  return registro('Mapa geológico do Brasil','pendente',d,observacao=str(e))

def gebco(repo,lg,override=None):
 d=repo/'05_GEBCO/GEBCO_2026_Brasil.nc';d.parent.mkdir(parents=True,exist_ok=True)
 if override:
  ok=baixar(override,d,lg);return registro('GEBCO 2026','concluído' if ok else 'falhou',d,override)
 (d.parent/'LEIA-ME.txt').write_text('Use https://download.gebco.net/\nGEBCO_2026, NetCDF, Oeste -54, Leste -38, Sul -30, Norte -17.\nDepois cole a URL direta em URL_GEBCO no config.py.\n',encoding='utf-8')
 return registro('GEBCO 2026','aguarda recorte',d,'https://download.gebco.net/','aplicação oficial dinâmica; grid global não baixado')
