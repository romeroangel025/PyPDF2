from PyPDF2 import PdfWriter
from DocumentoPDF import DocumentoPDF

class EscritorPDF(DocumentoPDF):
    def __init__(self, ruta_archivo):
        super().__init__(ruta_archivo)
        self.escritor = PdfWriter()

    def agregar_pagina(self, pagina):
        self.escritor.add_page(pagina)

    def guardar(self, ruta_salida):
        try:
            with open(ruta_salida, 'wb') as archivo_salida:
                self.escritor.write(archivo_salida)
            print(f"Archivo PDF guardado: {ruta_salida}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
