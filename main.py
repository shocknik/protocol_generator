import sys
from app.core.services import ProtocolService
from config import JSON_PATH, OUTPUT_DIR

def main():
    # Используем путь из аргументов или конфига
    json_path = sys.argv[1] if len(sys.argv) > 1 else JSON_PATH
    
    service = ProtocolService(json_path)
    service.load_data()
    
    # Создаем имя файла
    output_file = OUTPUT_DIR / f"Протокол_{service.protocol_data.test_object.brand}.docx"
    
    service.generate_protocol(output_file)
    print(f"Протокол успешно сгенерирован: {output_file}")

if __name__ == "__main__":
    main()