from .base_section import BaseSection

class CustomerSection(BaseSection):
    """Раздел с информацией о заказчике"""
    
    def build(self):
        self.logger.info("Формирование раздела Информация о заказчике")
        self._add_heading("2 Информация о заказчике", level=1)
        '''Получаем данные о заказчике'''
        customer = self.protocol_data.customer
        
        customer_info = (
            
            f"Наименование: {customer.name}\n"
            f"Юридический адрес: {customer.legal_address}\n"
            f"Физический адрес места осуществления деятельности: {customer.activity_address}\n"
            f"Телефон: {customer.phone}\n"
            f"Е-mail: {customer.email}\n"
            f"Номер в реестре аккредитованных лиц: {customer.registry_number}\n"
        )
        
        self._add_paragraph(customer_info)
        self.logger.debug("Раздел 'Информация о заказчике' завершен")
        