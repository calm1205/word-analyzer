import aspose.words as aw

doc = aw.Document("fixtures/original.docx")
# doc = aw.Document("fixtures/original.eng.docx") # english

doc.save("output/original.pdf", aw.SaveFormat.PDF)