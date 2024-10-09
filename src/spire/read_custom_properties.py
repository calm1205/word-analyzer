from spire.doc import *
from spire.doc.common import *
from pprint import pprint

# build-in propertiesはドキュメントが存在するが、custom propertiesはドキュメントなし
# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Document-Operation/Python-Add-Read-and-Remove-Built-in-Document-Properties-in-Word-Documents.html

# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("fixtures/original_custom_properties.doc")
# doc.LoadFromFile("fixtures/original_custom_properties.docx")

# Read custom properties
for i in range(doc.CustomDocumentProperties.Count):
    pprint(doc.CustomDocumentProperties[i].Name)
    pprint(vars(doc.CustomDocumentProperties[i].Value)) # 具体的なオブジェクトが取れない