from PyPDF2 import PdfReader

class DocumentoPDF:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.lector = None

    def abrir(self):
        try:
            self.lector = PdfReader(self.ruta_archivo)
            print(f"Archivo PDF abierto: {self.ruta_archivo}")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")

    def obtener_numero_paginas(self):
        if self.lector:
            return len(self.lector.pages)
        else:
            return 0

    def obtener_pagina(self, numero_pagina):
        if self.lector and 0 <= numero_pagina < self.obtener_numero_paginas():
            return self.lector.pages[numero_pagina]
        else:
            return None
        
    def cerrar(self):
        if self.lector:
            self.lector.stream.close()
            print(f"Archivo PDF cerrado: {self.ruta_archivo}")
    