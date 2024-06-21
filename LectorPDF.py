from DocumentoPDF import DocumentoPDF

class LectorPDF(DocumentoPDF):
    def extraer_texto(self, numero_pagina):
        pagina = self.obtener_pagina(numero_pagina)
        if pagina:
            return pagina.extract_text()
        else:
            return ""
