from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutFootnote (  BodyLayoutElement) :
    """
    <summary>
        Represents placeholder for footnote content.
    </summary>
    """
    @property

    def Footnote(self)->'Footnote':
        """
    <summary>
        Returns the footnote that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutFootnote_get_Footnote.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutFootnote_get_Footnote.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutFootnote_get_Footnote,self.Ptr)
        ret = None if intPtr==None else Footnote(intPtr)
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutFootnote_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutFootnote_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutFootnote_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


