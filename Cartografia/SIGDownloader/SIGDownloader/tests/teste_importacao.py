from sigdownloader import __version__
from sigdownloader.fontes import carregar_fontes


def main() -> None:
    assert __version__ == "0.4.0"
    catalogo = carregar_fontes()
    assert catalogo.get("fontes")
    print("SIGDownloader v0.4.0")
    print(f"Fontes cadastradas: {len(catalogo['fontes'])}")
    print("Teste de importação: OK")


if __name__ == "__main__":
    main()
