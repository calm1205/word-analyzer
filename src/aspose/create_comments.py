import aspose.words as aw
import datetime

doc = aw.Document()
builder = aw.DocumentBuilder(doc)
builder.write('Hello world!')
comment = aw.Comment(doc, 'John Doe', 'JD', datetime.date.today())
builder.current_paragraph.append_child(comment)
builder.move_to(comment.append_child(aw.Paragraph(doc)))
builder.write('Comment text.')

comment_reply = comment.add_reply('Joe Bloggs', 'J.B.', datetime.datetime.now(), 'New reply')
comment_reply.add_reply('J.K. Rowling', 'J.K.', datetime.datetime.now(), 'New reply 2')

# In Microsoft Word, we can right-click this comment in the document body to edit it, or reply to it.
doc.save('output/create_comment.docx')
