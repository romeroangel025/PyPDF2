from PyPDF2 import PdfReader, PdfWriter

class DivisorPDF:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.lector = PdfReader(ruta_archivo)

    def dividir_por_paginas(self, paginas_por_archivo):
        total_paginas = len(self.lector.pages)
        for i in range(0, total_paginas, paginas_por_archivo):
            escritor = PdfWriter()
            for j in range(i, min(i + paginas_por_archivo, total_paginas)):
                escritor.add_page(self.lector.pages[j])
            self.guardar(escritor, f"output_{i//paginas_por_archivo + 1}.pdf")

    def guardar(self, escritor, ruta_salida):
        try:
            with open(ruta_salida, 'wb') as archivo_salida:
                escritor.write(archivo_salida)
            print(f"Archivo PDF guardado: {ruta_salida}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python Divisor.py <ruta_al_archivo_pdf> <paginas_por_archivo>")
    else:
        ruta_archivo = sys.argv[1]
        paginas_por_archivo = int(sys.argv[2])
        divisor = DivisorPDF(ruta_archivo)
        divisor.dividir_por_paginas(paginas_por_archivo)



