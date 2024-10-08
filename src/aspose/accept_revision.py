import aspose.words as aw

doc = aw.Document('fixtures/' + 'original_revision.docx')
doc.revisions.accept_all()
doc.save('output.docx')