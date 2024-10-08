from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OwnerHolder (SpireObject) :
    """
    A class that holds the owner of a document.
    """
    @property

    def Document(self)->'Document':
        """
        Gets the document.

        Returns:
            The document.
        """
        GetDllLibDoc().OwnerHolder_get_Document.argtypes=[c_void_p]
        GetDllLibDoc().OwnerHolder_get_Document.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().OwnerHolder_get_Document,self.Ptr)
        from spire.doc import Document
        ret = None if intPtr==None else Document(intPtr)
        return ret


