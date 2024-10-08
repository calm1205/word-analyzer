from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class RevisionBase (SpireObject) :
    """
    Base class for revisions in a Word document.
    """
    @property

    def Author(self)->str:
        """
        Gets the author of the revision.

        Returns:
            str: The author of the revision.
        """
        GetDllLibDoc().RevisionBase_get_Author.argtypes=[c_void_p]
        GetDllLibDoc().RevisionBase_get_Author.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().RevisionBase_get_Author,self.Ptr))
        return ret


    @property

    def DateTime(self)->'DateTime':
        """
        Gets the date and time of the revision.

        Returns:
            DateTime: The date and time of the revision.
        """
        GetDllLibDoc().RevisionBase_get_DateTime.argtypes=[c_void_p]
        GetDllLibDoc().RevisionBase_get_DateTime.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().RevisionBase_get_DateTime,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @DateTime.setter
    def DateTime(self, value:'DateTime'):
        """
        Sets the date and time of the revision.

        Args:
            value (DateTime): The date and time of the revision.
        """
        GetDllLibDoc().RevisionBase_set_DateTime.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().RevisionBase_set_DateTime,self.Ptr, value.Ptr)

