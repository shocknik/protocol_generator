from .base_section import BaseSection
from app.document_builder.table_builder import TableBuilder

class TestResultsSection(BaseSection):
    """Раздел с результатами испытаний"""
    
    def build(self):
        self.logger.info("Начало формировани раздела 'Результаты испытаний'")
        
        self._add_heading("4 Результаты испытаний на соответствие техническим требованиям\
            представлены в таблице 2", level=1)
        
        