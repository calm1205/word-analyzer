from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class LayoutElement (SpireObject) :
    """
    <summary>
        The class serves as the foundation for elements in a document that have been rendered.
    </summary>
    """
    @property
    def PageIndex(self)->int:
        """
    <summary>
        Gets the index of a page in which rendered object. starting from 1.
    </summary>
        """
        GetDllLibDoc().LayoutElement_get_PageIndex.argtypes=[c_void_p]
        GetDllLibDoc().LayoutElement_get_PageIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LayoutElement_get_PageIndex,self.Ptr)
        return ret

    @property

    def Rectangle(self)->'RectangleF':
        """
    <summary>
        Returns bounding rectangle of the entity relative to the page top left corner (in points).
    </summary>
        """
        GetDllLibDoc().LayoutElement_get_Rectangle.argtypes=[c_void_p]
        GetDllLibDoc().LayoutElement_get_Rectangle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().LayoutElement_get_Rectangle,self.Ptr)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


    @property

    def Type(self)->'LayoutElementType':
        """
    <summary>
        Gets the type of this layout entity.
    </summary>
        """
        GetDllLibDoc().LayoutElement_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().LayoutElement_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LayoutElement_get_Type,self.Ptr)
        objwraped = LayoutElementType(ret)
        return objwraped

    @property

    def Text(self)->str:
        """
    <summary>
        Outputs the entity's contents as a plain text string.
    </summary>
        """
        GetDllLibDoc().LayoutElement_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().LayoutElement_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().LayoutElement_get_Text,self.Ptr))
        return ret


    @property

    def Parent(self)->'LayoutElement':
        """
    <summary>
        Gets the parent of this entity.
    </summary>
        """
        GetDllLibDoc().LayoutElement_get_Parent.argtypes=[c_void_p]
        GetDllLibDoc().LayoutElement_get_Parent.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().LayoutElement_get_Parent,self.Ptr)
        ret = None if intPtr==None else LayoutElement(intPtr)
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().LayoutElement_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().LayoutElement_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().LayoutElement_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret



    def GetChildEntities(self ,type:'LayoutElementType',isDeep:bool)->'LayoutCollection':
        """
    <summary>
        Obtains a group of child entities that are of a specific type.
    </summary>
    <param name="type">Specifies the type of entities to select.</param>
    <param name="isDeep">True to select from all child entities recursively.
            False to select only among immediate children</param>
        """
        enumtype:c_int = type.value

        GetDllLibDoc().LayoutElement_GetChildEntities.argtypes=[c_void_p ,c_int,c_bool]
        GetDllLibDoc().LayoutElement_GetChildEntities.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().LayoutElement_GetChildEntities,self.Ptr, enumtype,isDeep)
        from spire.doc.pages.LayoutCollection import LayoutCollection
        ret = None if intPtr==None else LayoutCollection(intPtr)
        return ret



