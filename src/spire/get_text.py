from spire.doc import *
from spire.doc.common import *
 
# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("fixtures/original.docx")

# Get text from the entire document
text = doc.GetText()

# Print text
print(text)
