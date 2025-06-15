from typing import Optional, Type
class InvalidJSONError(Exception):
    def __init__(self,
                 message: str,
                 file_path: Optional[str] = None,
                 original_exception: Optional[Exception] = None):
        """_summary_

        Args:
            message (str): Человекочитаемое сообщение об ошибке
            file_path (str, optional): Путь к файлу, вызвавшему ошибку (опционально)
            original_exception (Exception, optional): Оригинальное исключение (опционально)
        """
        self.message = message
        self.file_path = file_path
        self.original_exception = original_exception
        
        # Формирование сообщения об ошибке
        full_message = f"JSON Error: {message}"
        if file_path:
            full_message +=f" | File: {file_path}"
        if original_exception:
            full_message += f" | Original exception: {type(original_exception).__name__}: {str(original_exception)}"\
                
        super().__init__(full_message)
        
    def __str__(self) -> str:
        return self.message

        
        