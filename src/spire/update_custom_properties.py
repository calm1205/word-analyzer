from spire.doc import *
from spire.doc.common import *
from pprint import pprint

# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("fixtures/original.docx")

# Add custom properties
doc.CustomDocumentProperties.Add("MNTSQ_boolean", "")

# Save as New File
doc.SaveToFile("output/original_custom_properties.docx")