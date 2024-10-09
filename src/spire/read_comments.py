from spire.doc import *
from spire.doc.common import *
from pprint import pprint
import json

# Note: commentsは取得できるが構造化された状態では取得できないかも？
# ref: https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Comments/Python-Extract-Comments-from-Word.html

"""
docだと\x05という制御文字が入る。docxだと入らない。
[{'author': 'Nagi Moriyama', 'text': '\x05Comment1\n'},
 {'author': 'Nagi Moriyama', 'text': '\x05Comment2\n'},
 {'author': 'Nagi Moriyama', 'text': '\x05Comment3\n'},
 {'author': 'Nagi Moriyama', 'text': '\x05Comment3 return\n'},
 {'author': 'Nagi Moriyama', 'text': '\x05Comment3 return2\n'}]
"""

# Create a Document object
document = Document()

# Load a Word file
# document.LoadFromFile("fixtures/original_comment.doc")
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
