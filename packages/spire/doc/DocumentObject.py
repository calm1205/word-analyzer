import ctypes
from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentObject(DocumentSerializable, IDocumentObject):
    """
    Represents a document object.
    """

    @property
    def ChildObjects(self) -> 'DocumentObjectCollection':
        """
        Gets the child objects of the entity.
        """
        GetDllLibDoc().DocumentObject_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property
    def DocumentObjectType(self) -> 'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().DocumentObject_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentObject_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def Owner(self) -> 'DocumentObject':
        """
        Gets the owner of this entity.
        """
        GetDllLibDoc().DocumentObject_get_Owner.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_Owner.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_get_Owner,self.Ptr)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret

    @property
    def PreviousSibling(self) -> 'IDocumentObject':
        """
        Gets the previous sibling.
        """
        GetDllLibDoc().DocumentObject_get_PreviousSibling.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_PreviousSibling.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_get_PreviousSibling,self.Ptr)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret


    @property
    def NextSibling(self) -> 'IDocumentObject':
        """
        Gets the next sibling.
        """
        GetDllLibDoc().DocumentObject_get_NextSibling.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_NextSibling.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_get_NextSibling,self.Ptr)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret


    @property
    def IsComposite(self) -> bool:
        """
        Indicating whether this instance is composite.
        """
        GetDllLibDoc().DocumentObject_get_IsComposite.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_IsComposite.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocumentObject_get_IsComposite,self.Ptr)
        return ret

    @property
    def FirstChild(self) -> 'DocumentObject':
        """
        Gets the first child.
        """
        GetDllLibDoc().DocumentObject_get_FirstChild.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_FirstChild.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_get_FirstChild,self.Ptr)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret


    @property

    def LastChild(self)->'DocumentObject':
        """
        Gets the last child.
        """
        GetDllLibDoc().DocumentObject_get_LastChild.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_get_LastChild.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_get_LastChild,self.Ptr)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret

    def Clone(self) -> 'DocumentObject':
        """
        Clones the document object.
        """
        GetDllLibDoc().DocumentObject_Clone.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_Clone.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_Clone,self.Ptr)
        ret = None if intPtr==None else self._createDocumentObject(intPtr)
        return ret

    def _createDocumentObject(self, intPtrWithTypeName:IntPtrWithTypeName)->'DocumentObject':
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

    def ToString(self ,seperator:str)->str:
        """
        Exports the name and index in container of the object into a string in the specified seperator.

        Args:
            seperator (str): The specified seperator.
        Returns:
            str: The result str.

        """
        seperatorPtr = StrToPtr(seperator)
        GetDllLibDoc().DocumentObject_ToString.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().DocumentObject_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocumentObject_ToString,self.Ptr, seperatorPtr))
        return ret



    def GetPreviousWidgetSibling(self)->'IDocumentObject':
        """

        """
        GetDllLibDoc().DocumentObject_GetPreviousWidgetSibling.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_GetPreviousWidgetSibling.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_GetPreviousWidgetSibling,self.Ptr)
        ret = None if intPtr==None else IDocumentObject(intPtr)
        return ret



    def GetNextWidgetSibling(self)->'IDocumentObject':
        """

        """
        GetDllLibDoc().DocumentObject_GetNextWidgetSibling.argtypes=[c_void_p]
        GetDllLibDoc().DocumentObject_GetNextWidgetSibling.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_GetNextWidgetSibling,self.Ptr)
        ret = None if intPtr==None else IDocumentObject(intPtr)
        return ret



    def PrependChild(self ,newChild:'DocumentObject')->'DocumentObject':
        """

        """
        intPtrnewChild:c_void_p = newChild.Ptr

        GetDllLibDoc().DocumentObject_PrependChild.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().DocumentObject_PrependChild.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentObject_PrependChild,self.Ptr, intPtrnewChild)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


