from spire.doc import *
from spire.doc.common import *
import time

# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Document-Operation/Python-Enable-Track-Changes-Accept-or-Reject-Tracked-Changes-in-Word.html

# Create a Document object
doc = Document()

# Load a Word file
# doc.LoadFromFile("fixtures/original_revision.doc")
# doc.LoadFromFile("fixtures/original_revision.docx")
doc.LoadFromFile("fixtures/original_revision.long.docx")

start_time = time.time()
print('Start accept changes...')

# Accept all revisions
doc.AcceptChanges()

end_time = time.time()
print('All changes accepted.', end_time - start_time)

# Save as New
doc.SaveToFile("output/accept_revision.doc")
# doc.SaveToFile("output/accept_revision.docx")
