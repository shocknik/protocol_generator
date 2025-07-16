from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from app.utils.logger import logger


class TableBuilder:
    '''Класс для построения и форматирования таблиц'''
    
    def __init__(self, document: Document, rows: int, cols:int):
        """Инициализация построения таблиц

        Args:
            document (Document): Объект документа Word
            rows (int): Количество строк
            cols (int): Количество колонок
        """
        self.document = document
        self.table = document.add_table(rows=rows, cols=cols)
        self.logger = logger.bind(component="TableBuilder")
        self.logger.debug(f"Создана таблица {rows}x{cols}")
        
    def add_header_row(self, headers: list):
        """Добавляет строку с заголовками"""
        if len(headers) !=len(self.table.columns):
            self.logger.warning(
                f'Количество заголовков ({len(headers)}) не соответствует'
                f'количеству колонок ({len(self.table.columns)})'
            )
            
        header_row = self.table.rows[0]
        for i, header in enumerate(headers):
            cell = header_row.cells[i]
            cell.text = header
            
    def add_row(self, data: list, row_index: int):
        """Добавляет строку данных в таблицу

        Args:
            data (list): список значений для каждой ячейки
            row_index (int): Индекс строки (начинается с 0)
        """
        if row_index >= len(self.table.rows):
            self.logger.error(f'Недопустимый индекс строки: {row_index}')
            return
        
        row = self.table.rows[row_index]
        for i, value in enumerate(data):
            if i < len(row.cells):
                row.cells[i].text = str(value)
                
        def apply_styles(self, style: str = "Table Grid"):
            """Применяет стили к таблице"""
            self.logger.debug("Примение стилей к таблице")
            # Применяем стиль
            self.table.style = style
            
            # Выравниевание текста в ячейках
            for row in self.table.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                        
            # Автоподбор ширины колонок
            self.table.autofit= True
            
        def set_column_width(self, column_index: int, width: Cm):
            """Устанавливаем ширину колонки в сантиметрах"""
            if column_index < len(self.table.columns):
                self.table.columns[column_index].width = Cm(width)
                
        def merge_cells(self,
                        start_row: int,
                        start_col: int,
                        end_row: int,
                        end_col: int):
            """Объединяет ячейки в указаном диапазоне"""
            self.logger.debug(f"Объединение ячеек: ({start_row}, {start_col})-({end_row}, {end_col})")
            cell = self.table.cell(start_row, start_col)
            other_cell = self.table.cell(end_row, end_col)
            cell.merge(other_cell)