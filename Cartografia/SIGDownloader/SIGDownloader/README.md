# SIGDownloader v0.4.0

Esta versão substitui integralmente a v0.3.2. Ela mantém os downloads
existentes e acrescenta um catálogo centralizado de fontes oficiais.

## Instalação

Substitua a pasta do programa:

```text
D:\LaTex_Projects\Cartografia\SIGDownloader
```

pela pasta contida neste pacote.

**Não apague nem substitua**:

```text
D:\LaTex_Projects\Cartografia\SIG_BRASIL
```

O programa reconhece os arquivos já baixados e migra pastas antigas
sem sobrescrever arquivos diferentes.

## Execução

Pelo Explorador do Windows, use `executar.bat`.

Pelo PowerShell:

```powershell
cd D:\LaTex_Projects\Cartografia\SIGDownloader
py .\main.py
```

## Dependências

```powershell
py -m pip install -r requirements.txt
```

## Novidades da versão 0.4.0

- catálogo central de fontes em JSON;
- menu para consultar e abrir fontes oficiais;
- geração automática da tabela LaTeX;
- catálogo local dos arquivos efetivamente instalados;
- descoberta dinâmica da versão mais recente das malhas IBGE;
- descoberta dinâmica da BC250, incluindo as grafias `geopackage`
  e `geopakage`;
- descoberta dinâmica da pasta anual de estimativas populacionais;
- correção da pasta canônica do SIGMINE para `04_ANM/SIGMINE`;
- migração segura dos diretórios usados por versões anteriores;
- arquivos diferentes com o mesmo nome recebem sufixo numerado,
  sem perda de dados.

## Estrutura do repositório

```text
SIG_BRASIL/
├── 01_IBGE/
│   └── Malhas/
├── 02_IBGE_BC250/
├── 03_IBGE_POPULACAO/
├── 04_ANM/
│   └── SIGMINE/
├── 05_SGB/
│   └── Geologia/
├── 06_OCEANOGRAFIA/
│   ├── GEBCO/
│   └── Copernicus/
└── Documentacao/
```

## Observações

SGB, GEBCO e Copernicus não possuem sempre um único link estático
aplicável a qualquer área e período. Nesses casos, o programa cria
instruções ou comandos auxiliares e mantém a fonte oficial registrada.
