import argparse
from LectorPDF import LectorPDF
from EscritorPDF import EscritorPDF

def main(ruta_entrada, ruta_salida):
    # Leer PDF
    lector_pdf = LectorPDF(ruta_entrada)
    lector_pdf.abrir()
    num_paginas = lector_pdf.obtener_numero_paginas()
    print(f"Número de páginas: {num_paginas}")

    # Extraer texto de todas las páginas
    texto_completo = ""
    for i in range(num_paginas):
        texto = lector_pdf.extraer_texto(i)
        print(f"Texto de la página {i + 1}: {texto}")
        texto_completo += texto + "\n"

    # Escribir PDF
    escritor_pdf = EscritorPDF(ruta_salida)
    for i in range(num_paginas):
        pagina = lector_pdf.obtener_pagina(i)
        if pagina:
            escritor_pdf.agregar_pagina(pagina)
    escritor_pdf.guardar(ruta_salida)

   # En este archivo se guarda el texto 
    with open("texto_extraido.txt", "w", encoding="utf-8") as archivo_texto:
        archivo_texto.write(texto_completo)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesar archivos PDF.")
    parser.add_argument("entrada", help="Ruta del archivo PDF de entrada.")
    parser.add_argument("salida", help="Ruta del archivo PDF de salida.")
    args = parser.parse_args()
    main(args.entrada, args.salida)

