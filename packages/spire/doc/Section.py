from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Section (  DocumentContainer, ISection, ICompositeObject) :
    """
    Represents a section in a document.
    """
    @property

    def Body(self)->'Body':
        """
        Gets the section body.
        """
        GetDllLibDoc().Section_get_Body.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Body.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_Body,self.Ptr)
        ret = None if intPtr==None else Body(intPtr)
        return ret


    @property

    def EndnoteOptions(self)->'FootEndnoteOptions':
        """
        Gets or sets options that control numbering and positioning of endnotes in current section.
        """
        GetDllLibDoc().Section_get_EndnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_EndnoteOptions.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_EndnoteOptions,self.Ptr)
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def FootnoteOptions(self)->'FootEndnoteOptions':
        """
        Gets or sets options that control numbering and positioning of footnote in current section.
        """
        GetDllLibDoc().Section_get_FootnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_FootnoteOptions.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_FootnoteOptions,self.Ptr)
        from spire.doc import FootEndnoteOptions
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def HeadersFooters(self)->'HeadersFooters':
        """
        Gets headers/footers of current section.
        """
        GetDllLibDoc().Section_get_HeadersFooters.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_HeadersFooters.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_HeadersFooters,self.Ptr)
        from spire.doc import HeadersFooters
        ret = None if intPtr==None else HeadersFooters(intPtr)
        return ret


    @property

    def PageSetup(self)->'PageSetup':
        """
        Gets page Setup of current section.
        """
        GetDllLibDoc().Section_get_PageSetup.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_PageSetup.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_PageSetup,self.Ptr)
        from spire.doc import PageSetup
        ret = None if intPtr==None else PageSetup(intPtr)
        return ret


    @property

    def Columns(self)->'ColumnCollection':
        """
        Get collection of columns which logically divide page on many printing/publishing areas.
        """
        GetDllLibDoc().Section_get_Columns.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Columns.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_Columns,self.Ptr)
        ret = None if intPtr==None else ColumnCollection(intPtr)
        return ret


    @property

    def BreakCode(self)->'SectionBreakType':
        """
        Returns or sets break code.
        """
        GetDllLibDoc().Section_get_BreakCode.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_BreakCode.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Section_get_BreakCode,self.Ptr)
        objwraped = SectionBreakType(ret)
        return objwraped

    @BreakCode.setter
    def BreakCode(self, value:'SectionBreakType'):
        GetDllLibDoc().Section_set_BreakCode.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Section_set_BreakCode,self.Ptr, value.value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().Section_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Section_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects.
        """
        GetDllLibDoc().Section_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def Paragraphs(self)->ParagraphCollection:
        """
        Gets the paragraphs.
        """
        GetDllLibDoc().Section_get_Paragraphs.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Paragraphs.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_Paragraphs,self.Ptr)
        ret = None if intPtr==None else ParagraphCollection(intPtr)
        return ret


    @property

    def Tables(self)->'TableCollection':
        """
        Gets the tables.
        """
        GetDllLibDoc().Section_get_Tables.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_Tables.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_get_Tables,self.Ptr)
        ret = None if intPtr==None else TableCollection(intPtr)
        return ret


    @property

    def TextDirection(self)->'TextDirection':
        """
        Gets or Sets the text direction.
        """
        GetDllLibDoc().Section_get_TextDirection.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_TextDirection.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Section_get_TextDirection,self.Ptr)
        objwraped = TextDirection(ret)
        return objwraped

    @TextDirection.setter
    def TextDirection(self, value:'TextDirection'):
        GetDllLibDoc().Section_set_TextDirection.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Section_set_TextDirection,self.Ptr, value.value)

    @property
    def ProtectForm(self)->bool:
        """
        Gets or sets a value indicating whether [protect form].
        """
        GetDllLibDoc().Section_get_ProtectForm.argtypes=[c_void_p]
        GetDllLibDoc().Section_get_ProtectForm.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Section_get_ProtectForm,self.Ptr)
        return ret

    @ProtectForm.setter
    def ProtectForm(self, value:bool):
        GetDllLibDoc().Section_set_ProtectForm.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Section_set_ProtectForm,self.Ptr, value)


    def AddColumn(self ,width:float,spacing:float)->'Column':
        """
        Adds new column to the section.
        """
        
        GetDllLibDoc().Section_AddColumn.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().Section_AddColumn.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_AddColumn,self.Ptr, width,spacing)
        ret = None if intPtr==None else Column(intPtr)
        return ret


    def MakeColumnsSameWidth(self):
        """
        Makes all columns in current section to be of equal width.
        """
        GetDllLibDoc().Section_MakeColumnsSameWidth.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Section_MakeColumnsSameWidth,self.Ptr)


    def Clone(self)->'Section':
        """
        Clones the section.
        """
        GetDllLibDoc().Section_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Section_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_Clone,self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret



    def CloneSectionPropertiesTo(self ,destSection:'Section'):
        """
        Clones the properties of the current section to the destination section.
        """
        intPtrdestSection:c_void_p = destSection.Ptr

        GetDllLibDoc().Section_CloneSectionPropertiesTo.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Section_CloneSectionPropertiesTo,self.Ptr, intPtrdestSection)


    def AddParagraph(self)->'Paragraph':
        """
        Adds a new paragraph to the section.
        """
        GetDllLibDoc().Section_AddParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Section_AddParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_AddParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @dispatch

    def AddTable(self)->Table:
        """
        Adds a new table to the section.
        """
        GetDllLibDoc().Section_AddTable.argtypes=[c_void_p]
        GetDllLibDoc().Section_AddTable.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_AddTable,self.Ptr)
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def AddTable(self ,showBorder:bool)->Table:
        """
        Adds the table.

        Args:
            showBorder (bool): Display table borders.True to display;False does not display.

        Returns:
            Table: The result table.
        """
        
        GetDllLibDoc().Section_AddTableS.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Section_AddTableS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Section_AddTableS,self.Ptr, showBorder)
        ret = None if intPtr==None else Table(intPtr)
        return ret


