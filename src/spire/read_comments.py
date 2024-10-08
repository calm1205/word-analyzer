from spire.doc import *
from spire.doc.common import *
from pprint import pprint
import json
 
# Create a Document object
document = Document()

# Load a Word file
document.LoadFromFile("fixtures/original_comment.docx")

# Create a list to store the extracted comment data
comments = []

# Iterate through the comments in the document
for i in range(document.Comments.Count):
    comment = document.Comments[i]
    comment_text = ""

    # Iterate through the paragraphs in the comment body
    for j in range(comment.Body.Paragraphs.Count):
        paragraph = comment.Body.Paragraphs[j]
        comment_text += paragraph.Text + "\n"

    # Get the comment author
    comment_author = comment.Format.Author
    # Append the comment data to the list

    comments.append({
        "author": comment_author,
        "text": comment_text
    })


# Print text
pprint(comments)
