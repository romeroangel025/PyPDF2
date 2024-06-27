import argparse
from LectorPDF import LectorPDF
from EscritorPDF import EscritorPDF

def extraer_texto(ruta_entrada, ruta_salida):
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

    # Opcional: Guardar el texto extraído en un archivo de texto
    with open(ruta_salida, "w", encoding="utf-8") as archivo_texto:
        archivo_texto.write(texto_completo)

def unir_pdfs(rutas_entrada, ruta_salida):
    escritor_pdf = EscritorPDF(ruta_salida)
    
    for ruta in rutas_entrada:
        lector_pdf = LectorPDF(ruta)
        lector_pdf.abrir()
        
        for i in range(lector_pdf.obtener_numero_paginas()):
            pagina = lector_pdf.obtener_pagina(i)
            if pagina:
                escritor_pdf.agregar_pagina(pagina)
    
    escritor_pdf.guardar(ruta_salida)

def main():
    parser = argparse.ArgumentParser(description="Procesar archivos PDF.")
    parser.add_argument("accion", choices=["extraer_texto", "unir_pdfs"], help="Acción a realizar: extraer_texto o unir_pdfs.")
    parser.add_argument("entradas", nargs='+', help="Rutas de los archivos PDF de entrada.")
    parser.add_argument("salida", help="Ruta del archivo de salida.")
    args = parser.parse_args()

    if args.accion == "extraer_texto":
        if len(args.entradas) != 1:
            print("Para extraer texto, proporciona una sola ruta de entrada.")
            return
        extraer_texto(args.entradas[0], args.salida)
    elif args.accion == "unir_pdfs":
        unir_pdfs(args.entradas, args.salida)

if __name__ == "__main__":
    main()

