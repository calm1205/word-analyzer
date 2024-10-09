﻿from aspose.words import bibliography
from aspose.words import buildingblocks
from aspose.words import comparing
from aspose.words import digitalsignatures
from aspose.words import drawing
from aspose.words import fields
from aspose.words import fonts
from aspose.words import framesets
from aspose.words import layout
from aspose.words import lists
from aspose.words import loading
from aspose.words import lowcode
from aspose.words import mailmerging
from aspose.words import markup
from aspose.words import math
from aspose.words import notes
from aspose.words import properties
from aspose.words import rendering
from aspose.words import replacing
from aspose.words import reporting
from aspose.words import saving
from aspose.words import settings
from aspose.words import shaping
from aspose.words import tables
from aspose.words import themes
from aspose.words import vba
from aspose.words import webextensions
import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum
from typing import Any

def get_pyinstaller_hook_dirs() -> Any:
    """Function required by PyInstaller. Returns paths to module
    PyInstaller hooks. Not intended to be called explicitly."""
...

class AbsolutePositionTab(aspose.words.SpecialChar):
    """An absolute position tab is a character which is used to advance the position on
    the current line of text when displaying this WordprocessingML content.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article."""
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_absolute_position_tab`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    ...

class Body(aspose.words.Story):
    """Represents a container for the main text of a section.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    :class:`Body` can contain :class:`Paragraph` and :class:`aspose.words.tables.Table` child nodes.
    
    :class:`Body` is a section-level node and can only be a child of :class:`Section`.
    There can only be one :class:`Body` in a :class:`Section`.
    
    A minimal valid :class:`Body` needs to contain at least one :class:`Paragraph`."""
    
    def __init__(self, doc: aspose.words.DocumentBase):
        """Initializes a new instance of the :class:`Body` class.
        
        When :class:`Body` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append :class:`Body` to a :class:`Section` use :meth:`CompositeNode.append_child`
        :meth:`CompositeNode.insert_after` or :meth:`CompositeNode.insert_before`
        methods.
        
        :param doc: The owner document."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`DocumentVisitor.visit_body_start`, then calls :meth:`Node.accept` for all child nodes of the section
        and calls :meth:`DocumentVisitor.visit_body_end` at the end."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the start of the document's body.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the end of the document's body.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def ensure_minimum(self) -> None:
        """If the last child is not a paragraph, creates and appends one empty paragraph."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.BODY`."""
        ...
    
    @property
    def parent_section(self) -> aspose.words.Section:
        """Gets the parent section of this story.
        
        :attr:`Body.parent_section` is equivalent to :attr:`Node.parent_node` casted to :class:`Section`."""
        ...
    
    ...

class Bookmark:
    """Represents a single bookmark.
    To learn more, visit the `Working with Bookmarks <https://docs.aspose.com/words/python-net/working-with-bookmarks/>` documentation article.
    
    :class:`Bookmark` is a "facade" object that encapsulates two nodes :attr:`Bookmark.bookmark_start`
    and :attr:`Bookmark.bookmark_end` in a document tree and allows to work with a bookmark as a single object."""
    
    def remove(self) -> None:
        """Removes the bookmark from the document. Does not remove text inside the bookmark."""
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets the name of the bookmark.
        
        Note that if you change the name of a bookmark to a name that already exists in the document,
        no error will be given and only the first bookmark will be stored when you save the document."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def text(self) -> str:
        """Gets or sets the text enclosed in the bookmark."""
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def bookmark_start(self) -> aspose.words.BookmarkStart:
        """Gets the node that represents the start of the bookmark."""
        ...
    
    @property
    def bookmark_end(self) -> aspose.words.BookmarkEnd:
        """Gets the node that represents the end of the bookmark."""
        ...
    
    @property
    def is_column(self) -> bool:
        """Returns ``True`` if this bookmark is a table column bookmark."""
        ...
    
    @property
    def first_column(self) -> int:
        """Gets the zero-based index of the first column of the table column range associated with the bookmark.
        
        Returns **-1** if this bookmark is not a table column bookmark."""
        ...
    
    @property
    def last_column(self) -> int:
        """Gets the zero-based index of the last column of the table column range associated with the bookmark.
        
        Returns **-1** if this bookmark is not a table column bookmark."""
        ...
    
    ...

class BookmarkCollection:
    """A collection of :class:`Bookmark` objects that represent the bookmarks in the specified range.
    To learn more, visit the `Working with Bookmarks <https://docs.aspose.com/words/python-net/working-with-bookmarks/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.Bookmark:
        """Returns a bookmark at the specified index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection."""
        ...
    
    @overload
    def remove(self, bookmark: aspose.words.Bookmark) -> None:
        """Removes the specified bookmark from the document.
        
        :param bookmark: The bookmark to remove."""
        ...
    
    @overload
    def remove(self, bookmark_name: str) -> None:
        """Removes a bookmark with the specified name.
        
        :param bookmark_name: The case-insensitive name of the bookmark to remove."""
        ...
    
    def get_by_name(self, bookmark_name: str) -> aspose.words.Bookmark:
        """Returns a bookmark by name."""
        ...
    
    def remove_at(self, index: int) -> None:
        """Removes a bookmark at the specified index.
        
        :param index: The zero-based index of the bookmark to remove."""
        ...
    
    def clear(self) -> None:
        """Removes all bookmarks from this collection and from the document."""
        ...
    
    @property
    def count(self) -> int:
        """Returns the number of bookmarks in the collection."""
        ...
    
    ...

class BookmarkEnd(aspose.words.Node):
    """Represents an end of a bookmark in a Word document.
    To learn more, visit the `Working with Bookmarks <https://docs.aspose.com/words/python-net/working-with-bookmarks/>` documentation article.
    
    A complete bookmark in a Word document consists of a :class:`BookmarkStart`
    and a matching :class:`BookmarkEnd` with the same bookmark name.
    
    :class:`BookmarkStart` and :class:`BookmarkEnd` are just markers inside a document
    that specify where the bookmark starts and ends.
    
    Use the :class:`Bookmark` class as a "facade" to work with a bookmark
    as a single object."""
    
    def __init__(self, doc: aspose.words.DocumentBase, name: str):
        """Initializes a new instance of the :class:`BookmarkEnd` class.
        
        :param doc: The owner document.
        :param name: The name of the bookmark. Cannot be ``None``."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_bookmark_end`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.BOOKMARK_END`."""
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets the bookmark name.
        
        Cannot be ``None``."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    ...

class BookmarkStart(aspose.words.Node):
    """Represents a start of a bookmark in a Word document.
    To learn more, visit the `Working with Bookmarks <https://docs.aspose.com/words/python-net/working-with-bookmarks/>` documentation article.
    
    A complete bookmark in a Word document consists of a :class:`BookmarkStart`
    and a matching :class:`BookmarkEnd` with the same bookmark name.
    
    :class:`BookmarkStart` and :class:`BookmarkEnd` are just markers inside a document
    that specify where the bookmark starts and ends.
    
    Use the :attr:`BookmarkStart.bookmark` class as a "facade" to work with a bookmark
    as a single object."""
    
    def __init__(self, doc: aspose.words.DocumentBase, name: str):
        """Initializes a new instance of the :class:`BookmarkStart` class.
        
        :param doc: The owner document.
        :param name: The name of the bookmark. Cannot be ``None``."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_bookmark_start`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    def get_text(self) -> str:
        """Returns an empty string.
        
        :returns: An empty string."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.BOOKMARK_START`."""
        ...
    
    @property
    def bookmark(self) -> aspose.words.Bookmark:
        """Gets the facade object that encapsulates this bookmark start and end."""
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets the bookmark name.
        
        Cannot be ``None``."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    ...

class Border(aspose.words.InternableComplexAttr):
    """Represents a border of an object.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article.
    
    Borders can be applied to various document elements including paragraph,
    run of text inside a paragraph or a table cell."""
    
    def clear_formatting(self) -> None:
        """Resets border properties to default values.
        
        When border properties are reset to default values, the border is invisible."""
        ...
    
    def equals(self, rhs: aspose.words.Border) -> bool:
        """Determines whether the specified border is equal in value to the current border."""
        ...
    
    @property
    def line_style(self) -> aspose.words.LineStyle:
        """Gets or sets the border style.
        
        If you set line style to none, then line width is automatically changed to zero."""
        ...
    
    @line_style.setter
    def line_style(self, value: aspose.words.LineStyle):
        ...
    
    @property
    def line_width(self) -> float:
        """Gets or sets the border width in points.
        
        If you set line width greater than zero when line style is none, the line style is
        automatically changed to single line."""
        ...
    
    @line_width.setter
    def line_width(self, value: float):
        ...
    
    @property
    def is_visible(self) -> bool:
        """Returns ``True`` if the :attr:`Border.line_style` is not :attr:`LineStyle.NONE`."""
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        """Gets or sets the border color."""
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def distance_from_text(self) -> float:
        """Gets or sets distance of the border from text or from the page edge in points.
        
        Has no effect and will be automatically reset to zero for borders of table cells."""
        ...
    
    @distance_from_text.setter
    def distance_from_text(self, value: float):
        ...
    
    @property
    def shadow(self) -> bool:
        """Gets or sets a value indicating whether the border has a shadow.
        
        In Microsoft Word, for a border to have a shadow, the borders on all four sides
        (left, top, right and bottom) should be of the same type, width, color and all should have
        the Shadow property set to ``True``."""
        ...
    
    @shadow.setter
    def shadow(self, value: bool):
        ...
    
    @property
    def theme_color(self) -> aspose.words.themes.ThemeColor:
        """Gets or sets the theme color in the applied color scheme that is associated with this Border object."""
        ...
    
    @theme_color.setter
    def theme_color(self, value: aspose.words.themes.ThemeColor):
        ...
    
    @property
    def tint_and_shade(self) -> float:
        """Gets or sets a double value that lightens or darkens a color.
        
        The allowed values are in the range from -1 (the darkest) to 1 (the lightest) for this property.
        Zero (0) is neutral.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws if you attempt to set this property to a value less than -1 or more than 1.
        :raises RuntimeError (Proxy error(InvalidOperationException)): Throws if setting this property for Border object with non-theme colors."""
        ...
    
    @tint_and_shade.setter
    def tint_and_shade(self, value: float):
        ...
    
    ...

class BorderCollection:
    """A collection of :class:`Border` objects.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article.
    
    Different document elements have different borders.
    For example, :class:`ParagraphFormat` has :attr:`BorderCollection.bottom`, :attr:`BorderCollection.left`, :attr:`BorderCollection.right` and :attr:`BorderCollection.top` borders.
    You can specify different formatting for each border independently or
    enumerate through all borders and apply same formatting."""
    
    def __getitem__(self, index: int) -> aspose.words.Border:
        """Retrieves a :class:`Border` object by index.
        
        :param index: Zero-based index of the border to retrieve."""
        ...
    
    def equals(self, br_coll: aspose.words.BorderCollection) -> bool:
        """Compares collections of borders."""
        ...
    
    def get_by_border_type(self, border_type: aspose.words.BorderType) -> aspose.words.Border:
        """Retrieves a :class:`Border` object by border type."""
        ...
    
    def clear_formatting(self) -> None:
        """Removes all borders of an object."""
        ...
    
    @property
    def left(self) -> aspose.words.Border:
        """Gets the left border."""
        ...
    
    @property
    def right(self) -> aspose.words.Border:
        """Gets the right border."""
        ...
    
    @property
    def top(self) -> aspose.words.Border:
        """Gets the top border."""
        ...
    
    @property
    def bottom(self) -> aspose.words.Border:
        """Gets the bottom border."""
        ...
    
    @property
    def horizontal(self) -> aspose.words.Border:
        """Gets the horizontal border that is used between cells or conforming paragraphs."""
        ...
    
    @property
    def vertical(self) -> aspose.words.Border:
        """Gets the vertical border that is used between cells."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of borders in the collection."""
        ...
    
    @property
    def line_width(self) -> float:
        """Gets or sets the border width in points.
        
        Returns the width of the first border in the collection.
        
        Sets the width of all borders in the collection excluding diagonal borders."""
        ...
    
    @line_width.setter
    def line_width(self, value: float):
        ...
    
    @property
    def line_style(self) -> aspose.words.LineStyle:
        """Gets or sets the border style.
        
        Returns the style of the first border in the collection.
        
        Sets the style of all borders in the collection excluding diagonal borders."""
        ...
    
    @line_style.setter
    def line_style(self, value: aspose.words.LineStyle):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        """Gets or sets the border color.
        
        Returns the color of the first border in the collection.
        
        Sets the color of all borders in the collection excluding diagonal borders."""
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def distance_from_text(self) -> float:
        """Gets or sets distance of the border from text in points.
        
        Gets the distance from text for the first border.
        
        Sets the distance from text for all borders in the collection excluding diagonal borders.
        
        Has no effect and will be automatically reset to zero for borders of table cells."""
        ...
    
    @distance_from_text.setter
    def distance_from_text(self, value: float):
        ...
    
    @property
    def shadow(self) -> bool:
        """Gets or sets a value indicating whether the border has a shadow.
        
        Gets the value from the first border in the collection.
        
        Sets the value for all borders in the collection excluding diagonal borders."""
        ...
    
    @shadow.setter
    def shadow(self, value: bool):
        ...
    
    ...

class BuildVersionInfo:
    """Provides information about the current product name and version.
    To learn more, visit the `Generator or Producer Name Included in Output Documents <https://docs.aspose.com/words/python-net/generator-or-producer-name-included-in-output-documents/>` documentation article."""
    
    product: str
    
    version: str
    
    ...

class CleanupOptions:
    """Allows to specify options for document cleaning.
    To learn more, visit the `Clean Up a Document <https://docs.aspose.com/words/python-net/clean-up-a-document/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def unused_styles(self) -> bool:
        """Specifies whether unused styles should be removed from document.
        Default value is ``True``."""
        ...
    
    @unused_styles.setter
    def unused_styles(self, value: bool):
        ...
    
    @property
    def unused_lists(self) -> bool:
        """Specifies whether unused list and list definitions should be removed from document.
        Default value is ``True``."""
        ...
    
    @unused_lists.setter
    def unused_lists(self, value: bool):
        ...
    
    @property
    def duplicate_style(self) -> bool:
        """Gets/sets a flag indicating whether duplicate styles should be removed from document.
        Default value is ``False``."""
        ...
    
    @duplicate_style.setter
    def duplicate_style(self, value: bool):
        ...
    
    @property
    def unused_builtin_styles(self) -> bool:
        """Specifies that unused :attr:`Style.built_in` styles should be removed from document."""
        ...
    
    @unused_builtin_styles.setter
    def unused_builtin_styles(self, value: bool):
        ...
    
    ...

class ComHelper:
    """Provides methods for COM clients to load a document into Aspose.Words.
    
    Use the :class:`ComHelper` class to load a document from a file or stream into a
    :class:`Document` object in a COM application.
    
    The :class:`Document` class provides a default constructor to create a new document
    and also provides overloaded constructors to load a document from a file or stream.
    If you are using Aspose.Words from a .NET application, you can use all of the :class:`Document`
    constructors directly, but if you are using Aspose.Words from a COM application,
    only the default :class:`Document` constructor is available."""
    
    def __init__(self):
        """Initializes a new instance of this class."""
        ...
    
    @overload
    def open(self, file_name: str) -> aspose.words.Document:
        """Allows a COM application to load a :class:`Document` from a file.
        
        This method is same as calling the :class:`Document` constructor with a file name parameter.
        
        :param file_name: Filename of the document to load.
        :returns: A :class:`Document` object that represents a Word document."""
        ...
    
    @overload
    def open(self, stream: io.BytesIO) -> aspose.words.Document:
        """Allows a COM application to load :class:`Document` from a stream.
        
        This method is same as calling the :class:`Document` constructor with a stream parameter.
        
        :param stream: A .NET stream object that contains the document to load.
        :returns: A :class:`Document` object that represents a Word document."""
        ...
    
    ...

class Comment(aspose.words.InlineStory):
    """Represents a container for text of a comment.
    To learn more, visit the `Working with Comments <https://docs.aspose.com/words/python-net/working-with-comments/>` documentation article.
    
    A comment is an annotation which is anchored to a region of text or to a position in text.
    A comment can contain an arbitrary amount of block-level content.
    
    If a :class:`Comment` object occurs on its own, the comment is anchored to
    the position of the :class:`Comment` object.
    
    To anchor a comment to a region of text three objects are required: :class:`Comment`,
    :class:`CommentRangeStart` and :class:`CommentRangeEnd`. All three objects need to share the same
    :attr:`Comment.id` value.
    
    :class:`Comment` is an inline-level node and can only be a child of :class:`Paragraph`.
    
    :class:`Comment` can contain :class:`Paragraph` and :class:`aspose.words.tables.Table` child nodes."""
    
    @overload
    def __init__(self, doc: aspose.words.DocumentBase):
        """Initializes a new instance of the :class:`Comment` class.
        
        When :class:`Comment` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append :class:`Comment` to the document use :meth:`CompositeNode.insert_after` or :meth:`CompositeNode.insert_before`
        on the paragraph where you want the comment inserted.
        
        After creating a comment, don't forget to set its :attr:`Comment.author`,
        :attr:`Comment.initial` and :attr:`Comment.date_time` properties.
        
        :param doc: The owner document."""
        ...
    
    @overload
    def __init__(self, doc: aspose.words.DocumentBase, author: str, initial: str, date_time: datetime.datetime):
        """Initializes a new instance of the :class:`Comment` class.
        
        :param doc: The owner document.
        :param author: The author name for the comment. Cannot be ``None``.
        :param initial: The author initials for the comment. Cannot be ``None``.
        :param date_time: The date and time for the comment."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`DocumentVisitor.visit_comment_start`, then calls :meth:`Node.accept` for all
        child nodes of the comment and calls :meth:`DocumentVisitor.visit_comment_end` at the end."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the start of the comment.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the end of the comment.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def add_reply(self, author: str, initial: str, date_time: datetime.datetime, text: str) -> aspose.words.Comment:
        """Adds a reply to this comment.
        
        :param author: The author name for the reply.
        :param initial: The author initials for the reply.
        :param date_time: The date and time for the reply.
        :param text: The reply text.
        :returns: The created :class:`Comment` node for the reply.
        
        Due to the existing MS Office limitations only 1 level of replies is allowed in the document.
        
        :raises RuntimeError (Proxy error(InvalidOperationException)): Throws if this method is called on the existing Reply comment."""
        ...
    
    def remove_reply(self, reply: aspose.words.Comment) -> None:
        """Removes the specified reply to this comment.
        
        All constituent nodes of the reply will be deleted from the document.
        
        :param reply: The comment node of the deleting reply."""
        ...
    
    def remove_all_replies(self) -> None:
        """Removes all replies to this comment.
        
        All constituent nodes of the replies will be deleted from the document."""
        ...
    
    def set_text(self, text: str) -> None:
        """This is a convenience method that allows to easily set text of the comment.
        
        This method allows to quickly set text of a comment from a string. The string can contain
        paragraph breaks, this will create paragraphs of text in the comment accordingly.
        If you want to insert more complex elements into the comment, for example bookmarks
        or tables or apply rich formatting, then you need to use the appropriate node classes to
        build up the comment text.
        
        :param text: The new text of the comment."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.COMMENT`."""
        ...
    
    @property
    def story_type(self) -> aspose.words.StoryType:
        """Returns :attr:`StoryType.COMMENTS`."""
        ...
    
    @property
    def id(self) -> int:
        """Gets or sets the comment identifier.
        
        The comment identifier allows to anchor a comment to a region of text in the document.
        The region must be demarcated using the :class:`CommentRangeStart` and :class:`CommentRangeEnd`
        object sharing the same identifier value as the :class:`Comment` object.
        
        You would use this value when looking for the :class:`CommentRangeStart` and
        :class:`CommentRangeEnd` nodes that are linked to this comment.
        
        Comment identifiers are supposed to be unique across a document and Aspose.Words automatically
        maintains comment identifiers when loading, saving and combining documents."""
        ...
    
    @id.setter
    def id(self, value: int):
        ...
    
    @property
    def initial(self) -> str:
        """Returns or sets the initials of the user associated with a specific comment.
        
        Cannot be ``None``.
        
        Default is empty string."""
        ...
    
    @initial.setter
    def initial(self, value: str):
        ...
    
    @property
    def date_time(self) -> datetime.datetime:
        """Gets the date and time that the comment was made.
        
        Default is
        datetime.datetime.min"""
        ...
    
    @date_time.setter
    def date_time(self, value: datetime.datetime):
        ...
    
    @property
    def date_time_utc(self) -> datetime.datetime:
        """Gets the UTC date and time that the comment was made.
        
        The default value is
        datetime.datetime.min"""
        ...
    
    @property
    def author(self) -> str:
        """Returns or sets the author name for a comment.
        
        Cannot be ``None``.
        
        Default is empty string."""
        ...
    
    @author.setter
    def author(self, value: str):
        ...
    
    @property
    def ancestor(self) -> aspose.words.Comment:
        """Returns the parent :class:`Comment` object. Returns ``None`` for top-level comments."""
        ...
    
    @property
    def replies(self) -> aspose.words.CommentCollection:
        """Returns a collection of :class:`Comment` objects that are immediate children of the specified comment."""
        ...
    
    @property
    def done(self) -> bool:
        """Gets or sets flag indicating that the comment has been marked done."""
        ...
    
    @done.setter
    def done(self, value: bool):
        ...
    
    @property
    def parent_id(self) -> int:
        """Gets or sets the parent comment ID. A value of ``-1`` means the comment has no parent."""
        ...
    
    @parent_id.setter
    def parent_id(self, value: int):
        ...
    
    ...

class CommentCollection(aspose.words.NodeCollection):
    """Provides typed access to a collection of :class:`Comment` nodes.
    To learn more, visit the `Working with Comments <https://docs.aspose.com/words/python-net/working-with-comments/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.Comment:
        """Retrieves a :class:`Comment` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection."""
        ...
    
    ...

class CommentRangeEnd(aspose.words.Node):
    """Denotes the end of a region of text that has a comment associated with it.
    To learn more, visit the `Working with Comments <https://docs.aspose.com/words/python-net/working-with-comments/>` documentation article.
    
    To create a comment anchored to a region of text, you need to create a :class:`Comment` and
    then create :class:`CommentRangeStart` and :class:`CommentRangeEnd` and set their identifiers
    to the same :attr:`Comment.id` value.
    
    :class:`CommentRangeEnd` is an inline-level node and can only be a child of :class:`Paragraph`."""
    
    def __init__(self, doc: aspose.words.DocumentBase, id: int):
        """Initializes a new instance of this class.
        
        When :class:`CommentRangeEnd` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append a :class:`CommentRangeEnd` to the document use InsertAfter or InsertBefore
        on the paragraph where you want the comment inserted.
        
        :param doc: The owner document.
        :param id: The comment identifier to which this object is linked."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_comment_range_end`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.COMMENT_RANGE_END`."""
        ...
    
    @property
    def id(self) -> int:
        """Specifies the identifier of the comment to which this region is linked to."""
        ...
    
    @id.setter
    def id(self, value: int):
        ...
    
    ...

class CommentRangeStart(aspose.words.Node):
    """Denotes the start of a region of text that has a comment associated with it.
    To learn more, visit the `Working with Comments <https://docs.aspose.com/words/python-net/working-with-comments/>` documentation article.
    
    To create a comment anchored to a region of text, you need to create a :class:`Comment` and
    then create :class:`CommentRangeStart` and :class:`CommentRangeEnd` and set their identifiers
    to the same :attr:`Comment.id` value.
    
    :class:`CommentRangeStart` is an inline-level node and can only be a child of :class:`Paragraph`."""
    
    def __init__(self, doc: aspose.words.DocumentBase, id: int):
        """Initializes a new instance of this class.
        
        When :class:`CommentRangeStart` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append a :class:`CommentRangeStart` to the document use InsertAfter or InsertBefore
        on the paragraph where you want the comment inserted.
        
        :param doc: The owner document.
        :param id: The comment identifier to which this object is linked."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_comment_range_start`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.COMMENT_RANGE_START`."""
        ...
    
    @property
    def id(self) -> int:
        """Specifies the identifier of the comment to which this region is linked."""
        ...
    
    @id.setter
    def id(self, value: int):
        ...
    
    ...

class CompositeNode(aspose.words.Node):
    """Base class for nodes that can contain other nodes.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    A document is represented as a tree of nodes, similar to DOM or XmlDocument.
    
    For more info see the Composite design pattern.
    
    The :class:`CompositeNode` class:
    
    * Provides access to the child nodes.
    
    * Implements Composite operations such as insert and remove children.
    
    * Provides methods for XPath navigation."""
    
    def get_text(self) -> str:
        """Gets the text of this node and of all its children.
        
        The returned string includes all control and special characters as described in :class:`ControlChar`."""
        ...
    
    def get_child_nodes(self, node_type: aspose.words.NodeType, is_deep: bool) -> aspose.words.NodeCollection:
        """Returns a live collection of child nodes that match the specified type.
        
        The collection of nodes returned by this method is always live.
        
        A live collection is always in sync with the document. For example, if you
        selected all sections in a document and enumerate through the collection
        deleting the sections, the section is removed from the collection immediately
        when it is removed from the document.
        
        :param node_type: Specifies the type of nodes to select.
        :param is_deep: ``True`` to select from all child nodes recursively;
                        ``False`` to select only among immediate children.
        :returns: A live collection of child nodes of the specified type."""
        ...
    
    def get_child(self, node_type: aspose.words.NodeType, index: int, is_deep: bool) -> aspose.words.Node:
        """Returns an Nth child node that matches the specified type.
        
        If index is out of range, a ``None`` is returned.
        
        :param node_type: Specifies the type of the child node.
        :param index: Zero based index of the child node to select.
                      Negative indexes are also allowed and indicate access from the end,
                      that is -1 means the last node.
        :param is_deep: ``True`` to select from all child nodes recursively;
                        ``False`` to select only among immediate children. See remarks for more info.
        :returns: The child node that matches the criteria or ``None`` if no matching node is found.
        
        Note that markup nodes (:attr:`NodeType.STRUCTURED_DOCUMENT_TAG` and :attr:`NodeType.SMART_TAG`)
        are traversed even when *isDeep* =``False`` and :meth:`CompositeNode.get_child` is invoked for non-markup node type. For example if the first run in a para
        is wrapped in a :class:`aspose.words.markup.StructuredDocumentTag`, it will still be returned by :meth:`CompositeNode.get_child`(:attr:`NodeType.RUN`, 0, ``False``)."""
        ...
    
    def select_nodes(self, xpath: str) -> aspose.words.NodeList:
        """Selects a list of nodes matching the XPath expression.
        
        Only expressions with element names are supported at the moment. Expressions
        that use attribute names are not supported.
        
        :param xpath: The XPath expression.
        :returns: A list of nodes matching the XPath query."""
        ...
    
    def select_single_node(self, xpath: str) -> aspose.words.Node:
        """Selects the first :class:`Node` that matches the XPath expression.
        
        Only expressions with element names are supported at the moment. Expressions
        that use attribute names are not supported.
        
        :param xpath: The XPath expression.
        :returns: The first :class:`Node` that matches the XPath query or ``None`` if no matching node is found."""
        ...
    
    def append_child(self, new_child: aspose.words.Node) -> aspose.words.Node:
        """Adds the specified node to the end of the list of child nodes for this node.
        
        If the *newChild* is already in the tree, it is first removed.
        
        If the node being inserted was created from another document, you should use
        :meth:`DocumentBase.import_node` to import the node to the current document.
        The imported node can then be inserted into the current document.
        
        :param new_child: The node to add.
        :returns: The node added."""
        ...
    
    def prepend_child(self, new_child: aspose.words.Node) -> aspose.words.Node:
        """Adds the specified node to the beginning of the list of child nodes for this node.
        
        If the *newChild* is already in the tree, it is first removed.
        
        If the node being inserted was created from another document, you should use
        :meth:`DocumentBase.import_node` to import the node to the current document.
        The imported node can then be inserted into the current document.
        
        :param new_child: The node to add.
        :returns: The node added."""
        ...
    
    def insert_after(self, new_child: aspose.words.Node, ref_child: aspose.words.Node) -> aspose.words.Node:
        """Inserts the specified node immediately after the specified reference node.
        
        If *refChild* is``None``, inserts *newChild* at the beginning of the list of child nodes.
        
        If the *newChild* is already in the tree, it is first removed.
        
        If the node being inserted was created from another document, you should use
        :meth:`DocumentBase.import_node` to import the node to the current document.
        The imported node can then be inserted into the current document.
        
        :param new_child: The :class:`Node` to insert.
        :param ref_child: The :class:`Node` that is the reference node. The *newChild* is placed after the*refChild*.
        :returns: The inserted node."""
        ...
    
    def insert_before(self, new_child: aspose.words.Node, ref_child: aspose.words.Node) -> aspose.words.Node:
        """Inserts the specified node immediately before the specified reference node.
        
        If *refChild* is``None``, inserts *newChild* at the end of the list of child nodes.
        
        If the *newChild* is already in the tree, it is first removed.
        
        If the node being inserted was created from another document, you should use
        :meth:`DocumentBase.import_node` to import the node to the current document.
        The imported node can then be inserted into the current document.
        
        :param new_child: The :class:`Node` to insert.
        :param ref_child: The :class:`Node` that is the reference node. The *newChild* is placed before this node.
        :returns: The inserted node."""
        ...
    
    def remove_child(self, old_child: aspose.words.Node) -> aspose.words.Node:
        """Removes the specified child node.
        
        The parent of *oldChild* is set to``None`` after the node is removed.
        
        :param old_child: The node to remove.
        :returns: The removed node."""
        ...
    
    def remove_all_children(self) -> None:
        """Removes all the child nodes of the current node."""
        ...
    
    def remove_smart_tags(self) -> None:
        """Removes all :class:`aspose.words.markup.SmartTag` descendant nodes of the current node.
        
        This method does not remove the content of the smart tags."""
        ...
    
    def index_of(self, child: aspose.words.Node) -> int:
        """Returns the index of the specified child node in the child node array.
        
        Returns -1 if the node is not found in the child nodes."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """When implemented in a derived class, calls the VisitXXXStart method of the specified document visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """When implemented in a derived class, calls the VisitXXXEnd method of the specified document visitor."""
        ...
    
    @property
    def is_composite(self) -> bool:
        """Returns ``True`` as this node can have child nodes."""
        ...
    
    @property
    def has_child_nodes(self) -> bool:
        """Returns ``True`` if this node has any child nodes."""
        ...
    
    @property
    def first_child(self) -> aspose.words.Node:
        """Gets the first child of the node.
        
        If there is no first child node, a ``None`` is returned."""
        ...
    
    @property
    def last_child(self) -> aspose.words.Node:
        """Gets the last child of the node.
        
        If there is no last child node, a ``None`` is returned."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of immediate children of this node."""
        ...
    
    ...

class ConditionalStyle:
    """Represents special formatting applied to some area of a table with assigned table style.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/python-net/working-with-tables/>` documentation article."""
    
    def clear_formatting(self) -> None:
        """Clears formatting of this conditional style."""
        ...
    
    @property
    def paragraph_format(self) -> aspose.words.ParagraphFormat:
        """Gets the paragraph formatting of the conditional style."""
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        """Gets the character formatting of the conditional style."""
        ...
    
    @property
    def shading(self) -> aspose.words.Shading:
        """Gets a :class:`Shading` object that refers to the shading formatting for this conditional style."""
        ...
    
    @property
    def borders(self) -> aspose.words.BorderCollection:
        """Gets the collection of default cell borders for the conditional style."""
        ...
    
    @property
    def left_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add to the left of the contents of table cells."""
        ...
    
    @left_padding.setter
    def left_padding(self, value: float):
        ...
    
    @property
    def right_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add to the right of the contents of table cells."""
        ...
    
    @right_padding.setter
    def right_padding(self, value: float):
        ...
    
    @property
    def top_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add above the contents of table cells."""
        ...
    
    @top_padding.setter
    def top_padding(self, value: float):
        ...
    
    @property
    def bottom_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add below the contents of table cells."""
        ...
    
    @bottom_padding.setter
    def bottom_padding(self, value: float):
        ...
    
    @property
    def type(self) -> aspose.words.ConditionalStyleType:
        """Gets table area to which this conditional style relates."""
        ...
    
    ...

class ConditionalStyleCollection:
    """Represents a collection of :class:`ConditionalStyle` objects.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/python-net/working-with-tables/>` documentation article.
    
    It is not possible to add or remove items from this collection. It contains permanent set of items: one item for
    each value of the :class:`ConditionalStyleType` enumeration type."""
    
    def __getitem__(self, index: int) -> aspose.words.ConditionalStyle:
        """Retrieves a :class:`ConditionalStyle` object by index.
        
        :param index: Zero-based index of the conditional style to retrieve."""
        ...
    
    def clear_formatting(self) -> None:
        """Clears all conditional styles of the table style."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of conditional styles in the collection."""
        ...
    
    @property
    def first_row(self) -> aspose.words.ConditionalStyle:
        """Gets the first row style."""
        ...
    
    @property
    def first_column(self) -> aspose.words.ConditionalStyle:
        """Gets the first column style."""
        ...
    
    @property
    def last_row(self) -> aspose.words.ConditionalStyle:
        """Gets the last row style."""
        ...
    
    @property
    def last_column(self) -> aspose.words.ConditionalStyle:
        """Gets the last column style."""
        ...
    
    @property
    def odd_row_banding(self) -> aspose.words.ConditionalStyle:
        """Gets the odd row banding style."""
        ...
    
    @property
    def odd_column_banding(self) -> aspose.words.ConditionalStyle:
        """Gets the odd column banding style."""
        ...
    
    @property
    def even_row_banding(self) -> aspose.words.ConditionalStyle:
        """Gets the even row banding style."""
        ...
    
    @property
    def even_column_banding(self) -> aspose.words.ConditionalStyle:
        """Gets the even column banding style."""
        ...
    
    @property
    def top_left_cell(self) -> aspose.words.ConditionalStyle:
        """Gets the top left cell style."""
        ...
    
    @property
    def top_right_cell(self) -> aspose.words.ConditionalStyle:
        """Gets the top right cell style."""
        ...
    
    @property
    def bottom_left_cell(self) -> aspose.words.ConditionalStyle:
        """Gets the bottom left cell style."""
        ...
    
    @property
    def bottom_right_cell(self) -> aspose.words.ConditionalStyle:
        """Gets the bottom right cell style."""
        ...
    
    ...

class ControlChar:
    """Control characters often encountered in documents.
    To learn more, visit the `Working With Control Characters <https://docs.aspose.com/words/python-net/working-with-control-characters/>` documentation article.
    
    Provides both char and string versions of the same constants. For example:
    string :attr:`ControlChar.LINE_BREAK` and char :attr:`ControlChar.LINE_BREAK_CHAR` have the same value."""
    
    CELL_CHAR: str
    
    TAB_CHAR: str
    
    LINE_FEED_CHAR: str
    
    LINE_BREAK_CHAR: str
    
    PAGE_BREAK_CHAR: str
    
    SECTION_BREAK_CHAR: str
    
    PARAGRAPH_BREAK_CHAR: str
    
    COLUMN_BREAK_CHAR: str
    
    FIELD_START_CHAR: str
    
    FIELD_SEPARATOR_CHAR: str
    
    FIELD_END_CHAR: str
    
    NON_BREAKING_HYPHEN_CHAR: str
    
    OPTIONAL_HYPHEN_CHAR: str
    
    SPACE_CHAR: str
    
    NON_BREAKING_SPACE_CHAR: str
    
    DEFAULT_TEXT_INPUT_CHAR: str
    
    CELL: str
    
    TAB: str
    
    LF: str
    
    LINE_FEED: str
    
    LINE_BREAK: str
    
    PAGE_BREAK: str
    
    SECTION_BREAK: str
    
    CR: str
    
    PARAGRAPH_BREAK: str
    
    COLUMN_BREAK: str
    
    CR_LF: str
    
    NON_BREAKING_SPACE: str
    
    ...

class ConvertUtil:
    """Provides helper functions to convert between various measurement units.
    To learn more, visit the `Convert Between Measurement Units <https://docs.aspose.com/words/python-net/convert-between-measurement-units/>` documentation article."""
    
    @overload
    @staticmethod
    def point_to_pixel(points: float) -> float:
        """Converts points to pixels at 96 dpi.
        
        :param points: The value to convert.
        
        1 inch equals 72 points."""
        ...
    
    @overload
    @staticmethod
    def point_to_pixel(points: float, resolution: float) -> float:
        """Converts points to pixels at the specified pixel resolution.
        
        :param points: The value to convert.
        :param resolution: The dpi (dots per inch) resolution.
        
        1 inch equals 72 points."""
        ...
    
    @overload
    @staticmethod
    def pixel_to_point(pixels: float) -> float:
        """Converts pixels to points at 96 dpi.
        
        :param pixels: The value to convert.
        
        1 inch equals 72 points."""
        ...
    
    @overload
    @staticmethod
    def pixel_to_point(pixels: float, resolution: float) -> float:
        """Converts pixels to points at the specified pixel resolution.
        
        :param pixels: The value to convert.
        :param resolution: The dpi (dots per inch) resolution.
        
        1 inch equals 72 points."""
        ...
    
    @staticmethod
    def pixel_to_new_dpi(pixels: float, old_dpi: float, new_dpi: float) -> int:
        """Converts pixels from one resolution to another.
        
        :param pixels: The value to convert.
        :param old_dpi: The current dpi (dots per inch) resolution.
        :param new_dpi: The new dpi (dots per inch) resolution."""
        ...
    
    @staticmethod
    def inch_to_point(inches: float) -> float:
        """Converts inches to points.
        
        :param inches: The value to convert.
        
        1 inch equals 72 points."""
        ...
    
    @staticmethod
    def point_to_inch(points: float) -> float:
        """Converts points to inches.
        
        :param points: The value to convert.
        
        1 inch equals 72 points."""
        ...
    
    @staticmethod
    def millimeter_to_point(millimeters: float) -> float:
        """Converts millimeters to points.
        
        :param millimeters: The value to convert.
        
        1 inch equals 25.4 millimeters. 1 inch equals 72 points."""
        ...
    
    ...

class Document(aspose.words.DocumentBase):
    """Represents a Word document.
    To learn more, visit the `Working with Document <https://docs.aspose.com/words/python-net/working-with-document/>` documentation article.
    
    The **Document** is a central object in the Aspose.Words library.
    
    To load an existing document in any of the :class:`LoadFormat` formats, pass a file name
    or a stream into one of the **Document** constructors. To create a blank document, call the
    constructor without parameters.
    
    Use one of the Save method overloads to save the document in any of the
    :class:`SaveFormat` formats.
    
    :attr:`Document.mail_merge` is the Aspose.Words's reporting engine that allows to populate
    reports designed in Microsoft Word with data from various data sources quickly and easily.
    
    **Document** stores document-wide information such as :attr:`DocumentBase.styles`,
    :attr:`Document.built_in_document_properties`, :attr:`Document.custom_document_properties`, lists and macros.
    Most of these objects are accessible via the corresponding properties of the **Document**.
    
    The **Document** is a root node of a tree that contains all other nodes of the document.
    The tree is a Composite design pattern and in many ways similar to XmlDocument.
    The content of the document can be manipulated freely programmatically:
    
    * The nodes of the document can be accessed via typed collections, for example :attr:`Document.sections`,
      :class:`ParagraphCollection` etc.
    
    * The nodes of the document can be selected by their node type using
      :meth:`CompositeNode.get_child_nodes`
      or using an XPath query with :meth:`CompositeNode.select_nodes` or :meth:`CompositeNode.select_single_node`.
    
    * Content nodes can be added or removed from anywhere in the document using
      :meth:`CompositeNode.insert_before`, :meth:`CompositeNode.insert_after`,
      :meth:`CompositeNode.remove_child` and other
      methods provided by the base class :class:`CompositeNode`.
    
    * The formatting attributes of each node can be changed via the properties of that node.
    
    Consider using :class:`DocumentBuilder` that simplifies the task of programmatically creating
    or populating the document tree.
    
    The **Document** can contain only :class:`Section` objects.
    
    In Microsoft Word, a valid document needs to have at least one section."""
    
    @overload
    def __init__(self):
        """Creates a blank Word document.
        
        A blank document is retrieved from resources, and by default, the resulting document looks more like created by :attr:`aspose.words.settings.MsWordVersion.WORD2007`.
        This blank document contains a default fonts table, minimal default styles, and latent styles.
        
        :meth:`aspose.words.settings.CompatibilityOptions.optimize_for` method can be used to optimize the document contents as well as default Aspose.Words behavior to a particular version of MS Word.
        
        The document paper size is Letter by default. If you want to change page setup, use
        :attr:`Section.page_setup`.
        
        After creation, you can use :class:`DocumentBuilder` to add document content easily."""
        ...
    
    @overload
    def __init__(self, file_name: str):
        """Opens an existing document from a file. Automatically detects the file format.
        
        :param file_name: File name of the document to open.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentException)): The name of the file cannot be null or empty string."""
        ...
    
    @overload
    def __init__(self, file_name: str, load_options: aspose.words.loading.LoadOptions):
        """Opens an existing document from a file. Allows to specify additional options such as an encryption password.
        
        :param file_name: File name of the document to open.
        :param load_options: Additional options to use when loading a document. Can be ``None``.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentException)): The name of the file cannot be null or empty string."""
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO):
        """Opens an existing document from a stream. Automatically detects the file format.
        
        The document must be stored at the beginning of the stream. The stream must support random positioning.
        
        :param stream: Stream where to load the document from.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentNullException)): The stream cannot be null.
        :raises RuntimeError (Proxy error(NotSupportedException)): The stream does not support reading or seeking.
        :raises RuntimeError (Proxy error(ObjectDisposedException)): The stream is a disposed object."""
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO, load_options: aspose.words.loading.LoadOptions):
        """Opens an existing document from a stream. Allows to specify additional options such as an encryption password.
        
        The document must be stored at the beginning of the stream. The stream must support random positioning.
        
        :param stream: The stream where to load the document from.
        :param load_options: Additional options to use when loading a document. Can be ``None``.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentNullException)): The stream cannot be null.
        :raises RuntimeError (Proxy error(NotSupportedException)): The stream does not support reading or seeking.
        :raises RuntimeError (Proxy error(ObjectDisposedException)): The stream is a disposed object."""
        ...
    
    @overload
    def clone(self) -> aspose.words.Document:
        """Performs a deep copy of the :class:`Document`.
        
        :returns: The cloned document."""
        ...
    
    @overload
    def clone(self, is_clone_children: bool) -> aspose.words.Node:
        """Performs a deep copy of the :class:`Document`.
        
        :returns: The cloned document."""
        ...
    
    @overload
    def append_document(self, src_doc: aspose.words.Document, import_format_mode: aspose.words.ImportFormatMode) -> None:
        """Appends the specified document to the end of this document.
        
        :param src_doc: The document to append.
        :param import_format_mode: Specifies how to merge style formatting that clashes."""
        ...
    
    @overload
    def append_document(self, src_doc: aspose.words.Document, import_format_mode: aspose.words.ImportFormatMode, import_format_options: aspose.words.ImportFormatOptions) -> None:
        """Appends the specified document to the end of this document.
        
        :param src_doc: The document to append.
        :param import_format_mode: Specifies how to merge style formatting that clashes.
        :param import_format_options: Allows to specify options that affect formatting of a result document."""
        ...
    
    @overload
    def save(self, file_name: str) -> aspose.words.saving.SaveOutputParameters:
        """Saves the document to a file. Automatically determines the save format from the extension.
        
        :param file_name: The name for the document. If a document with the
                          specified file name already exists, the existing document is overwritten.
        :returns: Additional information that you can optionally use."""
        ...
    
    @overload
    def save(self, file_name: str, save_format: aspose.words.SaveFormat) -> aspose.words.saving.SaveOutputParameters:
        """Saves the document to a file in the specified format.
        
        :param file_name: The name for the document. If a document with the
                          specified file name already exists, the existing document is overwritten.
        :param save_format: The format in which to save the document.
        :returns: Additional information that you can optionally use."""
        ...
    
    @overload
    def save(self, file_name: str, save_options: aspose.words.saving.SaveOptions) -> aspose.words.saving.SaveOutputParameters:
        """Saves the document to a file using the specified save options.
        
        :param file_name: The name for the document. If a document with the
                          specified file name already exists, the existing document is overwritten.
        :param save_options: Specifies the options that control how the document is saved. Can be ``None``.
        :returns: Additional information that you can optionally use."""
        ...
    
    @overload
    def save(self, stream: io.BytesIO, save_format: aspose.words.SaveFormat) -> aspose.words.saving.SaveOutputParameters:
        """Saves the document to a stream using the specified format.
        
        :param stream: Stream where to save the document.
        :param save_format: The format in which to save the document.
        :returns: Additional information that you can optionally use."""
        ...
    
    @overload
    def save(self, stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> aspose.words.saving.SaveOutputParameters:
        """Saves the document to a stream using the specified save options.
        
        :param stream: Stream where to save the document.
        :param save_options: Specifies the options that control how the document is saved. Can be ``None``.
                             If this is ``None``, the document will be saved in the binary DOC format.
        :returns: Additional information that you can optionally use."""
        ...
    
    @overload
    def protect(self, type: aspose.words.ProtectionType) -> None:
        """Protects the document from changes without changing the existing password or assigns a random password.
        
        When a document is protected, the user can make only limited changes,
        such as adding annotations, making revisions, or completing a form.
        
        When you protect a document, and the document already has a protection password,
        the existing protection password is not changed.
        
        When you protect a document, and the document does not have a protection password,
        this method assigns a random password that makes it impossible to unprotect the document
        in Microsoft Word, but you still can unprotect the document in Aspose.Words as it does not
        require a password when unprotecting.
        
        :param type: Specifies the protection type for the document."""
        ...
    
    @overload
    def protect(self, type: aspose.words.ProtectionType, password: str) -> None:
        """Protects the document from changes and optionally sets a protection password.
        
        When a document is protected, the user can make only limited changes,
        such as adding annotations, making revisions, or completing a form.
        
        Note that document protection is different from write protection.
        Write protection is specified using the :attr:`Document.write_protection`.
        
        :param type: Specifies the protection type for the document.
        :param password: The password to protect the document with.
                         Specify ``None`` or empty string if you want to protect the document without a password."""
        ...
    
    @overload
    def unprotect(self) -> None:
        """Removes protection from the document regardless of the password.
        
        This method unprotects the document even if it has a protection password.
        
        Note that document protection is different from write protection.
        Write protection is specified using the :attr:`Document.write_protection`."""
        ...
    
    @overload
    def unprotect(self, password: str) -> bool:
        """Removes protection from the document if a correct password is specified.
        
        This method unprotects the document only if a correct password is specified.
        
        Note that document protection is different from write protection.
        Write protection is specified using the :attr:`Document.write_protection`.
        
        :param password: The password to unprotect the document with.
        :returns: ``True`` if a correct password was specified and the document was unprotected."""
        ...
    
    @overload
    def update_word_count(self) -> None:
        """Updates word count properties of the document.
        
        :meth:`Document.update_word_count` recalculates and updates Characters, Words and Paragraphs
        properties in the :attr:`Document.built_in_document_properties` collection of the :class:`Document`.
        
        Note that :meth:`Document.update_word_count` does not update number of lines and pages properties.
        Use the :meth:`Document.update_word_count` overload and pass ``True`` value as a parameter to do that.
        
        When you use an evaluation version, the evaluation watermark will also be included
        in the word count."""
        ...
    
    @overload
    def update_word_count(self, update_lines_count: bool) -> None:
        """Updates word count properties of the document, optionally updates :attr:`aspose.words.properties.BuiltInDocumentProperties.lines` property.
        
        This method will rebuild page layout of the document.
        
        :param update_lines_count: ``True`` if number of lines in the document shall be calculated."""
        ...
    
    @overload
    def cleanup(self) -> None:
        """Cleans unused styles and lists from the document."""
        ...
    
    @overload
    def cleanup(self, options: aspose.words.CleanupOptions) -> None:
        """Cleans unused styles and lists from the document depending on given :class:`CleanupOptions`."""
        ...
    
    @overload
    def start_track_revisions(self, author: str, date_time: datetime.datetime) -> None:
        """Starts automatically marking all further changes you make to the document programmatically as revision changes.
        
        If you call this method and then make some changes to the document programmatically,
        save the document and later open the document in MS Word you will see these changes as revisions.
        
        Currently Aspose.Words supports tracking of node insertions and deletions only. Formatting changes are not
        recorded as revisions.
        
        Automatic tracking of changes is supported both when modifying this document through node manipulations
        as well as when using :class:`DocumentBuilder`
        
        This method does not change the :attr:`Document.track_revisions` option and does not use its value
        for the purposes of revision tracking.
        
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions."""
        ...
    
    @overload
    def start_track_revisions(self, author: str) -> None:
        """Starts automatically marking all further changes you make to the document programmatically as revision changes.
        
        If you call this method and then make some changes to the document programmatically,
        save the document and later open the document in MS Word you will see these changes as revisions.
        
        Currently Aspose.Words supports tracking of node insertions and deletions only. Formatting changes are not
        recorded as revisions.
        
        Automatic tracking of changes is supported both when modifying this document through node manipulations
        as well as when using :class:`DocumentBuilder`
        
        This method does not change the :attr:`Document.track_revisions` option and does not use its value
        for the purposes of revision tracking.
        
        :param author: Initials of the author to use for revisions."""
        ...
    
    @overload
    def compare(self, document: aspose.words.Document, author: str, date_time: datetime.datetime) -> None:
        """Compares this document with another document producing changes as number of edit and format revisions :class:`Revision`.
        
        :param document: Document to compare.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions.
        
        **NOTE**: Documents must not have revisions before comparison."""
        ...
    
    @overload
    def compare(self, document: aspose.words.Document, author: str, date_time: datetime.datetime, options: aspose.words.comparing.CompareOptions) -> None:
        """Compares this document with another document producing changes as a number of edit and format revisions :class:`Revision`.
        Allows to specify comparison options using :class:`aspose.words.comparing.CompareOptions`."""
        ...
    
    @overload
    def copy_styles_from_template(self, template: str) -> None:
        """Copies styles from the specified template to a document.
        
        When styles are copied from a template to a document,
        like-named styles in the document are redefined to match the style descriptions in the template.
        Unique styles from the template are copied to the document. Unique styles in the document remain intact."""
        ...
    
    @overload
    def copy_styles_from_template(self, template: aspose.words.Document) -> None:
        """Copies styles from the specified template to a document.
        
        When styles are copied from a template to a document,
        like-named styles in the document are redefined to match the style descriptions in the template.
        Unique styles from the template are copied to the document. Unique styles in the document remain intact."""
        ...
    
    @overload
    def update_thumbnail(self, options: aspose.words.rendering.ThumbnailGeneratingOptions) -> None:
        """Updates :attr:`aspose.words.properties.BuiltInDocumentProperties.thumbnail` of the document according to the specified options.
        
        The :class:`aspose.words.rendering.ThumbnailGeneratingOptions` allows you to specify the source of thumbnail, size and other options.
        If attempt to generate thumbnail fails, doesn't change one.
        
        :param options: The generating options to use."""
        ...
    
    @overload
    def update_thumbnail(self) -> None:
        """Updates :attr:`aspose.words.properties.BuiltInDocumentProperties.thumbnail` of the document using default options."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`DocumentVisitor.visit_document_start`, then calls :meth:`Node.accept` for all child nodes of the document
        and calls :meth:`DocumentVisitor.visit_document_end` at the end."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the start of the document.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the end of the document.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def ensure_minimum(self) -> None:
        """If the document contains no sections, creates one section with one paragraph."""
        ...
    
    def accept_all_revisions(self) -> None:
        """Accepts all tracked changes in the document.
        
        This method is a shortcut for :meth:`RevisionCollection.accept_all`."""
        ...
    
    def update_table_layout(self) -> None:
        """Implements an earlier approach to table column widths re-calculation that has known issues.
        
        The method is deprecated and it will be removed in a few releases."""
        ...
    
    def update_list_labels(self) -> None:
        """Updates list labels for all list items in the document.
        
        This method updates list label properties such as :attr:`aspose.words.lists.ListLabel.label_value` and
        :attr:`aspose.words.lists.ListLabel.label_string` for each :attr:`Paragraph.list_label` object in the document.
        
        Also, this method is sometimes implicitly called when updating fields in the document. This is required
        because some fields that may reference list numbers (such as TOC or REF) need them be up-to-date."""
        ...
    
    def update_actual_reference_marks(self) -> None:
        """Updates the :attr:`aspose.words.notes.Footnote.actual_reference_mark` property of all footnotes and endnotes in the document.
        
        Updating fields (:meth:`Document.update_fields`) may be necessary to get the correct result."""
        ...
    
    def remove_macros(self) -> None:
        """Removes all macros (the VBA project) as well as toolbars and command customizations from the document.
        
        By removing all macros from a document you can ensure the document contains no macro viruses."""
        ...
    
    def update_fields(self) -> None:
        """Updates the values of fields in the whole document.
        
        When you open, modify and then save a document, Aspose.Words does not update fields automatically, it keeps them intact.
        Therefore, you would usually want to call this method before saving if you have modified the document
        programmatically and want to make sure the proper (calculated) field values appear in the saved document.
        
        There is no need to update fields after executing a mail merge because mail merge is a kind of field update
        and automatically updates all fields in the document.
        
        This method does not update all field types. For the detailed list of supported field types, see the Programmers Guide.
        
        This method does not update fields that are related to the page layout algorithms (e.g. PAGE, PAGES, PAGEREF).
        The page layout-related fields are updated when you render a document or call :meth:`Document.update_page_layout`.
        
        Use the :meth:`Document.normalize_field_types` method before fields updating if there were document changes that affected field types.
        
        To update fields in a specific part of the document use :meth:`Range.update_fields`."""
        ...
    
    def unlink_fields(self) -> None:
        """Unlinks fields in the whole document.
        
        Replaces all the fields in the whole document with their most recent results.
        
        To unlink fields in a specific part of the document use :meth:`Range.unlink_fields`."""
        ...
    
    def normalize_field_types(self) -> None:
        """Changes field type values :attr:`aspose.words.fields.FieldChar.field_type` of :class:`aspose.words.fields.FieldStart`, :class:`aspose.words.fields.FieldSeparator`, :class:`aspose.words.fields.FieldEnd`
        in the whole document so that they correspond to the field types contained in the field codes.
        
        Use this method after document changes that affect field types.
        
        To change field type values in a specific part of the document use :meth:`Range.normalize_field_types`."""
        ...
    
    def join_runs_with_same_formatting(self) -> int:
        """Joins runs with same formatting in all paragraphs of the document.
        
        This is an optimization method. Some documents contain adjacent runs with same formatting.
        Usually this occurs if a document was intensively edited manually.
        You can reduce the document size and speed up further processing by joining these runs.
        
        The operation checks every :class:`Paragraph` node in the document for adjacent :class:`Run`
        nodes having identical properties. It ignores unique identifiers used to track editing sessions of run
        creation and modification. First run in every joining sequence accumulates all text. Remaining
        runs are deleted from the document.
        
        :returns: Number of joins performed. When **N** adjacent runs are being joined they count as **N - 1** joins."""
        ...
    
    def expand_table_styles_to_direct_formatting(self) -> None:
        """Converts formatting specified in table styles into direct formatting on tables in the document.
        
        This method exists because this version of Aspose.Words provides only limited support for
        table styles (see below). This method might be useful when you load a DOCX or WordprocessingML
        document that contains tables formatted with table styles and you need to query formatting of
        tables, cells, paragraphs or text.
        
        This version of Aspose.Words provides limited support for table styles as follows:
        
        * Table styles defined in DOCX or WordprocessingML documents are preserved as table styles
          when saving the document as DOCX or WordprocessingML.
        
        * Table styles defined in DOCX or WordprocessingML documents are automatically converted
          to direct formatting on tables when saving the document into any other format,
          rendering or printing.
        
        * Table styles defined in DOC documents are preserved as table styles when
          saving the document as DOC only."""
        ...
    
    def remove_external_schema_references(self) -> None:
        """Removes external XML schema references from this document."""
        ...
    
    def stop_track_revisions(self) -> None:
        """Stops automatic marking of document changes as revisions."""
        ...
    
    def update_page_layout(self) -> None:
        """Rebuilds the page layout of the document.
        
        This method formats a document into pages and updates the page number related fields in the document such
        as PAGE, PAGES, PAGEREF and REF. The up-to-date page layout information is required for a correct rendering of the document
        to fixed-page formats.
        
        This method is automatically invoked when you first convert a document to PDF, XPS, image or print it.
        However, if you modify the document after rendering and then attempt to render it again - Aspose.Words will not
        update the page layout automatically. In this case you should call :meth:`Document.update_page_layout` before
        rendering again."""
        ...
    
    def get_page_info(self, page_index: int) -> aspose.words.rendering.PageInfo:
        """Gets the page size, orientation and other information about a page that might be useful for printing or rendering.
        
        :param page_index: The 0-based page index."""
        ...
    
    def extract_pages(self, index: int, count: int) -> aspose.words.Document:
        """Returns the :class:`Document` object representing specified range of pages.
        
        The resulting document should look like the one in MS Word, as if we had performed 'Print specific pages' – the numbering,
        headers/footers and cross tables layout will be preserved.
        But due to a large number of nuances, appearing while reducing the number of pages, full match of the layout is a quiet complicated task requiring a lot of effort.
        Depending on the document complexity there might be slight differences in the resulting document contents layout comparing to the source document.
        Any feedback would be greatly appreciated.
        
        :param index: The zero-based index of the first page to extract.
        :param count: Number of pages to be extracted."""
        ...
    
    def remove_blank_pages(self) -> None:
        """Removes blank pages from the document.
        
        The resulting document will not contain pages considered to be blank while other content,
        including numbering, headers/footers and overall layout should remain unchanged.
        
        Page is considered to be blank when body of the page have no visible content, for example,
        empty table having no borders will be considered as invisible and therefore page will be detected as blank.
        
        :returns: List of page numbers has been considered as blank and removed."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.DOCUMENT`."""
        ...
    
    @property
    def attached_template(self) -> str:
        """Gets or sets the full path of the template attached to the document.
        
        Empty string means the document is attached to the Normal template.
        
        :raises RuntimeError (Proxy error(ArgumentNullException)): Throws if you attempt to set to a ``None`` value."""
        ...
    
    @attached_template.setter
    def attached_template(self, value: str):
        ...
    
    @property
    def automatically_update_styles(self) -> bool:
        """Gets or sets a flag indicating whether the styles in the document are updated to match the styles in the
        attached template each time the document is opened in MS Word."""
        ...
    
    @automatically_update_styles.setter
    def automatically_update_styles(self, value: bool):
        ...
    
    @property
    def shade_form_data(self) -> bool:
        """Specifies whether to turn on the gray shading on form fields."""
        ...
    
    @shade_form_data.setter
    def shade_form_data(self, value: bool):
        ...
    
    @property
    def track_revisions(self) -> bool:
        """True if changes are tracked when this document is edited in Microsoft Word.
        
        Setting this option only instructs Microsoft Word whether the track changes
        is turned on or off. This property has no effect on changes to the document that you make
        programmatically via Aspose.Words.
        
        If you want to automatically track changes as they are made programmatically by Aspose.Words
        to this document use the :meth:`Document.start_track_revisions` method."""
        ...
    
    @track_revisions.setter
    def track_revisions(self, value: bool):
        ...
    
    @property
    def show_grammatical_errors(self) -> bool:
        """Specifies whether to display grammar errors in this document."""
        ...
    
    @show_grammatical_errors.setter
    def show_grammatical_errors(self, value: bool):
        ...
    
    @property
    def show_spelling_errors(self) -> bool:
        """Specifies whether to display spelling errors in this document."""
        ...
    
    @show_spelling_errors.setter
    def show_spelling_errors(self, value: bool):
        ...
    
    @property
    def spelling_checked(self) -> bool:
        """Returns ``True`` if the document has been checked for spelling.
        
        To recheck the spelling in the document, set this property to ``False``."""
        ...
    
    @spelling_checked.setter
    def spelling_checked(self, value: bool):
        ...
    
    @property
    def grammar_checked(self) -> bool:
        """Returns ``True`` if the document has been checked for grammar.
        
        To recheck the grammar in the document, set this property to ``False``."""
        ...
    
    @grammar_checked.setter
    def grammar_checked(self, value: bool):
        ...
    
    @property
    def punctuation_kerning(self) -> bool:
        """Specifies whether kerning applies to both Latin text and punctuation."""
        ...
    
    @punctuation_kerning.setter
    def punctuation_kerning(self, value: bool):
        ...
    
    @property
    def built_in_document_properties(self) -> aspose.words.properties.BuiltInDocumentProperties:
        """Returns a collection that represents all the built-in document properties of the document."""
        ...
    
    @property
    def web_extension_task_panes(self) -> aspose.words.webextensions.TaskPaneCollection:
        """Returns a collection that represents a list of task pane add-ins."""
        ...
    
    @property
    def custom_document_properties(self) -> aspose.words.properties.CustomDocumentProperties:
        """Returns a collection that represents all the custom document properties of the document."""
        ...
    
    @property
    def mail_merge(self) -> aspose.words.mailmerging.MailMerge:
        """Returns a :class:`aspose.words.mailmerging.MailMerge` object that represents the mail merge functionality for the document."""
        ...
    
    @property
    def protection_type(self) -> aspose.words.ProtectionType:
        """Gets the currently active document protection type.
        
        This property allows to retrieve the currently set document protection type.
        To change the document protection type use the :meth:`Document.protect`
        and :meth:`Document.unprotect` methods.
        
        When a document is protected, the user can make only limited changes,
        such as adding annotations, making revisions, or completing a form.
        
        Note that document protection is different from write protection.
        Write protection is specified using the :attr:`Document.write_protection`"""
        ...
    
    @property
    def sections(self) -> aspose.words.SectionCollection:
        """Returns a collection that represents all sections in the document."""
        ...
    
    @property
    def first_section(self) -> aspose.words.Section:
        """Gets the first section in the document.
        
        Returns ``None`` if there are no sections."""
        ...
    
    @property
    def last_section(self) -> aspose.words.Section:
        """Gets the last section in the document.
        
        Returns ``None`` if there are no sections."""
        ...
    
    @property
    def view_options(self) -> aspose.words.settings.ViewOptions:
        """Provides options to control how the document is displayed in Microsoft Word."""
        ...
    
    @property
    def write_protection(self) -> aspose.words.settings.WriteProtection:
        """Provides access to the document write protection options."""
        ...
    
    @property
    def compatibility_options(self) -> aspose.words.settings.CompatibilityOptions:
        """Provides access to document compatibility options (that is, the user preferences entered on the **Compatibility**
        tab of the **Options** dialog in Word)."""
        ...
    
    @property
    def mail_merge_settings(self) -> aspose.words.settings.MailMergeSettings:
        """Gets or sets the object that contains all of the mail merge information for a document.
        
        You can use this object to specify a mail merge data source for a document and this information
        (along with the available data fields) will appear in Microsoft Word when the user opens this document.
        Or you can use this object to query mail merge settings that the user has specified in Microsoft Word
        for this document.
        
        This object is never ``None``."""
        ...
    
    @mail_merge_settings.setter
    def mail_merge_settings(self, value: aspose.words.settings.MailMergeSettings):
        ...
    
    @property
    def hyphenation_options(self) -> aspose.words.settings.HyphenationOptions:
        """Provides access to document hyphenation options."""
        ...
    
    @property
    def has_revisions(self) -> bool:
        """Returns ``True`` if the document has any tracked changes.
        
        This property is a shortcut for comparing :attr:`RevisionCollection.count` to zero."""
        ...
    
    @property
    def has_macros(self) -> bool:
        """Returns ``True`` if the document has a VBA project (macros)."""
        ...
    
    @property
    def watermark(self) -> aspose.words.Watermark:
        """Provides access to the document watermark."""
        ...
    
    @property
    def versions_count(self) -> int:
        """Gets the number of document versions that was stored in the DOC document.
        
        Versions in Microsoft Word are accessed via the File/Versions menu. Microsoft Word supports
        versions only for DOC files.
        
        This property allows to detect if there were document versions stored in this document
        before it was opened in Aspose.Words. Aspose.Words provides no other support for document versions.
        If you save this document using Aspose.Words, the document will be saved without versions."""
        ...
    
    @property
    def default_tab_stop(self) -> float:
        """Gets or sets the interval (in points) between the default tab stops."""
        ...
    
    @default_tab_stop.setter
    def default_tab_stop(self, value: float):
        ...
    
    @property
    def theme(self) -> aspose.words.themes.Theme:
        """Gets the :attr:`Document.theme` object for this document."""
        ...
    
    @property
    def custom_xml_parts(self) -> aspose.words.markup.CustomXmlPartCollection:
        """Gets or sets the collection of Custom XML Data Storage Parts.
        
        Aspose.Words loads and saves Custom XML Parts into OOXML and DOC documents only.
        
        This property cannot be ``None``."""
        ...
    
    @custom_xml_parts.setter
    def custom_xml_parts(self, value: aspose.words.markup.CustomXmlPartCollection):
        ...
    
    @property
    def package_custom_parts(self) -> aspose.words.markup.CustomPartCollection:
        """Gets or sets the collection of custom parts (arbitrary content) that are linked to the OOXML package using "unknown relationships".
        
        Do not confuse these custom parts with Custom XML Data. If you need to access Custom XML parts,
        use the :attr:`Document.custom_xml_parts` property.
        
        This collection contains OOXML parts whose parent is the OOXML package and they targets are of an "unknown relationship".
        For more information see :class:`aspose.words.markup.CustomPart`.
        
        Aspose.Words loads and saves custom parts into OOXML documents only.
        
        This property cannot be ``None``."""
        ...
    
    @package_custom_parts.setter
    def package_custom_parts(self, value: aspose.words.markup.CustomPartCollection):
        ...
    
    @property
    def variables(self) -> aspose.words.VariableCollection:
        """Returns the collection of variables added to a document or template."""
        ...
    
    @property
    def glossary_document(self) -> aspose.words.buildingblocks.GlossaryDocument:
        """Gets or sets the glossary document within this document or template. A glossary document is a storage
        for AutoText, AutoCorrect and Building Block entries defined in a document.
        
        This property returns ``None`` if the document does not have a glossary document.
        
        You can add a glossary document to a document by creating a
        :class:`aspose.words.buildingblocks.GlossaryDocument` object and assigning to this property."""
        ...
    
    @glossary_document.setter
    def glossary_document(self, value: aspose.words.buildingblocks.GlossaryDocument):
        ...
    
    @property
    def original_file_name(self) -> str:
        """Gets the original file name of the document.
        
        Returns ``None`` if the document was loaded from a stream or created blank."""
        ...
    
    @property
    def original_load_format(self) -> aspose.words.LoadFormat:
        """Gets the format of the original document that was loaded into this object.
        
        If you created a new blank document, returns the :attr:`LoadFormat.DOC` value."""
        ...
    
    @property
    def compliance(self) -> aspose.words.saving.OoxmlCompliance:
        """Gets the OOXML compliance version determined from the loaded document content.
        Makes sense only for OOXML documents.
        
        If you created a new blank document or load non OOXML document
        returns the :attr:`aspose.words.saving.OoxmlCompliance.ECMA376_2006` value."""
        ...
    
    @property
    def digital_signatures(self) -> aspose.words.digitalsignatures.DigitalSignatureCollection:
        """Gets the collection of digital signatures for this document and their validation results.
        
        This collection contains digital signatures that were loaded from the original document.
        These digital signatures will not be saved when you save this :class:`Document` object
        into a file or stream because saving or converting will produce a document that is different from the
        original and the original digital signatures will no longer be valid.
        
        This collection is never ``None``. If the document is not signed, it will contain zero elements."""
        ...
    
    @property
    def font_settings(self) -> aspose.words.fonts.FontSettings:
        """Gets or sets document font settings.
        
        This property allows to specify font settings per document. If set to ``None``, default static font settings
        :attr:`aspose.words.fonts.FontSettings.default_instance` will be used.
        
        The default value is ``None``."""
        ...
    
    @font_settings.setter
    def font_settings(self, value: aspose.words.fonts.FontSettings):
        ...
    
    @property
    def bibliography(self) -> aspose.words.bibliography.Bibliography:
        """Gets the :attr:`Document.bibliography` object that represents the list of sources available in the document."""
        ...
    
    @property
    def frameset(self) -> aspose.words.framesets.Frameset:
        """Returns a :attr:`Document.frameset` instance if this document represents a frames page.
        
        If the document is not framed, the property has the ``None`` value."""
        ...
    
    @property
    def include_textboxes_footnotes_endnotes_in_stat(self) -> bool:
        """Specifies whether to include textboxes, footnotes and endnotes in word count statistics."""
        ...
    
    @include_textboxes_footnotes_endnotes_in_stat.setter
    def include_textboxes_footnotes_endnotes_in_stat(self, value: bool):
        ...
    
    @property
    def page_count(self) -> int:
        """Gets the number of pages in the document as calculated by the most recent page layout operation."""
        ...
    
    @property
    def revisions(self) -> aspose.words.RevisionCollection:
        """Gets a collection of revisions (tracked changes) that exist in this document.
        
        The returned collection is a "live" collection, which means if you remove parts of a document that contain
        revisions, the deleted revisions will automatically disappear from this collection."""
        ...
    
    @property
    def layout_options(self) -> aspose.words.layout.LayoutOptions:
        """Gets a :class:`aspose.words.layout.LayoutOptions` object that represents options to control the layout process of this document."""
        ...
    
    @property
    def revisions_view(self) -> aspose.words.RevisionsView:
        """Gets or sets a value indicating whether to work with the original or revised version of a document.
        
        The default value is ****."""
        ...
    
    @revisions_view.setter
    def revisions_view(self, value: aspose.words.RevisionsView):
        ...
    
    @property
    def justification_mode(self) -> aspose.words.settings.JustificationMode:
        """Gets or sets the character spacing adjustment of a document."""
        ...
    
    @justification_mode.setter
    def justification_mode(self, value: aspose.words.settings.JustificationMode):
        ...
    
    @property
    def footnote_options(self) -> aspose.words.notes.FootnoteOptions:
        """Provides options that control numbering and positioning of footnotes in this document."""
        ...
    
    @property
    def endnote_options(self) -> aspose.words.notes.EndnoteOptions:
        """Provides options that control numbering and positioning of endnotes in this document."""
        ...
    
    @property
    def field_options(self) -> aspose.words.fields.FieldOptions:
        """Gets a :class:`aspose.words.fields.FieldOptions` object that represents options to control field handling in the document."""
        ...
    
    @property
    def remove_personal_information(self) -> bool:
        """Gets or sets a flag indicating that Microsoft Word will remove all user information from comments, revisions and
        document properties upon saving the document."""
        ...
    
    @remove_personal_information.setter
    def remove_personal_information(self, value: bool):
        ...
    
    @property
    def vba_project(self) -> aspose.words.vba.VbaProject:
        """Gets or sets a :attr:`Document.vba_project`."""
        ...
    
    @vba_project.setter
    def vba_project(self, value: aspose.words.vba.VbaProject):
        ...
    
    ...

class DocumentBase(aspose.words.CompositeNode):
    """Provides the abstract base class for a main document and a glossary document of a Word document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    Aspose.Words represents a Word document as a tree of nodes. :class:`DocumentBase` is a
    root node of the tree that contains all other nodes of the document.
    
    :class:`DocumentBase` also stores document-wide information such as :attr:`DocumentBase.styles` and
    :attr:`DocumentBase.lists` that the tree nodes might refer to."""
    
    @overload
    def import_node(self, src_node: aspose.words.Node, is_import_children: bool) -> aspose.words.Node:
        """Imports a node from another document to the current document.
        
        This method uses the :attr:`ImportFormatMode.USE_DESTINATION_STYLES` option to resolve formatting.
        
        Importing a node creates a copy of the source node belonging to the importing document.
        The returned node has no parent. The source node is not altered or removed from the original document.
        
        Before a node from another document can be inserted into this document, it must be imported.
        During import, document-specific properties such as references to styles and lists are translated
        from the original to the importing document. After the node was imported, it can be inserted
        into the appropriate place in the document using :meth:`CompositeNode.insert_before` or
        :meth:`CompositeNode.insert_after`.
        
        If the source node already belongs to the destination document, then simply a deep clone
        of the source node is created.
        
        :param src_node: The node being imported.
        :param is_import_children: ``True`` to import all child nodes recursively; otherwise, ``False``.
        :returns: The cloned node that belongs to the current document."""
        ...
    
    @overload
    def import_node(self, src_node: aspose.words.Node, is_import_children: bool, import_format_mode: aspose.words.ImportFormatMode) -> aspose.words.Node:
        """Imports a node from another document to the current document with an option to control formatting.
        
        This overload is useful to control how styles and list formatting are imported.
        
        Importing a node creates a copy of the source node belonging to the importing document.
        The returned node has no parent. The source node is not altered or removed from the original document.
        
        Before a node from another document can be inserted into this document, it must be imported.
        During import, document-specific properties such as references to styles and lists are translated
        from the original to the importing document. After the node was imported, it can be inserted
        into the appropriate place in the document using :meth:`CompositeNode.insert_before` or
        :meth:`CompositeNode.insert_after`.
        
        If the source node already belongs to the destination document, then simply a deep clone
        of the source node is created.
        
        :param src_node: The node to imported.
        :param is_import_children: ``True`` to import all child nodes recursively; otherwise, ``False``.
        :param import_format_mode: Specifies how to merge style formatting that clashes.
        :returns: The cloned, imported node. The node belongs to the destination document, but has no parent."""
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        """Gets this instance."""
        ...
    
    @property
    def node_changing_callback(self) -> aspose.words.INodeChangingCallback:
        """Called when a node is inserted or removed in the document."""
        ...
    
    @node_changing_callback.setter
    def node_changing_callback(self, value: aspose.words.INodeChangingCallback):
        ...
    
    @property
    def resource_loading_callback(self) -> aspose.words.loading.IResourceLoadingCallback:
        """Allows to control how external resources are loaded."""
        ...
    
    @resource_loading_callback.setter
    def resource_loading_callback(self, value: aspose.words.loading.IResourceLoadingCallback):
        ...
    
    @property
    def font_infos(self) -> aspose.words.fonts.FontInfoCollection:
        """Provides access to properties of fonts used in this document.
        
        This collection of font definitions is loaded as is from the document.
        Font definitions might be optional, missing or incomplete in some documents.
        
        Do not rely on this collection to ascertain that a particular font is used in the document.
        You should only use this collection to get information about fonts that might be used in the document."""
        ...
    
    @property
    def styles(self) -> aspose.words.StyleCollection:
        """Returns a collection of styles defined in the document.
        
        For more information see the description of the :class:`StyleCollection` class."""
        ...
    
    @property
    def lists(self) -> aspose.words.lists.ListCollection:
        """Provides access to the list formatting used in the document.
        
        For more information see the description of the :class:`aspose.words.lists.ListCollection` class."""
        ...
    
    @property
    def warning_callback(self) -> aspose.words.IWarningCallback:
        """Called during various document processing procedures when an issue is detected that might result
        in data or formatting fidelity loss.
        
        Document may generate warnings at any stage of its existence, so it's important to setup warning callback as
        early as possible to avoid the warnings loss. E.g. such properties as :attr:`Document.page_count`
        actually build the document layout which is used later for rendering, and the layout warnings may be lost if
        warning callback is specified just for the rendering calls later."""
        ...
    
    @warning_callback.setter
    def warning_callback(self, value: aspose.words.IWarningCallback):
        ...
    
    @property
    def footnote_separators(self) -> aspose.words.notes.FootnoteSeparatorCollection:
        """Provides access to the footnote/endnote separators defined in the document."""
        ...
    
    @property
    def background_shape(self) -> aspose.words.drawing.Shape:
        """Gets or sets the background shape of the document. Can be ``None``.
        
        Microsoft Word allows only a shape that has its :attr:`aspose.words.drawing.ShapeBase.shape_type` property equal
        to :attr:`aspose.words.drawing.ShapeType.RECTANGLE` to be used as a background shape for a document.
        
        Microsoft Word supports only the fill properties of a background shape. All other properties
        are ignored.
        
        Setting this property to a non-null value will also set the :attr:`aspose.words.settings.ViewOptions.display_background_shape` to ``True``."""
        ...
    
    @background_shape.setter
    def background_shape(self, value: aspose.words.drawing.Shape):
        ...
    
    @property
    def page_color(self) -> aspose.pydrawing.Color:
        """Gets or sets the page color of the document. This property is a simpler version of :attr:`DocumentBase.background_shape`.
        
        This property provides a simple way to specify a solid page color for the document.
        Setting this property creates and sets an appropriate :attr:`DocumentBase.background_shape`.
        
        If the page color is not set (e.g. there is no background shape in the document) returns
        aspose.pydrawing.Color.empty."""
        ...
    
    @page_color.setter
    def page_color(self, value: aspose.pydrawing.Color):
        ...
    
    ...

class DocumentBuilder:
    """Provides methods to insert text, images and other content, specify font, paragraph and section formatting.
    To learn more, visit the `Document Builder Overview <https://docs.aspose.com/words/python-net/document-builder-overview/>` documentation article.
    
    :class:`DocumentBuilder` makes the process of building a :class:`Document` easier.
    :class:`Document` is a composite object consisting of a tree of nodes and while inserting content
    nodes directly into the tree is possible, it requires good understanding of the tree structure.
    :class:`DocumentBuilder` is a "facade" for the complex structure of :class:`Document` and allows
    to insert content and formatting quickly and easily.
    
    Create a :class:`DocumentBuilder` and associate it with a :class:`Document`.
    
    The :class:`DocumentBuilder` has an internal cursor where the text will be inserted
    when you call :meth:`DocumentBuilder.write`, :meth:`DocumentBuilder.writeln`, :meth:`DocumentBuilder.insert_break`
    and other methods. You can navigate the :class:`DocumentBuilder` cursor to a different location
    in a document using various MoveToXXX methods.
    
    Use the :attr:`DocumentBuilder.font` property to specify character formatting that will apply to
    all text inserted from the current position in the document onwards.
    
    Use the :attr:`DocumentBuilder.paragraph_format` property to specify paragraph formatting for the current
    and all paragraphs that will be inserted.
    
    Use the :attr:`DocumentBuilder.page_setup` property to specify page and section properties for the current
    section and all section that will be inserted.
    
    Use the :attr:`DocumentBuilder.cell_format` and :attr:`DocumentBuilder.row_format` properties to specify
    formatting properties for table cells and rows. User the :meth:`DocumentBuilder.insert_cell` and
    :meth:`DocumentBuilder.end_row` methods to build a table.
    
    Note that :attr:`DocumentBuilder.font`, :attr:`DocumentBuilder.paragraph_format` and :attr:`DocumentBuilder.page_setup` properties are updated whenever
    you navigate to a different place in the document to reflect formatting properties available at the new location."""
    
    @overload
    def __init__(self):
        """Initializes a new instance of this class.
        
        Creates a new :class:`DocumentBuilder` object and attaches it to a new :class:`Document` object."""
        ...
    
    @overload
    def __init__(self, options: aspose.words.DocumentBuilderOptions):
        """Initializes a new instance of this class.
        
        Creates a new :class:`DocumentBuilder` object and attaches it to a new :class:`Document` object.
        Additional document building options can be specified."""
        ...
    
    @overload
    def __init__(self, doc: aspose.words.Document):
        """Initializes a new instance of this class.
        
        Creates a new :class:`DocumentBuilder` object, attaches to the specified :class:`Document` object.
        The cursor is positioned at the beginning of the document.
        
        :param doc: The :class:`Document` object to attach to."""
        ...
    
    @overload
    def __init__(self, doc: aspose.words.Document, options: aspose.words.DocumentBuilderOptions):
        """Initializes a new instance of this class.
        
        Creates a new :class:`DocumentBuilder` object, attaches to the specified :class:`Document` object.
        The cursor is positioned at the beginning of the document.
        
        :param doc: The :class:`Document` object to attach to.
        :param options: Additional options for the document building process."""
        ...
    
    @overload
    def move_to_merge_field(self, field_name: str) -> bool:
        """Moves the cursor to a position just beyond the specified merge field and removes the merge field.
        
        Note that this method deletes the merge field from the document after moving the cursor.
        
        :param field_name: The case-insensitive name of the mail merge field.
        :returns: ``True`` if the merge field was found and the cursor was moved; ``False`` otherwise."""
        ...
    
    @overload
    def move_to_merge_field(self, field_name: str, is_after: bool, is_delete_field: bool) -> bool:
        """Moves the merge field to the specified merge field.
        
        :param field_name: The case-insensitive name of the mail merge field.
        :param is_after: When ``True``, moves the cursor to be after the field end.
                         When ``False``, moves the cursor to be before the field start.
        :param is_delete_field: When ``True``, deletes the merge field.
        :returns: ``True`` if the merge field was found and the cursor was moved; ``False`` otherwise."""
        ...
    
    @overload
    def move_to_bookmark(self, bookmark_name: str) -> bool:
        """Moves the cursor to a bookmark.
        
        Moves the cursor to a position just after the start of the bookmark with the
        specified name.
        
        The comparison is not case-sensitive. If the bookmark was not found, ``False`` is
        returned and the cursor is not moved.
        
        Inserting new text does not replace existing text of the bookmark.
        
        Note that some bookmarks in the document are assigned to form fields.
        Moving to such a bookmark and inserting text there inserts the text into the
        form field code. Although this will not invalidate the form field, the inserted
        text will not be visible because it becomes part of the field code.
        
        :param bookmark_name: The name of the bookmark to move the cursor to.
        :returns: ``True`` if the bookmark was found; ``False`` otherwise."""
        ...
    
    @overload
    def move_to_bookmark(self, bookmark_name: str, is_start: bool, is_after: bool) -> bool:
        """Moves the cursor to a bookmark with greater precision.
        
        Moves the cursor to a position before or after the bookmark start or end.
        
        If desired position is not at inline level, moves to the next paragraph.
        
        The comparison is not case-sensitive. If the bookmark was not found, ``False`` is
        returned and the cursor is not moved.
        
        :param bookmark_name: The name of the bookmark to move the cursor to.
        :param is_start: When ``True``, moves the cursor to the beginning of the bookmark.
                         When ``False``, moves the cursor to the end of the bookmark.
        :param is_after: When ``True``, moves the cursor to be after the bookmark
                         start or end position. When ``False``, moves the cursor to be before the bookmark
                         start or end position.
        :returns: ``True`` if the bookmark was found; ``False`` otherwise."""
        ...
    
    @overload
    def move_to_structured_document_tag(self, structured_document_tag_index: int, character_index: int) -> None:
        """Moves the cursor to a structured document tag in the current section.
        
        The navigation is performed inside the current story of the current section. That is, if you moved the
        cursor to the primary header of the first section, then *structuredDocumentTagIndex*
        specified the index of the structured document tag inside that header of that section.
        
        When *structuredDocumentTagIndex* is greater than or equal to 0, it specifies an index
        from the beginning of the section with 0 being the first structured document tag. When*structuredDocumentTagIndex* is less than 0, it specified an index from the end of the
        section with -1 being the last structured document tag.
        
        :param structured_document_tag_index: The index of the structured document tag to move to.
        :param character_index: The index of the character inside the structured document tag.
                                A negative value allows you to specify a position from the end of the structured document tag. Use -1 to
                                move to the end of the structured document tag. If the structured document tag is at the block level, and
                                you want to move the cursor to the end of its last paragraph, specify -2."""
        ...
    
    @overload
    def move_to_structured_document_tag(self, structured_document_tag: aspose.words.markup.StructuredDocumentTag, character_index: int) -> None:
        """Moves the cursor to the structured document tag.
        
        :param structured_document_tag: The structured document tag to move to.
        :param character_index: The index of the character inside the structured document tag.
                                A negative value allows you to specify a position from the end of the structured document tag. Use -1 to
                                move to the end of the structured document tag. If the structured document tag is at the block level, and
                                you want to move the cursor to the end of its last paragraph, specify -2."""
        ...
    
    @overload
    def writeln(self, text: str) -> None:
        """Inserts a string and a paragraph break into the document.
        
        Current font and paragraph formatting specified by the :attr:`DocumentBuilder.font` and :attr:`DocumentBuilder.paragraph_format` properties are used.
        
        :param text: The string to insert into the document."""
        ...
    
    @overload
    def writeln(self) -> None:
        """Inserts a paragraph break into the document.
        
        Calls :meth:`DocumentBuilder.insert_paragraph`."""
        ...
    
    @overload
    def insert_field(self, field_type: aspose.words.fields.FieldType, update_field: bool) -> aspose.words.fields.Field:
        """Inserts a Word field into a document and optionally updates the field result.
        
        This method inserts a field into a document.
        Aspose.Words can update fields of most types, but not all. For more details see the
        :meth:`DocumentBuilder.insert_field` overload.
        
        :param field_type: The type of the field to append.
        :param update_field: Specifies whether to update the field immediately.
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    @overload
    def insert_field(self, field_code: str) -> aspose.words.fields.Field:
        """Inserts a Word field into a document and updates the field result.
        
        This method inserts a field into a document and updates the field result immediately.
        Aspose.Words can update fields of most types, but not all. For more details see the
        :meth:`DocumentBuilder.insert_field` overload.
        
        :param field_code: The field code to insert (without curly braces).
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    @overload
    def insert_field(self, field_code: str, field_value: str) -> aspose.words.fields.Field:
        """Inserts a Word field into a document without updating the field result.
        
        Fields in Microsoft Word documents consist of a field code and a field result.
        The field code is like a formula and the field result is like the value that
        the formula produces. The field code may also contain field switches
        that are like additional instructions to perform a specific action.
        
        You can switch between displaying field codes and results in your document in
        Microsoft Word using the keyboard shortcut Alt+F9. Field codes appear between curly braces ( { } ).
        
        To create a field, you need to specify a field type, field code and a "placeholder" field value.
        If you are not sure about a particular field code syntax, create the field in Microsoft Word first
        and switch to see its field code.
        
        Aspose.Words can calculate field results for most of the field types, but this method
        does not update the field result automatically. Because the field result is not calculated automatically,
        you are expected to pass some string value (or even an empty string) that will be inserted into the field result.
        This value will remain in the field result as a placeholder until the field is updated.
        To update the field result you can call :meth:`aspose.words.fields.Field.update` on the field object returned
        to you or :meth:`Document.update_fields` to update fields in the whole document.
        
        :param field_code: The field code to insert (without curly braces).
        :param field_value: The field value to insert. Pass ``None`` for fields that do not have a value.
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    @overload
    def insert_check_box(self, name: str, checked_value: bool, size: int) -> aspose.words.fields.FormField:
        """Inserts a checkbox form field at the current position.
        
        If you specify a name for the form field, then a bookmark is automatically created with the same name.
        
        :param name: The name of the form field. Can be an empty string. The value longer than 20 characters will be truncated.
        :param checked_value: Checked status of the checkbox form field.
        :param size: Specifies the size of the checkbox in points. Specify 0 for MS Word
                     to calculate the size of the checkbox automatically.
        :returns: The form field node that was just inserted."""
        ...
    
    @overload
    def insert_check_box(self, name: str, default_value: bool, checked_value: bool, size: int) -> aspose.words.fields.FormField:
        """Inserts a checkbox form field at the current position.
        
        If you specify a name for the form field, then a bookmark is automatically created with the same name.
        
        :param name: The name of the form field. Can be an empty string. The value longer than 20 characters will be truncated.
        :param default_value: Default value of the checkbox form field.
        :param checked_value: Current checked status of the checkbox form field.
        :param size: Specifies the size of the checkbox in points. Specify 0 for MS Word
                     to calculate the size of the checkbox automatically.
        :returns: The form field node that was just inserted."""
        ...
    
    @overload
    def insert_footnote(self, footnote_type: aspose.words.notes.FootnoteType, footnote_text: str) -> aspose.words.notes.Footnote:
        """Inserts a footnote or endnote into the document.
        
        :param footnote_type: Specifies whether to insert a footnote or an endnote.
        :param footnote_text: Specifies the text of the footnote.
        :returns: Returns a footnote object that was just created."""
        ...
    
    @overload
    def insert_footnote(self, footnote_type: aspose.words.notes.FootnoteType, footnote_text: str, reference_mark: str) -> aspose.words.notes.Footnote:
        """Inserts a footnote or endnote into the document.
        
        :param footnote_type: Specifies whether to insert a footnote or an endnote.
        :param footnote_text: Specifies the text of the footnote.
        :param reference_mark: Specifies the custom reference mark of the footnote.
        :returns: Returns a footnote object that was just created."""
        ...
    
    @overload
    def insert_image(self, file_name: str) -> aspose.words.drawing.Shape:
        """Inserts an image from a file or URL into the document. The image is inserted inline and at 100% scale.
        
        :param file_name: The file with the image. Can be any valid local or remote URI.
        :returns: The image node that was just inserted.
        
        This overload will automatically download the image before inserting into the document
        if you specify a remote URI.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, stream: io.BytesIO) -> aspose.words.drawing.Shape:
        """Inserts an image from a stream into the document. The image is inserted inline and at 100% scale.
        
        :param stream: The stream that contains the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, image_bytes: bytes) -> aspose.words.drawing.Shape:
        """Inserts an image from a byte array into the document. The image is inserted inline and at 100% scale.
        
        :param image_bytes: The byte array that contains the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, file_name: str, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts an inline image from a file or URL into the document and scales it to the specified size.
        
        :param file_name: The file that contains the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, stream: io.BytesIO, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts an inline image from a stream into the document and scales it to the specified size.
        
        :param stream: The stream that contains the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, image_bytes: bytes, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts an inline image from a byte array into the document and scales it to the specified size.
        
        :param image_bytes: The byte array that contains the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, file_name: str, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts an image from a file or URL at the specified position and size.
        
        :param file_name: The file that contains the image.
        :param horz_pos: Specifies where the distance to the image is measured from.
        :param left: Distance in points from the origin to the left side of the image.
        :param vert_pos: Specifies where the distance to the image measured from.
        :param top: Distance in points from the origin to the top side of the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :param wrap_type: Specifies how to wrap text around the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, stream: io.BytesIO, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts an image from a stream at the specified position and size.
        
        :param stream: The stream that contains the image.
        :param horz_pos: Specifies where the distance to the image is measured from.
        :param left: Distance in points from the origin to the left side of the image.
        :param vert_pos: Specifies where the distance to the image measured from.
        :param top: Distance in points from the origin to the top side of the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :param wrap_type: Specifies how to wrap text around the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_image(self, image_bytes: bytes, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts an image from a byte array at the specified position and size.
        
        :param image_bytes: The byte array that contains the image.
        :param horz_pos: Specifies where the distance to the image is measured from.
        :param left: Distance in points from the origin to the left side of the image.
        :param vert_pos: Specifies where the distance to the image measured from.
        :param top: Distance in points from the origin to the top side of the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :param wrap_type: Specifies how to wrap text around the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_ole_object(self, stream: io.BytesIO, prog_id: str, as_icon: bool, presentation: io.BytesIO) -> aspose.words.drawing.Shape:
        """Inserts an embedded OLE object from a stream into the document.
        
        :param stream: Stream containing application data.
        :param prog_id: Programmatic Identifier of OLE object.
        :param as_icon: Specifies either Iconic or Normal mode of OLE object being inserted.
        :param presentation: Image presentation of OLE object. If value is ``None`` Aspose.Words will use one of the predefined images.
        :returns: Shape node containing Ole object and inserted at the current Builder position."""
        ...
    
    @overload
    def insert_ole_object(self, file_name: str, is_linked: bool, as_icon: bool, presentation: io.BytesIO) -> aspose.words.drawing.Shape:
        """Inserts an embedded or linked OLE object from a file into the document. Detects OLE object type using file extension.
        
        :param file_name: Full path to the file.
        :param is_linked: If ``True`` then linked OLE object is inserted otherwise embedded OLE object is inserted.
        :param as_icon: Specifies either Iconic or Normal mode of OLE object being inserted.
        :param presentation: Image presentation of OLE object. If value is ``None`` Aspose.Words will use one of the predefined images.
        :returns: Shape node containing Ole object and inserted at the current Builder position."""
        ...
    
    @overload
    def insert_ole_object(self, file_name: str, prog_id: str, is_linked: bool, as_icon: bool, presentation: io.BytesIO) -> aspose.words.drawing.Shape:
        """Inserts an embedded or linked OLE object from a file into the document. Detects OLE object type using given progID parameter.
        
        :param file_name: Full path to the file.
        :param prog_id: ProgId of OLE object.
        :param is_linked: If ``True`` then linked OLE object is inserted otherwise embedded OLE object is inserted.
        :param as_icon: Specifies either Iconic or Normal mode of OLE object being inserted.
        :param presentation: Image presentation of OLE object. If value is ``None`` Aspose.Words will use one of the predefined images.
        :returns: Shape node containing Ole object and inserted at the current Builder position."""
        ...
    
    @overload
    def insert_ole_object_as_icon(self, file_name: str, is_linked: bool, icon_file: str, icon_caption: str) -> aspose.words.drawing.Shape:
        """Inserts an embedded or linked OLE object as icon into the document.
        Allows to specify icon file and caption. Detects OLE object type using file extension.
        
        :param file_name: Full path to the file.
        :param is_linked: If ``True`` then linked OLE object is inserted otherwise embedded OLE object is inserted.
        :param icon_file: Full path to the ICO file. If the value is ``None``, Aspose.Words will use a predefined image.
        :param icon_caption: Icon caption. If the value is ``None``, Aspose.Words will use the file name.
        :returns: Shape node containing Ole object and inserted at the current Builder position."""
        ...
    
    @overload
    def insert_ole_object_as_icon(self, file_name: str, prog_id: str, is_linked: bool, icon_file: str, icon_caption: str) -> aspose.words.drawing.Shape:
        """Inserts an embedded or linked OLE object as icon into the document.
        Allows to specify icon file and caption. Detects OLE object type using given progID parameter.
        
        :param file_name: Full path to the file.
        :param prog_id: ProgId of OLE object.
        :param is_linked: If ``True`` then linked OLE object is inserted otherwise embedded OLE object is inserted.
        :param icon_file: Full path to the ICO file. If the value is ``None``, Aspose.Words will use a predefined image.
        :param icon_caption: Icon caption. If the value is ``None``, Aspose.Words will use the file name.
        :returns: Shape node containing Ole object and inserted at the current Builder position."""
        ...
    
    @overload
    def insert_ole_object_as_icon(self, stream: io.BytesIO, prog_id: str, icon_file: str, icon_caption: str) -> aspose.words.drawing.Shape:
        """Inserts an embedded OLE object as icon from a stream into the document.
        Allows to specify icon file and caption. Detects OLE object type using given progID parameter.
        
        :param stream: Stream containing application data.
        :param prog_id: ProgId of OLE object.
        :param icon_file: Full path to the ICO file. If the value is ``None``, Aspose.Words will use a predefined image.
        :param icon_caption: Icon caption. If the value is ``None``, Aspose.Words will use the a predefined icon caption.
        :returns: Shape node containing Ole object and inserted at the current Builder position."""
        ...
    
    @overload
    def insert_html(self, html: str) -> None:
        """Inserts an HTML string into the document.
        
        :param html: An HTML string to insert into the document.
        
        You can use this method to insert an HTML fragment or whole HTML document."""
        ...
    
    @overload
    def insert_html(self, html: str, use_builder_formatting: bool) -> None:
        """Inserts an HTML string into the document.
        
        :param html: An HTML string to insert into the document.
        :param use_builder_formatting: A value indicating whether formatting specified in :class:`DocumentBuilder`
                                       is used as base formatting for text imported from HTML.
        
        You can use this method to insert an HTML fragment or whole HTML document.
        
        When *useBuilderFormatting* is``False``,
        :class:`DocumentBuilder` formating is ignored and formatting of inserted text
        is based on default HTML formatting. As a result, the text looks as it is rendered in browsers.
        
        When *useBuilderFormatting* is``True``,
        formatting of inserted text is based on :class:`DocumentBuilder` formatting,
        and the text looks as if it were inserted with :meth:`DocumentBuilder.write`."""
        ...
    
    @overload
    def insert_html(self, html: str, options: aspose.words.HtmlInsertOptions) -> None:
        """Inserts an HTML string into the document. Allows to specify additional options.
        
        :param html: An HTML string to insert into the document.
        :param options: Options that are used when HTML string is inserted.
        
        You can use this method to insert an HTML fragment or whole HTML document."""
        ...
    
    @overload
    def insert_shape(self, shape_type: aspose.words.drawing.ShapeType, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts inline shape with specified type and size.
        
        :param shape_type: The shape type to insert into the document.
        :param width: The width of the shape in points.
        :param height: The height of the shape in points.
        :returns: The shape node that was inserted."""
        ...
    
    @overload
    def insert_shape(self, shape_type: aspose.words.drawing.ShapeType, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts free-floating shape with specified position, size and text wrap type.
        
        :param shape_type: The shape type to insert into the document
        :param horz_pos: Specifies where the horizontal distance to the shape is measured from.
        :param left: Distance in points from the origin to the left side of the shape.
        :param vert_pos: Specifies where the vertical distance to the shape is measured from.
        :param top: Distance in points from the origin to the top side of the shape.
        :param width: The width of the shape in points.
        :param height: The height of the shape in points.
        :param wrap_type: Specifies how to wrap text around the shape.
        :returns: The shape node that was inserted."""
        ...
    
    @overload
    def insert_group_shape(self, shapes: List[aspose.words.drawing.Shape]) -> aspose.words.drawing.GroupShape:
        """Groups the shapes passed as a parameter into a new GroupShape node which is inserted into the current position.
        
        :param shapes: The list of shapes to be grouped.
        
        The position and dimension of the new GroupShape will be calculated automatically.
        
        VML and DML shapes cannot be grouped together."""
        ...
    
    @overload
    def insert_group_shape(self, left: float, top: float, width: float, height: float, shapes: List[aspose.words.drawing.Shape]) -> aspose.words.drawing.GroupShape:
        """Groups the shapes passed as a parameter into a new GroupShape node of the specified size which is inserted into the specified position.
        
        :param left: Distance in points from the origin to the left side of the group shape.
        :param top: Distance in points from the origin to the top side of the group shape.
        :param width: The width of the group shape in points. A negative value is not allowed.
        :param height: The height of the group shape in points. A negative value is not allowed.
        :param shapes: The list of shapes to be grouped.
        
        VML and DML shapes cannot be grouped together."""
        ...
    
    @overload
    def insert_chart(self, chart_type: aspose.words.drawing.charts.ChartType, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts an chart object into the document and scales it to the specified size.
        
        :param chart_type: The chart type to insert into the document.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_chart(self, chart_type: aspose.words.drawing.charts.ChartType, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts an chart object into the document and scales it to the specified size.
        
        :param chart_type: The chart type to insert into the document.
        :param horz_pos: Specifies where the distance to the image is measured from.
        :param left: Distance in points from the origin to the left side of the image.
        :param vert_pos: Specifies where the distance to the image measured from.
        :param top: Distance in points from the origin to the top side of the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :param wrap_type: Specifies how to wrap text around the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_online_video(self, video_url: str, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts an online video object into the document and scales it to the specified size.
        
        :param video_url: The URL to the video.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method.
        
        Insertion of online video from the following resources is supported:
        
        * https://www.youtube.com/
        
        * https://vimeo.com/
        
        If your online video is not displaying correctly, use :meth:`DocumentBuilder.insert_online_video`, which accepts custom embedded html code.
        
        The code for embedding video can vary between providers, consult your corresponding provider of choice for details."""
        ...
    
    @overload
    def insert_online_video(self, video_url: str, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts an online video object into the document and scales it to the specified size.
        
        :param video_url: The URL to the video.
        :param horz_pos: Specifies where the distance to the image is measured from.
        :param left: Distance in points from the origin to the left side of the image.
        :param vert_pos: Specifies where the distance to the image measured from.
        :param top: Distance in points from the origin to the top side of the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :param wrap_type: Specifies how to wrap text around the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method.
        
        Insertion of online video from the following resources is supported:
        
        * https://www.youtube.com/
        
        * https://vimeo.com/
        
        If your online video is not displaying correctly, use :meth:`DocumentBuilder.insert_online_video`, which accepts custom embedded html code.
        
        The code for embedding video can vary between providers, consult your corresponding provider of choice for details."""
        ...
    
    @overload
    def insert_online_video(self, video_url: str, video_embed_code: str, thumbnail_image_bytes: bytes, width: float, height: float) -> aspose.words.drawing.Shape:
        """Inserts an online video object into the document and scales it to the specified size.
        
        :param video_url: The URL to the video.
        :param video_embed_code: The embed code for the video.
        :param thumbnail_image_bytes: The thumbnail image bytes.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_online_video(self, video_url: str, video_embed_code: str, thumbnail_image_bytes: bytes, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, width: float, height: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts an online video object into the document and scales it to the specified size.
        
        :param video_url: The URL to the video.
        :param video_embed_code: The embed code for the video.
        :param thumbnail_image_bytes: The thumbnail image bytes.
        :param horz_pos: Specifies where the distance to the image is measured from.
        :param left: Distance in points from the origin to the left side of the image.
        :param vert_pos: Specifies where the distance to the image measured from.
        :param top: Distance in points from the origin to the top side of the image.
        :param width: The width of the image in points. Can be a negative or zero value to request 100% scale.
        :param height: The height of the image in points. Can be a negative or zero value to request 100% scale.
        :param wrap_type: Specifies how to wrap text around the image.
        :returns: The image node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def insert_signature_line(self, signature_line_options: aspose.words.SignatureLineOptions) -> aspose.words.drawing.Shape:
        """Inserts a signature line at the current position.
        
        :param signature_line_options: The object that stores parameters of creating signature line.
        :returns: The signature line node that was just inserted."""
        ...
    
    @overload
    def insert_signature_line(self, signature_line_options: aspose.words.SignatureLineOptions, horz_pos: aspose.words.drawing.RelativeHorizontalPosition, left: float, vert_pos: aspose.words.drawing.RelativeVerticalPosition, top: float, wrap_type: aspose.words.drawing.WrapType) -> aspose.words.drawing.Shape:
        """Inserts a signature line at the specified position.
        
        :param signature_line_options: The object that stores parameters of creating signature line.
        :param horz_pos: Specifies where the distance to the signature line is measured from.
        :param left: Distance in points from the origin to the left side of the signature line.
        :param vert_pos: Specifies where the distance to the signature line measured from.
        :param top: Distance in points from the origin to the top side of the signature line.
        :param wrap_type: Specifies how to wrap text around the signature line.
        :returns: The signature line node that was just inserted.
        
        You can change the image size, location, positioning method and other settings using the
        :class:`aspose.words.drawing.Shape` object returned by this method."""
        ...
    
    @overload
    def end_editable_range(self) -> aspose.words.EditableRangeEnd:
        """Marks the current position in the document as an editable range end.
        
        Editable range in a document can overlap and span any range. To create a valid editable range you need to
        call both :meth:`DocumentBuilder.start_editable_range` and :meth:`DocumentBuilder.end_editable_range`
        or :meth:`DocumentBuilder.end_editable_range` methods.
        
        Badly formed editable range will be ignored when the document is saved.
        
        :returns: The editable range end node that was just created."""
        ...
    
    @overload
    def end_editable_range(self, start: aspose.words.EditableRangeStart) -> aspose.words.EditableRangeEnd:
        """Marks the current position in the document as an editable range end.
        
        Use this overload during creating nested editable ranges.
        
        Editable range in a document can overlap and span any range. To create a valid editable range you need to
        call both :meth:`DocumentBuilder.start_editable_range` and :meth:`DocumentBuilder.end_editable_range`
        or :meth:`DocumentBuilder.end_editable_range` methods.
        
        Badly formed editable range will be ignored when the document is saved.
        
        :param start: This editable range start.
        :returns: The editable range end node that was just created."""
        ...
    
    @overload
    def insert_document(self, src_doc: aspose.words.Document, import_format_mode: aspose.words.ImportFormatMode) -> aspose.words.Node:
        """Inserts a document at the cursor position.
        
        This method mimics the MS Word behavior, as if CTRL+'A' (select all content) was pressed,
        then CTRL+'C' (copy selected into the buffer) inside one document
        and then CTRL+'V' (insert content from the buffer) inside another document.
        
        :param src_doc: Source document for inserting.
        :param import_format_mode: Specifies how to merge style formatting that clashes.
        :returns: First node of the inserted content."""
        ...
    
    @overload
    def insert_document(self, src_doc: aspose.words.Document, import_format_mode: aspose.words.ImportFormatMode, import_format_options: aspose.words.ImportFormatOptions) -> aspose.words.Node:
        """Inserts a document at the cursor position.
        
        This method mimics the MS Word behavior, as if CTRL+'A' (select all content) was pressed,
        then CTRL+'C' (copy selected into the buffer) inside one document
        and then CTRL+'V' (insert content from the buffer) inside another document.
        
        :param src_doc: Source document for inserting.
        :param import_format_mode: Specifies how to merge style formatting that clashes.
        :param import_format_options: Allows to specify options that affect formatting of a result document.
        :returns: First node of the inserted content."""
        ...
    
    def move_to_document_start(self) -> None:
        """Moves the cursor to the beginning of the document."""
        ...
    
    def move_to_document_end(self) -> None:
        """Moves the cursor to the end of the document."""
        ...
    
    def move_to_section(self, section_index: int) -> None:
        """Moves the cursor to the beginning of the body in a specified section.
        
        When *sectionIndex* is greater than or equal to 0, it specifies an index from
        the beginning of the document with 0 being the first section. When*sectionIndex* is less than 0,
        it specified an index from the end of the document with -1 being the last section.
        
        The cursor is moved to the first paragraph in the :class:`Body` of the specified section.
        
        :param section_index: The index of the section to move to."""
        ...
    
    def move_to_header_footer(self, header_footer_type: aspose.words.HeaderFooterType) -> None:
        """Moves the cursor to the beginning of a header or footer in the current section.
        
        After you moved the cursor into a header or footer, you can use the rest of :class:`DocumentBuilder`
        methods to modify the contents of the header or footer.
        
        If you want to create headers and footers different for the first page, you need
        to set :attr:`PageSetup.different_first_page_header_footer`.
        
        If you want to create headers and footers different for even and odd pages, you need
        to set :attr:`PageSetup.odd_and_even_pages_header_footer`.
        
        Use :meth:`DocumentBuilder.move_to_section` to move out of the header into the main text.
        
        :param header_footer_type: Specifies the header or footer to move to."""
        ...
    
    def move_to_field(self, field: aspose.words.fields.Field, is_after: bool) -> None:
        """Moves the cursor to a field in the document.
        
        :param field: The field to move the cursor to.
        :param is_after: When ``True``, moves the cursor to be after the field end.
                         When ``False``, moves the cursor to be before the field start."""
        ...
    
    def move_to_paragraph(self, paragraph_index: int, character_index: int) -> None:
        """Moves the cursor to a paragraph in the current section.
        
        The navigation is performed inside the current story of the current section.
        That is, if you moved the cursor to the primary header of the first section,
        then *paragraphIndex* specified the index of the paragraph inside that header
        of that section.
        
        When *paragraphIndex* is greater than or equal to 0, it specifies an index from
        the beginning of the section with 0 being the first paragraph. When*paragraphIndex* is less than 0,
        it specified an index from the end of the section with -1 being the last paragraph.
        
        :param paragraph_index: The index of the paragraph to move to.
        :param character_index: The index of the character inside the paragraph.
                                A negative value allows you to specify a position from the end of the paragraph. Use -1 to move to the end of
                                the paragraph."""
        ...
    
    def move_to_cell(self, table_index: int, row_index: int, column_index: int, character_index: int) -> None:
        """Moves the cursor to a table cell in the current section.
        
        The navigation is performed inside the current story of the current section.
        
        For the index parameters, when index is greater than or equal to 0, it specifies an index from
        the beginning with 0 being the first element. When index is less than 0, it specified an index from
        the end with -1 being the last element.
        
        :param table_index: The index of the table to move to.
        :param row_index: The index of the row in the table.
        :param column_index: The index of the column in the table.
        :param character_index: The index of the character inside the cell.
                                A negative value allows you to specify a position from the end of the cell. Use -1 to move to the end of
                                the cell."""
        ...
    
    def move_to(self, node: aspose.words.Node) -> None:
        """Moves the cursor to an inline node or to the end of a paragraph.
        
        When *node* is an inline-level node, the cursor is moved to this node
        and further content will be inserted before that node.
        
        When *node* is a :class:`Paragraph`, the cursor is moved to the end of the paragraph
        and further content will be inserted just before the paragraph break.
        
        When *node* is a block-level node but not a :class:`Paragraph`, the cursor is moved to the end of the first paragraph into block-level node
        and further content will be inserted just before the paragraph break.
        
        :param node: The node must be a paragraph or a direct child of a paragraph."""
        ...
    
    def delete_row(self, table_index: int, row_index: int) -> aspose.words.tables.Row:
        """Deletes a row from a table.
        
        If the cursor is inside the row that is being deleted, the cursor is moved
        out to the next row or to the next paragraph after the table.
        
        If you delete a row from a table that contains only one row, the whole
        table is deleted.
        
        For the index parameters, when index is greater than or equal to 0, it specifies an index from
        the beginning with 0 being the first element. When index is less than 0, it specified an index from
        the end with -1 being the last element.
        
        :param table_index: The index of the table.
        :param row_index: The index of the row in the table.
        :returns: The row node that was just removed."""
        ...
    
    def write(self, text: str) -> None:
        """Inserts a string into the document at the current insert position.
        
        Current font formatting specified by the :attr:`DocumentBuilder.font` property is used.
        
        :param text: The string to insert into the document."""
        ...
    
    def insert_paragraph(self) -> aspose.words.Paragraph:
        """Inserts a paragraph break into the document.
        
        Current paragraph formatting specified by the :attr:`DocumentBuilder.paragraph_format` property is used.
        
        Breaks the current paragraph in two. After inserting the paragraph, the cursor is placed at the beginning of the new paragraph.
        
        An exception is thrown if it is not possible to insert a paragraph break at the current cursor position.
        
        :returns: The paragraph node that was just inserted. It is the same node as :attr:`DocumentBuilder.current_paragraph`."""
        ...
    
    def insert_structured_document_tag(self, type: aspose.words.markup.SdtType) -> aspose.words.markup.StructuredDocumentTag:
        """Inserts a :class:`aspose.words.markup.StructuredDocumentTag` into the document.
        
        :returns: The :class:`aspose.words.markup.StructuredDocumentTag` node that was just inserted."""
        ...
    
    def insert_style_separator(self) -> None:
        """Inserts style separator into the document.
        
        This method allows to apply different paragraph styles to two different parts of a text line."""
        ...
    
    def insert_break(self, break_type: aspose.words.BreakType) -> None:
        """Inserts a break of the specified type into the document.
        
        Use this method to insert paragraph, page, column, section or line break into the document.
        
        :param break_type: Specifies the type of the break to insert."""
        ...
    
    def insert_table_of_contents(self, switches: str) -> aspose.words.fields.Field:
        """Inserts a TOC (table of contents) field into the document.
        
        This method inserts a TOC (table of contents) field into the document at
        the current position.
        
        A table of contents in a Word document can be built in a number of ways
        and formatted using a variety of options. The way the table is built and
        displayed by Microsoft Word is controlled by the field switches.
        
        The easiest way to specify the switches is to insert and configure a table of
        contents into a Word document using the Insert-\>Reference-\>Index and Tables menu,
        then switch display of field codes on to see the switches. You can press Alt+F9 in
        Microsoft Word to toggle display of field codes on or off.
        
        For example, after creating a table of contents, the following field is inserted
        into the document: **{ TOC \\o "1-3" \\h \\z \\u }**.
        You can copy **\\o "1-3" \\h \\z \\u** and use it as the switches parameter.
        
        Note that :meth:`DocumentBuilder.insert_table_of_contents` will only insert a TOC field, but
        will not actually build the table of contents. The table of contents is built by
        Microsoft Word when the field is updated.
        
        If you insert a table of contents using this method and then open the file
        in Microsoft Word, you will not see the table of contents because the TOC field
        has not yet been updated.
        
        In Microsoft Word, fields are not automatically updated when a document is opened,
        but you can update fields in a document at any time by pressing F9.
        
        :param switches: The TOC field switches."""
        ...
    
    def insert_hyperlink(self, display_text: str, url_or_bookmark: str, is_bookmark: bool) -> aspose.words.fields.Field:
        """Inserts a hyperlink into the document.
        
        Note that you need to specify font formatting for the hyperlink display text explicitly
        using the :attr:`DocumentBuilder.font` property.
        
        This methods internally calls :meth:`DocumentBuilder.insert_field` to insert an MS Word HYPERLINK field
        into the document.
        
        :param display_text: Text of the link to be displayed in the document.
        :param url_or_bookmark: Link destination. Can be a url or a name of a bookmark inside the document.
                                This method always adds apostrophes at the beginning and end of the url.
        :param is_bookmark: ``True`` if the previous parameter is a name of a bookmark inside the document;
                            ``False`` is the previous parameter is a URL.
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    def insert_text_input(self, name: str, type: aspose.words.fields.TextFormFieldType, format: str, field_value: str, max_length: int) -> aspose.words.fields.FormField:
        """Inserts a text form field at the current position.
        
        If you specify a name for the form field, then a bookmark is automatically created with the same name.
        
        :param name: The name of the form field. Can be an empty string.
        :param type: Specifies the type of the text form field.
        :param format: Format string used to format the value of the form field.
        :param field_value: Text that will be shown in the field.
        :param max_length: Maximum length the user can enter into the form field. Set to zero for unlimited length.
        :returns: The form field node that was just inserted."""
        ...
    
    def insert_combo_box(self, name: str, items: List[str], selected_index: int) -> aspose.words.fields.FormField:
        """Inserts a combobox form field at the current position.
        
        If you specify a name for the form field, then a bookmark is automatically created with the same name.
        
        :param name: The name of the form field. Can be an empty string. The value longer than 20 characters will be truncated.
        :param items: The items of the ComboBox. Maximum is 25 items.
        :param selected_index: The index of the selected item in the ComboBox.
        :returns: The form field node that was just inserted."""
        ...
    
    def insert_horizontal_rule(self) -> aspose.words.drawing.Shape:
        """Inserts a horizontal rule shape into the document.
        
        :returns: The shape that is a horizontal rule."""
        ...
    
    def insert_cell(self) -> aspose.words.tables.Cell:
        """Inserts a table cell into the document.
        
        To start a table, just call :meth:`DocumentBuilder.insert_cell`. After this, any content you add using
        other methods of the :class:`DocumentBuilder` class will be added to the current cell.
        
        To start a new cell in the same row, call :meth:`DocumentBuilder.insert_cell` again.
        
        To end a table row call :meth:`DocumentBuilder.end_row`.
        
        Use the :attr:`DocumentBuilder.cell_format` property to specify cell formatting.
        
        :returns: The cell node that was just inserted."""
        ...
    
    def start_table(self) -> aspose.words.tables.Table:
        """Starts a table in the document.
        
        The next method to call is :meth:`DocumentBuilder.insert_cell`.
        
        This method starts a nested table when called inside a cell.
        
        :returns: The table node that was just created."""
        ...
    
    def end_table(self) -> aspose.words.tables.Table:
        """Ends a table in the document.
        
        This method should be called only once after :meth:`DocumentBuilder.end_row` was called. When called,
        :meth:`DocumentBuilder.end_table` moves the cursor out of the current cell to point just after the table.
        
        :returns: The table node that was just finished."""
        ...
    
    def end_row(self) -> aspose.words.tables.Row:
        """Ends a table row in the document.
        
        Call :meth:`DocumentBuilder.end_row` to end a table row. If you call :meth:`DocumentBuilder.insert_cell` immediately
        after that, then the table continues on a new row.
        
        Use the :attr:`DocumentBuilder.row_format` property to specify row formatting.
        
        :returns: The row node that was just finished."""
        ...
    
    def start_bookmark(self, bookmark_name: str) -> aspose.words.BookmarkStart:
        """Marks the current position in the document as a bookmark start.
        
        Bookmarks in a document can overlap and span any range. To create a valid bookmark you need to
        call both :meth:`DocumentBuilder.start_bookmark` and :meth:`DocumentBuilder.end_bookmark` with the same *bookmarkName*
        parameter.
        
        Badly formed bookmarks or bookmarks with duplicate names will be ignored when the document is saved.
        
        :param bookmark_name: Name of the bookmark.
        :returns: The bookmark start node that was just created."""
        ...
    
    def end_bookmark(self, bookmark_name: str) -> aspose.words.BookmarkEnd:
        """Marks the current position in the document as a bookmark end.
        
        Bookmarks in a document can overlap and span any range. To create a valid bookmark you need to
        call both :meth:`DocumentBuilder.start_bookmark` and :meth:`DocumentBuilder.end_bookmark` with the same *bookmarkName*
        parameter.
        
        Badly formed bookmarks or bookmarks with duplicate names will be ignored when the document is saved.
        
        :param bookmark_name: Name of the bookmark.
        :returns: The bookmark end node that was just created."""
        ...
    
    def start_column_bookmark(self, bookmark_name: str) -> aspose.words.BookmarkStart:
        """Marks the current position in the document as a column bookmark start. The position must be in a table cell.
        
        A column bookmark covers one or more columns in a range of rows. To create a valid bookmark you
        need to call both :meth:`DocumentBuilder.start_column_bookmark` and :meth:`DocumentBuilder.end_column_bookmark` with the same
        *bookmarkName* parameter.
        
        Badly formed bookmarks or bookmarks with duplicate names will be ignored when the document is saved.
        
        The actual position of the inserted :class:`BookmarkStart` node may differ from the current document
        builder position.
        
        :param bookmark_name: Name of the bookmark.
        :returns: The bookmark start node that was just created."""
        ...
    
    def end_column_bookmark(self, bookmark_name: str) -> aspose.words.BookmarkEnd:
        """Marks the current position in the document as a column bookmark end. The position must be in a table cell.
        
        A column bookmark covers one or more columns in a range of rows. To create a valid bookmark you
        need to call both :meth:`DocumentBuilder.start_column_bookmark` and :meth:`DocumentBuilder.end_column_bookmark` with the same
        *bookmarkName* parameter.
        
        Badly formed bookmarks or bookmarks with duplicate names will be ignored when the document is saved.
        
        The actual position of the inserted :class:`BookmarkEnd` node may differ from the current document
        builder position.
        
        :param bookmark_name: Name of the bookmark.
        :returns: The bookmark end node that was just created."""
        ...
    
    def start_editable_range(self) -> aspose.words.EditableRangeStart:
        """Marks the current position in the document as an editable range start.
        
        Editable range in a document can overlap and span any range. To create a valid editable range you need to
        call both :meth:`DocumentBuilder.start_editable_range` and :meth:`DocumentBuilder.end_editable_range`
        or :meth:`DocumentBuilder.end_editable_range` methods.
        
        Badly formed editable range will be ignored when the document is saved.
        
        :returns: The editable range start node that was just created."""
        ...
    
    def insert_document_inline(self, src_doc: aspose.words.Document, import_format_mode: aspose.words.ImportFormatMode, import_format_options: aspose.words.ImportFormatOptions) -> aspose.words.Node:
        """Inserts a document inline at the cursor position.
        
        This method mimics the MS Word behavior, as if CTRL+'A' (select all content) was pressed,
        then CTRL+'C' (copy selected into the buffer) inside one document
        and then CTRL+'V' (insert content from the buffer) inside another document.
        
        As a difference from :meth:`DocumentBuilder.insert_document`
        this method moves the content of the paragraph of the destination document,
        before which the source document is inserted, into the last
        paragraph of the inserted source document. Actually, this means that
        paragraph break of the last inserted paragraph is removed.
        
        Note, if the last node of the source document is not a paragraph, then nothing will be done.
        
        :param src_doc: Source document for inserting.
        :param import_format_mode: Specifies how to merge style formatting that clashes.
        :param import_format_options: Allows to specify options that affect formatting of a result document.
        :returns: First node of the inserted content."""
        ...
    
    def push_font(self) -> None:
        """Saves current character formatting onto the stack."""
        ...
    
    def pop_font(self) -> None:
        """Retrieves character formatting previously saved on the stack."""
        ...
    
    def insert_node(self, node: aspose.words.Node) -> None:
        """Inserts a node before the cursor."""
        ...
    
    @property
    def document(self) -> aspose.words.Document:
        """Gets or sets the :attr:`DocumentBuilder.document` object that this object is attached to."""
        ...
    
    @document.setter
    def document(self, value: aspose.words.Document):
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        """Returns an object that represents current font formatting properties.
        
        Use :attr:`DocumentBuilder.font` to access and modify font formatting properties.
        
        Specify font formatting before inserting text."""
        ...
    
    @property
    def bold(self) -> bool:
        """True if the font is formatted as bold."""
        ...
    
    @bold.setter
    def bold(self, value: bool):
        ...
    
    @property
    def italic(self) -> bool:
        """True if the font is formatted as italic."""
        ...
    
    @italic.setter
    def italic(self, value: bool):
        ...
    
    @property
    def underline(self) -> aspose.words.Underline:
        """Gets/sets underline type for the current font."""
        ...
    
    @underline.setter
    def underline(self, value: aspose.words.Underline):
        ...
    
    @property
    def paragraph_format(self) -> aspose.words.ParagraphFormat:
        """Returns an object that represents current paragraph formatting properties."""
        ...
    
    @property
    def list_format(self) -> aspose.words.lists.ListFormat:
        """Returns an object that represents current list formatting properties."""
        ...
    
    @property
    def page_setup(self) -> aspose.words.PageSetup:
        """Returns an object that represents current page setup and section properties."""
        ...
    
    @property
    def row_format(self) -> aspose.words.tables.RowFormat:
        """Returns an object that represents current table row formatting properties."""
        ...
    
    @property
    def cell_format(self) -> aspose.words.tables.CellFormat:
        """Returns an object that represents current table cell formatting properties."""
        ...
    
    @property
    def is_at_start_of_paragraph(self) -> bool:
        """Returns ``True`` if the cursor is at the beginning of the current paragraph (no text before the cursor)."""
        ...
    
    @property
    def is_at_end_of_paragraph(self) -> bool:
        """Returns ``True`` if the cursor is at the end of the current paragraph."""
        ...
    
    @property
    def is_at_end_of_structured_document_tag(self) -> bool:
        """Returns **true** if the cursor is at the end of a structured document tag."""
        ...
    
    @property
    def current_node(self) -> aspose.words.Node:
        """Gets the node that is currently selected in this DocumentBuilder.
        
        :attr:`DocumentBuilder.current_node` is a cursor of :class:`DocumentBuilder` and points to a :class:`Node`
        that is a direct child of a :class:`Paragraph`. Any insert operations you perform using
        :class:`DocumentBuilder` will insert before the :attr:`DocumentBuilder.current_node`.
        
        When the current paragraph is empty or the cursor is positioned just
        before the end of a paragraph or structured document tag, :attr:`DocumentBuilder.current_node` returns ``None``."""
        ...
    
    @property
    def current_paragraph(self) -> aspose.words.Paragraph:
        """Gets the paragraph that is currently selected in this :class:`DocumentBuilder`.
        
        :attr:`DocumentBuilder.current_node`"""
        ...
    
    @property
    def current_structured_document_tag(self) -> aspose.words.markup.StructuredDocumentTag:
        """Gets the structured document tag that is currently selected in this :class:`DocumentBuilder`."""
        ...
    
    @property
    def current_story(self) -> aspose.words.Story:
        """Gets the story that is currently selected in this :class:`DocumentBuilder`."""
        ...
    
    @property
    def current_section(self) -> aspose.words.Section:
        """Gets the section that is currently selected in this :class:`DocumentBuilder`."""
        ...
    
    ...

class DocumentBuilderOptions:
    """Allows to specify additional options for the document building process."""
    
    def __init__(self):
        ...
    
    @property
    def context_table_formatting(self) -> bool:
        """True if the formatting applied to table content does not affect the formatting of the content that follows it.
        Default value is ``True``."""
        ...
    
    @context_table_formatting.setter
    def context_table_formatting(self, value: bool):
        ...
    
    ...

class DocumentReaderPluginLoadException(RuntimeError):
    """Thrown during document load, when the plugin required for reading the document format cannot be loaded."""
    
    ...

class DocumentVisitor:
    """Base class for custom document visitors.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    With :class:`DocumentVisitor` you can define and execute custom operations
    that require enumeration over the document tree.
    
    For example, Aspose.Words uses :class:`DocumentVisitor` internally for saving :class:`Document`
    in various formats and for other operations like finding fields or bookmarks over
    a fragment of a document.
    
    To use :class:`DocumentVisitor`:
    
    1. Create a class derived from :class:`DocumentVisitor`.
    
    1. Override and provide implementations for some or all of the VisitXXX methods
       to perform some custom operations.
    
    1. Call :meth:`Node.accept` on the :class:`Node` that
       you want to start the enumeration from.
    
    :class:`DocumentVisitor` provides default implementations for all of the VisitXXX methods
    to make it easier to create new document visitors as only the methods required for the particular
    visitor need to be overridden. It is not necessary to override all of the visitor methods.
    
    For more information see the Visitor design pattern."""
    
    def visit_document_start(self, doc: aspose.words.Document) -> aspose.words.VisitorAction:
        """Called when enumeration of the document has started.
        
        :param doc: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_document_end(self, doc: aspose.words.Document) -> aspose.words.VisitorAction:
        """Called when enumeration of the document has finished.
        
        :param doc: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_section_start(self, section: aspose.words.Section) -> aspose.words.VisitorAction:
        """Called when enumeration of a section has started.
        
        :param section: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_section_end(self, section: aspose.words.Section) -> aspose.words.VisitorAction:
        """Called when enumeration of a section has ended.
        
        :param section: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_body_start(self, body: aspose.words.Body) -> aspose.words.VisitorAction:
        """Called when enumeration of the main text story in a section has started.
        
        :param body: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_body_end(self, body: aspose.words.Body) -> aspose.words.VisitorAction:
        """Called when enumeration of the main text story in a section has ended.
        
        :param body: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_header_footer_start(self, header_footer: aspose.words.HeaderFooter) -> aspose.words.VisitorAction:
        """Called when enumeration of a header or footer in a section has started.
        
        :param header_footer: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_header_footer_end(self, header_footer: aspose.words.HeaderFooter) -> aspose.words.VisitorAction:
        """Called when enumeration of a header or footer in a section has ended.
        
        :param header_footer: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_paragraph_start(self, paragraph: aspose.words.Paragraph) -> aspose.words.VisitorAction:
        """Called when enumeration of a paragraph has started.
        
        :param paragraph: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_paragraph_end(self, paragraph: aspose.words.Paragraph) -> aspose.words.VisitorAction:
        """Called when enumeration of a paragraph has ended.
        
        :param paragraph: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_table_start(self, table: aspose.words.tables.Table) -> aspose.words.VisitorAction:
        """Called when enumeration of a table has started.
        
        :param table: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_table_end(self, table: aspose.words.tables.Table) -> aspose.words.VisitorAction:
        """Called when enumeration of a table has ended.
        
        :param table: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_row_start(self, row: aspose.words.tables.Row) -> aspose.words.VisitorAction:
        """Called when enumeration of a table row has started.
        
        :param row: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_row_end(self, row: aspose.words.tables.Row) -> aspose.words.VisitorAction:
        """Called when enumeration of a table row has ended.
        
        :param row: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_cell_start(self, cell: aspose.words.tables.Cell) -> aspose.words.VisitorAction:
        """Called when enumeration of a table cell has started.
        
        :param cell: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_cell_end(self, cell: aspose.words.tables.Cell) -> aspose.words.VisitorAction:
        """Called when enumeration of a table cell has ended.
        
        :param cell: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_run(self, run: aspose.words.Run) -> aspose.words.VisitorAction:
        """Called when a run of text in the is encountered.
        
        :param run: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_field_start(self, field_start: aspose.words.fields.FieldStart) -> aspose.words.VisitorAction:
        """Called when a field starts in the document.
        
        A field in a Word document consists of a field code and field value.
        
        For example, a field that displays a page number can be represented as follows:
        
        [FieldStart]PAGE[FieldSeparator]98[FieldEnd]
        
        The field separator separates field code from field value in the document. Note that some
        fields have only field code and do not have field separator and field value.
        
        Fields can be nested.
        
        :param field_start: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_field_separator(self, field_separator: aspose.words.fields.FieldSeparator) -> aspose.words.VisitorAction:
        """Called when a field separator is encountered in the document.
        
        The field separator separates field code from field value in the document. Note that some
        fields have only field code and do not have field separator and field value.
        
        For more info see :meth:`DocumentVisitor.visit_field_start`
        
        :param field_separator: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_field_end(self, field_end: aspose.words.fields.FieldEnd) -> aspose.words.VisitorAction:
        """Called when a field ends in the document.
        
        For more info see :meth:`DocumentVisitor.visit_field_start`
        
        :param field_end: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_form_field(self, form_field: aspose.words.fields.FormField) -> aspose.words.VisitorAction:
        """Called when a form field is encountered in the document.
        
        :param form_field: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_bookmark_start(self, bookmark_start: aspose.words.BookmarkStart) -> aspose.words.VisitorAction:
        """Called when a start of a bookmark is encountered in the document.
        
        :param bookmark_start: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_bookmark_end(self, bookmark_end: aspose.words.BookmarkEnd) -> aspose.words.VisitorAction:
        """Called when an end of a bookmark is encountered in the document.
        
        :param bookmark_end: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_footnote_start(self, footnote: aspose.words.notes.Footnote) -> aspose.words.VisitorAction:
        """Called when enumeration of a footnote or endnote text has started.
        
        :param footnote: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_footnote_end(self, footnote: aspose.words.notes.Footnote) -> aspose.words.VisitorAction:
        """Called when enumeration of a footnote or endnote text has ended.
        
        :param footnote: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_comment_start(self, comment: aspose.words.Comment) -> aspose.words.VisitorAction:
        """Called when enumeration of a comment text has started.
        
        :param comment: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_comment_end(self, comment: aspose.words.Comment) -> aspose.words.VisitorAction:
        """Called when enumeration of a comment text has ended.
        
        :param comment: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_editable_range_start(self, editable_range_start: aspose.words.EditableRangeStart) -> aspose.words.VisitorAction:
        """Called when a start of an editable range is encountered in the document.
        
        :param editable_range_start: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_editable_range_end(self, editable_range_end: aspose.words.EditableRangeEnd) -> aspose.words.VisitorAction:
        """Called when an end of an editable range is encountered in the document.
        
        :param editable_range_end: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_shape_start(self, shape: aspose.words.drawing.Shape) -> aspose.words.VisitorAction:
        """Called when enumeration of a shape has started.
        
        :param shape: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_shape_end(self, shape: aspose.words.drawing.Shape) -> aspose.words.VisitorAction:
        """Called when enumeration of a shape has ended.
        
        :param shape: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_group_shape_start(self, group_shape: aspose.words.drawing.GroupShape) -> aspose.words.VisitorAction:
        """Called when enumeration of a group shape has started.
        
        :param group_shape: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_group_shape_end(self, group_shape: aspose.words.drawing.GroupShape) -> aspose.words.VisitorAction:
        """Called when enumeration of a group shape has ended.
        
        :param group_shape: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_office_math_start(self, office_math: aspose.words.math.OfficeMath) -> aspose.words.VisitorAction:
        """Called when enumeration of a Office Math object has started.
        
        :param office_math: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_office_math_end(self, office_math: aspose.words.math.OfficeMath) -> aspose.words.VisitorAction:
        """Called when enumeration of a Office Math object has ended.
        
        :param office_math: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_special_char(self, special_char: aspose.words.SpecialChar) -> aspose.words.VisitorAction:
        """Called when a :class:`SpecialChar` node is encountered in the document.
        
        :param special_char: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration.
        
        This method is not be called for generic control characters (see :class:`ControlChar`) that can be present in the document."""
        ...
    
    def visit_absolute_position_tab(self, tab: aspose.words.AbsolutePositionTab) -> aspose.words.VisitorAction:
        """Called when a :class:`AbsolutePositionTab` node is encountered in the document.
        
        :param tab: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_smart_tag_start(self, smart_tag: aspose.words.markup.SmartTag) -> aspose.words.VisitorAction:
        """Called when enumeration of a smart tag has started.
        
        :param smart_tag: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_smart_tag_end(self, smart_tag: aspose.words.markup.SmartTag) -> aspose.words.VisitorAction:
        """Called when enumeration of a smart tag has ended.
        
        :param smart_tag: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_structured_document_tag_start(self, sdt: aspose.words.markup.StructuredDocumentTag) -> aspose.words.VisitorAction:
        """Called when enumeration of a structured document tag has started.
        
        :param sdt: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_structured_document_tag_end(self, sdt: aspose.words.markup.StructuredDocumentTag) -> aspose.words.VisitorAction:
        """Called when enumeration of a structured document tag has ended.
        
        :param sdt: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_glossary_document_start(self, glossary: aspose.words.buildingblocks.GlossaryDocument) -> aspose.words.VisitorAction:
        """Called when enumeration of a glossary document has started.
        
        Note: A glossary document node and its children are not visited when you execute a
        Visitor over a :class:`Document`. If you want to execute a Visitor over a
        glossary document, you need to call :meth:`aspose.words.buildingblocks.GlossaryDocument.accept`.
        
        :param glossary: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_glossary_document_end(self, glossary: aspose.words.buildingblocks.GlossaryDocument) -> aspose.words.VisitorAction:
        """Called when enumeration of a glossary document has ended.
        
        Note: A glossary document node and its children are not visited when you execute a
        Visitor over a :class:`Document`. If you want to execute a Visitor over a
        glossary document, you need to call :meth:`aspose.words.buildingblocks.GlossaryDocument.accept`.
        
        :param glossary: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_building_block_start(self, block: aspose.words.buildingblocks.BuildingBlock) -> aspose.words.VisitorAction:
        """Called when enumeration of a building block has started.
        
        Note: A building block node and its children are not visited when you execute a
        Visitor over a :class:`Document`. If you want to execute a Visitor over a
        building block, you need to execute the visitor over :class:`aspose.words.buildingblocks.GlossaryDocument` or
        call :meth:`aspose.words.buildingblocks.BuildingBlock.accept`.
        
        :param block: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_building_block_end(self, block: aspose.words.buildingblocks.BuildingBlock) -> aspose.words.VisitorAction:
        """Called when enumeration of a building block has ended.
        
        Note: A building block node and its children are not visited when you execute a
        Visitor over a :class:`Document`. If you want to execute a Visitor over a
        building block, you need to execute the visitor over :class:`aspose.words.buildingblocks.GlossaryDocument` or
        call :meth:`aspose.words.buildingblocks.BuildingBlock.accept`.
        
        :param block: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_comment_range_start(self, comment_range_start: aspose.words.CommentRangeStart) -> aspose.words.VisitorAction:
        """Called when the start of a commented range of text is encountered.
        
        :param comment_range_start: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_comment_range_end(self, comment_range_end: aspose.words.CommentRangeEnd) -> aspose.words.VisitorAction:
        """Called when the end of a commented range of text is encountered.
        
        :param comment_range_end: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_sub_document(self, sub_document: aspose.words.SubDocument) -> aspose.words.VisitorAction:
        """Called when a sub-document is encountered.
        
        :param sub_document: The object that is being visited.
        :returns: A :class:`VisitorAction` value that specifies how to continue the enumeration."""
        ...
    
    def visit_structured_document_tag_range_start(self, sdt_range_start: aspose.words.markup.StructuredDocumentTagRangeStart) -> aspose.words.VisitorAction:
        """Called when a StructuredDocumentTagRangeStart is encountered."""
        ...
    
    def visit_structured_document_tag_range_end(self, sdt_range_end: aspose.words.markup.StructuredDocumentTagRangeEnd) -> aspose.words.VisitorAction:
        """Called when a StructuredDocumentTagRangeEnd is encountered."""
        ...
    
    ...

class EditableRange:
    """Represents a single editable range.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    :class:`EditableRange` is a "facade" object that encapsulates two nodes :attr:`EditableRange.editable_range_start`
    and :attr:`EditableRange.editable_range_end` in a document tree and allows to work with an editable range as a single object."""
    
    def remove(self) -> None:
        """Removes the editable range from the document. Does not remove content inside the editable range."""
        ...
    
    @property
    def id(self) -> int:
        """Gets the editable range identifier.
        
        The region must be demarcated using the :attr:`EditableRange.editable_range_start` and :attr:`EditableRange.editable_range_end`
        
        Editable range identifiers are supposed to be unique across a document and Aspose.Words automatically
        maintains editable range identifiers when loading, saving and combining documents."""
        ...
    
    @property
    def single_user(self) -> str:
        """Returns or sets the single user for editable range.
        
        This editor can be stored in one of the following forms:
        
        DOMAIN\\Username - for users whose access shall be authenticated using the current user's domain credentials.
        
        user@domain.com - for users whose access shall be authenticated using the user's e-mail address as credentials.
        
        user - for users whose access shall be authenticated using the current user's machine credentials.
        
        Single user and editor group cannot be set simultaneously for the specific editable range,
        if the one is set, the other will be clear."""
        ...
    
    @single_user.setter
    def single_user(self, value: str):
        ...
    
    @property
    def editor_group(self) -> aspose.words.EditorType:
        """Returns or sets an alias (or editing group) which shall be used to determine if the current user
        shall be allowed to edit this editable range.
        
        Single user and editor group cannot be set simultaneously for the specific editable range,
        if the one is set, the other will be clear."""
        ...
    
    @editor_group.setter
    def editor_group(self, value: aspose.words.EditorType):
        ...
    
    @property
    def editable_range_start(self) -> aspose.words.EditableRangeStart:
        """Gets the node that represents the start of the editable range."""
        ...
    
    @property
    def editable_range_end(self) -> aspose.words.EditableRangeEnd:
        """Gets the node that represents the end of the editable range."""
        ...
    
    ...

class EditableRangeEnd(aspose.words.Node):
    """Represents an end of an editable range in a Word document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    A complete editable range  in a Word document consists of a :attr:`EditableRangeEnd.editable_range_start`
    and a matching :class:`EditableRangeEnd` with the same Id.
    
    :attr:`EditableRangeEnd.editable_range_start` and :class:`EditableRangeEnd` are just markers inside a document
    that specify where the editable range starts and ends.
    
    Use the :class:`EditableRange` class as a "facade" to work with an editable range
    as a single object.
    
    **NOTE**: Currently editable ranges are supported only at the inline-level, that is inside :class:`Paragraph`,
    but editable range start and editable range end can be in different paragraphs."""
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_editable_range_end`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.EDITABLE_RANGE_END`."""
        ...
    
    @property
    def editable_range_start(self) -> aspose.words.EditableRangeStart:
        """Corresponding :class:`EditableRangeStart`, received by ID."""
        ...
    
    @property
    def id(self) -> int:
        """Specifies the identifier of the editable range."""
        ...
    
    @id.setter
    def id(self, value: int):
        ...
    
    ...

class EditableRangeStart(aspose.words.Node):
    """Represents a start of an editable range in a Word document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    A complete editable range in a Word document consists of a :class:`EditableRangeStart`
    and a matching :class:`EditableRangeEnd` with the same Id.
    
    :class:`EditableRangeStart` and :class:`EditableRangeEnd` are just markers inside a document
    that specify where the editable range starts and ends.
    
    Use the :attr:`EditableRangeStart.editable_range` class as a "facade" to work with an editable range
    as a single object.
    
    **NOTE**: Currently editable ranges are supported only at the inline-level, that is inside :class:`Paragraph`,
    but editable range start and editable range end can be in different paragraphs."""
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_editable_range_start`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.EDITABLE_RANGE_START`."""
        ...
    
    @property
    def id(self) -> int:
        """Specifies the identifier of the editable range."""
        ...
    
    @id.setter
    def id(self, value: int):
        ...
    
    @property
    def editable_range(self) -> aspose.words.EditableRange:
        """Gets the facade object that encapsulates this editable range start and end."""
        ...
    
    ...

class FileCorruptedException(RuntimeError):
    """Thrown during document load, when the document appears to be corrupted and impossible to load.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    ...

class FileFormatInfo:
    """Contains data returned by :class:`FileFormatUtil` document format detection methods.
    To learn more, visit the `Detect File Format and Check Format Compatibility <https://docs.aspose.com/words/python-net/detect-file-format-and-check-format-compatibility/>` documentation article.
    
    You do not create instances of this class directly. Objects of this class are returned by
    :meth:`FileFormatUtil.detect_file_format` methods."""
    
    @property
    def load_format(self) -> aspose.words.LoadFormat:
        """Gets the detected document format.
        
        When an OOXML document is encrypted, it is not possible to ascertained whether it is
        an Excel, Word or PowerPoint document without decrypting it first so for an encrypted OOXML
        document this property will always return :attr:`LoadFormat.DOCX`."""
        ...
    
    @property
    def is_encrypted(self) -> bool:
        """Returns ``True`` if the document is encrypted and requires a password to open.
        
        This property exists to help you sort documents that are encrypted from those that are not.
        If you attempt to load an encrypted document using Aspose.Words without supplying a password an
        exception will be thrown. You can use this property to detect whether a document requires a password
        and take some action before loading a document, for example, prompt the user for a password."""
        ...
    
    @property
    def has_digital_signature(self) -> bool:
        """Returns ``True`` if this document contains a digital signature.
        This property merely informs that a digital signature is present on a document,
        but it does not  specify whether the signature is valid or not.
        
        This property exists to help you sort documents that are digitally signed from those that are not.
        If you use Aspose.Words to modify and save a document that is digitally signed, then the digital signature will
        be lost. This is by design because a digital signature exists to guard the authenticity of a document.
        Using this property you can detect digitally signed documents before processing them in the same way as normal
        documents and take some action to avoid losing the digital signature, for example notify the user."""
        ...
    
    @property
    def has_macros(self) -> bool:
        """Returns ``True`` if this document contains a VBA macros."""
        ...
    
    @property
    def encoding(self) -> str:
        """Gets the detected encoding if applicable to the current document format.
        At the moment detects encoding only for HTML documents."""
        ...
    
    ...

class FileFormatUtil:
    """Provides utility methods for working with file formats, such as detecting file format
    or converting file extensions to/from file format enums.
    To learn more, visit the `Detect File Format and Check Format Compatibility <https://docs.aspose.com/words/python-net/detect-file-format-and-check-format-compatibility/>` documentation article."""
    
    @overload
    @staticmethod
    def detect_file_format(file_name: str) -> aspose.words.FileFormatInfo:
        """Detects and returns the information about a format of a document stored in a disk file.
        
        Even if this method detects the document format, it does not guarantee
        that the specified document is valid. This method only detects the document format by
        reading data that is sufficient for detection. To fully verify that a document is valid
        you need to load the document into a :class:`Document` object.
        
        This method throws :class:`FileCorruptedException` when the format is
        recognized, but the detection cannot complete because of corruption.
        
        :param file_name: The file name.
        :returns: A :class:`FileFormatInfo` object that contains the detected information."""
        ...
    
    @overload
    @staticmethod
    def detect_file_format(stream: io.BytesIO) -> aspose.words.FileFormatInfo:
        """Detects and returns the information about a format of a document stored in a stream.
        
        The stream must be positioned at the beginning of the document.
        
        When this method returns, the position in the stream is restored to the original position.
        
        Even if this method detects the document format, it does not guarantee
        that the specified document is valid. This method only detects the document format by
        reading data that is sufficient for detection. To fully verify that a document is valid
        you need to load the document into a :class:`Document` object.
        
        This method throws :class:`FileCorruptedException` when the format is
        recognized, but the detection cannot complete because of corruption.
        
        :param stream: The stream.
        :returns: A :class:`FileFormatInfo` object that contains the detected information."""
        ...
    
    @staticmethod
    def content_type_to_load_format(content_type: str) -> aspose.words.LoadFormat:
        """Converts IANA content type into a load format enumerated value.
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    @staticmethod
    def content_type_to_save_format(content_type: str) -> aspose.words.SaveFormat:
        """Converts IANA content type into a save format enumerated value.
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    @staticmethod
    def load_format_to_extension(load_format: aspose.words.LoadFormat) -> str:
        """Converts a load format enumerated value into a file extension. The returned extension is a lower-case string with a leading dot.
        
        The :attr:`SaveFormat.WORD_ML` value is converted to ".wml".
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    @staticmethod
    def save_format_to_load_format(save_format: aspose.words.SaveFormat) -> aspose.words.LoadFormat:
        """Converts a :class:`SaveFormat` value to a :class:`LoadFormat` value if possible.
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    @staticmethod
    def load_format_to_save_format(load_format: aspose.words.LoadFormat) -> aspose.words.SaveFormat:
        """Converts a :class:`LoadFormat` value to a :class:`SaveFormat` value if possible.
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    @staticmethod
    def save_format_to_extension(save_format: aspose.words.SaveFormat) -> str:
        """Converts a save format enumerated value into a file extension. The returned extension is a lower-case string with a leading dot.
        
        The :attr:`SaveFormat.WORD_ML` value is converted to ".wml".
        
        The :attr:`SaveFormat.FLAT_OPC` value is converted to ".fopc".
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    @staticmethod
    def extension_to_save_format(extension: str) -> aspose.words.SaveFormat:
        """Converts a file name extension into a :class:`SaveFormat` value.
        
        :param extension: The file extension. Can be with or without a leading dot. Case-insensitive.
        
        If the extension cannot be recognized, returns :attr:`SaveFormat.UNKNOWN`.
        
        :raises RuntimeError (Proxy error(ArgumentNullException)): Throws if the parameter is ``None``."""
        ...
    
    @staticmethod
    def image_type_to_extension(image_type: aspose.words.drawing.ImageType) -> str:
        """Converts an Aspose.Words image type enumerated value into a file extension. The returned extension is a lower-case string with a leading dot.
        
        :raises RuntimeError (Proxy error(ArgumentException)): Throws when cannot convert."""
        ...
    
    ...

class Font:
    """Contains font attributes (font name, font size, color, and so on) for an object.
    To learn more, visit the `Working with Fonts <https://docs.aspose.com/words/python-net/working-with-fonts/>` documentation article.
    
    You do not create instances of the :class:`Font` class directly. You just use
    :class:`Font` to access the font properties of the various objects such as :class:`Run`,
    :class:`Paragraph`, :class:`Style`, :class:`DocumentBuilder`."""
    
    def clear_formatting(self) -> None:
        """Resets to default font formatting.
        
        Removes all font formatting specified explicitly on the object from which
        :class:`Font` was obtained so the font formatting will be inherited from
        the appropriate parent."""
        ...
    
    def has_dml_effect(self, dml_effect_type: aspose.words.TextDmlEffect) -> bool:
        """Checks if particular DrawingML text effect is applied.
        
        :param dml_effect_type: DrawingML text effect type.
        :returns: ``True`` if particular DrawingML text effect is applied."""
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets the name of the font.
        
        When getting, returns :attr:`Font.name_ascii`.
        
        When setting, sets :attr:`Font.name_ascii`, :attr:`Font.name_bi`, :attr:`Font.name_far_east`
        and :attr:`Font.name_other` to the specified value."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def name_ascii(self) -> str:
        """Returns or sets the font used for Latin text (characters with character codes from 0 (zero) through 127)."""
        ...
    
    @name_ascii.setter
    def name_ascii(self, value: str):
        ...
    
    @property
    def name_bi(self) -> str:
        """Returns or sets the name of the font in a right-to-left language document."""
        ...
    
    @name_bi.setter
    def name_bi(self, value: str):
        ...
    
    @property
    def name_far_east(self) -> str:
        """Returns or sets an East Asian font name."""
        ...
    
    @name_far_east.setter
    def name_far_east(self, value: str):
        ...
    
    @property
    def name_other(self) -> str:
        """Returns or sets the font used for characters with character codes from 128 through 255."""
        ...
    
    @name_other.setter
    def name_other(self, value: str):
        ...
    
    @property
    def theme_font(self) -> aspose.words.themes.ThemeFont:
        """Gets or sets the theme font in the applied font scheme that is associated with this :class:`Font` object."""
        ...
    
    @theme_font.setter
    def theme_font(self, value: aspose.words.themes.ThemeFont):
        ...
    
    @property
    def theme_font_ascii(self) -> aspose.words.themes.ThemeFont:
        """Gets or sets the theme font used for Latin text (characters with character codes from 0 (zero) through 127)
        in the applied font scheme that is associated with this :class:`Font` object."""
        ...
    
    @theme_font_ascii.setter
    def theme_font_ascii(self, value: aspose.words.themes.ThemeFont):
        ...
    
    @property
    def theme_font_far_east(self) -> aspose.words.themes.ThemeFont:
        """Gets or sets the East Asian theme font in the applied font scheme that is associated with this :class:`Font` object."""
        ...
    
    @theme_font_far_east.setter
    def theme_font_far_east(self, value: aspose.words.themes.ThemeFont):
        ...
    
    @property
    def theme_font_other(self) -> aspose.words.themes.ThemeFont:
        """Gets or sets the theme font used for characters with character codes from 128 through 255
        in the applied font scheme that is associated with this :class:`Font` object."""
        ...
    
    @theme_font_other.setter
    def theme_font_other(self, value: aspose.words.themes.ThemeFont):
        ...
    
    @property
    def theme_font_bi(self) -> aspose.words.themes.ThemeFont:
        """Gets or sets the theme font in the applied font scheme that is associated with this :class:`Font` object
        in a right-to-left language document."""
        ...
    
    @theme_font_bi.setter
    def theme_font_bi(self, value: aspose.words.themes.ThemeFont):
        ...
    
    @property
    def size(self) -> float:
        """Gets or sets the font size in points."""
        ...
    
    @size.setter
    def size(self, value: float):
        ...
    
    @property
    def size_bi(self) -> float:
        """Gets or sets the font size in points used in a right-to-left document."""
        ...
    
    @size_bi.setter
    def size_bi(self, value: float):
        ...
    
    @property
    def bold(self) -> bool:
        """True if the font is formatted as bold."""
        ...
    
    @bold.setter
    def bold(self, value: bool):
        ...
    
    @property
    def bold_bi(self) -> bool:
        """True if the right-to-left text is formatted as bold."""
        ...
    
    @bold_bi.setter
    def bold_bi(self, value: bool):
        ...
    
    @property
    def italic(self) -> bool:
        """True if the font is formatted as italic."""
        ...
    
    @italic.setter
    def italic(self, value: bool):
        ...
    
    @property
    def italic_bi(self) -> bool:
        """True if the right-to-left text is formatted as italic."""
        ...
    
    @italic_bi.setter
    def italic_bi(self, value: bool):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        """Gets or sets the color of the font."""
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def theme_color(self) -> aspose.words.themes.ThemeColor:
        """Gets or sets the theme color in the applied color scheme that is associated with this :class:`Font` object."""
        ...
    
    @theme_color.setter
    def theme_color(self, value: aspose.words.themes.ThemeColor):
        ...
    
    @property
    def tint_and_shade(self) -> float:
        """Gets or sets a double value that lightens or darkens a color.
        
        The allowed values are in range from -1 (darkest) to 1 (lightest) for this property.
        
        Zero (0) is neutral.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throw if set this property to a value less than -1 or more than 1.
        :raises RuntimeError (Proxy error(InvalidOperationException)): Throw if set this property for :class:`Font` object with non-theme colors."""
        ...
    
    @tint_and_shade.setter
    def tint_and_shade(self, value: float):
        ...
    
    @property
    def auto_color(self) -> aspose.pydrawing.Color:
        """Returns the present calculated color of the text (black or white) to be used for 'auto color'.
        If the color is not 'auto' then returns :attr:`Font.color`.
        
        When text has 'automatic color', the actual color of text is calculated automatically
        so that it is readable against the background color. As you change the background color,
        the text color will automatically switch to black or white in MS Word to maximize legibility."""
        ...
    
    @property
    def strike_through(self) -> bool:
        """True if the font is formatted as strikethrough text."""
        ...
    
    @strike_through.setter
    def strike_through(self, value: bool):
        ...
    
    @property
    def double_strike_through(self) -> bool:
        """True if the font is formatted as double strikethrough text."""
        ...
    
    @double_strike_through.setter
    def double_strike_through(self, value: bool):
        ...
    
    @property
    def shadow(self) -> bool:
        """True if the font is formatted as shadowed."""
        ...
    
    @shadow.setter
    def shadow(self, value: bool):
        ...
    
    @property
    def outline(self) -> bool:
        """True if the font is formatted as outline."""
        ...
    
    @outline.setter
    def outline(self, value: bool):
        ...
    
    @property
    def emboss(self) -> bool:
        """True if the font is formatted as embossed."""
        ...
    
    @emboss.setter
    def emboss(self, value: bool):
        ...
    
    @property
    def engrave(self) -> bool:
        """True if the font is formatted as engraved."""
        ...
    
    @engrave.setter
    def engrave(self, value: bool):
        ...
    
    @property
    def superscript(self) -> bool:
        """True if the font is formatted as superscript."""
        ...
    
    @superscript.setter
    def superscript(self, value: bool):
        ...
    
    @property
    def subscript(self) -> bool:
        """True if the font is formatted as subscript."""
        ...
    
    @subscript.setter
    def subscript(self, value: bool):
        ...
    
    @property
    def small_caps(self) -> bool:
        """True if the font is formatted as small capital letters."""
        ...
    
    @small_caps.setter
    def small_caps(self, value: bool):
        ...
    
    @property
    def all_caps(self) -> bool:
        """True if the font is formatted as all capital letters."""
        ...
    
    @all_caps.setter
    def all_caps(self, value: bool):
        ...
    
    @property
    def hidden(self) -> bool:
        """True if the font is formatted as hidden text."""
        ...
    
    @hidden.setter
    def hidden(self, value: bool):
        ...
    
    @property
    def underline(self) -> aspose.words.Underline:
        """Gets or sets the type of underline applied to the font."""
        ...
    
    @underline.setter
    def underline(self, value: aspose.words.Underline):
        ...
    
    @property
    def underline_color(self) -> aspose.pydrawing.Color:
        """Gets or sets the color of the underline applied to the font."""
        ...
    
    @underline_color.setter
    def underline_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def scaling(self) -> int:
        """Gets or sets character width scaling in percent."""
        ...
    
    @scaling.setter
    def scaling(self, value: int):
        ...
    
    @property
    def spacing(self) -> float:
        """Returns or sets the spacing (in points) between characters ."""
        ...
    
    @spacing.setter
    def spacing(self, value: float):
        ...
    
    @property
    def line_spacing(self) -> float:
        """Returns line spacing of this font (in points)."""
        ...
    
    @property
    def position(self) -> float:
        """Gets or sets the position of text (in points) relative to the base line.
        A positive number raises the text, and a negative number lowers it."""
        ...
    
    @position.setter
    def position(self, value: float):
        ...
    
    @property
    def kerning(self) -> float:
        """Gets or sets the font size at which kerning starts."""
        ...
    
    @kerning.setter
    def kerning(self, value: float):
        ...
    
    @property
    def highlight_color(self) -> aspose.pydrawing.Color:
        """Gets or sets the highlight (marker) color."""
        ...
    
    @highlight_color.setter
    def highlight_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def text_effect(self) -> aspose.words.TextEffect:
        """Gets or sets the font animation effect."""
        ...
    
    @text_effect.setter
    def text_effect(self, value: aspose.words.TextEffect):
        ...
    
    @property
    def fill(self) -> aspose.words.drawing.Fill:
        """Gets fill formatting for the :class:`Font`."""
        ...
    
    @property
    def bidi(self) -> bool:
        """Specifies whether the contents of this run shall have right-to-left characteristics.
        
        This property, when on, shall not be used with strongly left-to-right text. Any behavior under that condition is unspecified.
        This property, when off, shall not be used with strong right-to-left text. Any behavior under that condition is unspecified.
        
        When the contents of this run are displayed, all characters shall be treated as complex script characters for formatting
        purposes. This means that :attr:`Font.bold_bi`, :attr:`Font.italic_bi`, :attr:`Font.size_bi` and a corresponding font name
        will be used when rendering this run.
        
        Also, when the contents of this run are displayed, this property acts as a right-to-left override for characters
        which are classified as "weak types" and "neutral types"."""
        ...
    
    @bidi.setter
    def bidi(self, value: bool):
        ...
    
    @property
    def complex_script(self) -> bool:
        """Specifies whether the contents of this run shall be treated as complex script text regardless
        of their Unicode character values when determining the formatting for this run."""
        ...
    
    @complex_script.setter
    def complex_script(self, value: bool):
        ...
    
    @property
    def no_proofing(self) -> bool:
        """True when the formatted characters are not to be spell checked."""
        ...
    
    @no_proofing.setter
    def no_proofing(self, value: bool):
        ...
    
    @property
    def locale_id(self) -> int:
        """Gets or sets the locale identifier (language) of the formatted characters.
        
        For the list of locale identifiers see https://msdn.microsoft.com/en-us/library/cc233965.aspx"""
        ...
    
    @locale_id.setter
    def locale_id(self, value: int):
        ...
    
    @property
    def locale_id_bi(self) -> int:
        """Gets or sets the locale identifier (language) of the formatted right-to-left characters.
        
        For the list of locale identifiers see https://msdn.microsoft.com/en-us/library/cc233965.aspx"""
        ...
    
    @locale_id_bi.setter
    def locale_id_bi(self, value: int):
        ...
    
    @property
    def locale_id_far_east(self) -> int:
        """Gets or sets the locale identifier (language) of the formatted Asian characters.
        
        For the list of locale identifiers see https://msdn.microsoft.com/en-us/library/cc233965.aspx"""
        ...
    
    @locale_id_far_east.setter
    def locale_id_far_east(self, value: int):
        ...
    
    @property
    def border(self) -> aspose.words.Border:
        """Returns a :class:`Border` object that specifies border for the font."""
        ...
    
    @property
    def shading(self) -> aspose.words.Shading:
        """Returns a :class:`Shading` object that refers to the shading formatting for the font."""
        ...
    
    @property
    def style(self) -> aspose.words.Style:
        """Gets or sets the character style applied to this formatting."""
        ...
    
    @style.setter
    def style(self, value: aspose.words.Style):
        ...
    
    @property
    def style_name(self) -> str:
        """Gets or sets the name of the character style applied to this formatting."""
        ...
    
    @style_name.setter
    def style_name(self, value: str):
        ...
    
    @property
    def style_identifier(self) -> aspose.words.StyleIdentifier:
        """Gets or sets the locale independent style identifier of the character style applied to this formatting."""
        ...
    
    @style_identifier.setter
    def style_identifier(self, value: aspose.words.StyleIdentifier):
        ...
    
    @property
    def snap_to_grid(self) -> bool:
        """Specifies whether the current font should use the document grid characters per line settings
        when laying out."""
        ...
    
    @snap_to_grid.setter
    def snap_to_grid(self, value: bool):
        ...
    
    @property
    def emphasis_mark(self) -> aspose.words.EmphasisMark:
        """Gets or sets the emphasis mark applied to this formatting."""
        ...
    
    @emphasis_mark.setter
    def emphasis_mark(self, value: aspose.words.EmphasisMark):
        ...
    
    ...

class FrameFormat:
    """Represents frame related formatting for a paragraph.
    
    This object is always created. If a paragraph is a frame, then all properties will contain respective values, otherwise
    all properties are set to their defaults.
    
    Use :attr:`FrameFormat.is_frame` to check whether paragraph is a frame."""
    
    @property
    def height_rule(self) -> aspose.words.HeightRule:
        """Gets the rule for determining the height of the specified frame."""
        ...
    
    @property
    def height(self) -> float:
        """Gets the height of the specified frame."""
        ...
    
    @property
    def horizontal_distance_from_text(self) -> float:
        """Gets horizontal distance between a frame and the surrounding text, in points."""
        ...
    
    @property
    def horizontal_position(self) -> float:
        """Gets horizontal distance between the edge of the frame and the item specified by the :attr:`FrameFormat.relative_horizontal_position` property."""
        ...
    
    @property
    def relative_horizontal_position(self) -> aspose.words.drawing.RelativeHorizontalPosition:
        """Gets the relative horizontal position of a frame."""
        ...
    
    @property
    def relative_vertical_position(self) -> aspose.words.drawing.RelativeVerticalPosition:
        """Gets the relative vertical position of a frame."""
        ...
    
    @property
    def vertical_distance_from_text(self) -> float:
        """Specifies vertical distance (in points) between a frame and the surrounding text."""
        ...
    
    @property
    def vertical_position(self) -> float:
        """Gets vertical distance between the edge of the frame and the item specified by the :attr:`FrameFormat.relative_vertical_position` property."""
        ...
    
    @property
    def width(self) -> float:
        """Gets the width of the specified frame, in points."""
        ...
    
    @property
    def vertical_alignment(self) -> aspose.words.drawing.VerticalAlignment:
        """Gets vertical alignment of the specified frame."""
        ...
    
    @property
    def horizontal_alignment(self) -> aspose.words.drawing.HorizontalAlignment:
        """Gets horizontal alignment of the specified frame."""
        ...
    
    @property
    def is_frame(self) -> bool:
        """Returns ``True`` if the paragraph is a frame."""
        ...
    
    ...

class HeaderFooter(aspose.words.Story):
    """Represents a container for the header or footer text of a section.
    To learn more, visit the `Working with Headers and Footers <https://docs.aspose.com/words/python-net/working-with-headers-and-footers/>` documentation article.
    
    :class:`HeaderFooter` can contain :class:`Paragraph` and :class:`aspose.words.tables.Table` child nodes.
    
    :class:`HeaderFooter` is a section-level node and can only be a child of :class:`Section`.
    There can only be one :class:`HeaderFooter` of each :attr:`HeaderFooter.header_footer_type` in a :class:`Section`.
    
    If :class:`Section` does not have a :class:`HeaderFooter` of a specific type or
    the :class:`HeaderFooter` has no child nodes, this header/footer is considered linked to
    the header/footer of the same type of the previous section in Microsoft Word.
    
    When :class:`HeaderFooter` contains at least one :class:`Paragraph`, it is no longer
    considered linked to previous in Microsoft Word."""
    
    def __init__(self, doc: aspose.words.DocumentBase, header_footer_type: aspose.words.HeaderFooterType):
        """Creates a new header or footer of the specified type.
        
        When :class:`HeaderFooter` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append :class:`HeaderFooter` to a :class:`Section` use :meth:`CompositeNode.insert_after`, :meth:`CompositeNode.insert_before`,
        or :attr:`Section.headers_footers` property and methods :meth:`NodeCollection.add`, :meth:`NodeCollection.insert`.
        
        :param doc: The owner document.
        :param header_footer_type: A :attr:`HeaderFooter.header_footer_type` value
                                   that specifies the type of the header or footer."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`DocumentVisitor.visit_header_footer_start`, then calls :meth:`Node.accept` for all child nodes of the section
        and calls :meth:`DocumentVisitor.visit_header_footer_end` at the end."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the start of the header.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the end of the header.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.HEADER_FOOTER`."""
        ...
    
    @property
    def parent_section(self) -> aspose.words.Section:
        """Gets the parent section of this story.
        
        :attr:`HeaderFooter.parent_section` is equivalent to :attr:`Node.parent_node` casted to :class:`Section`."""
        ...
    
    @property
    def header_footer_type(self) -> aspose.words.HeaderFooterType:
        """Gets the type of this header/footer."""
        ...
    
    @property
    def is_header(self) -> bool:
        """True if this :class:`HeaderFooter` object is a header."""
        ...
    
    @property
    def is_linked_to_previous(self) -> bool:
        """True if this header or footer is linked to the corresponding header or footer
        in the previous section.
        
        Default is ``True``.
        
        Note, when your link a header or footer, its contents is cleared."""
        ...
    
    @is_linked_to_previous.setter
    def is_linked_to_previous(self, value: bool):
        ...
    
    ...

class HeaderFooterCollection(aspose.words.NodeCollection):
    """Provides typed access to :class:`HeaderFooter` nodes of a :class:`Section`.
    To learn more, visit the `Working with Headers and Footers <https://docs.aspose.com/words/python-net/working-with-headers-and-footers/>` documentation article.
    
    There can be maximum of one :class:`HeaderFooter`
    
     of each:class:`HeaderFooterType` per
    :class:`Section`.
    :class:`HeaderFooter` objects can occur in any order in the collection."""
    
    def __getitem__(self, index: int) -> aspose.words.HeaderFooter:
        """Retrieves a :class:`HeaderFooter` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection."""
        ...
    
    @overload
    def link_to_previous(self, is_link_to_previous: bool) -> None:
        """Links or unlinks all headers and footers to the corresponding
        headers and footers in the previous section.
        
        If any of the headers or footers do not exist, creates them automatically.
        
        :param is_link_to_previous: ``True`` to link the headers and footers to the previous section;
                                    ``False`` to unlink them."""
        ...
    
    @overload
    def link_to_previous(self, header_footer_type: aspose.words.HeaderFooterType, is_link_to_previous: bool) -> None:
        """Links or unlinks the specified header or footer to the corresponding
        header or footer in the previous section.
        
        If the header or footer of the specified type does not exist, creates it automatically.
        
        :param header_footer_type: A :class:`HeaderFooterType` value
                                   that specifies the header or footer to link/unlink.
        :param is_link_to_previous: ``True`` to link the header or footer to the previous section;
                                    ``False`` to unlink."""
        ...
    
    def to_array(self) -> List[aspose.words.HeaderFooter]:
        """Copies all ``HeaderFooter`` s from the collection to a new array of ``HeaderFooter`` s.
        
        :returns: An array of ``HeaderFooter`` s."""
        ...
    
    def get_by_header_footer_type(self, header_footer_type: aspose.words.HeaderFooterType) -> aspose.words.HeaderFooter:
        """Retrieves a **HeaderFooter** of the specified type."""
        ...
    
    @property
    def header_even(self) -> aspose.words.HeaderFooter:
        """Retrieves a header for even numbered pages."""
        ...
    
    @property
    def header_primary(self) -> aspose.words.HeaderFooter:
        """Retrieves a primary header, also used for odd numbered pages."""
        ...
    
    @property
    def footer_even(self) -> aspose.words.HeaderFooter:
        """Retrieves a footer for even numbered pages."""
        ...
    
    @property
    def footer_primary(self) -> aspose.words.HeaderFooter:
        """Retrieves a primary footer, also used for odd numbered pages."""
        ...
    
    @property
    def header_first(self) -> aspose.words.HeaderFooter:
        """Retrieves a header for the first page of the section."""
        ...
    
    @property
    def footer_first(self) -> aspose.words.HeaderFooter:
        """Retrieves a footer for the first page of the section."""
        ...
    
    ...

class Hyphenation:
    """Provides methods for working with hyphenation dictionaries. These dictionaries prescribe where words of a specific language can be hyphenated.
    To learn more, visit the `Working with Hyphenation <https://docs.aspose.com/words/python-net/working-with-hyphenation/>` documentation article."""
    
    @overload
    @staticmethod
    def register_dictionary(language: str, stream: io.BytesIO) -> None:
        """Registers and loads a hyphenation dictionary for the specified language from a stream. Throws if dictionary cannot be read or has invalid format.
        
        :param language: A language name, e.g. "en-US". See .NET documentation for "culture name" and RFC 4646 for details.
        :param stream: A stream for the dictionary file in OpenOffice format."""
        ...
    
    @overload
    @staticmethod
    def register_dictionary(language: str, file_name: str) -> None:
        """Registers and loads a hyphenation dictionary for the specified language from file. Throws if dictionary cannot be read or has invalid format.
        
        This method can also be used to register Null dictionary to prevent:attr:`Hyphenation.callback` from being called repeatedly for the same language.
        
        :param language: A language name, e.g. "en-US". See .NET documentation for "culture name" and RFC 4646 for details.
        :param file_name: A path to the dictionary file in Open Office format.
                          If this parameter is``None`` or empty string then registered is Null dictionary and callback is not called anymore for this language.
                          To enable callback again use:meth:`Hyphenation.unregister_dictionary` method."""
        ...
    
    @staticmethod
    def unregister_dictionary(language: str) -> None:
        """Unregisters a hyphenation dictionary for the specified language.
        
        This is different from registering Null dictionary. Unregistering a dictionary enables callback for the specified language.
        
        :param language: A language name, e.g. "en-US". See .NET documentation for "culture name" and RFC 4646 for details.
                         If``None`` or empty string then all dictionaries are unregistered."""
        ...
    
    @staticmethod
    def is_dictionary_registered(language: str) -> bool:
        """Returns ``False`` if for the specified language there is no dictionary registered or if registered is Null dictionary, ``True`` otherwise."""
        ...
    
    callback: aspose.words.IHyphenationCallback
    
    warning_callback: aspose.words.IWarningCallback
    
    ...

class IDocumentConverterPlugin:
    """Defines an interface for external converter plugin."""
    
    def convert(self, input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts document using specified input output streams and save options.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_options: The save options."""
        ...
    
    def convert_to_images(self, input_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> List[io.BytesIO]:
        """Converts pages from document from input stream to array of images.
        
        :param input_stream: The input stream.
        :param save_options: The save options.
        :returns: Array of page images streams."""
        ...
    
    ...

class IDocumentMergerPlugin:
    """Defines an interface for external merger plugin that can merge Pdf documents."""
    
    def merge(self, output_stream: io.BytesIO, input_streams: List[io.BytesIO]) -> None:
        """Merges the given input PDF documents into a single output PDF document using specified input and output streams.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams."""
        ...
    
    ...

class IDocumentReaderPlugin:
    """Defines an interface for external reader plugins that can read a file into a document."""
    
    def read(self, src: io.BytesIO, load_options: aspose.words.loading.LoadOptions, document: aspose.words.Document) -> None:
        """Reads the data from the specified stream into the :class:`Document` instance.
        
        :param src: The source stream to read the document from.
        :param load_options: An additional load options to load the document.
        :param document: The instance of the :class:`Document` class to read the data to.
                         If the instance contains some content, it will be overridden by the data from the source stream"""
        ...
    
    ...

class IHyphenationCallback:
    """Implemented by classes which can register hyphenation dictionaries."""
    
    def request_dictionary(self, language: str) -> None:
        """Notifies application that hyphenation dictionary for the specified language wasn't found and may need to be registered.
        
        Implementation should find a dictionary and register it using:meth:`Hyphenation.register_dictionary` methods.
        
        If dictionary is unavailable for the specified language implementation can opt out of further calls for the same language
        using:meth:`Hyphenation.register_dictionary` with ``None`` value.
        
        :param language: A language name, e.g. "en-US". See .NET documentation for "culture name" and RFC 4646 for details.
        
        Exceptions thrown by this method will abort execution of page layout process."""
        ...
    
    ...

class INodeChangingCallback:
    """Implement this interface if you want to receive notifications when nodes are inserted or removed in the document."""
    
    def node_inserting(self, args: aspose.words.NodeChangingArgs) -> None:
        """Called just before a node belonging to this document is about to be inserted into another node."""
        ...
    
    def node_inserted(self, args: aspose.words.NodeChangingArgs) -> None:
        """Called when a node belonging to this document has been inserted into another node."""
        ...
    
    def node_removing(self, args: aspose.words.NodeChangingArgs) -> None:
        """Called just before a node belonging to this document is about to be removed from the document."""
        ...
    
    def node_removed(self, args: aspose.words.NodeChangingArgs) -> None:
        """Called when a node belonging to this document has been removed from its parent."""
        ...
    
    ...

class IRevisionCriteria:
    """Implement this interface if you want to control when certain :class:`Revision` should be accepted/rejected
    or not by the :meth:`RevisionCollection.accept`/:meth:`RevisionCollection.reject` methods."""
    
    def is_match(self, revision: aspose.words.Revision) -> bool:
        """Checks whether or not specified *revision* matches criteria.
        
        :param revision: The :class:`Revision` instance to match criteria.
        :returns: ``True`` if the *revision* matches criteria, otherwise``False``.
        
        The method implementation should not accept/reject the revision or modify it in any way due to unexpected results."""
        ...
    
    ...

class IWarningCallback:
    """Implement this interface if you want to have your own custom method called to
    capture loss of fidelity warnings that can occur during document loading or saving."""
    
    def warning(self, info: aspose.words.WarningInfo) -> None:
        """Aspose.Words invokes this method when it encounters some issue during document loading
        or saving that might result in loss of formatting or data fidelity."""
        ...
    
    ...

class ImageWatermarkOptions:
    """Contains options that can be specified when adding a watermark with image.
    To learn more, visit the `Working with Watermark <https://docs.aspose.com/words/python-net/working-with-watermark/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def scale(self) -> float:
        """Gets or sets the scale factor expressed as a fraction of the image. The default value is 0 - auto.
        
        Valid values range from 0 to 65.5 inclusive.
        
        Auto scale means that the watermark will be scaled to its max width and max height relative to
        the page margins.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws when argument was out of the range of valid values."""
        ...
    
    @scale.setter
    def scale(self, value: float):
        ...
    
    @property
    def is_washout(self) -> bool:
        """Gets or sets a boolean value which is responsible for washout effect of the watermark.
        The default value is ``True``."""
        ...
    
    @is_washout.setter
    def is_washout(self, value: bool):
        ...
    
    ...

class ImportFormatOptions:
    """Allows to specify various import options to format output.
    To learn more, visit the `Specify Load Options <https://docs.aspose.com/words/python-net/specify-load-options/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def smart_style_behavior(self) -> bool:
        """Gets or sets a boolean value that specifies how styles will be imported
        when they have equal names in source and destination documents.
        The default value is ``False``.
        
        When this option is **enabled**, the source style will be expanded into a direct attributes inside a
        destination document, if :attr:`ImportFormatMode.KEEP_SOURCE_FORMATTING` importing mode is used.
        
        When this option is **disabled**, the source style will be expanded only if it is numbered. Existing
        destination attributes will not be overridden, including lists."""
        ...
    
    @smart_style_behavior.setter
    def smart_style_behavior(self, value: bool):
        ...
    
    @property
    def keep_source_numbering(self) -> bool:
        """Gets or sets a boolean value that specifies how the numbering will be imported when it clashes in source and
        destination documents.
        The default value is ``False``."""
        ...
    
    @keep_source_numbering.setter
    def keep_source_numbering(self, value: bool):
        ...
    
    @property
    def ignore_text_boxes(self) -> bool:
        """Gets or sets a boolean value that specifies that source formatting of textboxes content ignored
        if :attr:`ImportFormatMode.KEEP_SOURCE_FORMATTING` mode is used.
        The default value is ``True``."""
        ...
    
    @ignore_text_boxes.setter
    def ignore_text_boxes(self, value: bool):
        ...
    
    @property
    def ignore_header_footer(self) -> bool:
        """Gets or sets a boolean value that specifies that source formatting of headers/footers content ignored
        if :attr:`ImportFormatMode.KEEP_SOURCE_FORMATTING` mode is used.
        The default value is ``True``."""
        ...
    
    @ignore_header_footer.setter
    def ignore_header_footer(self, value: bool):
        ...
    
    @property
    def merge_pasted_lists(self) -> bool:
        """Gets or sets a boolean value that specifies whether pasted lists will be merged with surrounding lists.
        The default value is ``False``."""
        ...
    
    @merge_pasted_lists.setter
    def merge_pasted_lists(self, value: bool):
        ...
    
    @property
    def force_copy_styles(self) -> bool:
        """Gets or sets a boolean value indicating either to copy conflicting styles
        in :attr:`ImportFormatMode.KEEP_SOURCE_FORMATTING` mode.
        The default value is ``False``.
        
        By default, if a matching style already exists in a destination document, the source style formatting
        is expanded into direct node attributes and the style of this node is reset to a default.
        
        When this option is set to ``True``, the source style will be forcibly copied
        into destination document with unique name and applied to the imported node.
        
        Note, in this case it is not guaranteed that formatting of the imported node in destination document
        will be preserved."""
        ...
    
    @force_copy_styles.setter
    def force_copy_styles(self, value: bool):
        ...
    
    @property
    def adjust_sentence_and_word_spacing(self) -> bool:
        """Gets or sets a boolean value that specifies whether to adjust sentence and word spacing automatically.
        The default value is ``False``."""
        ...
    
    @adjust_sentence_and_word_spacing.setter
    def adjust_sentence_and_word_spacing(self, value: bool):
        ...
    
    ...

class IncorrectPasswordException(RuntimeError):
    """Thrown if a document is encrypted with a password and the password specified when opening the document is incorrect or missing.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    ...

class Inline(aspose.words.Node):
    """Base class for inline-level nodes that can have character formatting associated with them, but cannot have child nodes of their own.
    To learn more, visit the `Logical Levels of Nodes in a Document <https://docs.aspose.com/words/python-net/logical-levels-of-nodes-in-a-document/>` documentation article.
    
    A class derived from :class:`Inline` can be a child of :class:`Paragraph`."""
    
    @property
    def parent_paragraph(self) -> aspose.words.Paragraph:
        """Retrieves the parent :class:`Paragraph` of this node."""
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        """Provides access to the font formatting of this object."""
        ...
    
    @property
    def is_insert_revision(self) -> bool:
        """Returns true if this object was inserted in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_delete_revision(self) -> bool:
        """Returns true if this object was deleted in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_move_from_revision(self) -> bool:
        """Returns ``True`` if this object was moved (deleted) in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_move_to_revision(self) -> bool:
        """Returns ``True`` if this object was moved (inserted) in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_format_revision(self) -> bool:
        """Returns true if formatting of the object was changed in Microsoft Word while change tracking was enabled."""
        ...
    
    ...

class InlineStory(aspose.words.CompositeNode):
    """Base class for inline-level nodes that can contain paragraphs and tables.
    To learn more, visit the `Logical Levels of Nodes in a Document <https://docs.aspose.com/words/python-net/logical-levels-of-nodes-in-a-document/>` documentation article.
    
    :class:`InlineStory` is a container for block-level nodes :class:`Paragraph` and :class:`aspose.words.tables.Table`.
    
    The classes that derive from :class:`InlineStory` are inline-level nodes that can contain
    their own text (paragraphs and tables). For example, a :class:`Comment` node contains text of a comment
    and a :class:`aspose.words.notes.Footnote` contains text of a footnote."""
    
    def ensure_minimum(self) -> None:
        """If the last child is not a paragraph, creates and appends one empty paragraph."""
        ...
    
    @property
    def story_type(self) -> aspose.words.StoryType:
        """Returns the type of the story."""
        ...
    
    @property
    def parent_paragraph(self) -> aspose.words.Paragraph:
        """Retrieves the parent :class:`Paragraph` of this node."""
        ...
    
    @property
    def first_paragraph(self) -> aspose.words.Paragraph:
        """Gets the first paragraph in the story."""
        ...
    
    @property
    def last_paragraph(self) -> aspose.words.Paragraph:
        """Gets the last paragraph in the story."""
        ...
    
    @property
    def paragraphs(self) -> aspose.words.ParagraphCollection:
        """Gets a collection of paragraphs that are immediate children of the story."""
        ...
    
    @property
    def tables(self) -> aspose.words.tables.TableCollection:
        """Gets a collection of tables that are immediate children of the story."""
        ...
    
    @property
    def is_insert_revision(self) -> bool:
        """Returns true if this object was inserted in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_delete_revision(self) -> bool:
        """Returns true if this object was deleted in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_move_from_revision(self) -> bool:
        """Returns ``True`` if this object was moved (deleted) in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_move_to_revision(self) -> bool:
        """Returns ``True`` if this object was moved (inserted) in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        """Provides access to the font formatting of the anchor character of this object."""
        ...
    
    ...

class InternableComplexAttr:
    """Base class for internable complex attribute.
    Internable complex attribute should notify parent collection when going to be changed.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article."""
    
    ...

class License:
    """Provides methods to license the component.
    To learn more, visit the `Licensing and Subscription <https://docs.aspose.com/words/python-net/licensing/>` documentation article."""
    
    def __init__(self):
        """Initializes a new instance of this class."""
        ...
    
    @overload
    def set_license(self, license_name: str) -> None:
        """Licenses the component.
        
        Tries to find the license in the following locations:
        
        1. Explicit path.
        
        2. The folder that contains the Aspose component assembly.
        
        3. The folder that contains the client's calling assembly.
        
        4. The folder that contains the entry (startup) assembly.
        
        5. An embedded resource in the client's calling assembly.
        
        **Note:** On the .NET Compact Framework, tries to find the license only in these locations:
        
        1. Explicit path.
        
        2. An embedded resource in the client's calling assembly.
        
        :param license_name: Can be a full or short file name or name of an embedded resource.
                             Use an empty string to switch to evaluation mode."""
        ...
    
    @overload
    def set_license(self, stream: io.BytesIO) -> None:
        """Licenses the component.
        
        :param stream: A stream that contains the license.
        
        Use this method to load a license from a stream."""
        ...
    
    ...

class Metered:
    """Provides methods to set metered key."""
    
    def __init__(self):
        """Initializes a new instance of this class."""
        ...
    
    def set_metered_key(self, public_key: str, private_key: str) -> None:
        """Sets metered public and private key.
        If you purchase metered license, when start application, this API should be called, normally, this is enough.
        However, if always fail to upload consumption data and exceed 24 hours, the license will be set to evaluation status,
        to avoid such case, you should regularly check the license status, if it is evaluation status, call this API again.
        
        :param public_key: public key
        :param private_key: private key"""
        ...
    
    @staticmethod
    def get_consumption_quantity() -> decimal.Decimal:
        """Gets consumption file size
        
        :returns: consumption quantity"""
        ...
    
    @staticmethod
    def get_consumption_credit() -> decimal.Decimal:
        """Gets consumption credit
        
        :returns: consumption quantity"""
        ...
    
    def get_product_name(self) -> str:
        """Returns Product name
        
        :returns: Product name"""
        ...
    
    @staticmethod
    def is_metered_licensed() -> bool:
        """Check whether metered is licensed
        
        :returns: True or false"""
        ...
    
    ...

class Node:
    """Base class for all nodes of a Word document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    A document is represented as a tree of nodes, similar to DOM or XmlDocument.
    
    For more info see the Composite design pattern.
    
    The :class:`Node` class:
    
    * Defines the child node interface.
    
    * Defines the interface for visiting nodes.
    
    * Provides default cloning capability.
    
    * Implements parent node and owner document mechanisms.
    
    * Implements access to sibling nodes."""
    
    @overload
    def get_ancestor(self, ancestor_type: object) -> aspose.words.CompositeNode:
        """Gets the first ancestor of the specified object type.
        
        :param ancestor_type: The object type of the ancestor to retrieve.
        :returns: The ancestor of the specified type or ``None`` if no ancestor of this type was found.
        
        The ancestor type matches if it is equal to *ancestorType* or derived from*ancestorType*."""
        ...
    
    @overload
    def get_ancestor(self, ancestor_type: aspose.words.NodeType) -> aspose.words.CompositeNode:
        """Gets the first ancestor of the specified :class:`NodeType`.
        
        :param ancestor_type: The node type of the ancestor to retrieve.
        :returns: The ancestor of the specified type or ``None`` if no ancestor of this type was found."""
        ...
    
    @overload
    def to_string(self, save_format: aspose.words.SaveFormat) -> str:
        """Exports the content of the node into a string in the specified format.
        
        :returns: The content of the node in the specified format."""
        ...
    
    @overload
    def to_string(self, save_options: aspose.words.saving.SaveOptions) -> str:
        """Exports the content of the node into a string using the specified save options.
        
        :param save_options: Specifies the options that control how the node is saved.
        :returns: The content of the node in the specified format."""
        ...
    
    def clone(self, is_clone_children: bool) -> aspose.words.Node:
        """Creates a duplicate of the node.
        
        This method serves as a copy constructor for nodes.
        The cloned node has no parent, but belongs to the same document as the original node.
        
        This method always performs a deep copy of the node. The *isCloneChildren* parameter
        specifies whether to perform copy all child nodes as well.
        
        :param is_clone_children: True to recursively clone the subtree under the specified node;
                                  false to clone only the node itself.
        :returns: The cloned node."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes."""
        ...
    
    def get_text(self) -> str:
        """Gets the text of this node and of all its children.
        
        The returned string includes all control and special characters as described in :class:`ControlChar`."""
        ...
    
    def remove(self) -> None:
        """Removes itself from the parent."""
        ...
    
    def next_pre_order(self, root_node: aspose.words.Node) -> aspose.words.Node:
        """Gets next node according to the pre-order tree traversal algorithm.
        
        :param root_node: The top node (limit) of traversal.
        :returns: Next node in pre-order order. Null if reached the *rootNode*."""
        ...
    
    def previous_pre_order(self, root_node: aspose.words.Node) -> aspose.words.Node:
        """Gets the previous node according to the pre-order tree traversal algorithm.
        
        :param root_node: The top node (limit) of traversal.
        :returns: Previous node in pre-order order. Null if reached the *rootNode*."""
        ...
    
    @staticmethod
    def node_type_to_string(node_type: aspose.words.NodeType) -> str:
        """A utility method that converts a node type enum value into a user friendly string."""
        ...
    
    def as_document(self) -> aspose.words.Document:
        """Cast node to :attr:`Node.document`."""
        ...
    
    def as_section(self) -> aspose.words.Section:
        """Cast node to :class:`Section`."""
        ...
    
    def as_body(self) -> aspose.words.Body:
        """Cast node to :class:`Body`."""
        ...
    
    def as_header_footer(self) -> aspose.words.HeaderFooter:
        """Cast node to :class:`HeaderFooter`."""
        ...
    
    def as_table(self) -> aspose.words.tables.Table:
        """Cast node to :class:`aspose.words.tables.Table`."""
        ...
    
    def as_row(self) -> aspose.words.tables.Row:
        """Cast node to :class:`aspose.words.tables.Row`."""
        ...
    
    def as_cell(self) -> aspose.words.tables.Cell:
        """Cast node to :class:`aspose.words.tables.Cell`."""
        ...
    
    def as_paragraph(self) -> aspose.words.Paragraph:
        """Cast node to :class:`Paragraph`."""
        ...
    
    def as_bookmark_start(self) -> aspose.words.BookmarkStart:
        """Cast node to :class:`BookmarkStart`."""
        ...
    
    def as_bookmark_end(self) -> aspose.words.BookmarkEnd:
        """Cast node to :class:`BookmarkEnd`."""
        ...
    
    def as_editable_range_start(self) -> aspose.words.EditableRangeStart:
        """Cast node to :class:`EditableRangeStart`."""
        ...
    
    def as_editable_range_end(self) -> aspose.words.EditableRangeEnd:
        """Cast node to :class:`EditableRangeEnd`."""
        ...
    
    def as_group_shape(self) -> aspose.words.drawing.GroupShape:
        """Cast node to :class:`aspose.words.drawing.GroupShape`."""
        ...
    
    def as_shape(self) -> aspose.words.drawing.Shape:
        """Cast node to :class:`aspose.words.drawing.Shape`."""
        ...
    
    def as_comment(self) -> aspose.words.Comment:
        """Cast node to :class:`Comment`."""
        ...
    
    def as_footnote(self) -> aspose.words.notes.Footnote:
        """Cast node to :class:`aspose.words.notes.Footnote`."""
        ...
    
    def as_run(self) -> aspose.words.Run:
        """Cast node to :class:`Run`."""
        ...
    
    def as_field_start(self) -> aspose.words.fields.FieldStart:
        """Cast node to :class:`aspose.words.fields.FieldStart`."""
        ...
    
    def as_field_separator(self) -> aspose.words.fields.FieldSeparator:
        """Cast node to :class:`aspose.words.fields.FieldSeparator`."""
        ...
    
    def as_field_end(self) -> aspose.words.fields.FieldEnd:
        """Cast node to :class:`aspose.words.fields.FieldEnd`."""
        ...
    
    def as_form_field(self) -> aspose.words.fields.FormField:
        """Cast node to :class:`aspose.words.fields.FormField`."""
        ...
    
    def as_special_char(self) -> aspose.words.SpecialChar:
        """Cast node to :class:`SpecialChar`."""
        ...
    
    def as_smart_tag(self) -> aspose.words.markup.SmartTag:
        """Cast node to :class:`aspose.words.markup.SmartTag`."""
        ...
    
    def as_structured_document_tag(self) -> aspose.words.markup.StructuredDocumentTag:
        """Cast node to :class:`aspose.words.markup.StructuredDocumentTag`."""
        ...
    
    def as_structured_document_tag_range_start(self) -> aspose.words.markup.StructuredDocumentTagRangeStart:
        """Cast node to :class:`aspose.words.markup.StructuredDocumentTagRangeStart`."""
        ...
    
    def as_structured_document_tag_range_end(self) -> aspose.words.markup.StructuredDocumentTagRangeEnd:
        """Cast node to :class:`aspose.words.markup.StructuredDocumentTagRangeEnd`."""
        ...
    
    def as_glossary_document(self) -> aspose.words.buildingblocks.GlossaryDocument:
        """Cast node to :class:`aspose.words.buildingblocks.GlossaryDocument`."""
        ...
    
    def as_building_block(self) -> aspose.words.buildingblocks.BuildingBlock:
        """Cast node to :class:`aspose.words.buildingblocks.BuildingBlock`."""
        ...
    
    def as_comment_range_start(self) -> aspose.words.CommentRangeStart:
        """Cast node to :class:`CommentRangeStart`."""
        ...
    
    def as_comment_range_end(self) -> aspose.words.CommentRangeEnd:
        """Cast node to :class:`CommentRangeEnd`."""
        ...
    
    def as_office_math(self) -> aspose.words.math.OfficeMath:
        """Cast node to :class:`aspose.words.math.OfficeMath`."""
        ...
    
    def as_sub_document(self) -> aspose.words.SubDocument:
        """Cast node to :class:`SubDocument`."""
        ...
    
    def as_composite_node(self) -> aspose.words.CompositeNode:
        """Cast node to :class:`CompositeNode`."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Gets the type of this node."""
        ...
    
    @property
    def parent_node(self) -> aspose.words.CompositeNode:
        """Gets the immediate parent of this node.
        
        If a node has just been created and not yet added to the tree,
        or if it has been removed from the tree, the parent is ``None``."""
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        """Gets the document to which this node belongs.
        
        The node always belongs to a document even if it has just been created
        and not yet added to the tree, or if it has been removed from the tree."""
        ...
    
    @property
    def previous_sibling(self) -> aspose.words.Node:
        """Gets the node immediately preceding this node.
        
        If there is no preceding node, a ``None`` is returned."""
        ...
    
    @property
    def next_sibling(self) -> aspose.words.Node:
        """Gets the node immediately following this node.
        
        If there is no next node, a ``None`` is returned."""
        ...
    
    @property
    def is_composite(self) -> bool:
        """Returns ``True`` if this node can contain other nodes."""
        ...
    
    @property
    def range(self) -> aspose.words.Range:
        """Returns a :class:`Range` object that represents the portion of a document that is contained in this node."""
        ...
    
    @property
    def custom_node_id(self) -> int:
        """Specifies custom node identifier.
        
        Default is zero.
        
        This identifier can be set and used arbitrarily. For example, as a key to get external data.
        
        Important note, specified value is not saved to an output file and exists only during the node lifetime."""
        ...
    
    @custom_node_id.setter
    def custom_node_id(self, value: int):
        ...
    
    ...

class NodeChangingArgs:
    """Provides data for methods of the :class:`INodeChangingCallback` interface.
    
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article."""
    
    @property
    def node(self) -> aspose.words.Node:
        """Gets the :attr:`NodeChangingArgs.node` that is being added or removed."""
        ...
    
    @property
    def old_parent(self) -> aspose.words.Node:
        """Gets the node's parent before the operation began."""
        ...
    
    @property
    def new_parent(self) -> aspose.words.Node:
        """Gets the node's parent that will be set after the operation completes."""
        ...
    
    @property
    def action(self) -> aspose.words.NodeChangingAction:
        """Gets a value indicating what type of node change event is occurring."""
        ...
    
    ...

class NodeCollection:
    """Represents a collection of nodes of a specific type.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    :class:`NodeCollection` does not own the nodes it contains, rather, is just a selection of nodes
    of the specified type, but the nodes are stored in the tree under their respective parent nodes.
    
    :class:`NodeCollection` supports indexed access, iteration and provides add and remove methods.
    
    The :class:`NodeCollection` collection is "live", i.e. changes to the children of the node object
    that it was created from are immediately reflected in the nodes returned by the :class:`NodeCollection`
    properties and methods.
    
    :class:`NodeCollection` is returned by :meth:`CompositeNode.get_child_nodes`
    and also serves as a base class for typed node collections such as :class:`SectionCollection`,
    :class:`ParagraphCollection` etc.
    
    :class:`NodeCollection` can be "flat" and contain only immediate children of the node it was created
    from, or it can be "deep" and contain all descendant children."""
    
    def __getitem__(self, index: int) -> aspose.words.Node:
        """Retrieves a node at the given index.
        
        :param index: An index into the collection of nodes.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference."""
        ...
    
    def add(self, node: aspose.words.Node) -> None:
        """Adds a node to the end of the collection.
        
        The node is inserted as a child into the node object from which the collection was created.
        
        If the node being inserted was created from another document, you should use
        :meth:`DocumentBase.import_node` to import the node to the current document.
        The imported node can then be inserted into the current document.
        
        :param node: The node to be added to the end of the collection.
        :raises RuntimeError (Proxy error(NotSupportedException)): The :class:`NodeCollection` is a "deep" collection."""
        ...
    
    def insert(self, index: int, node: aspose.words.Node) -> None:
        """Inserts a node into the collection at the specified index.
        
        The node is inserted as a child into the node object from which the collection was created.
        
        If the index is equal to or greater than :attr:`NodeCollection.count`, the node is added at the end of the collection.
        
        If the index is negative and its absolute value is greater than :attr:`NodeCollection.count`, the node is added at the end of the collection.
        
        If the node being inserted was created from another document, you should use
        :meth:`DocumentBase.import_node` to import the node to the current document.
        The imported node can then be inserted into the current document.
        
        :param index: The zero-based index of the node.
                      Negative indexes are allowed and indicate access from the back of the list.
                      For example -1 means the last node, -2 means the second before last and so on.
        :param node: The node to insert.
        :raises RuntimeError (Proxy error(NotSupportedException)): The :class:`NodeCollection` is a "deep" collection."""
        ...
    
    def remove(self, node: aspose.words.Node) -> None:
        """Removes the node from the collection and from the document.
        
        :param node: The node to remove."""
        ...
    
    def remove_at(self, index: int) -> None:
        """Removes the node at the specified index from the collection and from the document.
        
        :param index: The zero-based index of the node.
                      Negative indexes are allowed and indicate access from the back of the list.
                      For example -1 means the last node, -2 means the second before last and so on."""
        ...
    
    def clear(self) -> None:
        """Removes all nodes from this collection and from the document."""
        ...
    
    def contains(self, node: aspose.words.Node) -> bool:
        """Determines whether a node is in the collection.
        
        This method performs a linear search; therefore, the average execution time is proportional to :attr:`NodeCollection.count`.
        
        :param node: The node to locate.
        :returns: ``True`` if item is found in the collection; otherwise, ``False``."""
        ...
    
    def index_of(self, node: aspose.words.Node) -> int:
        """Returns the zero-based index of the specified node.
        
        :param node: The node to locate.
        :returns: The zero-based index of the node within the collection, if found; otherwise, -1.
        
        This method performs a linear search; therefore, the average execution time is proportional to :attr:`NodeCollection.count`."""
        ...
    
    def to_array(self) -> List[aspose.words.Node]:
        """Copies all nodes from the collection to a new array of nodes.
        
        You should not be adding/removing nodes while iterating over a collection
        of nodes because it invalidates the iterator and requires refreshes for live collections.
        
        To be able to add/remove nodes during iteration, use this method to copy
        nodes into a fixed-size array and then iterate over the array.
        
        :returns: An array of nodes."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of nodes in the collection."""
        ...
    
    ...

class NodeImporter:
    """Allows to efficiently perform repeated import of nodes from one document to another.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    Aspose.Words provides functionality for easy copying and moving fragments
    between Microsoft Word documents. This is known as "importing nodes".
    Before you can insert a fragment from one document into another, you need to "import" it.
    Importing creates a deep clone of the original node, ready to be inserted into the
    destination document.
    
    The simplest way to import a node is to use the :meth:`DocumentBase.import_node` method
    provided by the :class:`DocumentBase` object.
    
    However, when you need to import nodes from one document to another multiple times,
    it is better to use the :class:`NodeImporter` class. The :class:`NodeImporter`
    class allows to minimize the number of styles and lists created in the destination document.
    
    Copying or moving fragments from one Microsoft Word document to another presents a number
    of technical challenges for Aspose.Words. In a Word document, styles and list formatting
    are stored centrally, separately from the text of the document. The paragraphs
    and runs of text merely reference the styles by internal unique identifiers.
    
    The challenges arise from the fact that styles and lists are different in different documents.
    For example, to copy a paragraph formatted with the Heading 1 style from one document to another,
    a number of things must be taken into account: decide whether to copy the Heading 1 style from
    the source document to the destination document, clone the paragraph, update the cloned
    paragraph so it refers to the correct Heading 1 style in the destination document.
    If the style had to be copied, all the styles that it references (based on style
    and next paragraph style) should be analyzed and possibly copied too and so on.
    Similar issues exist when copying bulleted or numbered paragraphs because Microsoft Word
    stores list definitions separately from text.
    
    The :class:`NodeImporter` class is like a context, that holds the "translation tables"
    during the import. It correctly translates between styles and lists in the source and
    destination documents."""
    
    @overload
    def __init__(self, src_doc: aspose.words.DocumentBase, dst_doc: aspose.words.DocumentBase, import_format_mode: aspose.words.ImportFormatMode):
        """Initializes a new instance of the :class:`NodeImporter` class.
        
        :param src_doc: The source document.
        :param dst_doc: The destination document that will be the owner of imported nodes.
        :param import_format_mode: Specifies how to merge style formatting that clashes."""
        ...
    
    @overload
    def __init__(self, src_doc: aspose.words.DocumentBase, dst_doc: aspose.words.DocumentBase, import_format_mode: aspose.words.ImportFormatMode, import_format_options: aspose.words.ImportFormatOptions):
        """Initializes a new instance of the :class:`NodeImporter` class.
        
        :param src_doc: The source document.
        :param dst_doc: The destination document that will be the owner of imported nodes.
        :param import_format_mode: Specifies how to merge style formatting that clashes.
        :param import_format_options: Specifies various options to format imported node."""
        ...
    
    def import_node(self, src_node: aspose.words.Node, is_import_children: bool) -> aspose.words.Node:
        """Imports a node from one document into another.
        
        Importing a node creates a copy of the source node belonging to the importing document.
        The returned node has no parent. The source node is not altered or removed from the original document.
        
        Before a node from another document can be inserted into this document, it must be imported.
        During import, document-specific properties such as references to styles and lists are translated
        from the original to the importing document. After the node was imported, it can be inserted
        into the appropriate place in the document using :meth:`CompositeNode.insert_before` or
        :meth:`CompositeNode.insert_after`.
        
        If the source node already belongs to the destination document, then simply a deep clone
        of the source node is created.
        
        :param src_node: The node to import.
        :param is_import_children: ``True`` to import all child nodes recursively; otherwise, ``False``.
        :returns: The cloned, imported node. The node belongs to the destination document, but has no parent."""
        ...
    
    ...

class NodeList:
    """Represents a collection of nodes matching an XPath query executed using the :meth:`CompositeNode.select_nodes` method.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    :class:`NodeList` is returned by :meth:`CompositeNode.select_nodes` and contains a collection
    of nodes matching the XPath query.
    
    :class:`NodeList` supports indexed access and iteration.
    
    **NOTE**: Treat the :class:`NodeList` collection as a "snapshot" collection. :class:`NodeList` starts
    as a "live" collection because the nodes are not actually retrieved when the XPath query is run.
    The nodes are only retrieved upon access and at this time the node and all nodes that precede
    it are cached forming a "snapshot" collection."""
    
    def __getitem__(self, index: int) -> aspose.words.Node:
        """Retrieves a node at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the list of nodes."""
        ...
    
    def to_array(self) -> List[aspose.words.Node]:
        """Copies all nodes from the collection to a new array of nodes.
        
        You should not be adding/removing nodes while iterating over a collection
        of nodes because it invalidates the iterator and requires refreshes for live collections.
        
        To be able to add/remove nodes during iteration, use this method to copy
        nodes into a fixed-size array and then iterate over the array.
        
        :returns: An array of nodes."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of nodes in the list."""
        ...
    
    ...

class PageSetup:
    """Represents the page setup properties of a section.
    To learn more, visit the `Working with Sections <https://docs.aspose.com/words/python-net/working-with-sections/>` documentation article.
    
    :class:`PageSetup` object contains all the page setup attributes of a section
    (left margin, bottom margin, paper size, and so on) as properties."""
    
    def clear_formatting(self) -> None:
        """Resets page setup to default paper size, margins and orientation."""
        ...
    
    @property
    def odd_and_even_pages_header_footer(self) -> bool:
        """True if the document has different headers and footers for odd-numbered and even-numbered pages.
        
        Note, changing this property affects all sections in the document."""
        ...
    
    @odd_and_even_pages_header_footer.setter
    def odd_and_even_pages_header_footer(self, value: bool):
        ...
    
    @property
    def different_first_page_header_footer(self) -> bool:
        """True if a different header or footer is used on the first page."""
        ...
    
    @different_first_page_header_footer.setter
    def different_first_page_header_footer(self, value: bool):
        ...
    
    @property
    def multiple_pages(self) -> aspose.words.settings.MultiplePagesType:
        """For multiple page documents, gets or sets how a document is printed or rendered so that it can be bound as a booklet."""
        ...
    
    @multiple_pages.setter
    def multiple_pages(self, value: aspose.words.settings.MultiplePagesType):
        ...
    
    @property
    def sheets_per_booklet(self) -> int:
        """Returns or sets the number of pages to be included in each booklet."""
        ...
    
    @sheets_per_booklet.setter
    def sheets_per_booklet(self, value: int):
        ...
    
    @property
    def section_start(self) -> aspose.words.SectionStart:
        """Returns or sets the type of section break for the specified object."""
        ...
    
    @section_start.setter
    def section_start(self, value: aspose.words.SectionStart):
        ...
    
    @property
    def suppress_endnotes(self) -> bool:
        """True if endnotes are printed at the end of the next section that doesn't suppress endnotes.
        Suppressed endnotes are printed before the endnotes in that section."""
        ...
    
    @suppress_endnotes.setter
    def suppress_endnotes(self, value: bool):
        ...
    
    @property
    def vertical_alignment(self) -> aspose.words.PageVerticalAlignment:
        """Returns or sets the vertical alignment of text on each page in a document or section."""
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.words.PageVerticalAlignment):
        ...
    
    @property
    def bidi(self) -> bool:
        """Specifies that this section contains bidirectional (complex scripts) text.
        
        When ``True``, the columns in this section are laid out from right to left."""
        ...
    
    @bidi.setter
    def bidi(self, value: bool):
        ...
    
    @property
    def layout_mode(self) -> aspose.words.SectionLayoutMode:
        """Gets or sets the layout mode of this section."""
        ...
    
    @layout_mode.setter
    def layout_mode(self, value: aspose.words.SectionLayoutMode):
        ...
    
    @property
    def characters_per_line(self) -> int:
        """Gets or sets the number of characters per line in the document grid.
        
        Minimum value of the property is 1. Maximum value depends on page width and font size of the Normal
        style. Minimum character pitch is 90 percent of the font size. For example, maximum number of characters
        per line of a Letter page with one-inch margins is 43.
        
        By default, the property has a value, on which character pitch equals to font size of the Normal
        style."""
        ...
    
    @characters_per_line.setter
    def characters_per_line(self, value: int):
        ...
    
    @property
    def lines_per_page(self) -> int:
        """Gets or sets the number of lines per page in the document grid.
        
        Minimum value of the property is 1. Maximum value depends on page height and font size of the Normal
        style. Minimum line pitch is 136 percent of the font size. For example, maximum number of lines per page of
        a Letter page with one-inch margins is 39.
        
        By default, the property has a value, on which line pitch is in 1.5 times greater than font size of
        the Normal style."""
        ...
    
    @lines_per_page.setter
    def lines_per_page(self, value: int):
        ...
    
    @property
    def page_width(self) -> float:
        """Returns or sets the width of the page in points."""
        ...
    
    @page_width.setter
    def page_width(self, value: float):
        ...
    
    @property
    def page_height(self) -> float:
        """Returns or sets the height of the page in points."""
        ...
    
    @page_height.setter
    def page_height(self, value: float):
        ...
    
    @property
    def margins(self) -> aspose.words.Margins:
        """Returns or sets preset :class:`Margins` of the page."""
        ...
    
    @margins.setter
    def margins(self, value: aspose.words.Margins):
        ...
    
    @property
    def paper_size(self) -> aspose.words.PaperSize:
        """Returns or sets the paper size.
        
        Setting this property updates :attr:`PageSetup.page_width` and :attr:`PageSetup.page_height` values.
        Setting this value to :attr:`PaperSize.CUSTOM` does not change existing values."""
        ...
    
    @paper_size.setter
    def paper_size(self, value: aspose.words.PaperSize):
        ...
    
    @property
    def orientation(self) -> aspose.words.Orientation:
        """Returns or sets the orientation of the page.
        
        Changing :attr:`PageSetup.orientation` swaps :attr:`PageSetup.page_width` and :attr:`PageSetup.page_height`."""
        ...
    
    @orientation.setter
    def orientation(self, value: aspose.words.Orientation):
        ...
    
    @property
    def left_margin(self) -> float:
        """Returns or sets the distance (in points) between the left edge of the page and the left boundary of the body text."""
        ...
    
    @left_margin.setter
    def left_margin(self, value: float):
        ...
    
    @property
    def right_margin(self) -> float:
        """Returns or sets the distance (in points) between the right edge of the page and the right boundary of the body text."""
        ...
    
    @right_margin.setter
    def right_margin(self, value: float):
        ...
    
    @property
    def top_margin(self) -> float:
        """Returns or sets the distance (in points) between the top edge of the page and the top boundary of the body text."""
        ...
    
    @top_margin.setter
    def top_margin(self, value: float):
        ...
    
    @property
    def bottom_margin(self) -> float:
        """Returns or sets the distance (in points) between the bottom edge of the page and the bottom boundary of the body text."""
        ...
    
    @bottom_margin.setter
    def bottom_margin(self, value: float):
        ...
    
    @property
    def header_distance(self) -> float:
        """Returns or sets the distance (in points) between the header and the top of the page."""
        ...
    
    @header_distance.setter
    def header_distance(self, value: float):
        ...
    
    @property
    def footer_distance(self) -> float:
        """Returns or sets the distance (in points) between the footer and the bottom of the page."""
        ...
    
    @footer_distance.setter
    def footer_distance(self, value: float):
        ...
    
    @property
    def gutter(self) -> float:
        """Gets or sets the amount of extra space added to the margin for document binding."""
        ...
    
    @gutter.setter
    def gutter(self, value: float):
        ...
    
    @property
    def first_page_tray(self) -> int:
        """Gets or sets the paper tray (bin) to use for the first page of a section.
        The value is implementation (printer) specific."""
        ...
    
    @first_page_tray.setter
    def first_page_tray(self, value: int):
        ...
    
    @property
    def other_pages_tray(self) -> int:
        """Gets or sets the paper tray (bin) to be used for all but the first page of a section.
        The value is implementation (printer) specific."""
        ...
    
    @other_pages_tray.setter
    def other_pages_tray(self, value: int):
        ...
    
    @property
    def heading_level_for_chapter(self) -> int:
        """Gets or sets the heading level style that is applied to the chapter titles in the document.
        
        Can be a number from 0 through 9. 0 means no chapter number if applied to page number.
        
        Before you can create page numbers that include chapter numbers, the document headings must have a numbered outline format applied."""
        ...
    
    @heading_level_for_chapter.setter
    def heading_level_for_chapter(self, value: int):
        ...
    
    @property
    def chapter_page_separator(self) -> aspose.words.ChapterPageSeparator:
        """Gets or sets the separator character that appears between the chapter number and the page number.
        
        Before you can create page numbers that include chapter numbers, the document headings must have a numbered outline format applied."""
        ...
    
    @chapter_page_separator.setter
    def chapter_page_separator(self, value: aspose.words.ChapterPageSeparator):
        ...
    
    @property
    def page_number_style(self) -> aspose.words.NumberStyle:
        """Gets or sets the page number format."""
        ...
    
    @page_number_style.setter
    def page_number_style(self, value: aspose.words.NumberStyle):
        ...
    
    @property
    def restart_page_numbering(self) -> bool:
        """True if page numbering restarts at the beginning of the section.
        
        If set to ``False``, the :attr:`PageSetup.restart_page_numbering` property will override the
        :attr:`PageSetup.page_starting_number` property so that page numbering can continue from the previous section."""
        ...
    
    @restart_page_numbering.setter
    def restart_page_numbering(self, value: bool):
        ...
    
    @property
    def page_starting_number(self) -> int:
        """Gets or sets the starting page number of the section.
        
        The :attr:`PageSetup.restart_page_numbering` property, if set to ``False``, will override the
        :attr:`PageSetup.page_starting_number` property so that page numbering can continue from the previous section."""
        ...
    
    @page_starting_number.setter
    def page_starting_number(self, value: int):
        ...
    
    @property
    def line_number_restart_mode(self) -> aspose.words.LineNumberRestartMode:
        """Gets or sets the way line numbering runs  that is, whether it starts over at the beginning of a new
        page or section or runs continuously."""
        ...
    
    @line_number_restart_mode.setter
    def line_number_restart_mode(self, value: aspose.words.LineNumberRestartMode):
        ...
    
    @property
    def line_number_count_by(self) -> int:
        """Returns or sets the numeric increment for line numbers."""
        ...
    
    @line_number_count_by.setter
    def line_number_count_by(self, value: int):
        ...
    
    @property
    def line_number_distance_from_text(self) -> float:
        """Gets or sets distance between the right edge of line numbers and the left edge of the document.
        
        Set this property to zero for automatic distance between the line numbers and text of the document."""
        ...
    
    @line_number_distance_from_text.setter
    def line_number_distance_from_text(self, value: float):
        ...
    
    @property
    def line_starting_number(self) -> int:
        """Gets or sets the starting line number."""
        ...
    
    @line_starting_number.setter
    def line_starting_number(self, value: int):
        ...
    
    @property
    def text_columns(self) -> aspose.words.TextColumnCollection:
        """Returns a collection that represents the set of text columns."""
        ...
    
    @property
    def rtl_gutter(self) -> bool:
        """Gets or sets whether Microsoft Word uses gutters for the section based on a right-to-left language or a left-to-right language."""
        ...
    
    @rtl_gutter.setter
    def rtl_gutter(self, value: bool):
        ...
    
    @property
    def border_always_in_front(self) -> bool:
        """Specifies where the page border is positioned relative to intersecting texts and objects."""
        ...
    
    @border_always_in_front.setter
    def border_always_in_front(self, value: bool):
        ...
    
    @property
    def border_distance_from(self) -> aspose.words.PageBorderDistanceFrom:
        """Gets or sets a value that indicates whether the specified page border is measured from the edge of the page or from the text it surrounds."""
        ...
    
    @border_distance_from.setter
    def border_distance_from(self, value: aspose.words.PageBorderDistanceFrom):
        ...
    
    @property
    def border_applies_to(self) -> aspose.words.PageBorderAppliesTo:
        """Specifies which pages the page border is printed on."""
        ...
    
    @border_applies_to.setter
    def border_applies_to(self, value: aspose.words.PageBorderAppliesTo):
        ...
    
    @property
    def border_surrounds_header(self) -> bool:
        """Specifies whether the page border includes or excludes the header.
        
        Note, changing this property affects all sections in the document."""
        ...
    
    @border_surrounds_header.setter
    def border_surrounds_header(self, value: bool):
        ...
    
    @property
    def border_surrounds_footer(self) -> bool:
        """Specifies whether the page border includes or excludes the footer.
        
        Note, changing this property affects all sections in the document."""
        ...
    
    @border_surrounds_footer.setter
    def border_surrounds_footer(self, value: bool):
        ...
    
    @property
    def borders(self) -> aspose.words.BorderCollection:
        """Gets a collection of the page borders."""
        ...
    
    @property
    def footnote_options(self) -> aspose.words.notes.FootnoteOptions:
        """Provides options that control numbering and positioning of footnotes in this section."""
        ...
    
    @property
    def endnote_options(self) -> aspose.words.notes.EndnoteOptions:
        """Provides options that control numbering and positioning of endnotes in this section."""
        ...
    
    @property
    def text_orientation(self) -> aspose.words.TextOrientation:
        """Allows to specify :attr:`PageSetup.text_orientation` for the whole page.
        Default value is :attr:`TextOrientation.HORIZONTAL`
        
        This property is only supported for MS Word native formats DOCX, WML, RTF and DOC."""
        ...
    
    @text_orientation.setter
    def text_orientation(self, value: aspose.words.TextOrientation):
        ...
    
    ...

class Paragraph(aspose.words.CompositeNode):
    """Represents a paragraph of text.
    To learn more, visit the `Working with Paragraphs <https://docs.aspose.com/words/python-net/working-with-paragraphs/>` documentation article.
    
    :class:`Paragraph` is a block-level node and can be a child of classes derived from
    :class:`Story` or :class:`InlineStory`.
    
    :class:`Paragraph` can contain any number of inline-level nodes and bookmarks.
    
    The complete list of child nodes that can occur inside a paragraph consists of
    :class:`BookmarkStart`, :class:`BookmarkEnd`,
    :class:`aspose.words.fields.FieldStart`, :class:`aspose.words.fields.FieldSeparator`,
    :class:`aspose.words.fields.FieldEnd`, :class:`aspose.words.fields.FormField`,
    :class:`Comment`, :class:`aspose.words.notes.Footnote`,
    :class:`Run`, :class:`SpecialChar`,
    :class:`aspose.words.drawing.Shape`, :class:`aspose.words.drawing.GroupShape`,
    :class:`aspose.words.markup.SmartTag`.
    
    A valid paragraph in Microsoft Word always ends with a paragraph break character and
    a minimal valid paragraph consists just of a paragraph break. The :class:`Paragraph`
    class automatically appends the appropriate paragraph break character at the end
    and this character is not part of the child nodes of the :class:`Paragraph`, therefore
    a :class:`Paragraph` can be empty.
    
    Do not include the end of paragraph :attr:`ControlChar.PARAGRAPH_BREAK`
    or end of cell :attr:`ControlChar.CELL` characters inside the text of
    the paragraph as it might make the paragraph invalid when the document is opened in Microsoft Word."""
    
    def __init__(self, doc: aspose.words.DocumentBase):
        """Initializes a new instance of the :class:`Paragraph` class.
        
        When :class:`Paragraph` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append :class:`Paragraph` to the document use :meth:`CompositeNode.insert_after` or :meth:`CompositeNode.insert_before`
        on the story where you want the paragraph inserted.
        
        :param doc: The owner document."""
        ...
    
    @overload
    def append_field(self, field_type: aspose.words.fields.FieldType, update_field: bool) -> aspose.words.fields.Field:
        """Appends a field to this paragraph.
        
        :param field_type: The type of the field to append.
        :param update_field: Specifies whether to update the field immediately.
        :returns: A :class:`aspose.words.fields.Field` object that represents the appended field."""
        ...
    
    @overload
    def append_field(self, field_code: str) -> aspose.words.fields.Field:
        """Appends a field to this paragraph.
        
        :param field_code: The field code to append (without curly braces).
        :returns: A :class:`aspose.words.fields.Field` object that represents the appended field."""
        ...
    
    @overload
    def append_field(self, field_code: str, field_value: str) -> aspose.words.fields.Field:
        """Appends a field to this paragraph.
        
        :param field_code: The field code to append (without curly braces).
        :param field_value: The field value to append. Pass ``None`` for fields that do not have a value.
        :returns: A :class:`aspose.words.fields.Field` object that represents the appended field."""
        ...
    
    @overload
    def insert_field(self, field_type: aspose.words.fields.FieldType, update_field: bool, ref_node: aspose.words.Node, is_after: bool) -> aspose.words.fields.Field:
        """Inserts a field into this paragraph.
        
        :param field_type: The type of the field to insert.
        :param update_field: Specifies whether to update the field immediately.
        :param ref_node: Reference node inside this paragraph (if *refNode* is``None``, then appends to the end of the paragraph).
        :param is_after: Whether to insert the field after or before reference node.
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    @overload
    def insert_field(self, field_code: str, ref_node: aspose.words.Node, is_after: bool) -> aspose.words.fields.Field:
        """Inserts a field into this paragraph.
        
        :param field_code: The field code to insert (without curly braces).
        :param ref_node: Reference node inside this paragraph (if *refNode* is``None``, then appends to the end of the paragraph).
        :param is_after: Whether to insert the field after or before reference node.
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    @overload
    def insert_field(self, field_code: str, field_value: str, ref_node: aspose.words.Node, is_after: bool) -> aspose.words.fields.Field:
        """Inserts a field into this paragraph.
        
        :param field_code: The field code to insert (without curly braces).
        :param field_value: The field value to insert. Pass ``None`` for fields that do not have a value.
        :param ref_node: Reference node inside this paragraph (if *refNode* is``None``, then appends to the end of the paragraph).
        :param is_after: Whether to insert the field after or before reference node.
        :returns: A :class:`aspose.words.fields.Field` object that represents the inserted field."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`DocumentVisitor.visit_paragraph_start`, then calls :meth:`Node.accept` for all child nodes
        of the paragraph and calls :meth:`DocumentVisitor.visit_paragraph_end` at the end."""
        ...
    
    def get_text(self) -> str:
        """Gets the text of this paragraph including the end of paragraph character.
        
        The text of all child nodes is concatenated and the end of paragraph character is appended as follows:
        
        * If the paragraph is the last paragraph of :class:`Body`, then
          :attr:`ControlChar.SECTION_BREAK` (\\x000c) is appended.
        
        * If the paragraph is the last paragraph of :class:`aspose.words.tables.Cell`, then
          :attr:`ControlChar.CELL` (\\x0007) is appended.
        
        * For all other paragraphs
          :attr:`ControlChar.PARAGRAPH_BREAK` (\\r) is appended.
        
        The returned string includes all control and special characters as described in :class:`ControlChar`."""
        ...
    
    def accept_start(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the start of the document's paragraph.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def accept_end(self, visitor: aspose.words.DocumentVisitor) -> aspose.words.VisitorAction:
        """Accepts a visitor for visiting the end of the document's paragraph.
        
        :param visitor: The document visitor.
        :returns: The action to be taken by the visitor."""
        ...
    
    def get_effective_tab_stops(self) -> List[aspose.words.TabStop]:
        """Returns array of all tab stops applied to this paragraph, including applied indirectly by styles or lists."""
        ...
    
    def join_runs_with_same_formatting(self) -> int:
        """Joins runs with the same formatting in the paragraph.
        
        :returns: Number of joins performed. When **N** adjacent runs are being joined they count as **N - 1** joins."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.PARAGRAPH`."""
        ...
    
    @property
    def parent_story(self) -> aspose.words.Story:
        """Retrieves the parent section-level story that can be :class:`Body` or :class:`HeaderFooter`."""
        ...
    
    @property
    def parent_section(self) -> aspose.words.Section:
        """Retrieves the parent :class:`Section` of the paragraph."""
        ...
    
    @property
    def is_in_cell(self) -> bool:
        """True if this paragraph is an immediate child of :class:`aspose.words.tables.Cell`; false otherwise."""
        ...
    
    @property
    def is_end_of_cell(self) -> bool:
        """True if this paragraph is the last paragraph in a :class:`aspose.words.tables.Cell`; false otherwise."""
        ...
    
    @property
    def break_is_style_separator(self) -> bool:
        """True if this paragraph break is a Style Separator. A style separator allows one
        paragraph to consist of parts that have different paragraph styles."""
        ...
    
    @property
    def is_end_of_section(self) -> bool:
        """True if this paragraph is the last paragraph in the :class:`Body` (main text story) of a :class:`Section`; false otherwise."""
        ...
    
    @property
    def is_end_of_header_footer(self) -> bool:
        """True if this paragraph is the last paragraph in the :class:`HeaderFooter` (main text story) of a :class:`Section`; false otherwise."""
        ...
    
    @property
    def is_end_of_document(self) -> bool:
        """True if this paragraph is the last paragraph in the last section of the document."""
        ...
    
    @property
    def paragraph_format(self) -> aspose.words.ParagraphFormat:
        """Provides access to the paragraph formatting properties."""
        ...
    
    @property
    def list_format(self) -> aspose.words.lists.ListFormat:
        """Provides access to the list formatting properties of the paragraph."""
        ...
    
    @property
    def frame_format(self) -> aspose.words.FrameFormat:
        """Provides access to the frame formatting properties."""
        ...
    
    @property
    def list_label(self) -> aspose.words.lists.ListLabel:
        """Gets a :attr:`Paragraph.list_label` object that provides access to list numbering value and formatting
        for this paragraph."""
        ...
    
    @property
    def runs(self) -> aspose.words.RunCollection:
        """Provides access to the typed collection of pieces of text inside the paragraph."""
        ...
    
    @property
    def paragraph_break_font(self) -> aspose.words.Font:
        """Provides access to the font formatting of the paragraph break character."""
        ...
    
    @property
    def is_insert_revision(self) -> bool:
        """Returns true if this object was inserted in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_delete_revision(self) -> bool:
        """Returns true if this object was deleted in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_move_from_revision(self) -> bool:
        """Returns ``True`` if this object was moved (deleted) in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_move_to_revision(self) -> bool:
        """Returns ``True`` if this object was moved (inserted) in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_format_revision(self) -> bool:
        """Returns true if formatting of the object was changed in Microsoft Word while change tracking was enabled."""
        ...
    
    @property
    def is_list_item(self) -> bool:
        """True when the paragraph is an item in a bulleted or numbered list in original revision."""
        ...
    
    ...

class ParagraphCollection(aspose.words.NodeCollection):
    """Provides typed access to a collection of :class:`Paragraph` nodes.
    To learn more, visit the `Working with Paragraphs <https://docs.aspose.com/words/python-net/working-with-paragraphs/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.Paragraph:
        """Retrieves a :class:`Paragraph` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection."""
        ...
    
    def to_array(self) -> List[aspose.words.Paragraph]:
        """Copies all paragraphs from the collection to a new array of paragraphs.
        
        :returns: An array of paragraphs."""
        ...
    
    ...

class ParagraphFormat:
    """Represents all the formatting for a paragraph.
    To learn more, visit the `Working with Paragraphs <https://docs.aspose.com/words/python-net/working-with-paragraphs/>` documentation article."""
    
    def clear_formatting(self) -> None:
        """Resets to default paragraph formatting.
        
        Default paragraph formatting is Normal style, left aligned, no indentation,
        no spacing, no borders and no shading."""
        ...
    
    @property
    def alignment(self) -> aspose.words.ParagraphAlignment:
        """Gets or sets text alignment for the paragraph."""
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.words.ParagraphAlignment):
        ...
    
    @property
    def baseline_alignment(self) -> aspose.words.BaselineAlignment:
        """Gets or sets fonts vertical position on a line."""
        ...
    
    @baseline_alignment.setter
    def baseline_alignment(self, value: aspose.words.BaselineAlignment):
        ...
    
    @property
    def no_space_between_paragraphs_of_same_style(self) -> bool:
        """When ``True``, :attr:`ParagraphFormat.space_before` and :attr:`ParagraphFormat.space_after` will be ignored
        between the paragraphs of the same style.
        
        This setting only takes affect when applied to a paragraph style. If applied to
        a paragraph directly, it has no effect."""
        ...
    
    @no_space_between_paragraphs_of_same_style.setter
    def no_space_between_paragraphs_of_same_style(self, value: bool):
        ...
    
    @property
    def keep_together(self) -> bool:
        """True if all lines in the paragraph are to remain on the same page."""
        ...
    
    @keep_together.setter
    def keep_together(self, value: bool):
        ...
    
    @property
    def keep_with_next(self) -> bool:
        """True if the paragraph is to remains on the same page as the paragraph that follows it."""
        ...
    
    @keep_with_next.setter
    def keep_with_next(self, value: bool):
        ...
    
    @property
    def page_break_before(self) -> bool:
        """True if a page break is forced before the paragraph."""
        ...
    
    @page_break_before.setter
    def page_break_before(self, value: bool):
        ...
    
    @property
    def suppress_line_numbers(self) -> bool:
        """Specifies whether the current paragraph's lines should be exempted from line numbering
        which is applied in the parent section."""
        ...
    
    @suppress_line_numbers.setter
    def suppress_line_numbers(self, value: bool):
        ...
    
    @property
    def suppress_auto_hyphens(self) -> bool:
        """Specifies whether the current paragraph should be exempted from any hyphenation which
        is applied in the document settings."""
        ...
    
    @suppress_auto_hyphens.setter
    def suppress_auto_hyphens(self, value: bool):
        ...
    
    @property
    def widow_control(self) -> bool:
        """True if the first and last lines in the paragraph are to remain on the same page as the rest of the paragraph."""
        ...
    
    @widow_control.setter
    def widow_control(self, value: bool):
        ...
    
    @property
    def add_space_between_far_east_and_alpha(self) -> bool:
        """Gets or sets a flag indicating whether inter-character spacing is automatically adjusted between regions
        of Latin text and regions of East Asian text in the current paragraph."""
        ...
    
    @add_space_between_far_east_and_alpha.setter
    def add_space_between_far_east_and_alpha(self, value: bool):
        ...
    
    @property
    def add_space_between_far_east_and_digit(self) -> bool:
        """Gets or sets a flag indicating whether inter-character spacing is automatically adjusted between regions
        of numbers and regions of East Asian text in the current paragraph."""
        ...
    
    @add_space_between_far_east_and_digit.setter
    def add_space_between_far_east_and_digit(self, value: bool):
        ...
    
    @property
    def far_east_line_break_control(self) -> bool:
        """Gets or sets a flag indicating whether East Asian line-breaking rules are applied to the current paragraph."""
        ...
    
    @far_east_line_break_control.setter
    def far_east_line_break_control(self, value: bool):
        ...
    
    @property
    def word_wrap(self) -> bool:
        """If this property is ``False``, Latin text in the middle of a word can be wrapped for
        the current paragraph. Otherwise Latin text is wrapped by whole words."""
        ...
    
    @word_wrap.setter
    def word_wrap(self, value: bool):
        ...
    
    @property
    def hanging_punctuation(self) -> bool:
        """Gets or sets a flag indicating whether hanging punctuation is enabled for the current paragraph."""
        ...
    
    @hanging_punctuation.setter
    def hanging_punctuation(self, value: bool):
        ...
    
    @property
    def bidi(self) -> bool:
        """Gets or sets whether this is a right-to-left paragraph.
        
        When ``True``, the runs and other inline objects in this paragraph
        are laid out right to left."""
        ...
    
    @bidi.setter
    def bidi(self, value: bool):
        ...
    
    @property
    def left_indent(self) -> float:
        """Gets or sets the value (in points) that represents the left indent for paragraph."""
        ...
    
    @left_indent.setter
    def left_indent(self, value: float):
        ...
    
    @property
    def character_unit_left_indent(self) -> float:
        """Gets or sets the left indent value (in characters) for the specified paragraphs."""
        ...
    
    @character_unit_left_indent.setter
    def character_unit_left_indent(self, value: float):
        ...
    
    @property
    def right_indent(self) -> float:
        """Gets or sets the value (in points) that represents the right indent for paragraph."""
        ...
    
    @right_indent.setter
    def right_indent(self, value: float):
        ...
    
    @property
    def character_unit_right_indent(self) -> float:
        """Gets or sets the right indent value (in characters) for the specified paragraphs."""
        ...
    
    @character_unit_right_indent.setter
    def character_unit_right_indent(self, value: float):
        ...
    
    @property
    def first_line_indent(self) -> float:
        """Gets or sets the value (in points) for a first line or hanging indent.
        Use positive values to set the first-line indent, and negative values to set the hanging indent."""
        ...
    
    @first_line_indent.setter
    def first_line_indent(self, value: float):
        ...
    
    @property
    def character_unit_first_line_indent(self) -> float:
        """Gets or sets the value (in characters) for the first-line or hanging indent.
        Use positive values to set the first-line indent, and negative values to set the hanging indent."""
        ...
    
    @character_unit_first_line_indent.setter
    def character_unit_first_line_indent(self, value: float):
        ...
    
    @property
    def space_before_auto(self) -> bool:
        """True if the amount of spacing before the paragraph is set automatically.
        
        When set to ``True``, overrides the effect of :attr:`ParagraphFormat.space_before`.
        
        When you set paragraph Space Before and Space After to Auto,
        Microsoft Word adds 14 points spacing between paragraphs automatically
        according to the following rules:
        
        * Normally, spacing is added after all paragraphs.
        
        * In a bulleted or numbered list, spacing is added only after the last item in the list.
          Spacing is not added between the list items.
        
        * In a nested bulleted or numbered list spacing is not added.
        
        * Spacing is normally added after a table.
        
        * Spacing is not added after a table if it is the last block in a table cell.
        
        * Spacing is not added after the last paragraph in a table cell."""
        ...
    
    @space_before_auto.setter
    def space_before_auto(self, value: bool):
        ...
    
    @property
    def space_after_auto(self) -> bool:
        """True if the amount of spacing after the paragraph is set automatically.
        
        When set to ``True``, overrides the effect of :attr:`ParagraphFormat.space_after`.
        
        When you set paragraph Space Before and Space After to Auto,
        Microsoft Word adds 14 points spacing between paragraphs automatically
        according to the following rules:
        
        * Normally, spacing is added after all paragraphs.
        
        * In a bulleted or numbered list, spacing is added only after the last item in the list.
          Spacing is not added between the list items.
        
        * In a nested bulleted or numbered list spacing is not added.
        
        * Spacing is normally added after a table.
        
        * Spacing is not added after a table if it is the last block in a table cell.
        
        * Spacing is not added after the last paragraph in a table cell."""
        ...
    
    @space_after_auto.setter
    def space_after_auto(self, value: bool):
        ...
    
    @property
    def space_before(self) -> float:
        """Gets or sets the amount of spacing (in points) before the paragraph.
        
        Has no effect when :attr:`ParagraphFormat.space_before_auto` is ``True``.
        
        Valid values range from 0 to 1584 inclusive.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws when argument was out of the range of valid values."""
        ...
    
    @space_before.setter
    def space_before(self, value: float):
        ...
    
    @property
    def line_unit_before(self) -> float:
        """Gets or sets the amount of spacing (in gridlines) before the paragraphs."""
        ...
    
    @line_unit_before.setter
    def line_unit_before(self, value: float):
        ...
    
    @property
    def space_after(self) -> float:
        """Gets or sets the amount of spacing (in points) after the paragraph.
        
        Has no effect when :attr:`ParagraphFormat.space_after_auto` is ``True``.
        
        Valid values ​​range from 0 to 1584 inclusive.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws when argument was out of the range of valid values."""
        ...
    
    @space_after.setter
    def space_after(self, value: float):
        ...
    
    @property
    def line_unit_after(self) -> float:
        """Gets or sets the amount of spacing (in gridlines) after the paragraphs."""
        ...
    
    @line_unit_after.setter
    def line_unit_after(self, value: float):
        ...
    
    @property
    def line_spacing_rule(self) -> aspose.words.LineSpacingRule:
        """Gets or sets the line spacing for the paragraph."""
        ...
    
    @line_spacing_rule.setter
    def line_spacing_rule(self, value: aspose.words.LineSpacingRule):
        ...
    
    @property
    def line_spacing(self) -> float:
        """Gets or sets the line spacing (in points) for the paragraph.
        
        When :attr:`ParagraphFormat.line_spacing_rule` property is set to :attr:`LineSpacingRule.AT_LEAST`, the line spacing can be greater than or equal to,
        but never less than the specified :attr:`ParagraphFormat.line_spacing` value.
        
        When :attr:`ParagraphFormat.line_spacing_rule` property is set to :attr:`LineSpacingRule.EXACTLY`, the line spacing never changes from
        the specified :attr:`ParagraphFormat.line_spacing` value, even if a larger font is used within the paragraph."""
        ...
    
    @line_spacing.setter
    def line_spacing(self, value: float):
        ...
    
    @property
    def mirror_indents(self) -> bool:
        """Gets or sets a flag indicating whether the left and right indents are of the same width."""
        ...
    
    @mirror_indents.setter
    def mirror_indents(self, value: bool):
        ...
    
    @property
    def is_heading(self) -> bool:
        """True when the paragraph style is one of the built-in Heading styles."""
        ...
    
    @property
    def is_list_item(self) -> bool:
        """True when the paragraph is an item in a bulleted or numbered list."""
        ...
    
    @property
    def outline_level(self) -> aspose.words.OutlineLevel:
        """Specifies the outline level of the paragraph in the document."""
        ...
    
    @outline_level.setter
    def outline_level(self, value: aspose.words.OutlineLevel):
        ...
    
    @property
    def lines_to_drop(self) -> int:
        """Gets or sets the number of lines of the paragraph text used to calculate the drop cap height."""
        ...
    
    @lines_to_drop.setter
    def lines_to_drop(self, value: int):
        ...
    
    @property
    def drop_cap_position(self) -> aspose.words.DropCapPosition:
        """Gets or sets the position for a drop cap text."""
        ...
    
    @drop_cap_position.setter
    def drop_cap_position(self, value: aspose.words.DropCapPosition):
        ...
    
    @property
    def shading(self) -> aspose.words.Shading:
        """Returns a :class:`Shading` object that refers to the shading formatting for the paragraph."""
        ...
    
    @property
    def borders(self) -> aspose.words.BorderCollection:
        """Gets collection of borders of the paragraph."""
        ...
    
    @property
    def style(self) -> aspose.words.Style:
        """Gets or sets the paragraph style applied to this formatting."""
        ...
    
    @style.setter
    def style(self, value: aspose.words.Style):
        ...
    
    @property
    def style_name(self) -> str:
        """Gets or sets the name of the paragraph style applied to this formatting."""
        ...
    
    @style_name.setter
    def style_name(self, value: str):
        ...
    
    @property
    def style_identifier(self) -> aspose.words.StyleIdentifier:
        """Gets or sets the locale independent style identifier of the paragraph style applied to this formatting."""
        ...
    
    @style_identifier.setter
    def style_identifier(self, value: aspose.words.StyleIdentifier):
        ...
    
    @property
    def snap_to_grid(self) -> bool:
        """Specifies whether the current paragraph should use the document grid lines per page settings
        when laying out the contents in the paragraph."""
        ...
    
    @snap_to_grid.setter
    def snap_to_grid(self, value: bool):
        ...
    
    @property
    def tab_stops(self) -> aspose.words.TabStopCollection:
        """Gets the collection of custom tab stops defined for this object."""
        ...
    
    ...

class PhoneticGuide:
    """Represents Phonetic Guide."""
    
    @property
    def base_text(self) -> str:
        """Gets base text of the phonetic guide."""
        ...
    
    @property
    def ruby_text(self) -> str:
        """Gets ruby text of the phonetic guide."""
        ...
    
    ...

class PlainTextDocument:
    """Allows to extract plain-text representation of the document's content.
    To learn more, visit the `Working with Text Document <https://docs.aspose.com/words/python-net/working-with-text-document/>` documentation article."""
    
    @overload
    def __init__(self, file_name: str):
        """Creates a plain text document from a file. Automatically detects the file format.
        
        :param file_name: Name of the file to extract the text from.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentException)): The name of the file cannot be null or empty string."""
        ...
    
    @overload
    def __init__(self, file_name: str, load_options: aspose.words.loading.LoadOptions):
        """Creates a plain text document from a file. Allows to specify additional options such as an encryption password.
        
        :param file_name: Name of the file to extract the text from.
        :param load_options: Additional options to use when loading a document. Can be ``None``.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentException)): The name of the file cannot be null or empty string."""
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO):
        """Creates a plain text document from a stream. Automatically detects the file format.
        
        The document must be stored at the beginning of the stream. The stream must support random positioning.
        
        :param stream: The stream where to extract the text from.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentNullException)): The stream cannot be null.
        :raises RuntimeError (Proxy error(NotSupportedException)): The stream does not support reading or seeking.
        :raises RuntimeError (Proxy error(ObjectDisposedException)): The stream is a disposed object."""
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO, load_options: aspose.words.loading.LoadOptions):
        """Creates a plain text document from a stream. Allows to specify additional options such as an encryption password.
        
        The document must be stored at the beginning of the stream. The stream must support random positioning.
        
        :param stream: The stream where to extract the text from.
        :param load_options: Additional options to use when loading a document. Can be ``None``.
        :raises RuntimeError (Proxy error(UnsupportedFileFormatException)): The document format is not recognized or not supported.
        :raises RuntimeError (Proxy error(FileCorruptedException)): The document appears to be corrupted and cannot be loaded.
        :raises RuntimeError (Proxy error(Exception)): There is a problem with the document and it should be reported to Aspose.Words developers.
        :raises RuntimeError (Proxy error(IOException)): There is an input/output exception.
        :raises RuntimeError (Proxy error(IncorrectPasswordException)): The document is encrypted and requires a password to open, but you supplied an incorrect password.
        :raises RuntimeError (Proxy error(ArgumentNullException)): The stream cannot be null.
        :raises RuntimeError (Proxy error(NotSupportedException)): The stream does not support reading or seeking.
        :raises RuntimeError (Proxy error(ObjectDisposedException)): The stream is a disposed object."""
        ...
    
    @property
    def text(self) -> str:
        """Gets textual content of the document concatenated as a string."""
        ...
    
    @property
    def built_in_document_properties(self) -> aspose.words.properties.BuiltInDocumentProperties:
        """Gets :attr:`PlainTextDocument.built_in_document_properties` of the document."""
        ...
    
    @property
    def custom_document_properties(self) -> aspose.words.properties.CustomDocumentProperties:
        """Gets :attr:`PlainTextDocument.custom_document_properties` of the document."""
        ...
    
    ...

class Range:
    """Represents a contiguous area in a document.
    To learn more, visit the `Working with Ranges <https://docs.aspose.com/words/python-net/working-with-ranges/>` documentation article.
    
    The document is represented by a tree of nodes and the nodes provide operations
    to work with the tree, but some operations are easier to perform if the document
    is treated as a contiguous sequence of text.
    
    :class:`Range` is a "facade" interface that provide methods that treat the document
    or portions of the document as "flat" text regardless of the fact that the document
    nodes are stored in a tree-like object model.
    
    :class:`Range` does not contain any text or nodes, it is merely a view or "window"
    over a fragment of a document."""
    
    @overload
    def replace(self, pattern: str, replacement: str) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string.
        
        The pattern will not be used as regular expression.
        Please use Aspose.Words.Range.Replace(System.Text.RegularExpressions.Regex,System.String) if you need regular expressions.
        
        Used case-insensitive comparison.
        
        Method is able to process breaks in both pattern and replacement strings.
        
        You should use special meta-characters if you need to work with breaks:
        * **&p** - paragraph break
        
        * **&b** - section break
        
        * **&m** - page break
        
        * **&l** - manual line break
        
        Use method:meth:`Range.replace` to have more flexible customization.
        
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :returns: The number of replacements made."""
        ...
    
    @overload
    def replace(self, pattern: str, replacement: str, options: aspose.words.replacing.FindReplaceOptions) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string.
        
        The pattern will not be used as regular expression.
        Please use Aspose.Words.Range.Replace(System.Text.RegularExpressions.Regex,System.String,Aspose.Words.Replacing.FindReplaceOptions) if you need regular expressions.
        
        Method is able to process breaks in both pattern and replacement strings.
        
        You should use special meta-characters if you need to work with breaks:
        * **&p** - paragraph break
        
        * **&b** - section break
        
        * **&m** - page break
        
        * **&l** - manual line break
        
        * **&&** - & character
        
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :param options: :class:`aspose.words.replacing.FindReplaceOptions` object to specify additional options.
        :returns: The number of replacements made."""
        ...
    
    @overload
    def replace_regex(self, pattern: str, replacement: str) -> int:
        """Replaces all occurrences of a character pattern specified by a regular expression with another string.
        
        Replaces the whole match captured by the regular expression.
        
        Method is able to process breaks in both pattern and replacement strings.
        
        You should use special meta-characters if you need to work with breaks:
        * **&p** - paragraph break
        
        * **&b** - section break
        
        * **&m** - page break
        
        * **&l** - manual line break
        
        Use method:meth:`Range.replace_regex` to have more flexible customization.
        
        :param pattern: A regular expression pattern used to find matches.
        :param replacement: A string to replace all occurrences of pattern.
        :returns: The number of replacements made."""
        ...
    
    @overload
    def replace_regex(self, pattern: str, replacement: str, options: aspose.words.replacing.FindReplaceOptions) -> int:
        """Replaces all occurrences of a character pattern specified by a regular expression with another string.
        
        Replaces the whole match captured by the regular expression.
        
        Method is able to process breaks in both pattern and replacement strings.
        
        You should use special meta-characters if you need to work with breaks:
        * **&p** - paragraph break
        
        * **&b** - section break
        
        * **&m** - page break
        
        * **&l** - manual line break
        
        * **&&** - & character
        
        :param pattern: A regular expression pattern used to find matches.
        :param replacement: A string to replace all occurrences of pattern.
        :param options: :class:`aspose.words.replacing.FindReplaceOptions` object to specify additional options.
        :returns: The number of replacements made."""
        ...
    
    def delete(self) -> None:
        """Deletes all characters of the range."""
        ...
    
    def update_fields(self) -> None:
        """Updates the values of document fields in this range.
        
        When you open, modify and then save a document, Aspose.Words does not update fields automatically, it keeps them intact.
        Therefore, you would usually want to call this method before saving if you have modified the document
        programmatically and want to make sure the proper (calculated) field values appear in the saved document.
        
        There is no need to update fields after executing a mail merge because mail merge is a kind of field update
        and automatically updates all fields in the document.
        
        This method does not update all field types. For the detailed list of supported field types, see the Programmers Guide.
        
        This method does not update fields that are related to the page layout algorithms (e.g. PAGE, PAGES, PAGEREF).
        The page layout-related fields are updated when you render a document or call :meth:`Document.update_page_layout`.
        
        To update fields in the whole document use :meth:`Document.update_fields`."""
        ...
    
    def unlink_fields(self) -> None:
        """Unlinks fields in this range.
        
        Replaces all the fields in this range with their most recent results.
        
        To unlink fields in the whole document use :meth:`Range.unlink_fields`."""
        ...
    
    def normalize_field_types(self) -> None:
        """Changes field type values :attr:`aspose.words.fields.FieldChar.field_type` of :class:`aspose.words.fields.FieldStart`, :class:`aspose.words.fields.FieldSeparator`, :class:`aspose.words.fields.FieldEnd`
        in this range so that they correspond to the field types contained in the field codes.
        
        Use this method after document changes that affect field types.
        
        To change field type values in the whole document use :meth:`Document.normalize_field_types`."""
        ...
    
    def to_document(self) -> aspose.words.Document:
        """Constructs a new fully formed document that contains the range."""
        ...
    
    @property
    def text(self) -> str:
        """Gets the text of the range.
        
        The returned string includes all control and special characters as described in :class:`ControlChar`."""
        ...
    
    @property
    def form_fields(self) -> aspose.words.fields.FormFieldCollection:
        """Returns a :attr:`Range.form_fields` collection that represents all form fields in the range."""
        ...
    
    @property
    def bookmarks(self) -> aspose.words.BookmarkCollection:
        """Returns a :attr:`Range.bookmarks` collection that represents all bookmarks in the range."""
        ...
    
    @property
    def fields(self) -> aspose.words.fields.FieldCollection:
        """Returns a :attr:`Range.fields` collection that represents all fields in the range."""
        ...
    
    @property
    def structured_document_tags(self) -> aspose.words.markup.StructuredDocumentTagCollection:
        """Returns a :attr:`Range.structured_document_tags` collection that represents all structured document tags in the range."""
        ...
    
    @property
    def revisions(self) -> aspose.words.RevisionCollection:
        """Gets a collection of revisions (tracked changes) that exist in this range.
        
        The returned collection is a "live" collection, which means if you remove parts of a document that contain
        revisions, the deleted revisions will automatically disappear from this collection."""
        ...
    
    ...

class Revision:
    """Represents a revision (tracked change) in a document node or style.
    Use :attr:`Revision.revision_type` to check the type of this revision.
    To learn more, visit the `Track Changes in a Document <https://docs.aspose.com/words/python-net/track-changes-in-a-document/>` documentation article."""
    
    def accept(self) -> None:
        """Accepts this revision."""
        ...
    
    def reject(self) -> None:
        """Reject this revision."""
        ...
    
    @property
    def author(self) -> str:
        """Gets or sets the author of this revision. Can not be empty string or ``None``."""
        ...
    
    @author.setter
    def author(self, value: str):
        ...
    
    @property
    def date_time(self) -> datetime.datetime:
        """Gets or sets the date/time of this revision."""
        ...
    
    @date_time.setter
    def date_time(self, value: datetime.datetime):
        ...
    
    @property
    def revision_type(self) -> aspose.words.RevisionType:
        """Gets the type of this revision."""
        ...
    
    @property
    def parent_node(self) -> aspose.words.Node:
        """Gets the immediate parent node (owner) of this revision.
        This property will work for any revision type other than :attr:`RevisionType.STYLE_DEFINITION_CHANGE`.
        
        If this revision relates to change of Style formatting, use :attr:`Revision.parent_style` instead."""
        ...
    
    @property
    def parent_style(self) -> aspose.words.Style:
        """Gets the immediate parent style (owner) of this revision.
        This property will work for only for the :attr:`RevisionType.STYLE_DEFINITION_CHANGE` revision type.
        
        If this revision relates to changes on document nodes, use :attr:`Revision.parent_node` instead."""
        ...
    
    @property
    def group(self) -> aspose.words.RevisionGroup:
        """Gets the revision group. Returns ``None`` if the revision does not belong to any group.
        
        Revision has no group if revision type is :attr:`RevisionType.STYLE_DEFINITION_CHANGE` or
        if the revision is not longer exist in document context (accepted/rejected)."""
        ...
    
    ...

class RevisionCollection:
    """A collection of :class:`Revision` objects that represent revisions in the document.
    To learn more, visit the `Track Changes in a Document <https://docs.aspose.com/words/python-net/track-changes-in-a-document/>` documentation article.
    
    You do not create instances of this class directly. Use the :attr:`Document.revisions` property to get revisions present in a document."""
    
    def __getitem__(self, index: int) -> aspose.words.Revision:
        """Returns a :class:`Revision` at the specified index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection."""
        ...
    
    def accept_all(self) -> None:
        """Accepts all revisions in this collection."""
        ...
    
    def reject_all(self) -> None:
        """Rejects all revisions in this collection."""
        ...
    
    def accept(self, criteria: aspose.words.IRevisionCriteria) -> int:
        """Accepts revisions that match specified criteria.
        
        :param criteria: The :class:`IRevisionCriteria` implementation.
        :returns: The count of accepted revisions."""
        ...
    
    def reject(self, criteria: aspose.words.IRevisionCriteria) -> int:
        """Rejects revisions that match specified criteria.
        
        :param criteria: The :class:`IRevisionCriteria` implementation.
        :returns: The count of rejected revisions."""
        ...
    
    @property
    def count(self) -> int:
        """Returns the number of revisions in the collection."""
        ...
    
    @property
    def groups(self) -> aspose.words.RevisionGroupCollection:
        """Collection of revision groups."""
        ...
    
    ...

class RevisionGroup:
    """Represents a group of sequential :class:`Revision` objects.
    To learn more, visit the `Track Changes in a Document <https://docs.aspose.com/words/python-net/track-changes-in-a-document/>` documentation article."""
    
    @property
    def text(self) -> str:
        """Returns inserted/deleted/moved text or description of format change."""
        ...
    
    @property
    def author(self) -> str:
        """Gets the author of this revision group."""
        ...
    
    @property
    def revision_type(self) -> aspose.words.RevisionType:
        """Gets the type of revisions included in this group."""
        ...
    
    ...

class RevisionGroupCollection:
    """A collection of :class:`RevisionGroup` objects that represent revision groups in the document.
    To learn more, visit the `Track Changes in a Document <https://docs.aspose.com/words/python-net/track-changes-in-a-document/>` documentation article.
    
    You do not create instances of this class directly. Use the :attr:`RevisionCollection.groups`
    property to get revision groups present in a document."""
    
    def __getitem__(self, index: int) -> aspose.words.RevisionGroup:
        """Returns a revision group at the specified index."""
        ...
    
    @property
    def count(self) -> int:
        """Returns the number of revision groups in the collection."""
        ...
    
    ...

class Run(aspose.words.Inline):
    """Represents a run of characters with the same font formatting.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article.
    
    All text of the document is stored in runs of text.
    
    :class:`Run` can only be a child of :class:`Paragraph` or inline :class:`aspose.words.markup.StructuredDocumentTag`."""
    
    @overload
    def __init__(self, doc: aspose.words.DocumentBase):
        """Initializes a new instance of the :class:`Run` class.
        
        When :class:`Run` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append :class:`Run` to the document use :meth:`CompositeNode.insert_after` or :meth:`CompositeNode.insert_before`
        on the paragraph where you want the run inserted.
        
        :param doc: The owner document."""
        ...
    
    @overload
    def __init__(self, doc: aspose.words.DocumentBase, text: str):
        """Initializes a new instance of the **Run** class.
        
        When :class:`Run` is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To append :class:`Run` to the document use :meth:`CompositeNode.insert_after` or :meth:`CompositeNode.insert_before`
        on the paragraph where you want the run inserted.
        
        :param doc: The owner document.
        :param text: The text of the run."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_run`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    def get_text(self) -> str:
        """Gets the text of the run.
        
        :returns: The text of the run."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.RUN`."""
        ...
    
    @property
    def text(self) -> str:
        """Gets or sets the text of the run."""
        ...
    
    @text.setter
    def text(self, value: str):
        ...
    
    @property
    def is_phonetic_guide(self) -> bool:
        """Gets a boolean value indicating either the run is a phonetic guide."""
        ...
    
    @property
    def phonetic_guide(self) -> aspose.words.PhoneticGuide:
        """Gets a :attr:`Run.phonetic_guide` object."""
        ...
    
    ...

class RunCollection(aspose.words.NodeCollection):
    """Provides typed access to a collection of :class:`Run` nodes.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.Run:
        """Retrieves a :class:`Run` at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the collection."""
        ...
    
    def to_array(self) -> List[aspose.words.Run]:
        """Copies all runs from the collection to a new array of runs.
        
        :returns: An array of runs."""
        ...
    
    ...

class Section(aspose.words.CompositeNode):
    """Represents a single section in a document.
    To learn more, visit the `Working with Sections <https://docs.aspose.com/words/python-net/working-with-sections/>` documentation article.
    
    :class:`Section` can have one :class:`Body` and maximum one :class:`HeaderFooter`
    of each :class:`HeaderFooterType`. :class:`Body` and :class:`HeaderFooter` nodes
    can be in any order inside :class:`Section`.
    
    A minimal valid section needs to have :class:`Body` with one :class:`Paragraph`.
    
    Each section has its own set of properties that specify page size, orientation, margins etc.
    
    You can create a copy of a section using :meth:`Node.clone`. The copy can be inserted into
    the same or different document.
    
    To add, insert or remove a whole section including section break and
    section properties use methods of the :attr:`Document.sections` object.
    
    To copy and insert just content of the section excluding the section break
    and section properties use :meth:`Section.append_content` and :meth:`Section.prepend_content` methods."""
    
    def __init__(self, doc: aspose.words.DocumentBase):
        """Initializes a new instance of the Section class.
        
        When the section is created, it belongs to the specified document, but is not
        yet part of the document and :attr:`Node.parent_node` is ``None``.
        
        To include :class:`Section` into a document use :meth:`CompositeNode.insert_after` and
        :meth:`CompositeNode.insert_before` methods of the :class:`Document` OR
        :meth:`NodeCollection.add` and :meth:`NodeCollection.insert` methods of the :attr:`Document.sections` property.
        
        :param doc: The owner document."""
        ...
    
    @overload
    def clone(self) -> aspose.words.Section:
        """Creates a duplicate of this section."""
        ...
    
    @overload
    def clone(self, is_clone_children: bool) -> aspose.words.Node:
        """Creates a duplicate of this section."""
        ...
    
    @overload
    def clear_headers_footers(self) -> None:
        """Clears the headers and footers of this section.
        
        The text of all headers and footers is cleared, but :class:`HeaderFooter` objects themselves are not removed.
        
        This makes headers and footers of this section linked to headers and footers of the previous section."""
        ...
    
    @overload
    def clear_headers_footers(self, preserve_watermarks: bool) -> None:
        """Clears the headers and footers of this section.
        
        The text of all headers and footers is cleared, but :class:`HeaderFooter` objects themselves are not removed.
        
        This makes headers and footers of this section linked to headers and footers of the previous section.
        
        :param preserve_watermarks: True if the watermarks shall not be removed."""
        ...
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes.
        
        Calls :meth:`DocumentVisitor.visit_section_start`, then calls :meth:`Node.accept` for all child nodes of the section
        and calls :meth:`DocumentVisitor.visit_section_end` at the end."""
        ...
    
    def prepend_content(self, source_section: aspose.words.Section) -> None:
        """Inserts a copy of content of the source section at the beginning of this section.
        
        Only content of :attr:`Section.body` of the source section is copied, page setup,
        headers and footers are not copied.
        
        The nodes are automatically imported if the source section belongs to a different document.
        
        No new section is created in the destination document.
        
        :param source_section: The section to copy content from."""
        ...
    
    def append_content(self, source_section: aspose.words.Section) -> None:
        """Inserts a copy of content of the source section at the end of this section.
        
        Only content of :attr:`Section.body` of the source section is copied, page setup,
        headers and footers are not copied.
        
        The nodes are automatically imported if the source section belongs to a different document.
        
        No new section is created in the destination document.
        
        :param source_section: The section to copy content from."""
        ...
    
    def clear_content(self) -> None:
        """Clears the section.
        
        The text of :attr:`Section.body` is cleared, only one empty paragraph is left that represents the section break.
        
        The text of all headers and footers is cleared, but :class:`HeaderFooter` objects themselves are not removed."""
        ...
    
    def delete_header_footer_shapes(self) -> None:
        """Deletes all shapes (drawing objects) from the headers and footers of this section."""
        ...
    
    def ensure_minimum(self) -> None:
        """Ensures that the section has :attr:`Section.body` with one :class:`Paragraph`."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.SECTION`."""
        ...
    
    @property
    def body(self) -> aspose.words.Body:
        """Returns the :class:`Body` child node of the section.
        
        :class:`Body` contains main text of the section.
        
        Returns ``None`` if the section does not have a :class:`Body` node among its children."""
        ...
    
    @property
    def headers_footers(self) -> aspose.words.HeaderFooterCollection:
        """Provides access to the headers and footers nodes of the section."""
        ...
    
    @property
    def page_setup(self) -> aspose.words.PageSetup:
        """Returns an object that represents page setup and section properties."""
        ...
    
    @property
    def protected_for_forms(self) -> bool:
        """True if the section is protected for forms. When a section is protected for forms,
        users can select and modify text only in form fields in Microsoft Word."""
        ...
    
    @protected_for_forms.setter
    def protected_for_forms(self, value: bool):
        ...
    
    ...

class SectionCollection(aspose.words.NodeCollection):
    """A collection of :class:`Section` objects in the document.
    To learn more, visit the `Working with Sections <https://docs.aspose.com/words/python-net/working-with-sections/>` documentation article.
    
    A Microsoft Word document can contain multiple sections. To create a section in a Microsoft Word,
    select the Insert/Break command and select a break type. The break specifies whether section starts
    on a new page or on the same page.
    
    Programmatically inserting and removing sections can be used to customize documents produced
    during mail merge. If a document needs to have different content or parts of the
    content depending on some criteria, then you can create a "master" document that contains
    multiple sections and delete some of the sections before or after mail merge."""
    
    def __getitem__(self, index: int) -> aspose.words.Section:
        """Retrieves a section at the given index.
        
        The index is zero-based.
        
        Negative indexes are allowed and indicate access from the back of the collection.
        For example -1 means the last item, -2 means the second before last and so on.
        
        If index is greater than or equal to the number of items in the list, this returns a null reference.
        
        If index is negative and its absolute value is greater than the number of items in the list, this returns a null reference.
        
        :param index: An index into the list of sections."""
        ...
    
    def to_array(self) -> List[aspose.words.Section]:
        """Copies all sections from the collection to a new array of sections.
        
        :returns: An array of sections."""
        ...
    
    ...

class Shading(aspose.words.InternableComplexAttr):
    """Contains shading attributes for an object.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    def clear_formatting(self) -> None:
        """Removes shading from the object."""
        ...
    
    def equals(self, rhs: aspose.words.Shading) -> bool:
        """Determines whether the specified :class:`Shading` is equal in value to the current :class:`Shading`."""
        ...
    
    @property
    def background_pattern_color(self) -> aspose.pydrawing.Color:
        """Gets or sets the color that's applied to the background of the :class:`Shading` object."""
        ...
    
    @background_pattern_color.setter
    def background_pattern_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def foreground_pattern_color(self) -> aspose.pydrawing.Color:
        """Gets or sets the color that's applied to the foreground of the :class:`Shading` object."""
        ...
    
    @foreground_pattern_color.setter
    def foreground_pattern_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def texture(self) -> aspose.words.TextureIndex:
        """Gets or sets the shading texture."""
        ...
    
    @texture.setter
    def texture(self, value: aspose.words.TextureIndex):
        ...
    
    @property
    def foreground_pattern_theme_color(self) -> aspose.words.themes.ThemeColor:
        """Gets or sets the foreground pattern theme color in the applied color scheme that is associated with this :class:`Shading` object."""
        ...
    
    @foreground_pattern_theme_color.setter
    def foreground_pattern_theme_color(self, value: aspose.words.themes.ThemeColor):
        ...
    
    @property
    def background_pattern_theme_color(self) -> aspose.words.themes.ThemeColor:
        """Gets or sets the background pattern theme color in the applied color scheme that is associated with this :class:`Shading` object."""
        ...
    
    @background_pattern_theme_color.setter
    def background_pattern_theme_color(self, value: aspose.words.themes.ThemeColor):
        ...
    
    @property
    def foreground_tint_and_shade(self) -> float:
        """Gets or sets a double value that lightens or darkens a foreground theme color.
        
        The allowed values are in the range from -1 (the darkest) to 1 (the lightest) for this property.
        
        Zero (0) is neutral.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throw if set this property to a value less than -1 or more than 1.
        :raises RuntimeError (Proxy error(InvalidOperationException)): Throw if set this property for Shading object with non-theme colors."""
        ...
    
    @foreground_tint_and_shade.setter
    def foreground_tint_and_shade(self, value: float):
        ...
    
    @property
    def background_tint_and_shade(self) -> float:
        """Gets or sets a double value that lightens or darkens a background theme color.
        
        The allowed values are in the range from -1 (the darkest) to 1 (the lightest) for this property.
        
        Zero (0) is neutral.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throw if set this property to a value less than -1 or more than 1.
        :raises RuntimeError (Proxy error(InvalidOperationException)): Throw if set this property for Shading object with non-theme colors."""
        ...
    
    @background_tint_and_shade.setter
    def background_tint_and_shade(self, value: float):
        ...
    
    ...

class SignatureLineOptions:
    """Allows to specify options for signature line being inserted. Used in :class:`DocumentBuilder`.
    To learn more, visit the `Work with Digital Signatures <https://docs.aspose.com/words/python-net/working-with-digital-signatures/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def signer(self) -> str:
        """Gets or sets suggested signer of the signature line.
        Default value for this property is **empty string** ()."""
        ...
    
    @signer.setter
    def signer(self, value: str):
        ...
    
    @property
    def signer_title(self) -> str:
        """Gets or sets suggested signer's title.
        Default value for this property is **empty string** ()."""
        ...
    
    @signer_title.setter
    def signer_title(self, value: str):
        ...
    
    @property
    def email(self) -> str:
        """Gets or sets suggested signer's e-mail address.
        Default value for this property is **empty string** ()."""
        ...
    
    @email.setter
    def email(self, value: str):
        ...
    
    @property
    def default_instructions(self) -> bool:
        """Gets or sets a value indicating that default instructions is shown in the Sign dialog.
        Default value for this property is ``True``."""
        ...
    
    @default_instructions.setter
    def default_instructions(self, value: bool):
        ...
    
    @property
    def instructions(self) -> str:
        """Gets or sets instructions to the signer that are displayed on signing the signature line.
        Default value for this property is **empty string** ()."""
        ...
    
    @instructions.setter
    def instructions(self, value: str):
        ...
    
    @property
    def allow_comments(self) -> bool:
        """Gets or sets a value indicating that the signer can add comments in the Sign dialog.
        Default value for this property is ``False``."""
        ...
    
    @allow_comments.setter
    def allow_comments(self, value: bool):
        ...
    
    @property
    def show_date(self) -> bool:
        """Gets or sets a value indicating that sign date is shown in the signature line.
        Default value for this property is ``True``."""
        ...
    
    @show_date.setter
    def show_date(self, value: bool):
        ...
    
    ...

class SpecialChar(aspose.words.Inline):
    """Base class for special characters in the document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    A Microsoft Word document can include a number of special characters
    that represent fields, form fields, shapes, OLE objects, footnotes etc. For the list
    of special characters see :class:`ControlChar`.
    
    :class:`SpecialChar` is an inline-node and can only be a child of :class:`Paragraph`.
    
    :class:`SpecialChar` char is used as a base class for more specific classes
    that represent special characters that Aspose.Words provides programmatic access for.
    The :class:`SpecialChar` class is also used itself to represent special character for which
    Aspose.Words does not provide detailed programmatic access."""
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Calls :meth:`DocumentVisitor.visit_special_char`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the node.
        :returns: ``False`` if the visitor requested the enumeration to stop."""
        ...
    
    def get_text(self) -> str:
        """Gets the special character that this node represents.
        
        :returns: The string that contains the character that this node represents."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.SPECIAL_CHAR`."""
        ...
    
    ...

class Story(aspose.words.CompositeNode):
    """Base class for elements that contain block-level nodes :class:`Paragraph` and :class:`aspose.words.tables.Table`.
    To learn more, visit the `Logical Levels of Nodes in a Document <https://docs.aspose.com/words/python-net/logical-levels-of-nodes-in-a-document/>` documentation article.
    
    Text of a Word document is said to consist of several stories.
    The main text is stored in the main text story represented by :class:`Body`,
    each header and footer is stored in a separate story represented by :class:`HeaderFooter`."""
    
    def delete_shapes(self) -> None:
        """Deletes all shapes from the text of this story."""
        ...
    
    def append_paragraph(self, text: str) -> aspose.words.Paragraph:
        """A shortcut method that creates a :class:`Paragraph` object with optional text and appends it to the end of this object.
        
        :param text: The text for the paragraph. Can be ``None`` or empty string.
        :returns: The newly created and appended paragraph."""
        ...
    
    @property
    def story_type(self) -> aspose.words.StoryType:
        """Gets the type of this story."""
        ...
    
    @property
    def first_paragraph(self) -> aspose.words.Paragraph:
        """Gets the first paragraph in the story."""
        ...
    
    @property
    def last_paragraph(self) -> aspose.words.Paragraph:
        """Gets the last paragraph in the story."""
        ...
    
    @property
    def paragraphs(self) -> aspose.words.ParagraphCollection:
        """Gets a collection of paragraphs that are immediate children of the story."""
        ...
    
    @property
    def tables(self) -> aspose.words.tables.TableCollection:
        """Gets a collection of tables that are immediate children of the story."""
        ...
    
    ...

class Style:
    """Represents a single built-in or user-defined style.
    To learn more, visit the `Working with Styles and Themes <https://docs.aspose.com/words/python-net/working-with-styles-and-themes/>` documentation article."""
    
    def remove(self) -> None:
        """Removes the specified style from the document.
        
        Style removal has following effects on the document model:
        
        * All references to the style are removed from corresponding paragraphs, runs and tables.
        
        * If base style is removed its formatting is moved to child styles.
        
        * If style to be deleted has a linked style, then both of these are deleted."""
        ...
    
    def equals(self, style: aspose.words.Style) -> bool:
        """Compares with the specified style.
        Styles Istds are compared for built-in styles only.
        Styles defaults are not included in comparison.
        Base style, linked style and next paragraph style are recursively compared."""
        ...
    
    def as_table_style(self) -> aspose.words.TableStyle:
        ...
    
    @property
    def name(self) -> str:
        """Gets or sets the name of the style.
        
        Can not be empty string.
        
        If there already is a style with such name in the collection, then this style will override it. All affected nodes will reference new style."""
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def style_identifier(self) -> aspose.words.StyleIdentifier:
        """Gets the locale independent style identifier for a built-in style.
        
        For user defined (custom) styles, this property returns :attr:`StyleIdentifier.USER`."""
        ...
    
    @property
    def aliases(self) -> List[str]:
        """Gets all aliases of this style. If style has no aliases then empty array of string is returned."""
        ...
    
    @property
    def is_heading(self) -> bool:
        """True when the style is one of the built-in Heading styles."""
        ...
    
    @property
    def type(self) -> aspose.words.StyleType:
        """Gets the style type (paragraph or character)."""
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        """Gets the owner document."""
        ...
    
    @property
    def linked_style_name(self) -> str:
        """Gets/sets the name of the :class:`Style` linked to this one. Returns empty string if no styles are linked.
        
        It is only allowed to link the paragraph style to the character style and vice versa.
        
        Setting LinkedStyleName for the current style automatically leads to setting LinkedStyleName for the linked style.
        
        Assigning the empty string is equivalent to unlinking the previously linked style."""
        ...
    
    @linked_style_name.setter
    def linked_style_name(self, value: str):
        ...
    
    @property
    def base_style_name(self) -> str:
        """Gets/sets the name of the style this style is based on.
        
        This will be an empty string if the style is not based on any other style and it can be set
        to an empty string."""
        ...
    
    @base_style_name.setter
    def base_style_name(self, value: str):
        ...
    
    @property
    def next_paragraph_style_name(self) -> str:
        """Gets/sets the name of the style to be applied automatically to a new paragraph inserted after a
        paragraph formatted with the specified style.
        
        This property is not used by Aspose.Words. The next paragraph style will only
        be applied automatically when you edit the document in MS Word."""
        ...
    
    @next_paragraph_style_name.setter
    def next_paragraph_style_name(self, value: str):
        ...
    
    @property
    def built_in(self) -> bool:
        """True if this style is one of the built-in styles in MS Word."""
        ...
    
    @property
    def font(self) -> aspose.words.Font:
        """Gets the character formatting of the style.
        
        For list styles this property returns ``None``."""
        ...
    
    @property
    def paragraph_format(self) -> aspose.words.ParagraphFormat:
        """Gets the paragraph formatting of the style.
        
        For character and list styles this property returns ``None``."""
        ...
    
    @property
    def semi_hidden(self) -> bool:
        """Gets/sets whether the style hides from the Styles gallery and from the Styles task pane."""
        ...
    
    @semi_hidden.setter
    def semi_hidden(self, value: bool):
        ...
    
    @property
    def unhide_when_used(self) -> bool:
        """Gets/sets whether the style used in the current document unhides from the Styles gallery and from the Styles task pane.
        True when the used style should be shown in the Styles gallery."""
        ...
    
    @unhide_when_used.setter
    def unhide_when_used(self, value: bool):
        ...
    
    @property
    def priority(self) -> int:
        """Gets/sets the integer value that represents the priority for sorting the styles in the Styles task pane."""
        ...
    
    @priority.setter
    def priority(self, value: int):
        ...
    
    @property
    def list(self) -> aspose.words.lists.List:
        """Gets the list that defines formatting of this list style.
        
        This property is only valid for list styles.
        For other style types this property returns ``None``."""
        ...
    
    @property
    def list_format(self) -> aspose.words.lists.ListFormat:
        """Provides access to the list formatting properties of a paragraph style.
        
        This property is only valid for paragraph styles.
        For other style types this property returns ``None``."""
        ...
    
    @property
    def is_quick_style(self) -> bool:
        """Specifies whether this style is shown in the Quick Style gallery inside MS Word UI."""
        ...
    
    @is_quick_style.setter
    def is_quick_style(self, value: bool):
        ...
    
    @property
    def automatically_update(self) -> bool:
        """Specifies whether this style is automatically redefined based on the appropriate value.
        
        If the property value is set to true, MS Word automatically redefines the current style when
        the appropriate paragraph formatting has been changed.
        
        AutomaticallyUpdate property is applicable to paragraph styles only.
        
        The default value is ``False``."""
        ...
    
    @automatically_update.setter
    def automatically_update(self, value: bool):
        ...
    
    @property
    def locked(self) -> bool:
        """Specifies whether this style is locked."""
        ...
    
    @locked.setter
    def locked(self, value: bool):
        ...
    
    @property
    def styles(self) -> aspose.words.StyleCollection:
        """Gets the collection of styles this style belongs to."""
        ...
    
    ...

class StyleCollection:
    """A collection of :class:`Style` objects that represent both the built-in and user-defined styles in a document.
    To learn more, visit the `Working with Styles and Themes <https://docs.aspose.com/words/python-net/working-with-styles-and-themes/>` documentation article."""
    
    def __getitem__(self, index: int) -> aspose.words.Style:
        """Gets a style by index."""
        ...
    
    def clear_quick_style_gallery(self) -> None:
        """Removes all styles from the Quick Style Gallery panel."""
        ...
    
    def get_by_name(self, name: str) -> aspose.words.Style:
        """Gets a style by name or alias."""
        ...
    
    def get_by_style_identifier(self, sti: aspose.words.StyleIdentifier) -> aspose.words.Style:
        """Gets a built-in style by its locale independent identifier."""
        ...
    
    def add(self, type: aspose.words.StyleType, name: str) -> aspose.words.Style:
        """Creates a new user defined style and adds it the collection.
        
        You can create character, paragraph or a list style.
        
        When creating a list style, the style is created with default numbered list formatting (1 \\ a \\ i).
        
        Throws an exception if a style with this name already exists.
        
        :param type: A :class:`StyleType` value that specifies the type of the style to create.
        :param name: Case sensitive name of the style to create."""
        ...
    
    def add_copy(self, style: aspose.words.Style) -> aspose.words.Style:
        """Copies a style into this collection.
        
        :param style: Style to be copied.
        :returns: Copied style ready for usage.
        
        Style to be copied can belong to the same document as well as to different document.
        
        Linked style is copied.
        
        This method does doesn't copy base styles.
        
        If collection already contains a style with the same name, then new name is
        automatically generated by adding "_number" suffix starting from 0 e.g. "Normal_0", "Heading 1_1" etc.
        Use :attr:`Style.name` setter for changing the name of the imported style."""
        ...
    
    @property
    def document(self) -> aspose.words.DocumentBase:
        """Gets the owner document."""
        ...
    
    @property
    def default_font(self) -> aspose.words.Font:
        """Gets document default text formatting.
        
        Note that document-wide defaults were introduced in Microsoft Word 2007 and are fully supported in OOXML formats (:attr:`LoadFormat.DOCX`) only.
        Earlier document formats have limited support for this feature and only font names can be stored."""
        ...
    
    @property
    def default_paragraph_format(self) -> aspose.words.ParagraphFormat:
        """Gets document default paragraph formatting.
        
        Note that document-wide defaults were introduced in Microsoft Word 2007 and are fully supported in OOXML formats (:attr:`LoadFormat.DOCX`) only.
        Earlier document formats have no support for document default paragraph formatting."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of styles in the collection."""
        ...
    
    ...

class SubDocument(aspose.words.Node):
    """Represents a **SubDocument** - which is a reference to an externally stored document.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    In this version of Aspose.Words, :class:`SubDocument` nodes do not provide public methods
    and properties to create or modify a subdocument. In this version you are not able to instantiate
    :class:`SubDocument` nodes or modify existing except deleting them.
    
    :class:`SubDocument` can only be a child of :class:`Paragraph`."""
    
    def accept(self, visitor: aspose.words.DocumentVisitor) -> bool:
        """Accepts a visitor.
        
        Enumerates over this node and all of its children. Each node calls a corresponding method on :class:`DocumentVisitor`.
        
        For more info see the Visitor design pattern.
        
        :param visitor: The visitor that will visit the nodes.
        :returns: True if all nodes were visited; false if :class:`DocumentVisitor` stopped the operation before visiting all nodes."""
        ...
    
    @property
    def node_type(self) -> aspose.words.NodeType:
        """Returns :attr:`NodeType.SUB_DOCUMENT`."""
        ...
    
    ...

class TabStop:
    """Represents a single custom tab stop. The :class:`TabStop` object is a member of the
    :class:`TabStopCollection` collection.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    Normally, a tab stop specifies a position where a tab stop exists. But because
    tab stops can be inherited from parent styles, it might be needed for the child object
    to define explicitly that there is no tab stop at a given position. To clear
    an inherited tab stop at a given position, create a :class:`TabStop` object and set
    :attr:`TabStop.alignment` to :attr:`TabAlignment.CLEAR`.
    
    For more information see :class:`TabStopCollection`."""
    
    @overload
    def __init__(self, position: float):
        """Initializes a new instance of this class."""
        ...
    
    @overload
    def __init__(self, position: float, alignment: aspose.words.TabAlignment, leader: aspose.words.TabLeader):
        """Initializes a new instance of this class.
        
        :param position: The position of the tab stop in points.
        :param alignment: A :class:`TabAlignment` value that
                          specifies the alignment of text at this tab stop.
        :param leader: A :class:`TabLeader` value that specifies
                       the type of the leader line displayed under the tab character."""
        ...
    
    def equals(self, rhs: aspose.words.TabStop) -> bool:
        """Compares with the specified :class:`TabStop`."""
        ...
    
    @property
    def position(self) -> float:
        """Gets the position of the tab stop in points."""
        ...
    
    @property
    def alignment(self) -> aspose.words.TabAlignment:
        """Gets or sets the alignment of text at this tab stop."""
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.words.TabAlignment):
        ...
    
    @property
    def leader(self) -> aspose.words.TabLeader:
        """Gets or sets the type of the leader line displayed under the tab character."""
        ...
    
    @leader.setter
    def leader(self, value: aspose.words.TabLeader):
        ...
    
    @property
    def is_clear(self) -> bool:
        """Returns ``True`` if this tab stop clears any existing tab stops in this position."""
        ...
    
    ...

class TabStopCollection(aspose.words.InternableComplexAttr):
    """A collection of :class:`TabStop` objects that represent custom tabs for a paragraph or a style.
    To learn more, visit the `Aspose.Words Document Object Model (DOM) <https://docs.aspose.com/words/python-net/aspose-words-document-object-model/>` documentation article.
    
    In Microsoft Word documents, a tab stop can be defined in the properties of a paragraph
    style or directly in the properties of a paragraph. A style can be based on another style.
    Therefore, the complete set of tab stops for a given object is a combination of tab stops
    defined directly on this object and tab stops inherited from the parent styles.
    
    In Aspose.Words, when you obtain a :class:`TabStopCollection` for a paragraph or a style,
    it contains only the custom tab stops defined directly for this paragraph or style.
    The collection does not include tab stops defined in the parent styles or default tab stops."""
    
    def __getitem__(self, index: int) -> aspose.words.TabStop:
        """Gets a tab stop at the given index.
        
        :param index: An index into the collection of tab stops."""
        ...
    
    @overload
    def add(self, tab_stop: aspose.words.TabStop) -> None:
        """Adds or replaces a tab stop in the collection.
        
        If a tab stop already exists at the specified position, it is replaced.
        
        :param tab_stop: A tab stop object to add."""
        ...
    
    @overload
    def add(self, position: float, alignment: aspose.words.TabAlignment, leader: aspose.words.TabLeader) -> None:
        """Adds or replaces a tab stop in the collection.
        
        If a tab stop already exists at the specified position, it is replaced.
        
        :param position: A position (in points) where to add the tab stop.
        :param alignment: A :class:`TabAlignment` value that
                          specifies the alignment of text at the tab stop.
        :param leader: A :class:`TabLeader` value that
                       specifies the type of the leader line displayed under the tab character."""
        ...
    
    def equals(self, rhs: aspose.words.TabStopCollection) -> bool:
        """Determines whether the specified :class:`TabStopCollection` is equal in value to the current :class:`TabStopCollection`."""
        ...
    
    def clear(self) -> None:
        """Deletes all tab stop positions."""
        ...
    
    def get_position_by_index(self, index: int) -> float:
        """Gets the position (in points) of the tab stop at the specified index.
        
        :param index: An index into the collection of tab stops.
        :returns: The position of the tab stop."""
        ...
    
    def get_index_by_position(self, position: float) -> int:
        """Gets the index of a tab stop with the specified position in points."""
        ...
    
    def remove_by_position(self, position: float) -> None:
        """Removes a tab stop at the specified position from the collection.
        
        :param position: The position (in points) of the tab stop to remove."""
        ...
    
    def remove_by_index(self, index: int) -> None:
        """Removes a tab stop at the specified index from the collection.
        
        :param index: An index into the collection of tab stops."""
        ...
    
    def after(self, position: float) -> aspose.words.TabStop:
        """Gets a first tab stop to the right of the specified position.
        
        Skips tab stops with :attr:`TabStop.alignment` set to :attr:`TabAlignment.BAR`.
        
        :param position: The reference position (in points).
        :returns: A tab stop object or ``None`` if a suitable tab stop was not found."""
        ...
    
    def before(self, position: float) -> aspose.words.TabStop:
        """Gets a first tab stop to the left of the specified position.
        
        Skips tab stops with :attr:`TabStop.alignment` set to :attr:`TabAlignment.BAR`.
        
        :param position: The reference position (in points).
        :returns: A tab stop object or ``None`` if a suitable tab stop was not found."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of tab stops in the collection."""
        ...
    
    ...

class TableStyle(aspose.words.Style):
    """Represents a table style.
    To learn more, visit the `Working with Tables <https://docs.aspose.com/words/python-net/working-with-tables/>` documentation article."""
    
    @property
    def allow_break_across_pages(self) -> bool:
        """Gets or sets a flag indicating whether text in a table row is allowed to split across a page break.
        
        The default value is ``True``."""
        ...
    
    @allow_break_across_pages.setter
    def allow_break_across_pages(self, value: bool):
        ...
    
    @property
    def borders(self) -> aspose.words.BorderCollection:
        """Gets the collection of default cell borders for the style."""
        ...
    
    @property
    def left_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add to the left of the contents of table cells."""
        ...
    
    @left_padding.setter
    def left_padding(self, value: float):
        ...
    
    @property
    def right_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add to the right of the contents of table cells."""
        ...
    
    @right_padding.setter
    def right_padding(self, value: float):
        ...
    
    @property
    def top_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add above the contents of table cells."""
        ...
    
    @top_padding.setter
    def top_padding(self, value: float):
        ...
    
    @property
    def bottom_padding(self) -> float:
        """Gets or sets the amount of space (in points) to add below the contents of table cells."""
        ...
    
    @bottom_padding.setter
    def bottom_padding(self, value: float):
        ...
    
    @property
    def alignment(self) -> aspose.words.tables.TableAlignment:
        """Specifies the alignment for the table style.
        
        The default value is :attr:`aspose.words.tables.TableAlignment.LEFT`."""
        ...
    
    @alignment.setter
    def alignment(self, value: aspose.words.tables.TableAlignment):
        ...
    
    @property
    def cell_spacing(self) -> float:
        """Gets or sets the amount of space (in points) between the cells."""
        ...
    
    @cell_spacing.setter
    def cell_spacing(self, value: float):
        ...
    
    @property
    def bidi(self) -> bool:
        """Gets or sets whether this is a style for a right-to-left table.
        
        When ``True``, the cells in rows are laid out right to left.
        
        The default value is ``False``."""
        ...
    
    @bidi.setter
    def bidi(self, value: bool):
        ...
    
    @property
    def left_indent(self) -> float:
        """Gets or sets the value that represents the left indent of a table."""
        ...
    
    @left_indent.setter
    def left_indent(self, value: float):
        ...
    
    @property
    def shading(self) -> aspose.words.Shading:
        """Gets a :class:`Shading` object that refers to the shading formatting for table cells."""
        ...
    
    @property
    def vertical_alignment(self) -> aspose.words.tables.CellVerticalAlignment:
        """Specifies the vertical alignment for the cells.
        
        The default value is :attr:`aspose.words.tables.CellVerticalAlignment.TOP`."""
        ...
    
    @vertical_alignment.setter
    def vertical_alignment(self, value: aspose.words.tables.CellVerticalAlignment):
        ...
    
    @property
    def row_stripe(self) -> int:
        """Gets or sets a number of rows to include in the banding when the style specifies odd/even row banding."""
        ...
    
    @row_stripe.setter
    def row_stripe(self, value: int):
        ...
    
    @property
    def column_stripe(self) -> int:
        """Gets or sets a number of columns to include in the banding when the style specifies odd/even columns banding."""
        ...
    
    @column_stripe.setter
    def column_stripe(self, value: int):
        ...
    
    @property
    def conditional_styles(self) -> aspose.words.ConditionalStyleCollection:
        """Collection of conditional styles that may be defined for this table style."""
        ...
    
    ...

class TextColumn:
    """Represents a single text column. :class:`TextColumn` is a member of the :class:`TextColumnCollection` collection.
    The :class:`TextColumn` collection includes all the columns in a section of a document.
    To learn more, visit the `Working with Sections <https://docs.aspose.com/words/python-net/working-with-sections/>` documentation article.
    
    :class:`TextColumn` objects are only used to specify columns with custom width and spacing. If you want
    the columns in the document to be of equal width, set TextColumns.:attr:`TextColumnCollection.evenly_spaced` to ``True``.
    
    When a new :class:`TextColumn` is created it has its width and spacing set to zero."""
    
    @property
    def width(self) -> float:
        """Gets or sets the width of the text column in points."""
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def space_after(self) -> float:
        """Gets or sets the space between this column and the next column in points. Not required for the last column."""
        ...
    
    @space_after.setter
    def space_after(self, value: float):
        ...
    
    ...

class TextColumnCollection:
    """A collection of :class:`TextColumn` objects that represent all the columns of text in a section of a document.
    To learn more, visit the `Working with Sections <https://docs.aspose.com/words/python-net/working-with-sections/>` documentation article.
    
    Use :meth:`TextColumnCollection.set_count` to set the number of text columns.
    
    To make all columns equal width and spaced evenly, set :attr:`TextColumnCollection.evenly_spaced` to ``True``
    and specify the amount of space between the columns in :attr:`TextColumnCollection.spacing`. MS Word will
    automatically calculate column widths.
    
    If you have :attr:`TextColumnCollection.evenly_spaced` set to ``False``, you need to specify width and spacing for each
    column individually. Use the indexer to access individual :class:`TextColumn` objects.
    
    When using custom column widths, make sure the sum of all column widths and spacings between them
    equals page width minus left and right page margins."""
    
    def __getitem__(self, index: int) -> aspose.words.TextColumn:
        """Returns a text column at the specified index."""
        ...
    
    def set_count(self, new_count: int) -> None:
        """Arranges text into the specified number of text columns.
        
        When :attr:`TextColumnCollection.evenly_spaced` is ``False`` and you increase the number of columns,
        new :class:`TextColumn` objects are created with zero width and spacing.
        You need to set width and spacing for the new columns.
        
        :param new_count: The number of columns the text is to be arranged into."""
        ...
    
    @property
    def evenly_spaced(self) -> bool:
        """True if text columns are of equal width and evenly spaced."""
        ...
    
    @evenly_spaced.setter
    def evenly_spaced(self, value: bool):
        ...
    
    @property
    def spacing(self) -> float:
        """When columns are evenly spaced, gets or sets the amount of space between each column in points.
        
        Has effect only when :attr:`TextColumnCollection.evenly_spaced` is set to ``True``."""
        ...
    
    @spacing.setter
    def spacing(self, value: float):
        ...
    
    @property
    def width(self) -> float:
        """When columns are evenly spaced, gets the width of the columns.
        
        Has effect only when :attr:`TextColumnCollection.evenly_spaced` is set to ``True``."""
        ...
    
    @property
    def line_between(self) -> bool:
        """When ``True``, adds a vertical line between columns."""
        ...
    
    @line_between.setter
    def line_between(self, value: bool):
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of columns in the section of a document."""
        ...
    
    ...

class TextWatermarkOptions:
    """Contains options that can be specified when adding a watermark with text.
    To learn more, visit the `Working with Watermark <https://docs.aspose.com/words/python-net/working-with-watermark/>` documentation article."""
    
    def __init__(self):
        ...
    
    @property
    def font_family(self) -> str:
        """Gets or sets font family name. The default value is "Calibri"."""
        ...
    
    @font_family.setter
    def font_family(self, value: str):
        ...
    
    @property
    def color(self) -> aspose.pydrawing.Color:
        """Gets or sets font color. The default value is aspose.pydrawing.Color.silver."""
        ...
    
    @color.setter
    def color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def font_size(self) -> float:
        """Gets or sets a font size. The default value is 0 - auto.
        
        Valid values range from 0 to 65.5 inclusive.
        
        Auto font size means that the watermark will be scaled to its max width and max height relative to
        the page margins.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws when argument was out of the range of valid values."""
        ...
    
    @font_size.setter
    def font_size(self, value: float):
        ...
    
    @property
    def is_semitrasparent(self) -> bool:
        """Gets or sets a boolean value which is responsible for opacity of the watermark.
        The default value is ``True``."""
        ...
    
    @is_semitrasparent.setter
    def is_semitrasparent(self, value: bool):
        ...
    
    @property
    def layout(self) -> aspose.words.WatermarkLayout:
        """Gets or sets layout of the watermark. The default value is :attr:`WatermarkLayout.DIAGONAL`."""
        ...
    
    @layout.setter
    def layout(self, value: aspose.words.WatermarkLayout):
        ...
    
    ...

class UnsupportedFileFormatException(RuntimeError):
    """Thrown during document load, when the document format is not recognized or not supported by Aspose.Words.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    ...

class VariableCollection:
    """A collection of document variables.
    To learn more, visit the `Work with Document Properties <https://docs.aspose.com/words/python-net/work-with-document-properties/>` documentation article.
    
    Variable names and values are strings.
    
    Variable names are case-insensitive."""
    
    def __getitem__(self, index: int) -> str:
        """Gets or sets a document variable at the specified index.
        ``None`` values are not allowed as a right hand side of the assignment and will be replaced by empty string.
        
        :param index: Zero-based index of the document variable."""
        ...
    
    def __setitem__(self, index: int, value: str):
        ...
    
    def get_by_name(self, name: str) -> str:
        """Gets or a sets a document variable by the case-insensitive name.
        ``None`` values are not allowed as a right hand side of the assignment and will be replaced by empty string."""
        ...
    
    def add(self, name: str, value: str) -> None:
        """Adds a document variable to the collection.
        
        :param name: The case-insensitive name of the variable to add.
        :param value: The value of the variable. The value cannot be ``None``, if value is null empty string will be used instead."""
        ...
    
    def contains(self, name: str) -> bool:
        """Determines whether the collection contains a document variable with the given name.
        
        :param name: Case-insensitive name of the document variable to locate.
        :returns: ``True`` if item is found in the collection; otherwise, ``False``."""
        ...
    
    def index_of_key(self, name: str) -> int:
        """Returns the zero-based index of the specified document variable in the collection.
        
        :param name: The case-insensitive name of the variable.
        :returns: The zero based index. Negative value if not found."""
        ...
    
    def remove(self, name: str) -> None:
        """Removes a document variable with the specified name from the collection.
        
        :param name: The case-insensitive name of the variable."""
        ...
    
    def remove_at(self, index: int) -> None:
        """Removes a document variable at the specified index.
        
        :param index: The zero based index."""
        ...
    
    def clear(self) -> None:
        """Removes all elements from the collection."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of elements contained in the collection."""
        ...
    
    ...

class WarningInfo:
    """Contains information about a warning that Aspose.Words issued during document loading or saving.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article.
    
    You do not create instances of this class. Objects of this class are created
    and passed by Aspose.Words to the :meth:`IWarningCallback.warning` method."""
    
    @property
    def warning_type(self) -> aspose.words.WarningType:
        """Returns the type of the warning."""
        ...
    
    @property
    def description(self) -> str:
        """Returns the description of the warning."""
        ...
    
    @property
    def source(self) -> aspose.words.WarningSource:
        """Returns the source of the warning."""
        ...
    
    ...

class WarningInfoCollection:
    """Represents a typed collection of :class:`WarningInfo` objects.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article.
    
    You can use this collection object as the simplest form of :class:`IWarningCallback` implementation to gather
    all warnings that Aspose.Words generates during a load or save operation. Create an instance of this class and assign it
    to the :attr:`aspose.words.loading.LoadOptions.warning_callback` or :attr:`DocumentBase.warning_callback` property."""
    
    def __init__(self):
        ...
    
    def __getitem__(self, index: int) -> aspose.words.WarningInfo:
        """Gets an item at the specified index.
        
        :param index: Zero-based index of the item."""
        ...
    
    def clear(self) -> None:
        """Removes all elements from the collection."""
        ...
    
    def warning(self, info: aspose.words.WarningInfo) -> None:
        """Implements the :class:`IWarningCallback` interface. Adds a warning to this collection."""
        ...
    
    @property
    def count(self) -> int:
        """Gets the number of elements contained in the collection."""
        ...
    
    ...

class Watermark:
    """Represents class to work with document watermark.
    To learn more, visit the `Working with Watermark <https://docs.aspose.com/words/python-net/working-with-watermark/>` documentation article."""
    
    @overload
    def set_text(self, text: str) -> None:
        """Adds Text watermark into the document.
        
        :param text: Text that is displayed as a watermark.
        
        The text length must be in the range from 1 to 200 inclusive.
        The text cannot be ``None`` or contain only whitespaces.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws when the text length is out of range or the text contains only whitespaces.
        :raises RuntimeError (Proxy error(ArgumentNullException)): Throws when the text is ``None``."""
        ...
    
    @overload
    def set_text(self, text: str, options: aspose.words.TextWatermarkOptions) -> None:
        """Adds Text watermark into the document.
        
        :param text: Text that is displayed as a watermark.
        :param options: Defines additional options for the text watermark.
        
        The text length must be in the range from 1 to 200 inclusive.
        The text cannot be ``None`` or contain only whitespaces.
        
        :raises RuntimeError (Proxy error(ArgumentOutOfRangeException)): Throws when the text length is out of range or the text contain only whitespaces.
        :raises RuntimeError (Proxy error(ArgumentNullException)): Throws when the text is ``None``.
        
        If :class:`TextWatermarkOptions` is ``None``, the watermark will be set with default options."""
        ...
    
    def set_image(self, image_path: str, options: aspose.words.ImageWatermarkOptions) -> None:
        """Adds Image watermark into the document.
        
        :param image_path: Path to the image file that is displayed as a watermark.
        :param options: Defines additional options for the image watermark.
        :raises RuntimeError (Proxy error(ArgumentNullException)): Throws when the path is ``None``.
        
        If :class:`ImageWatermarkOptions` is ``None``, the watermark will be set with default options."""
        ...
    
    def remove(self) -> None:
        """Removes the watermark."""
        ...
    
    @property
    def type(self) -> aspose.words.WatermarkType:
        """Gets the watermark type."""
        ...
    
    ...

class BaselineAlignment(Enum):
    """Specifies fonts vertical position on a line."""
    
    """Aligns along the top of each font."""
    TOP: int
    
    """Aligns the center points of each font."""
    CENTER: int
    
    """Aligns to the baseline of the paragraph."""
    BASELINE: int
    
    """Aligns to the bottom of each font."""
    BOTTOM: int
    
    """Baseline is adjusted automatically."""
    AUTO: int
    

class BorderType(Enum):
    """Specifies sides of a border.
    To learn more, visit the `Programming with Documents <https://docs.aspose.com/words/python-net/programming-with-documents/>` documentation article."""
    
    """Default value."""
    NONE: int
    
    """Specifies the bottom border of a paragraph or a table cell."""
    BOTTOM: int
    
    """Specifies the left border of a paragraph or a table cell."""
    LEFT: int
    
    """Specifies the right border of a paragraph or a table cell."""
    RIGHT: int
    
    """Specifies the top border of a paragraph or a table cell."""
    TOP: int
    
    """Specifies the horizontal border between cells in a table or between conforming paragraphs."""
    HORIZONTAL: int
    
    """Specifies the vertical border between cells in a table."""
    VERTICAL: int
    
    """Specifies the diagonal border in a table cell."""
    DIAGONAL_DOWN: int
    
    """Specifies the diagonal border in a table cell."""
    DIAGONAL_UP: int
    

class BreakType(Enum):
    """Specifies type of a break inside a document."""
    
    """Break between paragraphs."""
    PARAGRAPH_BREAK: int
    
    """Explicit page break."""
    PAGE_BREAK: int
    
    """Explicit column break."""
    COLUMN_BREAK: int
    
    """Specifies start of new section on the same page as the previous section."""
    SECTION_BREAK_CONTINUOUS: int
    
    """Specifies start of new section in the new column."""
    SECTION_BREAK_NEW_COLUMN: int
    
    """Specifies start of new section on a new page."""
    SECTION_BREAK_NEW_PAGE: int
    
    """Specifies start of new section on a new even page."""
    SECTION_BREAK_EVEN_PAGE: int
    
    """Specifies start of new section on a odd page."""
    SECTION_BREAK_ODD_PAGE: int
    
    """Explicit line break."""
    LINE_BREAK: int
    

class CalendarType(Enum):
    """Specifies the type of a calendar."""
    
    """The Gregorian calendar."""
    GREGORIAN: int
    
    """The Hijri Lunar calendar."""
    HIJRI: int
    
    """The Hebrew Lunar calendar."""
    HEBREW: int
    
    """The Saka Era calendar."""
    SAKA_ERA: int
    
    """The Um-al-Qura calendar."""
    UM_AL_QURA: int
    

class ChapterPageSeparator(Enum):
    """Defines the separator character that appears between the chapter and page number."""
    
    """A colon."""
    HYPHEN: int
    
    """A period."""
    PERIOD: int
    
    """A colon."""
    COLON: int
    
    """An emphasized dash."""
    EM_DASH: int
    
    """A standard dash."""
    EN_DASH: int
    

class ConditionalStyleType(Enum):
    """Represents possible table areas to which conditional formatting may be defined in a table style."""
    
    """Specifies formatting of the first row of a table."""
    FIRST_ROW: int
    
    """Specifies formatting of the first column of a table."""
    FIRST_COLUMN: int
    
    """Specifies formatting of the last row of a table."""
    LAST_ROW: int
    
    """Specifies formatting of the last column of a table."""
    LAST_COLUMN: int
    
    """Specifies formatting of odd-numbered row stripe."""
    ODD_ROW_BANDING: int
    
    """Specifies formatting of odd-numbered column stripe."""
    ODD_COLUMN_BANDING: int
    
    """Specifies formatting of even-numbered row stripe."""
    EVEN_ROW_BANDING: int
    
    """Specifies formatting of even-numbered column stripe."""
    EVEN_COLUMN_BANDING: int
    
    """Specifies formatting of the top left cell of a table."""
    TOP_LEFT_CELL: int
    
    """Specifies formatting of the top right cell of a table."""
    TOP_RIGHT_CELL: int
    
    """Specifies formatting of the bottom left cell of a table."""
    BOTTOM_LEFT_CELL: int
    
    """Specifies formatting of the bottom right cell of a table."""
    BOTTOM_RIGHT_CELL: int
    

class ContentDisposition(Enum):
    """Enumerates different ways of presenting the document at the client browser.
    
    Note that the actual behavior on the client browser might be affected by security configuration of the browser."""
    
    """Send the document to the browser and present an option to save the document to disk or open in the application
    associated with the document's extension."""
    ATTACHMENT: int
    
    """Send the document to the browser and presents an option to save the document to disk or open inside the browser."""
    INLINE: int
    

class DropCapPosition(Enum):
    """Specifies the position for a drop cap text."""
    
    """The paragraph does not have a drop cap."""
    NONE: int
    
    """The drop cap is positioned inside the text margin on the anchor paragraph."""
    NORMAL: int
    
    """The drop cap is positioned outside the text margin on the anchor paragraph."""
    MARGIN: int
    

class EditorType(Enum):
    """Specifies the set of possible aliases (or editing groups) which can be used as aliases to
    determine if the current user shall be allowed to edit a single range
    defined by an editable range within a document."""
    
    """Means that editor type is not specified."""
    UNSPECIFIED: int
    
    """Specifies that users associated with the Administrators group shall be allowed to edit editable ranges using
    this editing type when document protection is enabled."""
    ADMINISTRATORS: int
    
    """Specifies that users associated with the Contributors group shall be allowed to edit editable ranges using
    this editing type when document protection is enabled."""
    CONTRIBUTORS: int
    
    """Specifies that users associated with the Current group shall be allowed to edit editable ranges using this
    editing type when document protection is enabled."""
    CURRENT: int
    
    """Specifies that users associated with the Editors group shall be allowed to edit editable ranges using this
    editing type when document protection is enabled."""
    EDITORS: int
    
    """Specifies that all users that open the document shall be allowed to edit editable ranges using this editing
    type when document protection is enabled."""
    EVERYONE: int
    
    """Specifies that none of the users that open the document shall be allowed to edit editable ranges
    using this editing type when document protection is enabled."""
    NONE: int
    
    """Specifies that users associated with the Owners group shall be allowed to edit editable ranges using this
    editing type when document protection is enabled."""
    OWNERS: int
    
    """Same as :attr:`EditorType.UNSPECIFIED`."""
    DEFAULT: int
    

class EmphasisMark(Enum):
    """Specifies possible types of emphasis mark."""
    
    """No emphasis mark."""
    NONE: int
    
    """Emphasis mark is a solid black circle displayed above text."""
    OVER_SOLID_CIRCLE: int
    
    """Emphasis mark is a comma character displayed above text."""
    OVER_COMMA: int
    
    """Emphasis mark is an empty white circle displayed above text."""
    OVER_WHITE_CIRCLE: int
    
    """Emphasis mark is a solid black circle displayed below text."""
    UNDER_SOLID_CIRCLE: int
    

class HeaderFooterType(Enum):
    """Identifies the type of header or footer found in a Word file."""
    
    """Header for even numbered pages."""
    HEADER_EVEN: int
    
    """Primary header, also used for odd numbered pages."""
    HEADER_PRIMARY: int
    
    """Footer for even numbered pages."""
    FOOTER_EVEN: int
    
    """Primary footer, also used for odd numbered pages."""
    FOOTER_PRIMARY: int
    
    """Header for the first page of the section."""
    HEADER_FIRST: int
    
    """Footer for the first page of the section."""
    FOOTER_FIRST: int
    

class HeightRule(Enum):
    """Specifies the rule for determining the height of an object."""
    
    """The height will be at least the specified height in points. It will grow, if needed,
    to accommodate all text inside an object."""
    AT_LEAST: int
    
    """The height is specified exactly in points. Please note that if the text cannot
    fit inside the object of this height, it will appear truncated."""
    EXACTLY: int
    
    """The height will grow automatically to accommodate all text inside an object."""
    AUTO: int
    

class HtmlInsertOptions(Enum):
    """Specifies options for the :meth:`DocumentBuilder.insert_html` method."""
    
    """Use the default options when inserting HTML."""
    NONE: int
    
    """Use font and paragraph formatting specified in :class:`DocumentBuilder` as base formatting for text
    inserted from HTML.
    
    If this option is not specified, formatting of :class:`DocumentBuilder` is ignored and text is inserted
    with default HTML formatting. As a result, the text looks as it is rendered in browsers.
    
    If this option is specified, formatting of inserted text is based on formatting specified in
    :class:`DocumentBuilder`, and the text looks as if it were inserted using :meth:`DocumentBuilder.write`."""
    USE_BUILDER_FORMATTING: int
    
    """Remove the empty paragraph that is normally inserted after HTML that ends with a block-level element.
    
    By default, :class:`DocumentBuilder` makes sure that the last block-level element imported from HTML
    is closed after import and inserts a paragraph break after the element. This paragraph break separates
    content imported from HTML from content of the template document. However, if a HTML fragment is inserted into
    an empty paragraph, that paragraph break will create an extra empty paragraph. If this behavior is undesired,
    specify this option."""
    REMOVE_LAST_EMPTY_PARAGRAPH: int
    
    """Preserve properties of block-level elements.
    
    By default, properties of parent blocks are merged and stored on their child elements (i.e. paragraphs or tables).
    If this option is specified, properties of each block are stored separately in a special logical structure.
    As a result, this option allows to better preserve individual borders and margins seen in the HTML document
    and get better conversion results. The downside is that the resulting document gets harder to modify, since borders
    and margins stored in the logical structure are not available for editing.
    
    Only margins and borders of 'body', 'div', and 'blockquote' HTML elements are preserved. Properties of each HTML
    element are stored separately.
    
    If this option is specified, Aspose.Words mimics MS Word's behavior regarding import of block properties."""
    PRESERVE_BLOCKS: int
    

class ImportFormatMode(Enum):
    """Specifies how formatting is merged when importing content from another document.
    
    When you copy nodes from one document to another, this option specifies how formatting
    is resolved when both documents have a style with the same name, but different formatting.
    
    The formatting is resolved as follows:
    
    1. Built-in styles are matched using their locale independent style identifier.
       User defined styles are matched using case-sensitive style name.
    
    1. If a matching style is not found in the destination document, the style
       (and all styles referenced by it) are copied into the destination document
       and the imported nodes are updated to reference the new style.
    
    1. If a matching style already exists in the destination document, what happens
       depends on the ``importFormatMode`` parameter passed to
       :meth:`DocumentBase.import_node`
       as described below.
    
    When using the :attr:`ImportFormatMode.USE_DESTINATION_STYLES` option, if a matching style already exists
    in the destination document, the style is not copied and the imported nodes are updated
    to reference the existing style.
    
    The drawback of using :attr:`ImportFormatMode.USE_DESTINATION_STYLES` is that the imported text might
    look different in the destination document comparing to the source document.
    For example, the "Heading 1" style in the source document uses Arial 16pt font and
    the "Heading 1" style in the destination document uses Times New Roman 14pt font.
    When importing text of "Heading 1" style with no other direct formatting, it will
    appear as Times New Roman 14pt font in the destination document.
    
    :attr:`ImportFormatMode.KEEP_SOURCE_FORMATTING` option allows to make sure the imported content looks the same
    in the destination document like it looks in the source document.
    If a matching style already exists in the destination document, the source style formatting is expanded
    into direct Node attributes and the style is changed to Normal.
    If the style does not exist in the destination document, then the source style is imported
    into the destination document and applied to the imported node.
    Note, that it is not always possible to preserve the source style even if it does not exist in the destination document.
    In this case formatting of such style will be expanded into direct Node attributes in favor of preserving original Node formatting.
    
    The drawback of using :attr:`ImportFormatMode.KEEP_SOURCE_FORMATTING` is that if you perform several imports,
    you could end up with many styles in the destination document and that could make using
    consistent style formatting in Microsoft Word difficult for this document.
    
    Using :attr:`ImportFormatMode.KEEP_DIFFERENT_STYLES` option allows to reuse destination styles
    if the formatting they provide is identical to the styles in the source document.
    If the style in destination document is different from the source then it is imported."""
    
    """Use the destination document styles and copy new styles. This is the default option."""
    USE_DESTINATION_STYLES: int
    
    """Copy all required styles to the destination document, generate unique style names if needed."""
    KEEP_SOURCE_FORMATTING: int
    
    """Only copy styles that are different from those in the source document."""
    KEEP_DIFFERENT_STYLES: int
    

class LineNumberRestartMode(Enum):
    """Determines when automatic line numbering restarts."""
    
    """Line numbering restarts at the start of every page."""
    RESTART_PAGE: int
    
    """Line numbering restarts at the section start."""
    RESTART_SECTION: int
    
    """Line numbering continuous from the previous section."""
    CONTINUOUS: int
    

class LineSpacingRule(Enum):
    """Specifies line spacing values for a paragraph."""
    
    """The line spacing can be greater than or equal to, but never less than,
    the value specified in the :attr:`ParagraphFormat.line_spacing` property."""
    AT_LEAST: int
    
    """The line spacing never changes from the value specified in the
    :attr:`ParagraphFormat.line_spacing` property,
    even if a larger font is used within the paragraph."""
    EXACTLY: int
    
    """The line spacing is specified in the :attr:`ParagraphFormat.line_spacing`
    property as the number of lines. One line equals 12 points."""
    MULTIPLE: int
    

class LineStyle(Enum):
    """Specifies line style of a :class:`Border`."""
    
    NONE: int
    
    SINGLE: int
    
    THICK: int
    
    DOUBLE: int
    
    HAIRLINE: int
    
    DOT: int
    
    DASH_LARGE_GAP: int
    
    DOT_DASH: int
    
    DOT_DOT_DASH: int
    
    TRIPLE: int
    
    THIN_THICK_SMALL_GAP: int
    
    THICK_THIN_SMALL_GAP: int
    
    THIN_THICK_THIN_SMALL_GAP: int
    
    THIN_THICK_MEDIUM_GAP: int
    
    THICK_THIN_MEDIUM_GAP: int
    
    THIN_THICK_THIN_MEDIUM_GAP: int
    
    THIN_THICK_LARGE_GAP: int
    
    THICK_THIN_LARGE_GAP: int
    
    THIN_THICK_THIN_LARGE_GAP: int
    
    WAVE: int
    
    DOUBLE_WAVE: int
    
    DASH_SMALL_GAP: int
    
    DASH_DOT_STROKER: int
    
    EMBOSS_3D: int
    
    ENGRAVE_3D: int
    
    OUTSET: int
    
    INSET: int
    

class LoadFormat(Enum):
    """Indicates the format of the document that is to be loaded."""
    
    """Instructs Aspose.Words to recognize the format automatically."""
    AUTO: int
    
    """Microsoft Word 95 or Word 97 - 2003 Document."""
    DOC: int
    
    """Microsoft Word 95 or Word 97 - 2003 Template."""
    DOT: int
    
    """The document is in pre-Word 95 format.
    Aspose.Words does not currently support loading such documents."""
    DOC_PRE_WORD60: int
    
    """Office Open XML WordprocessingML Document (macro-free)."""
    DOCX: int
    
    """Office Open XML WordprocessingML Macro-Enabled Document."""
    DOCM: int
    
    """Office Open XML WordprocessingML Template (macro-free)."""
    DOTX: int
    
    """Office Open XML WordprocessingML Macro-Enabled Template."""
    DOTM: int
    
    """Office Open XML WordprocessingML stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC: int
    
    """Office Open XML WordprocessingML Macro-Enabled Document stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC_MACRO_ENABLED: int
    
    """Office Open XML WordprocessingML Template (macro-free) stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC_TEMPLATE: int
    
    """Office Open XML WordprocessingML Macro-Enabled Template stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC_TEMPLATE_MACRO_ENABLED: int
    
    """RTF format."""
    RTF: int
    
    """Microsoft Word 2003 WordprocessingML format."""
    WORD_ML: int
    
    """HTML format."""
    HTML: int
    
    """MHTML (Web archive) format."""
    MHTML: int
    
    """MOBI format. Used by MobiPocket reader and Amazon Kindle readers."""
    MOBI: int
    
    """CHM (Compiled HTML Help) format."""
    CHM: int
    
    """AZW3 format. Used by Amazon Kindle readers."""
    AZW3: int
    
    """EPUB format."""
    EPUB: int
    
    """ODF Text Document."""
    ODT: int
    
    """ODF Text Document Template."""
    OTT: int
    
    """Plain Text."""
    TEXT: int
    
    """Markdown text document."""
    MARKDOWN: int
    
    """Pdf document."""
    PDF: int
    
    """XML document."""
    XML: int
    
    """Unrecognized format, cannot be loaded by Aspose.Words."""
    UNKNOWN: int
    

class Margins(Enum):
    """Specifies preset margins."""
    
    """Normal margins."""
    NORMAL: int
    
    """Narrow margins."""
    NARROW: int
    
    """Moderate margins."""
    MODERATE: int
    
    """Wide margins."""
    WIDE: int
    
    """Mirrored margins.
    
    Setting margins to Mirrored will set the appropriate value for :attr:`PageSetup.multiple_pages` property.
    This will affect the whole document, not just the current section."""
    MIRRORED: int
    
    """Custom margins."""
    CUSTOM: int
    

class MeasurementUnits(Enum):
    """Specifies the unit of measurement."""
    
    """Inches."""
    INCHES: int
    
    """Centimeters."""
    CENTIMETERS: int
    
    """Millimeters."""
    MILLIMETERS: int
    
    """Points."""
    POINTS: int
    
    """Picas (commonly used in traditional typewriter font spacing)."""
    PICAS: int
    

class NodeChangingAction(Enum):
    """Specifies the type of node change."""
    
    """A node is being inserted in the tree."""
    INSERT: int
    
    """A node is being removed from the tree."""
    REMOVE: int
    

class NodeType(Enum):
    """Specifies the type of a Word document node."""
    
    """Indicates all node types. Allows to select all children."""
    ANY: int
    
    """A :class:`Document` object that, as the root of the document tree,
    provides access to the entire Word document.
    
    A :class:`Document` node can have :class:`Section` nodes."""
    DOCUMENT: int
    
    """A :class:`Section` object that corresponds to one section in a Word document.
    
    A :class:`Section` node can have :class:`Body` and :class:`HeaderFooter` nodes."""
    SECTION: int
    
    """A :class:`Body` object that contains the main text of a section (main text story).
    
    A :class:`Body` node can have :class:`Paragraph` and :class:`aspose.words.tables.Table` nodes."""
    BODY: int
    
    """A :class:`HeaderFooter` object that contains text of a particular header or footer inside a section.
    
    A :class:`HeaderFooter` node can have :class:`Paragraph` and :class:`aspose.words.tables.Table` nodes."""
    HEADER_FOOTER: int
    
    """A :class:`aspose.words.tables.Table` object that represents a table in a Word document.
    
    A :class:`aspose.words.tables.Table` node can have :class:`aspose.words.tables.Row` nodes."""
    TABLE: int
    
    """A row of a table.
    
    A :class:`aspose.words.tables.Row` node can have :class:`aspose.words.tables.Cell` nodes."""
    ROW: int
    
    """A cell of a table row.
    
    A :class:`aspose.words.tables.Cell` node can have :class:`Paragraph` and :class:`aspose.words.tables.Table` nodes."""
    CELL: int
    
    """A paragraph of text.
    
    A :class:`Paragraph` node is a container for inline level elements
    :class:`Run`,
    :class:`aspose.words.fields.FieldStart`,
    :class:`aspose.words.fields.FieldSeparator`,
    :class:`aspose.words.fields.FieldEnd`,
    :class:`aspose.words.fields.FormField`,
    :class:`aspose.words.drawing.Shape`,
    :class:`aspose.words.drawing.GroupShape`,
    :class:`aspose.words.notes.Footnote`,
    :class:`Comment`,
    :class:`SpecialChar`,
    as well as :class:`BookmarkStart` and :class:`BookmarkEnd`."""
    PARAGRAPH: int
    
    """A beginning of a bookmark marker."""
    BOOKMARK_START: int
    
    """An end of a bookmark marker."""
    BOOKMARK_END: int
    
    """A beginning of an editable range."""
    EDITABLE_RANGE_START: int
    
    """An end of an editable range."""
    EDITABLE_RANGE_END: int
    
    """A beginning of an MoveFrom range."""
    MOVE_FROM_RANGE_START: int
    
    """An end of an MoveFrom range."""
    MOVE_FROM_RANGE_END: int
    
    """A beginning of an MoveTo range."""
    MOVE_TO_RANGE_START: int
    
    """An end of an MoveTo range."""
    MOVE_TO_RANGE_END: int
    
    """A group of shapes, images, OLE objects or other group shapes.
    
    A :class:`aspose.words.drawing.GroupShape` node can contain other
    :class:`aspose.words.drawing.Shape` and :class:`aspose.words.drawing.GroupShape` nodes."""
    GROUP_SHAPE: int
    
    """A drawing object, such as an OfficeArt shape, image or an OLE object.
    
    A :class:`aspose.words.drawing.Shape` node can contain :class:`Paragraph`
    and :class:`aspose.words.tables.Table` nodes."""
    SHAPE: int
    
    """A comment in a Word document.
    
    A :class:`Comment` node can have :class:`Paragraph` and :class:`aspose.words.tables.Table` nodes."""
    COMMENT: int
    
    """A footnote or endnote in a Word document.
    
    A :class:`aspose.words.notes.Footnote` node can have :class:`Paragraph` and :class:`aspose.words.tables.Table` nodes."""
    FOOTNOTE: int
    
    """A run of text."""
    RUN: int
    
    """A special character that designates the start of a Word field."""
    FIELD_START: int
    
    """A special character that separates the field code from the field result."""
    FIELD_SEPARATOR: int
    
    """A special character that designates the end of a Word field."""
    FIELD_END: int
    
    """A form field."""
    FORM_FIELD: int
    
    """A special character that is not one of the more specific special character types."""
    SPECIAL_CHAR: int
    
    """A smart tag around one or more inline structures (runs, images, fields,etc.) within a paragraph"""
    SMART_TAG: int
    
    """Allows to define customer-specific information and its means of presentation."""
    STRUCTURED_DOCUMENT_TAG: int
    
    """A start of **ranged** structured document tag which accepts multi-sections content."""
    STRUCTURED_DOCUMENT_TAG_RANGE_START: int
    
    """A end of **ranged** structured document tag which accepts multi-sections content."""
    STRUCTURED_DOCUMENT_TAG_RANGE_END: int
    
    """A glossary document within the main document."""
    GLOSSARY_DOCUMENT: int
    
    """A building block within a glossary document (e.g. glossary document entry)."""
    BUILDING_BLOCK: int
    
    """A marker node that represents the start of a commented range."""
    COMMENT_RANGE_START: int
    
    """A marker node that represents the end of a commented range."""
    COMMENT_RANGE_END: int
    
    """An Office Math object. Can be equation, function, matrix or one of other mathematical objects.
    Can be a collection of mathematical object and also can contain some non-mathematical objects such as runs of text."""
    OFFICE_MATH: int
    
    """A subdocument node which is a link to another document."""
    SUB_DOCUMENT: int
    
    """Reserved for internal use by Aspose.Words."""
    SYSTEM: int
    
    """Reserved for internal use by Aspose.Words."""
    NULL: int
    

class NumberStyle(Enum):
    """Specifies the number style for a list, footnotes and endnotes, page numbers."""
    
    """Arabic numbering (1, 2, 3, ...)"""
    ARABIC: int
    
    """Upper case Roman (I, II, III, ...)"""
    UPPERCASE_ROMAN: int
    
    """Lower case Roman (i, ii, iii, ...)"""
    LOWERCASE_ROMAN: int
    
    """Upper case Letter (A, B, C, ...)"""
    UPPERCASE_LETTER: int
    
    """Lower case letter (a, b, c, ...)"""
    LOWERCASE_LETTER: int
    
    """Ordinal (1st, 2nd, 3rd, ...)"""
    ORDINAL: int
    
    """Numbered (One, Two, Three, ...)"""
    NUMBER: int
    
    """Ordinal (text) (First, Second, Third, ...)"""
    ORDINAL_TEXT: int
    
    """Hexadecimal: 8, 9, A, B, C, D, E, F, 10, 11, 12"""
    HEX: int
    
    """Chicago Manual of Style: \*, †, †"""
    CHICAGO_MANUAL: int
    
    """Ideograph-digital"""
    KANJI: int
    
    """Japanese counting"""
    KANJI_DIGIT: int
    
    """Aiueo"""
    AIUEO_HALF_WIDTH: int
    
    """Iroha"""
    IROHA_HALF_WIDTH: int
    
    """Full-width Arabic: 1, 2, 3, 4"""
    ARABIC_FULL_WIDTH: int
    
    """Half-width Arabic: 1, 2, 3, 4"""
    ARABIC_HALF_WIDTH: int
    
    """Japanese legal"""
    KANJI_TRADITIONAL: int
    
    """Japanese digital ten thousand"""
    KANJI_TRADITIONAL2: int
    
    """Enclosed circles"""
    NUMBER_IN_CIRCLE: int
    
    """Decimal full width: 1, 2, 3, 4"""
    DECIMAL_FULL_WIDTH: int
    
    """Aiueo full width"""
    AIUEO: int
    
    """Iroha full width"""
    IROHA: int
    
    """Leading Zero (01, 02,..., 09, 10, 11,..., 99, 100, 101,...)"""
    LEADING_ZERO: int
    
    """Bullet (check the character code in the text)"""
    BULLET: int
    
    """Korean Ganada"""
    GANADA: int
    
    """Korea Chosung"""
    CHOSUNG: int
    
    """Enclosed full stop"""
    GB1: int
    
    """Enclosed parenthesis"""
    GB2: int
    
    """Enclosed circle Chinese"""
    GB3: int
    
    """Ideograph enclosed circle"""
    GB4: int
    
    """Ideograph traditional"""
    ZODIAC1: int
    
    """Ideograph Zodiac"""
    ZODIAC2: int
    
    """Ideograph Zodiac traditional"""
    ZODIAC3: int
    
    """Taiwanese counting"""
    TRAD_CHIN_NUM1: int
    
    """Ideograph legal traditional"""
    TRAD_CHIN_NUM2: int
    
    """Taiwanese counting thousand"""
    TRAD_CHIN_NUM3: int
    
    """Taiwanese digital"""
    TRAD_CHIN_NUM4: int
    
    """Chinese counting"""
    SIMP_CHIN_NUM1: int
    
    """Chinese legal simplified"""
    SIMP_CHIN_NUM2: int
    
    """Chinese counting thousand"""
    SIMP_CHIN_NUM3: int
    
    """Chinese (not implemented)"""
    SIMP_CHIN_NUM4: int
    
    """Korean digital"""
    HANJA_READ: int
    
    """Korean counting"""
    HANJA_READ_DIGIT: int
    
    """Korea legal"""
    HANGUL: int
    
    """Korea digital2"""
    HANJA: int
    
    """Hebrew-1"""
    HEBREW1: int
    
    """Arabic alpha"""
    ARABIC1: int
    
    """Hebrew-2"""
    HEBREW2: int
    
    """Arabic abjad"""
    ARABIC2: int
    
    """Hindi vowels"""
    HINDI_LETTER1: int
    
    """Hindi consonants"""
    HINDI_LETTER2: int
    
    """Hindi numbers"""
    HINDI_ARABIC: int
    
    """Hindi descriptive (cardinals)"""
    HINDI_CARDINAL_TEXT: int
    
    """Thai letters"""
    THAI_LETTER: int
    
    """Thai numbers"""
    THAI_ARABIC: int
    
    """Thai descriptive (cardinals)"""
    THAI_CARDINAL_TEXT: int
    
    """Vietnamese descriptive (cardinals)"""
    VIET_CARDINAL_TEXT: int
    
    """Page number format: - 1 -, - 2 -, - 3 -, - 4 -"""
    NUMBER_IN_DASH: int
    
    """Lowercase Russian alphabet"""
    LOWERCASE_RUSSIAN: int
    
    """Uppercase Russian alphabet"""
    UPPERCASE_RUSSIAN: int
    
    """No bullet or number."""
    NONE: int
    
    """Custom number format. It is supported by DOCX format only."""
    CUSTOM: int
    

class Orientation(Enum):
    """Specifies page orientation."""
    
    """Portrait page orientation (narrow and tall)."""
    PORTRAIT: int
    
    """Landscape page orientation (wide and short)."""
    LANDSCAPE: int
    

class OutlineLevel(Enum):
    """Specifies the outline level of a paragraph in the document."""
    
    """The paragraph is at the outline level 1 (topmost level)."""
    LEVEL1: int
    
    """The paragraph is at the outline level 2."""
    LEVEL2: int
    
    """The paragraph is at the outline level 3."""
    LEVEL3: int
    
    """The paragraph is at the outline level 4."""
    LEVEL4: int
    
    """The paragraph is at the outline level 5."""
    LEVEL5: int
    
    """The paragraph is at the outline level 6."""
    LEVEL6: int
    
    """The paragraph is at the outline level 7."""
    LEVEL7: int
    
    """The paragraph is at the outline level 8."""
    LEVEL8: int
    
    """The paragraph is at the outline level 9."""
    LEVEL9: int
    
    """The paragraph is at the level of the main text."""
    BODY_TEXT: int
    

class PageBorderAppliesTo(Enum):
    """Specifies which pages the page border is printed on."""
    
    """Page border is shown on all pages of the section."""
    ALL_PAGES: int
    
    """Page border is shown on the first page of the section only."""
    FIRST_PAGE: int
    
    """Page border is shown on all pages except the first page of the section."""
    OTHER_PAGES: int
    

class PageBorderDistanceFrom(Enum):
    """Specifies the positioning of the page border relative to the page margin."""
    
    """Border position is measured from the page margin."""
    TEXT: int
    
    """Border position is measured from the page edge."""
    PAGE_EDGE: int
    

class PageVerticalAlignment(Enum):
    """Specifies vertical justification of text on each page."""
    
    """Text is aligned at the bottom of the page."""
    BOTTOM: int
    
    """Text is aligned in the middle of the page."""
    CENTER: int
    
    """Text is spread to fill the page."""
    JUSTIFY: int
    
    """Text is aligned at the top of the page."""
    TOP: int
    

class PaperSize(Enum):
    """Specifies paper size."""
    
    """297 x 420 mm."""
    A3: int
    
    """210 x 297 mm."""
    A4: int
    
    """148 x 210 mm."""
    A5: int
    
    """250 x 353 mm."""
    B4: int
    
    """176 x 250 mm."""
    B5: int
    
    """7.25 x 10.5 inches."""
    EXECUTIVE: int
    
    """8.5 x 13 inches."""
    FOLIO: int
    
    """17 x 11 inches."""
    LEDGER: int
    
    """8.5 x 14 inches."""
    LEGAL: int
    
    """8.5 x 11 inches."""
    LETTER: int
    
    """110 x 220 mm."""
    ENVELOPE_DL: int
    
    """8.47 x 10.83 inches."""
    QUARTO: int
    
    """8.5 x 5.5 inches."""
    STATEMENT: int
    
    """11 x 17 inches."""
    TABLOID: int
    
    """10 x 14 inches."""
    PAPER_10X14: int
    
    """11 x 17 inches."""
    PAPER_11X17: int
    
    """4.125 x 9.5 inches."""
    NUMBER_10_ENVELOPE: int
    
    """Custom paper size."""
    CUSTOM: int
    

class ParagraphAlignment(Enum):
    """Specifies text alignment in a paragraph."""
    
    """Text is aligned to the left."""
    LEFT: int
    
    """Text is centered horizontally."""
    CENTER: int
    
    """Text is aligned to the right."""
    RIGHT: int
    
    """Text is aligned to both left and right."""
    JUSTIFY: int
    
    """Text is evenly distributed."""
    DISTRIBUTED: int
    
    """Arabic only. Kashida length for text is extended to a medium length determined by the consumer."""
    ARABIC_MEDIUM_KASHIDA: int
    
    """Arabic only. Kashida length for text is extended to its widest possible length."""
    ARABIC_HIGH_KASHIDA: int
    
    """Arabic only. Kashida length for text is extended to a slightly longer length."""
    ARABIC_LOW_KASHIDA: int
    
    """Thai only. Text is justified with an optimization for Thai."""
    THAI_DISTRIBUTED: int
    
    """The only Math element in a line, aligned as 'Centered As Group'."""
    MATH_ELEMENT_CENTER_AS_GROUP: int
    

class ProtectionType(Enum):
    """Protection type for a document."""
    
    """User can only modify comments in the document."""
    ALLOW_ONLY_COMMENTS: int
    
    """User can only enter data in the form fields in the document."""
    ALLOW_ONLY_FORM_FIELDS: int
    
    """User can only add revision marks to the document."""
    ALLOW_ONLY_REVISIONS: int
    
    """No changes are allowed to the document. Available since Microsoft Word 2003."""
    READ_ONLY: int
    
    """The document is not protected."""
    NO_PROTECTION: int
    

class RevisionType(Enum):
    """Specifies the type of change being tracked in :class:`Revision`."""
    
    """New content was inserted in the document."""
    INSERTION: int
    
    """Content was removed from the document."""
    DELETION: int
    
    """Change of formatting was applied to the parent node."""
    FORMAT_CHANGE: int
    
    """Change of formatting was applied to the parent style."""
    STYLE_DEFINITION_CHANGE: int
    
    """Content was moved in the document."""
    MOVING: int
    

class RevisionsView(Enum):
    """Allows to specify whether to work with the original or revised version of a document."""
    
    """Specifies original version of a document."""
    ORIGINAL: int
    
    """Specifies revised version of a document."""
    FINAL: int
    

class SaveFormat(Enum):
    """Indicates the format in which the document is saved."""
    
    """Default, invalid value for file format."""
    UNKNOWN: int
    
    """Saves the document in the Microsoft Word 97 - 2007 Document format."""
    DOC: int
    
    """Saves the document in the Microsoft Word 97 - 2007 Template format."""
    DOT: int
    
    """Saves the document as an Office Open XML WordprocessingML Document (macro-free)."""
    DOCX: int
    
    """Saves the document as an Office Open XML WordprocessingML Macro-Enabled Document."""
    DOCM: int
    
    """Saves the document as an Office Open XML WordprocessingML Template (macro-free)."""
    DOTX: int
    
    """Saves the document as an Office Open XML WordprocessingML Macro-Enabled Template."""
    DOTM: int
    
    """Saves the document as an Office Open XML WordprocessingML stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC: int
    
    """Saves the document as an Office Open XML WordprocessingML Macro-Enabled Document stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC_MACRO_ENABLED: int
    
    """Saves the document as an Office Open XML WordprocessingML Template (macro-free) stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC_TEMPLATE: int
    
    """Saves the document as an Office Open XML WordprocessingML Macro-Enabled Template stored in a flat XML file instead of a ZIP package."""
    FLAT_OPC_TEMPLATE_MACRO_ENABLED: int
    
    """Saves the document in the RTF format.
    All characters above 7-bits are escaped as hexadecimal or Unicode characters."""
    RTF: int
    
    """Saves the document in the Microsoft Word 2003 WordprocessingML format."""
    WORD_ML: int
    
    """Saves the document as PDF (Adobe Portable Document) format."""
    PDF: int
    
    """Saves the document in the XPS (XML Paper Specification) format."""
    XPS: int
    
    """Saves the document in the Extensible Application Markup Language (XAML) format as a fixed document."""
    XAML_FIXED: int
    
    """Saves the document in the Svg (Scalable Vector Graphics) format."""
    SVG: int
    
    """Saves the document in the HTML format using absolutely positioned elements"""
    HTML_FIXED: int
    
    """Saves the document in the OpenXPS (Ecma-388) format."""
    OPEN_XPS: int
    
    """Saves the document in the PS (PostScript) format."""
    PS: int
    
    """Saves the document in the PCL (Printer Control Language) format."""
    PCL: int
    
    """Saves the document in the HTML format."""
    HTML: int
    
    """Saves the document in the MHTML (Web archive) format."""
    MHTML: int
    
    """Saves the document in the EPUB format."""
    EPUB: int
    
    """Saves the document in the AZW3 format."""
    AZW3: int
    
    """Saves the document in the MOBI format."""
    MOBI: int
    
    """Saves the document as an ODF Text Document."""
    ODT: int
    
    """Saves the document as an ODF Text Document Template."""
    OTT: int
    
    """Saves the document in the plain text format."""
    TEXT: int
    
    """**Beta.** Saves the document in the Extensible Application Markup Language (XAML) format as a flow document."""
    XAML_FLOW: int
    
    """**Beta.** Saves the document in the Extensible Application Markup Language (XAML) package format as a flow document."""
    XAML_FLOW_PACK: int
    
    """Saves the document in the Markdown format."""
    MARKDOWN: int
    
    """Saves the document as an Office Open XML SpreadsheetML Document (macro-free)."""
    XLSX: int
    
    """Renders a page or pages of the document and saves them into a single or multipage TIFF file."""
    TIFF: int
    
    """Renders a page of the document and saves it as a PNG file."""
    PNG: int
    
    """Renders a page of the document and saves it as a BMP file."""
    BMP: int
    
    """Renders a page of the document and saves it as a vector EMF (Enhanced Meta File) file."""
    EMF: int
    
    """Renders a page of the document and saves it as a JPEG file."""
    JPEG: int
    
    """Renders a page of the document and saves it as a GIF file."""
    GIF: int
    
    """Renders a page of the document and saves it as an EPS file."""
    EPS: int
    
    """Renders a page of the document and saves it as a WebP file."""
    WEB_P: int
    

class SectionLayoutMode(Enum):
    """Specifies the layout mode for a section allowing to define the document grid behavior."""
    
    """Specifies that no document grid shall be applied to the contents of the corresponding section in the document."""
    DEFAULT: int
    
    """Specifies that the corresponding section shall have both the additional line pitch and character pitch
    added to each line and character within it in order to maintain a specific number
    of lines per page and characters per line.
    Characters will not be automatically aligned with gridlines on typing."""
    GRID: int
    
    """Specifies that the corresponding section shall have additional line pitch added to each line within it
    in order to maintain the specified number of lines per page."""
    LINE_GRID: int
    
    """Specifies that the corresponding section shall have both the additional line pitch and character pitch
    added to each line and character within it in order to maintain a specific number
    of lines per page and characters per line.
    Characters will be automatically aligned with gridlines on typing."""
    SNAP_TO_CHARS: int
    

class SectionStart(Enum):
    """The type of break at the beginning of the section."""
    
    """The new section starts on the same page as the previous section."""
    CONTINUOUS: int
    
    """The section starts from a new column."""
    NEW_COLUMN: int
    
    """The section starts from a new page."""
    NEW_PAGE: int
    
    """The section starts on a new even page."""
    EVEN_PAGE: int
    
    """The section starts on a new odd page."""
    ODD_PAGE: int
    

class StoryType(Enum):
    """Text of a Word document is stored in stories. :class:`StoryType` identifies a story."""
    
    """Default value. There is no such story in the document."""
    NONE: int
    
    """Contains the main text of the document, represented by :class:`Body`."""
    MAIN_TEXT: int
    
    """Contains footnote text, represented by :class:`aspose.words.notes.Footnote`."""
    FOOTNOTES: int
    
    """Contains endnotes text, represented by :class:`aspose.words.notes.Footnote`."""
    ENDNOTES: int
    
    """Contains document comments (annotations), represented by :class:`Comment`."""
    COMMENTS: int
    
    """Contains shape or textbox text, represented by :class:`aspose.words.drawing.Shape`."""
    TEXTBOX: int
    
    """Contains text of the even pages header, represented by :class:`HeaderFooter`."""
    EVEN_PAGES_HEADER: int
    
    """Contains text of the primary header. When header is different for odd and even pages,
    contains text of the odd pages header. Represented by :class:`HeaderFooter`."""
    PRIMARY_HEADER: int
    
    """Contains text of the even pages footer, represented by :class:`HeaderFooter`."""
    EVEN_PAGES_FOOTER: int
    
    """Contains text of the primary footer. When footer is different for odd and even pages,
    contains text of the odd pages footer. Represented by :class:`HeaderFooter`."""
    PRIMARY_FOOTER: int
    
    """Contains text of the first page header, represented by :class:`HeaderFooter`."""
    FIRST_PAGE_HEADER: int
    
    """Contains text of the first page footer, represented by :class:`HeaderFooter`."""
    FIRST_PAGE_FOOTER: int
    
    """Contains the text of the footnote separator."""
    FOOTNOTE_SEPARATOR: int
    
    """Contains the text of the footnote continuation separator."""
    FOOTNOTE_CONTINUATION_SEPARATOR: int
    
    """Contains the text of the footnote continuation notice separator."""
    FOOTNOTE_CONTINUATION_NOTICE: int
    
    """Contains the text of the endnote separator."""
    ENDNOTE_SEPARATOR: int
    
    """Contains the text of the endnote continuation separator."""
    ENDNOTE_CONTINUATION_SEPARATOR: int
    
    """Contains the text of the endnote continuation notice separator."""
    ENDNOTE_CONTINUATION_NOTICE: int
    

class StyleIdentifier(Enum):
    """Locale independent style identifier.
    
    The names of built-in styles in MS Word are localized for different languages.
    Using a style identifier you can find the correct style regardless of the document language.
    
    All user defined styles are assigned the :attr:`StyleIdentifier.USER` value."""
    
    BOOK_TITLE: int
    
    """The Annotation (Comment) Reference style."""
    COMMENT_REFERENCE: int
    
    """The Default Paragraph Font style."""
    DEFAULT_PARAGRAPH_FONT: int
    
    EMPHASIS: int
    
    """The Endnote Reference style."""
    ENDNOTE_REFERENCE: int
    
    FOLLOWED_HYPERLINK: int
    
    """The Footnote Reference style."""
    FOOTNOTE_REFERENCE: int
    
    HTML_ACRONYM: int
    
    HTML_CITE: int
    
    HTML_CODE: int
    
    HTML_DEFINITION: int
    
    HTML_KEYBOARD: int
    
    HTML_SAMPLE: int
    
    HTML_TYPEWRITER: int
    
    HTML_VARIABLE: int
    
    """The Hyperlink style."""
    HYPERLINK: int
    
    INTENSE_EMPHASIS: int
    
    INTENSE_REFERENCE: int
    
    """The Line Number style."""
    LINE_NUMBER: int
    
    """The Page Number style."""
    PAGE_NUMBER: int
    
    PLACEHOLDER_TEXT: int
    
    """The Smart Link style."""
    SMART_LINK: int
    
    STRONG: int
    
    SUBTLE_EMPHASIS: int
    
    SUBTLE_REFERENCE: int
    
    BALLOON_TEXT: int
    
    """The Body Text style."""
    BODY_TEXT: int
    
    BODY_TEXT2: int
    
    BODY_TEXT3: int
    
    BODY_TEXT1_I: int
    
    BODY_TEXT1_I2: int
    
    BODY_TEXT_IND: int
    
    BODY_TEXT_IND2: int
    
    BODY_TEXT_IND3: int
    
    CLOSING: int
    
    COMMENT_SUBJECT: int
    
    """The Annotation (Comment) Text style."""
    COMMENT_TEXT: int
    
    DATE: int
    
    DOCUMENT_MAP: int
    
    EMAIL_SIGNATURE: int
    
    """The Endnote Text style."""
    ENDNOTE_TEXT: int
    
    """The Footer style."""
    FOOTER: int
    
    """The Footnote Text style."""
    FOOTNOTE_TEXT: int
    
    """The Header style."""
    HEADER: int
    
    """The Heading 1 style."""
    HEADING1: int
    
    """The Heading 2 style."""
    HEADING2: int
    
    """The Heading 3 style."""
    HEADING3: int
    
    """The Heading 4 style."""
    HEADING4: int
    
    """The Heading 5 style."""
    HEADING5: int
    
    """The Heading 6 style."""
    HEADING6: int
    
    """The Heading 7 style."""
    HEADING7: int
    
    """The Heading 8 style."""
    HEADING8: int
    
    """The Heading 9 style."""
    HEADING9: int
    
    HTML_ADDRESS: int
    
    HTML_TOP_OF_FORM: int
    
    HTML_BOTTOM_OF_FORM: int
    
    HTML_PREFORMATTED: int
    
    INTENSE_QUOTE: int
    
    MACRO: int
    
    MESSAGE_HEADER: int
    
    NOTE_HEADING: int
    
    PLAIN_TEXT: int
    
    QUOTE: int
    
    SALUTATION: int
    
    SIGNATURE: int
    
    SUBTITLE: int
    
    """The Title style."""
    TITLE: int
    
    BIBLIOGRAPHY: int
    
    BLOCK_TEXT: int
    
    CAPTION: int
    
    """The Envelope Address style."""
    ENVELOPE_ADDRESS: int
    
    """The Envelope Return style."""
    ENVELOPE_RETURN: int
    
    INDEX1: int
    
    INDEX2: int
    
    INDEX3: int
    
    INDEX4: int
    
    INDEX5: int
    
    INDEX6: int
    
    INDEX7: int
    
    INDEX8: int
    
    INDEX9: int
    
    """The Index Heading style."""
    INDEX_HEADING: int
    
    """The List style."""
    LIST: int
    
    LIST2: int
    
    LIST3: int
    
    LIST4: int
    
    LIST5: int
    
    """The List Bullet style."""
    LIST_BULLET: int
    
    LIST_BULLET2: int
    
    LIST_BULLET3: int
    
    LIST_BULLET4: int
    
    LIST_BULLET5: int
    
    LIST_CONTINUE: int
    
    LIST_CONTINUE2: int
    
    LIST_CONTINUE3: int
    
    LIST_CONTINUE4: int
    
    LIST_CONTINUE5: int
    
    """The List Number style."""
    LIST_NUMBER: int
    
    LIST_NUMBER2: int
    
    LIST_NUMBER3: int
    
    LIST_NUMBER4: int
    
    LIST_NUMBER5: int
    
    LIST_PARAGRAPH: int
    
    NO_SPACING: int
    
    """The Normal style."""
    NORMAL: int
    
    NORMAL_WEB: int
    
    """The Normal Indent style."""
    NORMAL_INDENT: int
    
    TABLE_OF_AUTHORITIES: int
    
    """The Table of Figures style."""
    TABLE_OF_FIGURES: int
    
    TOA_HEADING: int
    
    TOC1: int
    
    TOC2: int
    
    TOC3: int
    
    TOC4: int
    
    TOC5: int
    
    TOC6: int
    
    TOC7: int
    
    TOC8: int
    
    TOC9: int
    
    TOC_HEADING: int
    
    REVISION: int
    
    """The 1 / a / i style."""
    OUTLINE_LIST1: int
    
    """The 1 / 1.1 / 1.1.1 style."""
    OUTLINE_LIST2: int
    
    """The Article / Section style."""
    OUTLINE_LIST3: int
    
    NO_LIST: int
    
    COLORFUL_GRID: int
    
    COLORFUL_GRID_ACCENT1: int
    
    COLORFUL_GRID_ACCENT2: int
    
    COLORFUL_GRID_ACCENT3: int
    
    COLORFUL_GRID_ACCENT4: int
    
    COLORFUL_GRID_ACCENT5: int
    
    COLORFUL_GRID_ACCENT6: int
    
    COLORFUL_LIST: int
    
    COLORFUL_LIST_ACCENT1: int
    
    COLORFUL_LIST_ACCENT2: int
    
    COLORFUL_LIST_ACCENT3: int
    
    COLORFUL_LIST_ACCENT4: int
    
    COLORFUL_LIST_ACCENT5: int
    
    COLORFUL_LIST_ACCENT6: int
    
    COLORFUL_SHADING: int
    
    COLORFUL_SHADING_ACCENT1: int
    
    COLORFUL_SHADING_ACCENT2: int
    
    COLORFUL_SHADING_ACCENT3: int
    
    COLORFUL_SHADING_ACCENT4: int
    
    COLORFUL_SHADING_ACCENT5: int
    
    COLORFUL_SHADING_ACCENT6: int
    
    DARK_LIST: int
    
    DARK_LIST_ACCENT1: int
    
    DARK_LIST_ACCENT2: int
    
    DARK_LIST_ACCENT3: int
    
    DARK_LIST_ACCENT4: int
    
    DARK_LIST_ACCENT5: int
    
    DARK_LIST_ACCENT6: int
    
    LIGHT_GRID: int
    
    LIGHT_GRID_ACCENT1: int
    
    LIGHT_GRID_ACCENT2: int
    
    LIGHT_GRID_ACCENT3: int
    
    LIGHT_GRID_ACCENT4: int
    
    LIGHT_GRID_ACCENT5: int
    
    LIGHT_GRID_ACCENT6: int
    
    LIGHT_LIST: int
    
    LIGHT_LIST_ACCENT1: int
    
    LIGHT_LIST_ACCENT2: int
    
    LIGHT_LIST_ACCENT3: int
    
    LIGHT_LIST_ACCENT4: int
    
    LIGHT_LIST_ACCENT5: int
    
    LIGHT_LIST_ACCENT6: int
    
    LIGHT_SHADING: int
    
    LIGHT_SHADING_ACCENT1: int
    
    LIGHT_SHADING_ACCENT2: int
    
    LIGHT_SHADING_ACCENT3: int
    
    LIGHT_SHADING_ACCENT4: int
    
    LIGHT_SHADING_ACCENT5: int
    
    LIGHT_SHADING_ACCENT6: int
    
    MEDIUM_GRID1: int
    
    MEDIUM_GRID1_ACCENT1: int
    
    MEDIUM_GRID1_ACCENT2: int
    
    MEDIUM_GRID1_ACCENT3: int
    
    MEDIUM_GRID1_ACCENT4: int
    
    MEDIUM_GRID1_ACCENT5: int
    
    MEDIUM_GRID1_ACCENT6: int
    
    MEDIUM_GRID2: int
    
    MEDIUM_GRID2_ACCENT1: int
    
    MEDIUM_GRID2_ACCENT2: int
    
    MEDIUM_GRID2_ACCENT3: int
    
    MEDIUM_GRID2_ACCENT4: int
    
    MEDIUM_GRID2_ACCENT5: int
    
    MEDIUM_GRID2_ACCENT6: int
    
    MEDIUM_GRID3: int
    
    MEDIUM_GRID3_ACCENT1: int
    
    MEDIUM_GRID3_ACCENT2: int
    
    MEDIUM_GRID3_ACCENT3: int
    
    MEDIUM_GRID3_ACCENT4: int
    
    MEDIUM_GRID3_ACCENT5: int
    
    MEDIUM_GRID3_ACCENT6: int
    
    MEDIUM_LIST1: int
    
    MEDIUM_LIST1_ACCENT1: int
    
    MEDIUM_LIST1_ACCENT2: int
    
    MEDIUM_LIST1_ACCENT3: int
    
    MEDIUM_LIST1_ACCENT4: int
    
    MEDIUM_LIST1_ACCENT5: int
    
    MEDIUM_LIST1_ACCENT6: int
    
    MEDIUM_LIST2: int
    
    MEDIUM_LIST2_ACCENT1: int
    
    MEDIUM_LIST2_ACCENT2: int
    
    MEDIUM_LIST2_ACCENT3: int
    
    MEDIUM_LIST2_ACCENT4: int
    
    MEDIUM_LIST2_ACCENT5: int
    
    MEDIUM_LIST2_ACCENT6: int
    
    MEDIUM_SHADING1: int
    
    MEDIUM_SHADING1_ACCENT1: int
    
    MEDIUM_SHADING1_ACCENT2: int
    
    MEDIUM_SHADING1_ACCENT3: int
    
    MEDIUM_SHADING1_ACCENT4: int
    
    MEDIUM_SHADING1_ACCENT5: int
    
    MEDIUM_SHADING1_ACCENT6: int
    
    MEDIUM_SHADING2: int
    
    MEDIUM_SHADING2_ACCENT1: int
    
    MEDIUM_SHADING2_ACCENT2: int
    
    MEDIUM_SHADING2_ACCENT3: int
    
    MEDIUM_SHADING2_ACCENT4: int
    
    MEDIUM_SHADING2_ACCENT5: int
    
    MEDIUM_SHADING2_ACCENT6: int
    
    TABLE_3D_EFFECTS1: int
    
    TABLE_3D_EFFECTS2: int
    
    TABLE_3D_EFFECTS3: int
    
    TABLE_CLASSIC1: int
    
    TABLE_CLASSIC2: int
    
    TABLE_CLASSIC3: int
    
    TABLE_CLASSIC4: int
    
    TABLE_COLORFUL1: int
    
    TABLE_COLORFUL2: int
    
    TABLE_COLORFUL3: int
    
    TABLE_COLUMNS1: int
    
    TABLE_COLUMNS2: int
    
    TABLE_COLUMNS3: int
    
    TABLE_COLUMNS4: int
    
    TABLE_COLUMNS5: int
    
    TABLE_CONTEMPORARY: int
    
    TABLE_ELEGANT: int
    
    TABLE_GRID: int
    
    TABLE_GRID1: int
    
    TABLE_GRID2: int
    
    TABLE_GRID3: int
    
    TABLE_GRID4: int
    
    TABLE_GRID5: int
    
    TABLE_GRID6: int
    
    TABLE_GRID7: int
    
    TABLE_GRID8: int
    
    TABLE_LIST1: int
    
    TABLE_LIST2: int
    
    TABLE_LIST3: int
    
    TABLE_LIST4: int
    
    TABLE_LIST5: int
    
    TABLE_LIST6: int
    
    TABLE_LIST7: int
    
    TABLE_LIST8: int
    
    TABLE_NORMAL: int
    
    TABLE_PROFESSIONAL: int
    
    TABLE_SIMPLE1: int
    
    TABLE_SIMPLE2: int
    
    TABLE_SIMPLE3: int
    
    TABLE_SUBTLE1: int
    
    TABLE_SUBTLE2: int
    
    TABLE_THEME: int
    
    TABLE_WEB1: int
    
    TABLE_WEB2: int
    
    TABLE_WEB3: int
    
    """Plain Table 1"""
    PLAIN_TABLE1: int
    
    """Plain Table 2"""
    PLAIN_TABLE2: int
    
    """Plain Table 3"""
    PLAIN_TABLE3: int
    
    """Plain Table 4"""
    PLAIN_TABLE4: int
    
    """Plain Table 5"""
    PLAIN_TABLE5: int
    
    """Table Grid Light"""
    TABLE_GRID_LIGHT: int
    
    """Grid Table 1 Light"""
    GRID_TABLE1_LIGHT: int
    
    """Grid Table 2"""
    GRID_TABLE2: int
    
    """Grid Table 3"""
    GRID_TABLE3: int
    
    """Grid Table 4"""
    GRID_TABLE4: int
    
    """Grid Table 5 Dark"""
    GRID_TABLE5_DARK: int
    
    """Grid Table 6 Colorful"""
    GRID_TABLE6_COLORFUL: int
    
    """Grid Table 7 Colorful"""
    GRID_TABLE7_COLORFUL: int
    
    """Grid Table 1 Light - Accent 1"""
    GRID_TABLE1_LIGHT_ACCENT1: int
    
    """Grid Table 2 - Accent 1"""
    GRID_TABLE2_ACCENT1: int
    
    """Grid Table 3 - Accent 1"""
    GRID_TABLE3_ACCENT1: int
    
    """Grid Table 4 - Accent 1"""
    GRID_TABLE4_ACCENT1: int
    
    """Grid Table 5 Dark - Accent 1"""
    GRID_TABLE5_DARK_ACCENT1: int
    
    """Grid Table 6 Colorful - Accent 1"""
    GRID_TABLE6_COLORFUL_ACCENT1: int
    
    """Grid Table 7 Colorful - Accent 1"""
    GRID_TABLE7_COLORFUL_ACCENT1: int
    
    """Grid Table 1 Light - Accent 2"""
    GRID_TABLE1_LIGHT_ACCENT2: int
    
    """Grid Table 2 - Accent 2"""
    GRID_TABLE2_ACCENT2: int
    
    """Grid Table 3 - Accent 2"""
    GRID_TABLE3_ACCENT2: int
    
    """Grid Table 4 - Accent 2"""
    GRID_TABLE4_ACCENT2: int
    
    """Grid Table 5 Dark - Accent 2"""
    GRID_TABLE5_DARK_ACCENT2: int
    
    """Grid Table 6 Colorful - Accent 2"""
    GRID_TABLE6_COLORFUL_ACCENT2: int
    
    """Grid Table 7 Colorful - Accent 2"""
    GRID_TABLE7_COLORFUL_ACCENT2: int
    
    """Grid Table 1 Light - Accent 3"""
    GRID_TABLE1_LIGHT_ACCENT3: int
    
    """Grid Table 2 - Accent 3"""
    GRID_TABLE2_ACCENT3: int
    
    """Grid Table 3 - Accent 3"""
    GRID_TABLE3_ACCENT3: int
    
    """Grid Table 4 - Accent 3"""
    GRID_TABLE4_ACCENT3: int
    
    """Grid Table 5 Dark - Accent 3"""
    GRID_TABLE5_DARK_ACCENT3: int
    
    """Grid Table 6 Colorful - Accent 3"""
    GRID_TABLE6_COLORFUL_ACCENT3: int
    
    """Grid Table 7 Colorful - Accent 3"""
    GRID_TABLE7_COLORFUL_ACCENT3: int
    
    """Grid Table 1 Light - Accent 4"""
    GRID_TABLE1_LIGHT_ACCENT4: int
    
    """Grid Table 2 - Accent 4"""
    GRID_TABLE2_ACCENT4: int
    
    """Grid Table 3 - Accent 4"""
    GRID_TABLE3_ACCENT4: int
    
    """Grid Table 4 - Accent 4"""
    GRID_TABLE4_ACCENT4: int
    
    """Grid Table 5 Dark - Accent 4"""
    GRID_TABLE5_DARK_ACCENT4: int
    
    """Grid Table 6 Colorful - Accent 4"""
    GRID_TABLE6_COLORFUL_ACCENT4: int
    
    """Grid Table 7 Colorful - Accent 4"""
    GRID_TABLE7_COLORFUL_ACCENT4: int
    
    """Grid Table 1 Light - Accent 5"""
    GRID_TABLE1_LIGHT_ACCENT5: int
    
    """Grid Table 2 - Accent 5"""
    GRID_TABLE2_ACCENT5: int
    
    """Grid Table 3 - Accent 5"""
    GRID_TABLE3_ACCENT5: int
    
    """Grid Table 4 - Accent 5"""
    GRID_TABLE4_ACCENT5: int
    
    """Grid Table 5 Dark - Accent 5"""
    GRID_TABLE5_DARK_ACCENT5: int
    
    """Grid Table 6 Colorful - Accent 5"""
    GRID_TABLE6_COLORFUL_ACCENT5: int
    
    """Grid Table 7 Colorful - Accent 5"""
    GRID_TABLE7_COLORFUL_ACCENT5: int
    
    """Grid Table 1 Light - Accent 6"""
    GRID_TABLE1_LIGHT_ACCENT6: int
    
    """Grid Table 2 - Accent 6"""
    GRID_TABLE2_ACCENT6: int
    
    """Grid Table 3 - Accent 6"""
    GRID_TABLE3_ACCENT6: int
    
    """Grid Table 4 - Accent 6"""
    GRID_TABLE4_ACCENT6: int
    
    """Grid Table 5 Dark - Accent 6"""
    GRID_TABLE5_DARK_ACCENT6: int
    
    """Grid Table 6 Colorful - Accent 6"""
    GRID_TABLE6_COLORFUL_ACCENT6: int
    
    """Grid Table 7 Colorful - Accent 6"""
    GRID_TABLE7_COLORFUL_ACCENT6: int
    
    """List Table 1 Light"""
    LIST_TABLE1_LIGHT: int
    
    """List Table 2"""
    LIST_TABLE2: int
    
    """List Table 3"""
    LIST_TABLE3: int
    
    """List Table 4"""
    LIST_TABLE4: int
    
    """List Table 5 Dark"""
    LIST_TABLE5_DARK: int
    
    """List Table 6 Colorful"""
    LIST_TABLE6_COLORFUL: int
    
    """List Table 7 Colorful"""
    LIST_TABLE7_COLORFUL: int
    
    """List Table 1 Light - Accent 1"""
    LIST_TABLE1_LIGHT_ACCENT1: int
    
    """List Table 2 - Accent 1"""
    LIST_TABLE2_ACCENT1: int
    
    """List Table 3 - Accent 1"""
    LIST_TABLE3_ACCENT1: int
    
    """List Table 4 - Accent 1"""
    LIST_TABLE4_ACCENT1: int
    
    """List Table 5 Dark - Accent 1"""
    LIST_TABLE5_DARK_ACCENT1: int
    
    """List Table 6 Colorful - Accent 1"""
    LIST_TABLE6_COLORFUL_ACCENT1: int
    
    """List Table 7 Colorful - Accent 1"""
    LIST_TABLE7_COLORFUL_ACCENT1: int
    
    """List Table 1 Light - Accent 2"""
    LIST_TABLE1_LIGHT_ACCENT2: int
    
    """List Table 2 - Accent 2"""
    LIST_TABLE2_ACCENT2: int
    
    """List Table 3 - Accent 2"""
    LIST_TABLE3_ACCENT2: int
    
    """List Table 4 - Accent 2"""
    LIST_TABLE4_ACCENT2: int
    
    """List Table 5 Dark - Accent 2"""
    LIST_TABLE5_DARK_ACCENT2: int
    
    """List Table 6 Colorful - Accent 2"""
    LIST_TABLE6_COLORFUL_ACCENT2: int
    
    """List Table 7 Colorful - Accent 2"""
    LIST_TABLE7_COLORFUL_ACCENT2: int
    
    """List Table 1 Light - Accent 3"""
    LIST_TABLE1_LIGHT_ACCENT3: int
    
    """List Table 2 - Accent 3"""
    LIST_TABLE2_ACCENT3: int
    
    """List Table 3 - Accent 3"""
    LIST_TABLE3_ACCENT3: int
    
    """List Table 4 - Accent 3"""
    LIST_TABLE4_ACCENT3: int
    
    """List Table 5 Dark - Accent 3"""
    LIST_TABLE5_DARK_ACCENT3: int
    
    """List Table 6 Colorful - Accent 3"""
    LIST_TABLE6_COLORFUL_ACCENT3: int
    
    """List Table 7 Colorful - Accent 3"""
    LIST_TABLE7_COLORFUL_ACCENT3: int
    
    """List Table 1 Light - Accent 4"""
    LIST_TABLE1_LIGHT_ACCENT4: int
    
    """List Table 2 - Accent 4"""
    LIST_TABLE2_ACCENT4: int
    
    """List Table 3 - Accent 4"""
    LIST_TABLE3_ACCENT4: int
    
    """List Table 4 - Accent 4"""
    LIST_TABLE4_ACCENT4: int
    
    """List Table 5 Dark - Accent 4"""
    LIST_TABLE5_DARK_ACCENT4: int
    
    """List Table 6 Colorful - Accent 4"""
    LIST_TABLE6_COLORFUL_ACCENT4: int
    
    """List Table 7 Colorful - Accent 4"""
    LIST_TABLE7_COLORFUL_ACCENT4: int
    
    """List Table 1 Light - Accent 5"""
    LIST_TABLE1_LIGHT_ACCENT5: int
    
    """List Table 2 - Accent 5"""
    LIST_TABLE2_ACCENT5: int
    
    """List Table 3 - Accent 5"""
    LIST_TABLE3_ACCENT5: int
    
    """List Table 4 - Accent 5"""
    LIST_TABLE4_ACCENT5: int
    
    """List Table 5 Dark - Accent 5"""
    LIST_TABLE5_DARK_ACCENT5: int
    
    """List Table 6 Colorful - Accent 5"""
    LIST_TABLE6_COLORFUL_ACCENT5: int
    
    """List Table 7 Colorful - Accent 5"""
    LIST_TABLE7_COLORFUL_ACCENT5: int
    
    """List Table 1 Light - Accent 6"""
    LIST_TABLE1_LIGHT_ACCENT6: int
    
    """List Table 2 - Accent 6"""
    LIST_TABLE2_ACCENT6: int
    
    """List Table 3 - Accent 6"""
    LIST_TABLE3_ACCENT6: int
    
    """List Table 4 - Accent 6"""
    LIST_TABLE4_ACCENT6: int
    
    """List Table 5 Dark - Accent 6"""
    LIST_TABLE5_DARK_ACCENT6: int
    
    """List Table 6 Colorful - Accent 6"""
    LIST_TABLE6_COLORFUL_ACCENT6: int
    
    """List Table 7 Colorful - Accent 6"""
    LIST_TABLE7_COLORFUL_ACCENT6: int
    
    """The Mention style."""
    MENTION: int
    
    """The SmartHyperlink style."""
    SMART_HYPERLINK: int
    
    """The Hashtag style."""
    HASHTAG: int
    
    """The UnresolvedMention style."""
    UNRESOLVED_MENTION: int
    
    """A user defined style."""
    USER: int
    
    """Reserved for internal use."""
    NIL: int
    

class StyleType(Enum):
    """Represents type of the style."""
    
    """The style is a paragraph style."""
    PARAGRAPH: int
    
    """The style is a character style."""
    CHARACTER: int
    
    """The style is a table style."""
    TABLE: int
    
    """The style is a list style."""
    LIST: int
    

class TabAlignment(Enum):
    """Specifies the alignment/type of a tab stop."""
    
    """Left-aligns the text after the tab stop."""
    LEFT: int
    
    """Centers the text around the tab stop."""
    CENTER: int
    
    """Right-aligns the text at the tab stop."""
    RIGHT: int
    
    """Aligns the text at the decimal dot."""
    DECIMAL: int
    
    """Draws a vertical bar at the tab stop position."""
    BAR: int
    
    """The tab is a delimiter between the number/bullet and text in a list item."""
    LIST: int
    
    """Clears any tab stop in this position."""
    CLEAR: int
    

class TabLeader(Enum):
    """Specifies the type of the leader line displayed under the tab character."""
    
    """No leader line is displayed."""
    NONE: int
    
    """The leader line is made up from dots."""
    DOTS: int
    
    """The leader line is made up from dashes."""
    DASHES: int
    
    """The leader line is a single line."""
    LINE: int
    
    """The leader line is a single thick line."""
    HEAVY: int
    
    """The leader line is made up from middle-dots."""
    MIDDLE_DOT: int
    

class TextDmlEffect(Enum):
    """Dml text effect for text runs."""
    
    """Glow effect, in which a color blurred outline is added outside the edges of the object."""
    GLOW: int
    
    """Fill overlay effect."""
    FILL: int
    
    """Shadow effect."""
    SHADOW: int
    
    """Outline effect."""
    OUTLINE: int
    
    """3D effect."""
    EFFECT_3D: int
    
    """Reflection effect."""
    REFLECTION: int
    

class TextEffect(Enum):
    """Animation effect for text runs."""
    
    NONE: int
    
    LAS_VEGAS_LIGHTS: int
    
    BLINKING_BACKGROUND: int
    
    SPARKLE_TEXT: int
    
    MARCHING_BLACK_ANTS: int
    
    MARCHING_RED_ANTS: int
    
    SHIMMER: int
    

class TextOrientation(Enum):
    """Specifies orientation of text on a page, in a table cell or a text frame."""
    
    """Text is arranged horizontally (lr-tb)."""
    HORIZONTAL: int
    
    """Text is rotated 90 degrees to the right to appear from top to bottom (tb-rl)."""
    DOWNWARD: int
    
    """Text is rotated 90 degrees to the left to appear from bottom to top (bt-lr)."""
    UPWARD: int
    
    """Text is arranged horizontally, but Far East characters are rotated 90 degrees to the left (lr-tb-v)."""
    HORIZONTAL_ROTATED_FAR_EAST: int
    
    """Far East characters appear vertical, other text is rotated 90 degrees
    to the right to appear from top to bottom (tb-rl-v)."""
    VERTICAL_FAR_EAST: int
    
    """Far East characters appear vertical, other text is rotated 90 degrees
    to the right to appear from top to bottom vertically, then left to right horizontally  (tb-lr-v)."""
    VERTICAL_ROTATED_FAR_EAST: int
    

class TextureIndex(Enum):
    """Specifies shading texture."""
    
    TEXTURE_10_PERCENT: int
    
    TEXTURE_12PT5_PERCENT: int
    
    TEXTURE_15_PERCENT: int
    
    TEXTURE_17PT5_PERCENT: int
    
    TEXTURE_20_PERCENT: int
    
    TEXTURE_22PT5_PERCENT: int
    
    TEXTURE_25_PERCENT: int
    
    TEXTURE_27PT5_PERCENT: int
    
    TEXTURE_2PT5_PERCENT: int
    
    TEXTURE_30_PERCENT: int
    
    TEXTURE_32PT5_PERCENT: int
    
    TEXTURE_35_PERCENT: int
    
    TEXTURE_37PT5_PERCENT: int
    
    TEXTURE_40_PERCENT: int
    
    TEXTURE_42PT5_PERCENT: int
    
    TEXTURE_45_PERCENT: int
    
    TEXTURE_47PT5_PERCENT: int
    
    TEXTURE_50_PERCENT: int
    
    TEXTURE_52PT5_PERCENT: int
    
    TEXTURE_55_PERCENT: int
    
    TEXTURE_57PT5_PERCENT: int
    
    TEXTURE_5_PERCENT: int
    
    TEXTURE_60_PERCENT: int
    
    TEXTURE_62PT5_PERCENT: int
    
    TEXTURE_65_PERCENT: int
    
    TEXTURE_67PT5_PERCENT: int
    
    TEXTURE_70_PERCENT: int
    
    TEXTURE_72PT5_PERCENT: int
    
    TEXTURE_75_PERCENT: int
    
    TEXTURE_77PT5_PERCENT: int
    
    TEXTURE_7PT5_PERCENT: int
    
    TEXTURE_80_PERCENT: int
    
    TEXTURE_82PT5_PERCENT: int
    
    TEXTURE_85_PERCENT: int
    
    TEXTURE_87PT5_PERCENT: int
    
    TEXTURE_90_PERCENT: int
    
    TEXTURE_92PT5_PERCENT: int
    
    TEXTURE_95_PERCENT: int
    
    TEXTURE_97PT5_PERCENT: int
    
    TEXTURE_CROSS: int
    
    TEXTURE_DARK_CROSS: int
    
    TEXTURE_DARK_DIAGONAL_CROSS: int
    
    TEXTURE_DARK_DIAGONAL_DOWN: int
    
    TEXTURE_DARK_DIAGONAL_UP: int
    
    TEXTURE_DARK_HORIZONTAL: int
    
    TEXTURE_DARK_VERTICAL: int
    
    TEXTURE_DIAGONAL_CROSS: int
    
    TEXTURE_DIAGONAL_DOWN: int
    
    TEXTURE_DIAGONAL_UP: int
    
    TEXTURE_HORIZONTAL: int
    
    TEXTURE_NONE: int
    
    TEXTURE_SOLID: int
    
    TEXTURE_VERTICAL: int
    
    """Specifies that there shall be no pattern used on the current shaded region
    (i.e. the pattern shall be a complete fill with the background color)."""
    TEXTURE_NIL: int
    

class Underline(Enum):
    """Indicates type of the underline applied to a font."""
    
    NONE: int
    
    SINGLE: int
    
    WORDS: int
    
    DOUBLE: int
    
    DOTTED: int
    
    THICK: int
    
    DASH: int
    
    DASH_LONG: int
    
    DOT_DASH: int
    
    DOT_DOT_DASH: int
    
    WAVY: int
    
    DOTTED_HEAVY: int
    
    DASH_HEAVY: int
    
    DASH_LONG_HEAVY: int
    
    DOT_DASH_HEAVY: int
    
    DOT_DOT_DASH_HEAVY: int
    
    WAVY_HEAVY: int
    
    WAVY_DOUBLE: int
    

class VisitorAction(Enum):
    """Allows the visitor to control the enumeration of nodes."""
    
    """The visitor requests the enumeration to continue."""
    CONTINUE: int
    
    """The visitor requests to skip the current node and continue enumeration."""
    SKIP_THIS_NODE: int
    
    """The visitor requests the enumeration of nodes to stop."""
    STOP: int
    

class WarningSource(Enum):
    """Specifies the module that produces a warning during document loading or saving."""
    
    """The warning source is not specified."""
    UNKNOWN: int
    
    """Module that builds a document layout."""
    LAYOUT: int
    
    """Module that renders DrawingML shapes."""
    DRAWING_ML: int
    
    """Module that renders OfficeMath."""
    OFFICE_MATH: int
    
    """Module that renders ordinary shapes."""
    SHAPES: int
    
    """Module that renders metafiles."""
    METAFILE: int
    
    """Module that renders XPS."""
    XPS: int
    
    """Module that renders PDF."""
    PDF: int
    
    """Module that renders images."""
    IMAGE: int
    
    """Module that reads/writes DOCX files."""
    DOCX: int
    
    """Module that reads/writes binary DOC files."""
    DOC: int
    
    """Module that reads/writes plaintext files."""
    TEXT: int
    
    """Module that reads/writes RTF files."""
    RTF: int
    
    """Module that reads/writes WML files."""
    WORD_ML: int
    
    """Common modules that are shared between DOCX/WML reader/writer modules."""
    NRX: int
    
    """Module that reads/writes ODT files."""
    ODT: int
    
    """Module that reads/writes HTML/MHTML files."""
    HTML: int
    
    """Module that verifies model consistency and validity."""
    VALIDATOR: int
    
    """Module that reads/writes Xaml files."""
    XAML: int
    
    """Module that reads Svm files."""
    SVM: int
    
    """Module that reads W3C MathML files."""
    MATH_ML: int
    
    """Module that reads font files."""
    FONT: int
    
    """Module that reads SVG files."""
    SVG: int
    
    """Module that reads/writes Markdown files."""
    MARKDOWN: int
    
    """Module that reads CHM files."""
    CHM: int
    
    """Module that reads/writes EPUB files."""
    EPUB: int
    
    """Module that reads XML files."""
    XML: int
    
    """Module that writes XLSX files."""
    XLSX: int
    

class WarningType(Enum):
    """Specifies the type of a warning that is issued by Aspose.Words during document loading or saving."""
    
    """Some text/char/image or other data will be missing from either the document tree following load,
    or from the created document following save."""
    DATA_LOSS_CATEGORY: int
    
    """Generic data loss, no specific code."""
    DATA_LOSS: int
    
    """The resulting document or a particular location in it might look substantially different
    compared to the original document."""
    MAJOR_FORMATTING_LOSS_CATEGORY: int
    
    """Generic major formatting loss, no specific code."""
    MAJOR_FORMATTING_LOSS: int
    
    """The resulting document or a particular location in it might look somewhat different compared
    to the original document."""
    MINOR_FORMATTING_LOSS_CATEGORY: int
    
    """Generic minor formatting loss, no specific code."""
    MINOR_FORMATTING_LOSS: int
    
    """Font has been substituted."""
    FONT_SUBSTITUTION: int
    
    """Loss of embedded font information during document saving."""
    FONT_EMBEDDING: int
    
    """Some content in the source document could not be recognized (i.e. is unsupported), this may or may not
    cause issues or result in data/formatting loss."""
    UNEXPECTED_CONTENT_CATEGORY: int
    
    """Generic unexpected content, no specific code."""
    UNEXPECTED_CONTENT: int
    
    """Advises of a potential problem or suggests an improvement."""
    HINT: int
    

class WatermarkLayout(Enum):
    """Defines layout of the watermark relative to the watermark center."""
    
    """Horizontal watermark layout. Corresponds to 0 degrees of rotation."""
    HORIZONTAL: int
    
    """Diagonal watermark layout. Corresponds to 315 degrees of rotation."""
    DIAGONAL: int
    

class WatermarkType(Enum):
    """Specifies the watermark type."""
    
    """Indicates that the text will be used as a watermark.
    Such a watermark corresponds to a WordArt object."""
    TEXT: int
    
    """Indicates that the image will be used as a watermark.
    Such a watermark corresponds to a shape with image."""
    IMAGE: int
    
    """Indicates watermark is no set."""
    NONE: int
    

