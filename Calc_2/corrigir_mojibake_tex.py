from pathlib import Path
import argparse
import shutil


MOJIBAKE_MAP = {
    "Ã¡": "á",
    "Ã ": "à",
    "Ã¢": "â",
    "Ã£": "ã",
    "Ã¤": "ä",
    "Ã©": "é",
    "Ãª": "ê",
    "Ã­": "í",
    "Ã³": "ó",
    "Ã´": "ô",
    "Ãµ": "õ",
    "Ãº": "ú",
    "Ã¼": "ü",
    "Ã§": "ç",
    "Ã": "Á",
    "Ã€": "À",
    "Ã‚": "Â",
    "Ãƒ": "Ã",
    "Ã‰": "É",
    "ÃŠ": "Ê",
    "Ã": "Í",
    "Ã“": "Ó",
    "Ã”": "Ô",
    "Ã•": "Õ",
    "Ãš": "Ú",
    "Ã‡": "Ç",

    "Âº": "º",
    "Âª": "ª",
    "Â°": "°",
    "Â´": "´",
    "Â¨": "¨",
    "Â ": " ",

    "â€“": "–",
    "â€”": "—",
    "â€˜": "‘",
    "â€™": "’",
    "â€œ": "“",
    "â€": "”",
    "â€¦": "…",
    "â€¢": "•",
}


def ler_texto(caminho: Path) -> str:
    """
    Tenta ler o arquivo com encodings comuns.
    """
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return caminho.read_text(encoding=enc)
        except UnicodeDecodeError:
            pass

    raise UnicodeDecodeError(
        "encoding",
        b"",
        0,
        1,
        f"Não consegui ler o arquivo {caminho}"
    )


def tentativa_reinterpretar(texto: str) -> str:
    """
    Corrige o caso clássico:
    UTF-8 foi interpretado como cp1252/latin-1.
    Exemplo: 'Ã§Ã£o' -> 'ção'
    """
    candidatos = []

    for enc_errado in ("cp1252", "latin-1"):
        try:
            corrigido = texto.encode(enc_errado).decode("utf-8")
            candidatos.append(corrigido)
        except UnicodeError:
            pass

    if not candidatos:
        return texto

    # Escolhe o candidato com menos sinais típicos de mojibake.
    def pontuacao(s: str) -> int:
        sinais_ruins = ["Ã", "Â", "â€", "�"]
        return sum(s.count(x) for x in sinais_ruins)

    return min(candidatos, key=pontuacao)


def aplicar_mapa(texto: str) -> str:
    """
    Faz substituições pontuais que sobram depois da reinterpretação.
    """
    anterior = None
    atual = texto

    # Repete algumas vezes porque às vezes há mojibake em camadas.
    for _ in range(3):
        if atual == anterior:
            break
        anterior = atual
        for ruim, bom in MOJIBAKE_MAP.items():
            atual = atual.replace(ruim, bom)

    return atual


def corrigir_mojibake(texto: str) -> str:
    texto = tentativa_reinterpretar(texto)
    texto = aplicar_mapa(texto)
    return texto


def contar_suspeitos(texto: str) -> dict:
    suspeitos = ["Ã", "Â", "â€", "�"]
    return {s: texto.count(s) for s in suspeitos if texto.count(s) > 0}


def corrigir_arquivo(caminho: Path, in_place: bool = False) -> Path:
    original = ler_texto(caminho)
    corrigido = corrigir_mojibake(original)

    print(f"Arquivo: {caminho}")
    print("Suspeitos antes :", contar_suspeitos(original))
    print("Suspeitos depois:", contar_suspeitos(corrigido))

    if corrigido == original:
        print("Nenhuma alteração necessária.")
        return caminho

    if in_place:
        backup = caminho.with_suffix(caminho.suffix + ".bak")
        shutil.copy2(caminho, backup)

        # UTF-8 sem BOM
        caminho.write_text(corrigido, encoding="utf-8", newline="")
        print(f"Arquivo corrigido no lugar.")
        print(f"Backup criado em: {backup}")
        return caminho

    saida = caminho.with_suffix(".corrigido" + caminho.suffix)

    # UTF-8 sem BOM
    saida.write_text(corrigido, encoding="utf-8", newline="")
    print(f"Arquivo corrigido salvo em: {saida}")
    return saida


def main():
    parser = argparse.ArgumentParser(
        description="Corrige mojibake comum em arquivos .tex."
    )
    parser.add_argument("arquivo", help="Caminho do arquivo .tex")
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Sobrescreve o arquivo original, criando .bak antes."
    )

    args = parser.parse_args()

    caminho = Path(args.arquivo)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if caminho.suffix.lower() != ".tex":
        print("Aviso: o arquivo não tem extensão .tex.")

    corrigir_arquivo(caminho, in_place=args.in_place)


if __name__ == "__main__":
    main()