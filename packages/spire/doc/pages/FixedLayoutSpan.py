from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutSpan (  LayoutElement) :
    """
    <summary>
        Represents one or more characters in a line.
    </summary>
    """
    @property

    def Kind(self)->str:
        """
    <summary>
        Gets kind of the span. This cannot be null.
    </summary>
        """
        GetDllLibDoc().FixedLayoutSpan_get_Kind.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutSpan_get_Kind.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FixedLayoutSpan_get_Kind,self.Ptr))
        return ret


    @property

    def Text(self)->str:
        """
    <summary>
        Exports the contents of the entity into a string in plain text format.
    </summary>
        """
        GetDllLibDoc().FixedLayoutSpan_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutSpan_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().FixedLayoutSpan_get_Text,self.Ptr))
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutSpan_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutSpan_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutSpan_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


