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
        header_row = table.row[0]
        for i, header in enumerate(headers):
            header_row.cells[i].text = header
        # Заполняем таблицу данными об оборудовании
        for idx, (equip_id, equip) in enumerate(equipment.items(), start=1):
            row = table.rows[idx]
            row.cell[0].text = str(idx)
            row.cell[1].text = equip.name
            row.cell[2].text = equip.type
            row.cell[3].text = equip.modification
            row.cell[4].text = equip.inventory_number
            row.cell[5].text = equip.measurement_range
            row.cell[6].text = equip.accuracy
            row.cell[7].text = equip.calibration_date
        self.logger.success(f"Добавлено {len(equipment)} удиниц оборудования")
        
               
        
            
        