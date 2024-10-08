from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class BookmarksNavigator(SpireObject):
    """
    Represents a bookmarks navigator.
    """

    @dispatch
    def __init__(self, doc: IDocument):
        """
        Initializes a new instance of the BookmarksNavigator class.

        Args:
            doc (IDocument): The document to navigate.
        """
        intPdoc: c_void_p = doc.Ptr;

        GetDllLibDoc().BookmarksNavigator_CreateBookmarksNavigatorD.argtypes = [c_void_p]
        GetDllLibDoc().BookmarksNavigator_CreateBookmarksNavigatorD.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_CreateBookmarksNavigatorD,intPdoc)
        super(BookmarksNavigator, self).__init__(intPtr)

    @property
    def Document(self) -> 'IDocument':
        """
        Gets or sets the document associated with the bookmarks navigator.

        Returns:
            IDocument: The document associated with the bookmarks navigator.
        """
        GetDllLibDoc().BookmarksNavigator_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().BookmarksNavigator_get_Document.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_get_Document,self.Ptr)
        ret = None if intPtr==None else IDocument(intPtr)
        return ret

    @Document.setter
    def Document(self, value:'IDocument'):
        GetDllLibDoc().BookmarksNavigator_set_Document.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_set_Document,self.Ptr, value.Ptr)

    @property
    def CurrentBookmark(self) -> 'Bookmark':
        """
        Gets the current bookmark in the bookmarks navigator.

        Returns:
            Bookmark: The current bookmark in the bookmarks navigator.
        """
        GetDllLibDoc().BookmarksNavigator_get_CurrentBookmark.argtypes=[c_void_p]
        GetDllLibDoc().BookmarksNavigator_get_CurrentBookmark.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_get_CurrentBookmark,self.Ptr)
        ret = None if intPtr==None else Bookmark(intPtr)
        return ret

    @dispatch
    def MoveToBookmark(self, bookmarkName: str):
        """
        Moves the bookmarks navigator to the specified bookmark.

        Args:
            bookmarkName (str): The name of the bookmark to move to.
        """
        bookmarkNamePtr = StrToPtr(bookmarkName)
        GetDllLibDoc().BookmarksNavigator_MoveToBookmark.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_MoveToBookmark,self.Ptr, bookmarkNamePtr)

    @dispatch
    def MoveToBookmark(self, bookmarkName: str, isStart: bool, isAfter: bool):
        """
        Moves the bookmarks navigator to the specified bookmark with additional options.

        Args:
            bookmarkName (str): The name of the bookmark to move to.
            isStart (bool): True to move to the start of the bookmark, False to move to the end.
            isAfter (bool): True to move to the position after the bookmark, False to move to the position before.
        """
        bookmarkNamePtr = StrToPtr(bookmarkName)
        GetDllLibDoc().BookmarksNavigator_MoveToBookmarkBII.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_MoveToBookmarkBII,self.Ptr, bookmarkNamePtr,isStart,isAfter)

    @dispatch

    def InsertText(self ,text:str)->'ITextRange':
        """
        Inserts the specified text at the current position of the bookmarks navigator.

        Args:
            text (str): The text to insert.

        Returns:
            ITextRange: The inserted text range.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().BookmarksNavigator_InsertText.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().BookmarksNavigator_InsertText.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_InsertText,self.Ptr, textPtr)
        ret = None if intPtr==None else ITextRange(intPtr)
        return ret

    @dispatch
    def InsertText(self, text: str, saveFormatting: bool) -> 'ITextRange':
        """
        Inserts the specified text at the current position of the bookmarks navigator with additional options.

        Args:
            text (str): The text to insert.
            saveFormatting (bool): True to save the formatting of the inserted text, False otherwise.

        Returns:
            ITextRange: The inserted text range.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().BookmarksNavigator_InsertTextTS.argtypes=[c_void_p ,c_char_p,c_bool]
        GetDllLibDoc().BookmarksNavigator_InsertTextTS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_InsertTextTS,self.Ptr, textPtr,saveFormatting)
        ret = None if intPtr==None else ITextRange(intPtr)
        return ret

    def InsertTable(self, table: 'ITable'):
        """
        Inserts the specified table at the current position of the bookmarks navigator.

        Args:
            table (ITable): The table to insert.
        """
        intPtrtable:c_void_p = table.Ptr

        GetDllLibDoc().BookmarksNavigator_InsertTable.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_InsertTable,self.Ptr, intPtrtable)


    def InsertParagraphItem(self ,itemType:'ParagraphItemType')->'IParagraphBase':
        """
        Inserts a paragraph item of the specified type at the current position of the bookmarks navigator.

        Args:
            itemType (ParagraphItemType): The type of the paragraph item to insert.

        Returns:
            IParagraphBase: The inserted paragraph item.
        """
        enumitemType:c_int = itemType.value

        GetDllLibDoc().BookmarksNavigator_InsertParagraphItem.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().BookmarksNavigator_InsertParagraphItem.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_InsertParagraphItem,self.Ptr, enumitemType)
        ret = None if intPtr==None else IParagraphBase(intPtr)
        return ret

    def InsertParagraph(self, paragraph: 'IParagraph'):
        """
        Inserts the specified paragraph at the current position of the bookmarks navigator.

        Args:
            paragraph (IParagraph): The paragraph to insert.
        """
        intPtrparagraph:c_void_p = paragraph.Ptr

        GetDllLibDoc().BookmarksNavigator_InsertParagraph.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_InsertParagraph,self.Ptr, intPtrparagraph)

    def InsertTextBodyPart(self, bodyPart: 'TextBodyPart'):
        """
        Inserts the specified text body part at the current position of the bookmarks navigator.

        Args:
            bodyPart (TextBodyPart): The text body part to insert.
        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_InsertTextBodyPart.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_InsertTextBodyPart,self.Ptr, intPtrbodyPart)


    def GetBookmarkContent(self)->'TextBodyPart':
        """
        Gets the content of the current bookmark in the bookmarks navigator.

        Returns:
            TextBodyPart: The content of the current bookmark.
        """
        GetDllLibDoc().BookmarksNavigator_GetBookmarkContent.argtypes=[c_void_p]
        GetDllLibDoc().BookmarksNavigator_GetBookmarkContent.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().BookmarksNavigator_GetBookmarkContent,self.Ptr)
        ret = None if intPtr==None else TextBodyPart(intPtr)
        return ret



    def DeleteBookmarkContent(self ,saveFormatting:bool):
        """
        Deletes the content of the current bookmark in the bookmarks navigator.

        Args:
            saveFormatting (bool): True to save the formatting of the deleted content, False otherwise.
        """
        
        GetDllLibDoc().BookmarksNavigator_DeleteBookmarkContent.argtypes=[c_void_p ,c_bool]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_DeleteBookmarkContent,self.Ptr, saveFormatting)

    @dispatch

    def ReplaceBookmarkContent(self ,bodyPart:TextBodyPart):
        """
        Replaces the content of the current bookmark with the specified text body part.

        Args:
            bodyPart (TextBodyPart): The text body part to replace with.
        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContent.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContent,self.Ptr, intPtrbodyPart)

    @dispatch

    def ReplaceBookmarkContent(self ,bodyPart:TextBodyPart,isKeepSourceFirstParaFormat:bool):
        """
        Replaces the content of the current bookmark with the specified text body part and keeps the formatting of the first paragraph.

        Args:
            bodyPart (TextBodyPart): The text body part to replace with.
            isKeepSourceFirstParaFormat (bool): True to keep the formatting of the first paragraph, False otherwise.
        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBI.argtypes=[c_void_p ,c_void_p,c_bool]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBI,self.Ptr, intPtrbodyPart,isKeepSourceFirstParaFormat)

    @dispatch

    def ReplaceBookmarkContent(self ,bodyPart:TextBodyPart,isKeepSourceFirstParaFormat:bool,saveFormatting:bool):
        """
        Replaces the content of the current bookmark with the specified text body part and keeps the formatting of the first paragraph with additional options.

        Args:
            bodyPart (TextBodyPart): The text body part to replace with.
            isKeepSourceFirstParaFormat (bool): True to keep the formatting of the first paragraph, False otherwise.
            saveFormatting (bool): True to save the formatting of the replaced content, False otherwise.
        """
        intPtrbodyPart:c_void_p = bodyPart.Ptr

        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBIS.argtypes=[c_void_p ,c_void_p,c_bool,c_bool]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentBIS,self.Ptr, intPtrbodyPart,isKeepSourceFirstParaFormat,saveFormatting)

    @dispatch

    def ReplaceBookmarkContent(self ,text:str,saveFormatting:bool):
        """
        Replaces the content of the current bookmark with the specified text.

        Args:
            text (str): The text to replace with.
            saveFormatting (bool): True to save the formatting of the replaced content, False otherwise.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentTS.argtypes=[c_void_p ,c_char_p,c_bool]
        CallCFunction(GetDllLibDoc().BookmarksNavigator_ReplaceBookmarkContentTS,self.Ptr, textPtr,saveFormatting)

