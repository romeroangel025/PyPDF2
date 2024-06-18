import PyPDF2

class DocumentoPDF:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.lector = None

    def abrir(self):
        try:
            with open(self.ruta_archivo, 'rb') as archivo:
                self.lector = PyPDF2.PdfFileReader(archivo)
            print(f"Archivo PDF abierto: {self.ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    def obtener_numero_paginas(self):
        if self.lector:
            return self.lector.numPages
        else:
            return 0

    def obtener_pagina(self, numero_pagina):
        if self.lector and 0 <= numero_pagina < self.obtener_numero_paginas():
            return self.lector.getPage(numero_pagina)
        else:
            return None
