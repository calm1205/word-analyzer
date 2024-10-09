from spire.doc import *
from spire.doc.common import *
from pprint import pprint

# build-in propertiesはドキュメントが存在するが、custom propertiesはドキュメントなし
# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Document-Operation/Python-Add-Read-and-Remove-Built-in-Document-Properties-in-Word-Documents.html

# Create a Document object
doc = Document()

# Load a Word file
# doc.LoadFromFile("fixtures/original_custom_properties.doc")
doc.LoadFromFile("fixtures/original_custom_properties.docx")

# Read custom properties
for i in range(doc.CustomDocumentProperties.Count):
    name = doc.CustomDocumentProperties[i].Name
    value = doc.CustomDocumentProperties.get_Item(name).ToString()
    pprint({"name": name, "value": value})
