import aspose.words as aw

doc = aw.Document("fixtures/original.docx")

doc.custom_document_properties.add("MNTSQ", True)

doc.save("output/original_custom_properties.docx")