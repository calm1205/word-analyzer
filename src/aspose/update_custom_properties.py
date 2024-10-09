import aspose.words as aw

# ref: https://reference.aspose.com/words/python-net/aspose.words.properties/customdocumentproperties/

# doc = aw.Document("fixtures/original.docx")
doc = aw.Document("fixtures/original.doc")

doc.custom_document_properties.add("MNTSQ_boolean", True)
doc.custom_document_properties.add("MNTSQ_number", 123)
doc.custom_document_properties.add("MNTSQ_string", "Hello, World!")

# doc.save("output/original_custom_properties.docx")
doc.save("output/original_custom_properties.doc")