# SIGDownloader v0.2

Esta versão mantém o foco exclusivamente na aquisição dos arquivos.

## Atualização
Copie o conteúdo deste ZIP para a pasta do projeto anterior. A pasta `SIG_BRASIL` existente será reutilizada e os arquivos válidos serão ignorados.

## Execução
```powershell
py -m pip install -r requirements.txt
py .\main.py
```

## Observações
- População municipal: descoberta automática na página oficial do IBGE.
- SGB: tentativa automática; se o portal não expuser o ZIP, será criado `LEIA-ME.txt`.
- GEBCO: o recorte oficial de 2026 usa aplicação dinâmica; o programa evita baixar o grid global de vários GB e cria a instrução do recorte.
- Copernicus: gera comandos para correntes (`uo`, `vo`) e temperatura (`thetao`). Em julho de 2026, o Toolbox oficial suporta Python 3.10–3.13; use Python 3.13 e faça `copernicusmarine login`.
