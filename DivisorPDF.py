from PyPDF2 import PdfReader, PdfWriter

class DivisorPDF:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.lector = PdfReader(ruta_archivo)

    def dividir_pagina_por_pagina(self):
        total_paginas = len(self.lector.pages)
        for i in range(total_paginas):
            escritor = PdfWriter()
            escritor.add_page(self.lector.pages[i])
            self.guardar(escritor, f"output_page_{i + 1}.pdf")

    def guardar(self, escritor, ruta_salida):
        try:
            with open(ruta_salida, 'wb') as archivo_salida:
                escritor.write(archivo_salida)
            print(f"Archivo PDF guardado: {ruta_salida}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")




