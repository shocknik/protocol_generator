import os
from pathlib import Path

# Базовые пути
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
LOGS_DIR = BASE_DIR / "logs"

# Создаём директории если их нет
for directory in [DATA_DIR, OUTPUT_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Конфигурационные пути
JSON_PATH = DATA_DIR / "protocol_data.json"
LOG_PATH = LOGS_DIR / "app.log"

# Текстовые константы
TEST_CENTER = "ООО «НИЦ «Кабель-Тест»"
TEST_CENTER_ADDRESS = "107497, г. Москва, ул. Бирюсинка, д. 6, корп. 1-5, 6, 7, 9А"
CERTIFICATION_TEXT = "Руководитель испытательного центра"
TEST_TYPES = {
    "certification": "сертификационных испытаний",
    "acceptance": "приёмочных испытаний",
    "periodic": "периодических испытаний"
}

class TestType:
    certif_test = TEST_TYPES["certification"]
    accept_test = TEST_TYPES["acceptance"]
    periodic_test = TEST_TYPES["periodic"]