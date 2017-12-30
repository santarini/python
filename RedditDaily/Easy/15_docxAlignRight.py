from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

document = Document()

paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

document.save('demo.docx')
