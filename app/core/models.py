from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, List, Optional, Union

class CompanyInfo(BaseModel):
    legal_address: str = Field(..., alias="юридический адрес: ")
    activity_address: str = Field(..., alias="адрес места осуществления деятельности: ")
    name: str = Field(..., alias="наименование: ")
    phone: str = Field(..., alias="телефон: ")
    email: str = Field(..., alias="e-mail: ")
    registry_number: Optional[str] = "номер в реестре аккредитованных лиц: "
    
class TestObjectInfo(BaseModel):
    id: str = Field(..., alias="ID: ")
    submission_date: str = Field(..., alias="Образец представлен на испытания: ")
    brand: str = Field(..., alias="Марка: ")
    batch: str = Field(..., alias="Партия: ")
    photo_folder: str = Field(..., alias="Папка с фото образца: ")
    
class TestDates(BaseModel):
    start_date: datetime = Field(..., alias="Дата начала")
    end_date: datetime = Field(..., alias="Дата окончания")
    
class EnvironmentConditions(BaseModel):
    temperature: str = Field(..., alias = "Температура")
    humidity: str = Field(..., alias = "Относительная влажность воздуха")
    pressure: str = Field(..., alias = "Атмосферное давление")
    
class EquipmentInfo(BaseModel):
    name: str = Field(..., alias="Наименование ИО и СИ")
    type: str = Field(..., alias="Тип ИО и СИ")
    modification: str = Field(..., alias="Модификация ИО и СИ")
    inventory_number: str = Field(..., alias="Инвентарный номер")
    serial_namber: str = Field(..., alias="Заводской номер")
    measurement_range: str = Field(..., alias="Диапазон измерений")
    accuracy: str = Field(..., alias="Точность измерений")
    certificate_number: str = Field(..., alias="Номер аттестата (свидетельства)")
    calibration_date: str = Field(..., alias="Дата аттестации (поверки) очередной")
    
class TestResult(BaseModel):
    temperature: Optional[str] = None
    humidity: Optional[str] = None
    pressure: Optional[str] = None
    date: Optional[str] = None
    executor: Optional[str] = None
    instrument: Optional[str] = None
    requirement: Optional[str] = None
    tolerance: Optional[str] = None
    result: Optional[Union[str, List[Dict]]] = None
    technical_requirements: Optional[str] = None
    test_methods: Optional[str] = None
        
class ProtocolData(BaseModel):
    primary: Dict[str, str]
    test_basis: str
    customer: CompanyInfo
    manufacturer: CompanyInfo
    test_object: TestObjectInfo
    test_dates: TestDates
    test_purpose: str
    environment: EnvironmentConditions
    test_methods: Dict[str, str]
    equipment: Dict[str, EquipmentInfo]
    test_results: Dict[str, Dict[str, TestResult]]
    performed_by: str
    