from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentObjectCollection (  DocumentSerializableCollection, IDocumentObjectCollection) :
    """
    Represents a collection of DLS entities.
    """

    def get_Item(self ,index:int)->'DocumentObject':
        """
        Gets the DocumentObject at the specified index.

        Args:
            index(int): The index of the DocumentObject.

        Returns:
            The DocumentObject at the specified index.
        """
        
        GetDllLibDoc().DocumentObjectCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().DocumentObjectCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObjectCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret


    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->'DocumentObject':
        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Documents.Paragraph"):
            from spire.doc import Paragraph
            ret = Paragraph(intPtr)
        elif(strName == "Spire.Doc.PictureWatermark"):
            from spire.doc import PictureWatermark
            ret = PictureWatermark(intPtr)
        elif (strName == "Spire.Doc.TextWatermark"):
            from spire.doc import TextWatermark
            ret = TextWatermark(intPtr)
        elif (strName == "Spire.Doc.Fields.TextRange"):
            from spire.doc import TextRange
            ret = TextRange(intPtr)
        #elif (strName == "Spire.Doc.BodyRegion"):
        #  ret = BodyRegion(intPtr)
        elif (strName == "Spire.Doc.Body"):
            from spire.doc import Body
            ret = Body(intPtr)
        elif (strName == "Spire.Doc.HeaderFooter"):
            from spire.doc import HeaderFooter
            ret = HeaderFooter(intPtr)
        elif (strName == "Spire.Doc.Section"):
            from spire.doc import Section
            ret = Section(intPtr)
        elif (strName == "Spire.Doc.Table"):
            from spire.doc import Table
            ret = Table(intPtr)
        elif (strName == "Spire.Doc.TableCell"):
            from spire.doc import TableCell
            ret = TableCell(intPtr)
        elif (strName == "Spire.Doc.TableRow"):
            from spire.doc import TableRow
            ret = TableRow(intPtr)
        elif (strName == "Spire.Doc.BookmarkEnd"):
            from spire.doc import BookmarkEnd
            ret = BookmarkEnd(intPtr)
        elif (strName == "Spire.Doc.BookmarkStart"):
            from spire.doc import BookmarkStart
            ret = BookmarkStart(intPtr)
        elif (strName == "Spire.Doc.Break"):
            from spire.doc import Break
            ret = Break(intPtr)
        elif (strName == "Spire.Doc.PermissionStart"):
            from spire.doc import PermissionStart
            ret = PermissionStart(intPtr)
        elif (strName == "Spire.Doc.PermissionEnd"):
            from spire.doc import PermissionEnd
            ret = PermissionEnd(intPtr)
        elif (strName == "Spire.Doc.Fields.OMath.OfficeMath"):
            from spire.doc import OfficeMath
            ret = OfficeMath(intPtr)
        elif (strName == "Spire.Doc.Fields.ShapeGroup"):
            from spire.doc import ShapeGroup
            ret = ShapeGroup(intPtr)
        elif (strName == "Spire.Doc.Fields.DocOleObject"):
            from spire.doc import DocOleObject
            ret = DocOleObject(intPtr)
        elif (strName == "Spire.Doc.Fields.ShapeObject"):
            from spire.doc import ShapeObject
            ret = ShapeObject(intPtr)
        elif (strName == "Spire.Doc.Fields.TableOfContent"):
            from spire.doc import TableOfContent
            ret = TableOfContent(intPtr)
        elif (strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.Comment"):
            from spire.doc import Comment
            ret = Comment(intPtr)
        elif (strName == "Spire.Doc.Documents.CommentMark"):
            from spire.doc import CommentMark
            ret = CommentMark(intPtr)
        elif (strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.ControlField"):
            from spire.doc import ControlField
            ret = ControlField(intPtr)
        elif (strName == "Spire.Doc.Fields.Field"):
            from spire.doc import Field
            ret = Field(intPtr)
        elif (strName == "Spire.Doc.Fields.FieldMark"):
            from spire.doc import FieldMark
            ret = FieldMark(intPtr)
        elif (strName == "Spire.Doc.Fields.Footnote"):
            from spire.doc import Footnote
            ret = Footnote(intPtr)
        elif (strName == "Spire.Doc.Fields.IfField"):
            from spire.doc import IfField
            ret = IfField(intPtr)
        elif (strName == "Spire.Doc.Fields.MergeField"):
            from spire.doc import MergeField
            ret = MergeField(intPtr)
        elif (strName == "Spire.Doc.Fields.DocPicture"):
            from spire.doc import DocPicture
            ret = DocPicture(intPtr)
        elif (strName == "Spire.Doc.Fields.SequenceField"):
            from spire.doc import SequenceField
            ret = SequenceField(intPtr)
        elif (strName == "Spire.Doc.Fields.Symbol"):
            from spire.doc import Symbol
            ret = Symbol(intPtr)
        elif (strName == "Spire.Doc.Fields.TextBox"):
            from spire.doc import TextBox
            ret = TextBox(intPtr)
        elif (strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        elif (strName == "Spire.Doc.Documents.SDTContent"):
            from spire.doc import SDTContent
            ret = SDTContent(intPtr)
        elif (strName == "Spire.Doc.Documents.SDTInlineContent"):
            from spire.doc import SDTInlineContent
            ret = SDTInlineContent(intPtr)
        elif (strName == "Spire.Doc.Documents.StructureDocumentTag"):
            from spire.doc import StructureDocumentTag
            ret = StructureDocumentTag(intPtr)
        elif (strName == "Spire.Doc.Documents.StructureDocumentTagRow"):
            from spire.doc import StructureDocumentTagRow
            ret = StructureDocumentTagRow(intPtr)
        elif (strName == "Spire.Doc.Documents.StructureDocumentTagCell"):
            from spire.doc import StructureDocumentTagCell
            ret = StructureDocumentTagCell(intPtr)
        elif (strName == "Spire.Doc.Documents.StructureDocumentTagInline"):
            from spire.doc import StructureDocumentTagInline
            ret = StructureDocumentTagInline(intPtr)
        else:
            ret = DocumentObject(intPtr)

        return ret

    @property

    def FirstItem(self)->'DocumentObject':
        """
        Gets the first item.

        Returns:
            The first item.
        """
        GetDllLibDoc().DocumentObjectCollection_get_FirstItem.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObjectCollection_get_FirstItem.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentObjectCollection_get_FirstItem,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    @property

    def LastItem(self)->'DocumentObject':
        """
        Gets the last item.

        Returns:
            The last item.
        """
        GetDllLibDoc().DocumentObjectCollection_get_LastItem.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObjectCollection_get_LastItem.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentObjectCollection_get_LastItem,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret



    def Add(self ,entity:'IDocumentObject')->int:
        """
        Adds the specified entity.

        Args:
            entity(IDocumentObject): the document object.

        Returns:
            The index.
        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentObjectCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocumentObjectCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentObjectCollection_Add,self.Ptr, intPtrentity)
        return ret

    def Clear(self):
        """
        Removes all items
        """
        GetDllLibDoc().DocumentObjectCollection_Clear.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().DocumentObjectCollection_Clear,self.Ptr)


    def Contains(self ,entity:'IDocumentObject')->bool:
        """
        Determines whether a entity is in the collection.

        Args:
            entity(IDocumentObject): The document object.

        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentObjectCollection_Contains.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocumentObjectCollection_Contains.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocumentObjectCollection_Contains,self.Ptr, intPtrentity)
        return ret


    def IndexOf(self ,entity:'IDocumentObject')->int:
        """
        Returns the zero-based index of the specified entity.

        Args:
            entity(IDocumentObject): The document object.

        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentObjectCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocumentObjectCollection_IndexOf.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentObjectCollection_IndexOf,self.Ptr, intPtrentity)
        return ret


    def Insert(self ,index:int,entity:'IDocumentObject'):
        """
        Inserts a entity into the collection at the specified index.

        Args:
            index(int): The index.
            entity(IDocumentObject): The document object.

        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentObjectCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().DocumentObjectCollection_Insert,self.Ptr, index,intPtrentity)


    def Remove(self ,entity:'IDocumentObject'):
        """
        Removes the document object from the collection.

        Args:
            entity(IDocumentObject): The document object.

        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().DocumentObjectCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().DocumentObjectCollection_Remove,self.Ptr, intPtrentity)


    def RemoveAt(self ,index:int):
        """
        Removes the document object at the specified index from the collection.

        Args:
            index(int): The index.

        """
        
        GetDllLibDoc().DocumentObjectCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().DocumentObjectCollection_RemoveAt,self.Ptr, index)

