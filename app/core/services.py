from datetime import datetime
from app.data_processing.json_parser import parse_protocol_data, load_json_data
from app.utils.logger import logger
from app.document_builder.docx_handler import DocumentGeneration



class ProtocolService:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.protocol_data = None
        
    def load_data(self):
        logger.info("Загрузка данных для протокола из JSON файла")
        self.protocol_data = parse_protocol_data(load_json_data(self.json_path))
        logger.success("Данный для протокола успешно загружены")
    
    def generate_protocol(self, output_path: str):
        if not self.protocol_data:
            self.load_data()
        logger.info("Начинаю генерить протокол")
        doc_generator = DocumentGeneration(self.protocol_data)
        doc_generator.generate_document(output_path)
        logger.success(f"Протокол успешно создан: {output_path}")
        
    
    def get_test_results_summary(self) -> dict:
        """Анализ результов испытание на соответствие(не соответствие)"""
        summary = {}
        return summary