import aspose.words as aw

# ref: https://reference.aspose.com/words/python-net/aspose.words/document/custom_document_properties/

doc = aw.Document("fixtures/original_custom_properties.doc")
# doc = aw.Document("fixtures/original_custom_properties.docx")

for property in doc.custom_document_properties:
    print(f"{property.name}: {property.value}")

# MNTSQ_boolean: True
# MNTSQ_number: 123
# MNTSQ_string: Hello, World!