from LectorPDF import LectorPDF
from EscritorPDF import EscritorPDF
from DivisorPDF import DivisorPDF
import argparse

def extraer_texto(ruta_entrada, ruta_salida):
    lector_pdf = LectorPDF(ruta_entrada)
    lector_pdf.abrir()
    num_paginas = lector_pdf.obtener_numero_paginas()
    print(f"Número de páginas: {num_paginas}")

    texto_completo = ""
    for i in range(num_paginas):
        texto = lector_pdf.extraer_texto(i)
        print(f"Texto de la página {i + 1}: {texto}")
        texto_completo += texto + "\n"

    with open(ruta_salida, "w", encoding="utf-8") as archivo_texto:
        archivo_texto.write(texto_completo)

    lector_pdf.cerrar()  # Llamar al método cerrar() al finalizar

def unir_pdfs(rutas_entrada, ruta_salida):
    escritor_pdf = EscritorPDF(ruta_salida)
    
    total_archivos = len(rutas_entrada)
    print(f"Unir {total_archivos} archivos PDF")

    for idx, ruta in enumerate(rutas_entrada):
        print(f"Procesando archivo {idx + 1} de {total_archivos}: {ruta}")
        lector_pdf = LectorPDF(ruta)
        lector_pdf.abrir()
        
        for i in range(lector_pdf.obtener_numero_paginas()):
            pagina = lector_pdf.obtener_pagina(i)
            if pagina:
                escritor_pdf.agregar_pagina(pagina)
        
        lector_pdf.cerrar()  # Cerrar el lector después de procesar el archivo
    
    escritor_pdf.guardar(ruta_salida)  # Llama a guardar con la ruta_salida
    print(f"Archivo PDF unido guardado como {ruta_salida}")

def dividir_pdf(ruta_entrada):
    divisor_pdf = DivisorPDF(ruta_entrada)
    divisor_pdf.dividir_pagina_por_pagina()
def main():
    parser = argparse.ArgumentParser(description="Procesar archivos PDF.")
    parser.add_argument("accion", choices=["extraer_texto", "unir_pdfs", "dividir_pdf"], help="Acción a realizar: extraer_texto, unir_pdfs o dividir_pdf.")
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
    elif args.accion == "dividir_pdf":
        if len(args.entradas) != 1:
            print("Para dividir un PDF, proporciona una sola ruta de entrada.")
            return
        dividir_pdf(args.entradas[0])

if __name__ == "__main__":
    main()

