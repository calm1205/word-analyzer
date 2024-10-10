import aspose.words as aw
import time

# ref: https://reference.aspose.com/words/python-net/aspose.words/compositenode/get_child_nodes/#nodetype_bool

# doc = aw.Document('fixtures/original_comment.doc')
# doc = aw.Document('fixtures/original_comment.docx')
doc = aw.Document('fixtures/original_comment.long.docx')

start_time = time.time()
print('Start print comment...')

comments = doc.get_child_nodes(aw.NodeType.COMMENT, True)
# If a comment has no ancestor, it is a "top-level" comment as opposed to a reply-type comment.
# Print all top-level comments along with any replies they may have.
for comment in comments:
    comment = comment.as_comment()
    if comment.ancestor is None:
        print('Top-level:')
        print(f'\t"Content: {comment.get_text().strip()}", by: {comment.author}, parent: {comment.parent_id}')
        print(f'Has {comment.replies.count} replies')
        for comment_reply in comment.replies:
            comment_reply = comment_reply.as_comment()
            print(f'\t"Content: {comment_reply.get_text().strip()}", by: {comment_reply.author}, parent: {comment_reply.parent_id}')
        print()

end_time = time.time()
print('All comments shown.', end_time - start_time)