import aspose.words as aw

doc = aw.Document("fixtures/original.docx")

doc.save("output/original.pdf", aw.SaveFormat.PDF)