from .base_section import BaseSection

class TestMethod(BaseSection):
    """Раздел для списка методов испытаний"""
    
    def build(self):
        self.logger.info("Формирование раздела с применяемыми методами")
        self._add_heading("7 Методы испытаний", level=1)
        "Текст с методами"
        test_methods = self.protocol_data.test_methods
        self._add_paragraph("Методы испытаний в соответсвтии с требованиями:")  # доработать после доработки модели
        for standart in test_methods.items():
            txt = f'{standart[0]} {standart[1]}'
            self._add_paragraph(txt, 'List Paragraph')
            
            