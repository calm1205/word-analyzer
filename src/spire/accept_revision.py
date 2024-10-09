from spire.doc import *
from spire.doc.common import *

# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Document-Operation/Python-Enable-Track-Changes-Accept-or-Reject-Tracked-Changes-in-Word.html

# Create a Document object
doc = Document()

# Load a Word file
doc.LoadFromFile("fixtures/original_revision.doc")
# doc.LoadFromFile("fixtures/original_revision.docx")

# Accept all revisions
doc.AcceptChanges()

# Save as New
doc.SaveToFile("output/accept_revision.doc")
# doc.SaveToFile("output/accept_revision.docx")
