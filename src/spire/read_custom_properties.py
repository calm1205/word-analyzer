from spire.doc import *
from spire.doc.common import *
from pprint import pprint

# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("fixtures/original_custom_properties.docx")

# Read custom properties
for i in range(doc.CustomDocumentProperties.Count):
    pprint(doc.CustomDocumentProperties[i].Name)
    pprint(vars(doc.CustomDocumentProperties[i].Value)) # 具体的なオブジェクトが取れない