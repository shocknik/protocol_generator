from datetime import datetime
from data_processing.json_parser import parse_protocol_data, load_json_data
from utils.logger import logger
import pandas


class ProtocolService:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.protocol_data = None
        
    def load_data(self):
        logger.info("Загрузка данных для протокола из JSON файла")
        self.protocol_data = parse_protocol_data(load_json_data(self.json_path))
        logger.success("Данный для протокола успешно загружены")
    
    def generate_protocol(self, output_path: str):
        pass
    
    def get_test_results_summary(self) -> dict:
        """Анализ результов испытание на соответствие(не соответствие)"""
        summary = {}
        return summary