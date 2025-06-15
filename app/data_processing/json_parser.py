import json
from core.models import ProtocolData
from core.exceptions import InvalidJSONError

def load_json_data(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise InvalidJSONError(
            message = "Ошибка при загрузке JSON-файла",
            file_path = file_path,
            original_exception = e
        )
    
def parse_protocol_data(json_data: dict) -> ProtocolData:
    try:
        # Основные разделы протокола
        primary = json_data['PRIMARY']
        
        # Собираем данные по входному json-файлу
        parsed_data = {
            "primary": primary,
            "test_basis": json_data["2"]["Основание для проведения испытаний"],
            "customer": json_data["3"]["Информация о заказчике"],
            "manufacturer": json_data["4"]["Информация об изготовителе"],
            "test_object": json_data["5"]["Информация об объекте испытаний"],
            "test_dates": json_data["6"]["Даты проведения испытаний"],
            "test_purpose": json_data["7"]["Цель испытаний"],
            "environment": json_data["8"]["Условия окружающей среды при проведении испытаний"],
            "test_methods": json_data["9"]["Методы испытаний"],
            "equipment": json_data["11"]["Перечень применяемого испытательного оборудования и средств измерений"],
            "test_results": json_data["10"]["Результаты испытаний"],
            "performed_by": json_data["12"]["Испытания провели"],
        }
        
        return ProtocolData(**parsed_data)

    except ValueError as e:
        raise InvalidJSONError(
            message="Ошибка преобразования данных",
            original_exception=e
        )
        
    except Exception as e:
        raise InvalidJSONError(
            message="Отсутствует обязательный ключ в JSON",
            original_exception=e
        )