from .base_section import BaseSection

class EquipmentSection(BaseSection):
    '''Раздел с перечнем оболрудования'''
    
    def build(self):
        self.logger.info("Формирование раздела 'Оборудование'")
        self._add_heading("3 Перечень применяемого испытательного оборудования и средств измерений", level=1)
        
        '''Создаем таблицу с оборудованием'''
        equipment = self.protocol_data.equipment
        table = self._add_table(rows=len(equipment) + 1, cols=8)
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
        
               
        
            
        