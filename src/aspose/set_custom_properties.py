import aspose.words as aw

doc = aw.Document("fixtures/original.docx")

doc.custom_document_properties.add("MNTSQ_boolean", True)
doc.custom_document_properties.add("MNTSQ_number", 123)
doc.custom_document_properties.add("MNTSQ_string", "Hello, World!")

doc.save("output/original_custom_properties.docx")