from spire.doc import *
from spire.doc.common import *
from pprint import pprint

# build-in propertiesはドキュメントが存在するが、custom propertiesはドキュメントなし
# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Document-Operation/Python-Add-Read-and-Remove-Built-in-Document-Properties-in-Word-Documents.html
# ref: https://www.e-iceblue.com/api_documents/652f3a117501c0-89206493/res/html/CustomDocumentProperties.html

doc = Document()

# doc.LoadFromFile("fixtures/original.doc")
doc.LoadFromFile("fixtures/original.docx")

# spire_object = SpireObject(ptr) # SpireObjectは自分でinstance化する必要があるのか
# value = DocumentProperty(spire_object)
doc.CustomDocumentProperties.Add("MNTSQ_boolean", value) # to See: packages/spire/doc/CustomDocumentProperties.py

doc.SaveToFile("output/original_custom_properties.docx")