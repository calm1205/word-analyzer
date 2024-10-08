from spire.doc import *
from spire.doc.common import *
 
# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("fixtures/original_revision.docx")

# Accept all revisions
doc.AcceptChanges()

# Save as New
doc.SaveToFile("output/accept_revision.docx")
