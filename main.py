import argparse
from LectorPDF import LectorPDF
from EscritorPDF import EscritorPDF

def main(ruta_entrada, ruta_salida):
    # Leer PDF
    lector_pdf = LectorPDF(ruta_entrada)
    lector_pdf.abrir()
    num_paginas = lector_pdf.obtener_numero_paginas()
    print(f"Número de páginas: {num_paginas}")
    texto = lector_pdf.extraer_texto(0)# aca se elije que pagina queres obtener 
    print(f"Texto de la primera página: {texto}")

    # Escribir PDF
    escritor_pdf = EscritorPDF(ruta_salida)
    primera_pagina = lector_pdf.obtener_pagina(0)
    if primera_pagina:
        escritor_pdf.agregar_pagina(primera_pagina)
    escritor_pdf.guardar(ruta_salida)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesar archivos PDF.")
    parser.add_argument("entrada", help="Ruta del archivo PDF de entrada.")
    parser.add_argument("salida", help="Ruta del archivo PDF de salida.")
    args = parser.parse_args()
    main(args.entrada, args.salida)

