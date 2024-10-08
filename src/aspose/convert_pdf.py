import aspose.words as aw

# for English
# doc = aw.Document("fixtures/original.eng.docx")
# doc.save("output/original.pdf", aw.SaveFormat.PDF)

# for Japanese (not working) 文字化け回避策が分からず
doc = aw.Document("fixtures/original.docx")
save_options = aw.saving.PdfSaveOptions()
save_options.embed_full_fonts = True

doc.save("output/original.pdf", save_options)