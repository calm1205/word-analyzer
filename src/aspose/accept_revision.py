import aspose.words as aw

# ref: https://reference.aspose.com/words/python-net/aspose.words/document/accept_all_revisions/

doc = aw.Document('fixtures/original_revision.docx')
doc.revisions.accept_all()
doc.save('output.docx')