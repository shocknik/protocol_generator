from docx import Document
from docx.shared import Pt, Cm, Mm
from .sections.header_section import HeaderSection
from .sections.basis_section import BasisSection
from .sections.customer_section import CustomerSection
from .sections.equipment_section import EquipmentSection


class DocumentGeneration:
    def __init__(self, protocol_data):
        self.protocol_data = protocol_data
        self.document = Document()
        self._setup_document()
        
    def _setup_document(self):
        '''Настройка параметров страницы'''
        section = self.document.sections[0]
        section.page_width = Cm(29.7)
        section.page_height = Cm(21.0)
        section.orientation = 1 # альбомная ориентация
        section.left_margin = Mm(15)
        section.right_margin = Mm(15)
        section.top_margin = Mm(20)
        section.bottom_margin = Mm(20)
        
        '''Настройка стилей'''
        styles = self.document.styles
        style = styles['Normal']
        style.font.name = 'Times_New_Roman'
        style.font.size = Pt(12)
    
    def generate_document(self, output_path: str):
        '''Формирование разделов'''
        sections = [
            HeaderSection(self.document, self.protocol_data),
            BasisSection(self.document, self.protocol_data),
            CustomerSection(self.document, self.protocol_data),
            TestResultSection(self.document, self.protocol_data),
            EquipmentSection(self.document, self.protocol_data),
            SignaturesSection(self.document, self.protocol_data)
        ]
        
        for section in sections:
            section.build() # Единый интерфейс для разных классов секций(sections) - в кадом модуле есть метод build  
            
        self.document.save(output_path) 
        