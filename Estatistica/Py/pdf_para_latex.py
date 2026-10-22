import PyPDF2
import io

def extrair_texto_pdf(caminho_pdf):
    """
    Extrai o texto de um arquivo PDF.

    Args:
        caminho_pdf: Caminho para o arquivo PDF.

    Returns:
        Uma string contendo o texto extraído do PDF.
    """

    texto = ""
    try:
        with open(caminho_pdf, 'rb') as arquivo_pdf:
            leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
            for num_pagina in range(len(leitor_pdf.pages)):
                pagina = leitor_pdf.pages[num_pagina]
                texto += pagina.extract_text()
    except Exception as e:
        print(f"Erro ao extrair texto do PDF: {e}")
        return None
    return texto


def gerar_latex(texto, caminho_latex):
    """
    Gera um arquivo LaTeX com o texto extraído.
    Garante que o arquivo seja salvo em UTF-8 sem BOM.

    Args:
        texto: O texto a ser inserido no arquivo LaTeX.
        caminho_latex: Caminho para o arquivo LaTeX de saída.
    """
    try:
        with open(caminho_latex, 'w', encoding='utf-8') as arquivo_latex:
            arquivo_latex.write(texto)
        print(f"Arquivo LaTeX gerado com sucesso em: {caminho_latex}")
    except Exception as e:
        print(f"Erro ao gerar arquivo LaTeX: {e}")


if __name__ == "__main__":
    caminho_pdf = "C:\LaTex_Projects\Estatistica\Páginas de 2. Separatrizes.pdf"  # Substitua pelo caminho do seu arquivo PDF
    caminho_latex = "C:\LaTex_Projects\Estatistica\Box.tex"  # Substitua pelo caminho desejado para o arquivo LaTeX

    texto_extraido = extrair_texto_pdf(caminho_pdf)

    if texto_extraido:
        gerar_latex(texto_extraido, caminho_latex)
