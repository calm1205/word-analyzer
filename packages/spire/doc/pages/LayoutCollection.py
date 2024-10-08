from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class LayoutCollection ( SpireObject) :
    """
    <summary>
        Represents a generic collection of layout entity types.
    </summary>
    """
    @property

    def First(self)->'LayoutElement':
        """
    <summary>
        Returns the first entity in the collection.
    </summary>
        """
        GetDllLibDoc().LayoutCollection_get_First.argtypes=[c_void_p]
        GetDllLibDoc().LayoutCollection_get_First.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().LayoutCollection_get_First,self.Ptr)
        ret = None if intPtr==None else self._create(intPtr)
        return ret



    @property

    def Last(self)->'LayoutElement':
        """
    <summary>
        Returns the last entity in the collection.
    </summary>
        """
        GetDllLibDoc().LayoutCollection_get_Last.argtypes=[c_void_p]
        GetDllLibDoc().LayoutCollection_get_Last.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().LayoutCollection_get_Last,self.Ptr)
        ret = None if intPtr==None else self._create(intPtr)
        return ret




    def get_Item(self ,index:int)->'LayoutElement':
        """
    <summary>
        Retrieves the entity at the given index. 
    </summary>
        """
        
        GetDllLibDoc().LayoutCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().LayoutCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().LayoutCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret

    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->'LayoutElement':
        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Pages.FixedLayoutCell"):
            from spire.doc.pages import FixedLayoutCell
            ret = FixedLayoutCell(intPtr)
        elif(strName == "Spire.Doc.Pages.FixedLayoutColumn"):
            from spire.doc.pages import FixedLayoutColumn
            ret = FixedLayoutColumn(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutComment"):
            from spire.doc.pages import FixedLayoutComment
            ret = FixedLayoutComment(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutDocument"):
            from spire.doc.pages import FixedLayoutDocument
            ret = FixedLayoutDocument(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutEndnote"):
            from spire.doc.pages import FixedLayoutEndnote
            ret = FixedLayoutEndnote(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutFootnote"):
            from spire.doc.pages import FixedLayoutFootnote
            ret = FixedLayoutFootnote(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutHeaderFooter"):
            from spire.doc.pages import FixedLayoutHeaderFooter
            ret = FixedLayoutHeaderFooter(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutLine"):
            from spire.doc.pages import FixedLayoutLine
            ret = FixedLayoutLine(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutNoteSeparator"):
            from spire.doc.pages import FixedLayoutNoteSeparator
            ret = FixedLayoutNoteSeparator(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutPage"):
            from spire.doc.pages import FixedLayoutPage
            ret = FixedLayoutPage(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutRow"):
            from spire.doc.pages import FixedLayoutRow
            ret = FixedLayoutRow(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutSpan"):
            from spire.doc.pages import FixedLayoutSpan
            ret = FixedLayoutSpan(intPtr)
        elif (strName == "Spire.Doc.Pages.FixedLayoutTextBox"):
            from spire.doc.pages import FixedLayoutTextBox
            ret = FixedLayoutTextBox(intPtr)
        else:
            ret = LayoutElement(intPtr)

        return ret

    @property
    def Count(self)->int:
        """
    <summary>
        Gets the number of entities in the collection.
    </summary>
        """
        GetDllLibDoc().LayoutCollection_get_Count.argtypes=[c_void_p]
        GetDllLibDoc().LayoutCollection_get_Count.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LayoutCollection_get_Count,self.Ptr)
        return ret

