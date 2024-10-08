from spire.doc import *
from spire.doc.common import *

# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Conversion/Python-Convert-Word-to-PDF.html

# Create word document
document = Document()

# Load a doc or docx file
# document.LoadFromFile("fixtures/original.docx")
document.LoadFromFile("fixtures/original.eng.docx") # for English version

#Save the document to PDF
document.SaveToFile("output/original.pdf", FileFormat.PDF)
document.Close()