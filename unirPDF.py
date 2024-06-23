import argparse
from LectorPDF import LectorPDF
from EscritorPDF import EscritorPDF

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unir múltiples archivos PDF en uno solo.")
    parser.add_argument("entradas", nargs='+', help="Rutas de los archivos PDF de entrada.")
    parser.add_argument("salida", help="Ruta del archivo PDF de salida.")
    args = parser.parse_args()
    
    unir_pdfs(args.entradas, args.salida)
