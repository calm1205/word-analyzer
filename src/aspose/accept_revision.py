import aspose.words as aw
import time

# ref: https://reference.aspose.com/words/python-net/aspose.words/document/accept_all_revisions/

# doc = aw.Document('fixtures/original_revision.doc')
# doc = aw.Document('fixtures/original_revision.docx')
doc = aw.Document('fixtures/original_revision.long.docx')

start_time = time.time()
print('Start accepting all revisions...')

doc.revisions.accept_all()

end_time = time.time()
print('All revisions accepted.', end_time - start_time)

doc.save('output/original_revision.docx')