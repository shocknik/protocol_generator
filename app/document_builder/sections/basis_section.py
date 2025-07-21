from .base_section import BaseSection

class BasisSection(BaseSection):
    '''Раздел с основанием для проведения испытаний'''
    
    def build(self):
        self.logger.info("Формирование раздела 'Основание для испытаний'")
        self._add_heading("1 Основание для проведения исытаний", level=1)
        '''Текст основания'''
        basis_text = (
            f'{self.protocol_data.test_basis}'
        )
        self._add_paragraph(basis_text)
        self.logger.debug("Раздел для основания испытаний завершен")