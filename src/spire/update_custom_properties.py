from spire.doc import *
from spire.doc.common import *
from pprint import pprint

# build-in propertiesはドキュメントが存在するが、custom propertiesはドキュメントなし
# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Document-Operation/Python-Add-Read-and-Remove-Built-in-Document-Properties-in-Word-Documents.html

doc = Document()

doc.LoadFromFile("fixtures/original.doc")
# doc.LoadFromFile("fixtures/original.docx")

doc.CustomDocumentProperties.Add("MNTSQ_boolean", "")

doc.SaveToFile("output/original_custom_properties.docx")