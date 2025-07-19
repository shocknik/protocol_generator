from datetime import datetime
from .base_section import BaseSection

class SignaturesSection(BaseSection):
    """Раздел с подписями в конце"""
    
    def build(self):
        self.logger.info("Формирование раздела 'Подписи'")
        
        # Информация об исполнителях
        performers = self.protocol_data.performed_by
        self._add_paragraph(f"Испытания провели: {performers}")
        # Создаем таблицу для подписей
        table = self._add_table(rows = 2, cols= len(performers.split(',')) + 1)
        # Заполняем таблицу для подписей
        self._fill_signatures_table(table, performers)
        self.logger.debug('Раздел "Подписи" завершен')
        
    def _fill_signatures_table(self, table, performers):
        '''Заполняет таблицу подписей'''
        header_row = table.rows[0]
        header_row.cells[0].text = 'Должность'
        performers_list = performers.split(',')
        for i, performer in enumerate(performers_list, start=1):
            header_row.cells[i].text = performer.strip()
        # Строка подписей
        signature_row = table.rows[1]
        signature_row.cells[0].text = 'Подпись'
        
        for i in range(1, len(performers_list) + 1):
            signature_row.cells[i].text = '____________________'
        
        
        