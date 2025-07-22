from .base_section import BaseSection
from docx.shared import Cm, Inches

class EquipmentSection(BaseSection):
    '''Раздел с перечнем оболрудования'''
    
    def build(self):
        self.logger.info("Формирование раздела 'Оборудование'")
        self._add_heading("3 Перечень применяемого испытательного оборудования и средств измерений", level=1)
        
        '''Создаем таблицу с оборудованием'''
        equipment = self.protocol_data.equipment
        table = self._add_table(rows=len(equipment) + 1, cols=8)
        table.style = 'Table Grid'
        table.autofit = False
        
        # Добавляем заголовок таблицы
        headers = [
            "№ п.п",
            "Наименование",
            "Тип",
            "Модификация",
            "Инвентарный номер",
            "Диапазон измерений",
            "Точность",
            "Дата очередной поверки(аттестации)",
        ]
        header_row = table.rows[0]
        for i, header in enumerate(headers):
            header_row.cells[i].text = header
        # Заполняем таблицу данными об оборудовании
        for idx, (equip_id, equip) in enumerate(equipment.items(), start=1):
            row = table.rows[idx]
            row.cells[0].text = str(idx)
            row.cells[1].text = equip.name
            row.cells[2].text = equip.type
            row.cells[3].text = equip.modification
            row.cells[4].text = equip.inventory_number
            row.cells[5].text = equip.measurement_range
            row.cells[6].text = equip.accuracy
            row.cells[7].text = equip.calibration_date
        self.logger.success(f"Добавлено {len(equipment)} единиц оборудования")
        
        for row in table.rows:
            row.cells[0].width = Cm(1.2)
            row.cells[1].width = Cm(6.5)
            row.cells[2].width = Cm(2.05)
            row.cells[4].width = Cm(3.0)
            row.cells[5].width = Cm(4.3)
            row.cells[6].width = Cm(2.7)
            row.cells[7].width = Cm(4.0)
        
               
        
            
        