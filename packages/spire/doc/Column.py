from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Column (  DocumentSerializable) :
    """
    Represents a column in a document.
    """
    @property
    def Width(self)->float:
        """
        Returns or sets the width of the column.
        """
        GetDllLibDoc().Column_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().Column_get_Width.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Column_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        """
        Sets the width of the column.
        """
        GetDllLibDoc().Column_set_Width.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Column_set_Width,self.Ptr, value)

    @property
    def Space(self)->float:
        """
        Gets or sets the spacing between the current and next column.
        """
        GetDllLibDoc().Column_get_Space.argtypes=[c_void_p]
        GetDllLibDoc().Column_get_Space.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Column_get_Space,self.Ptr)
        return ret

    @Space.setter
    def Space(self, value:float):
        """
        Sets the spacing between the current and next column.
        """
        GetDllLibDoc().Column_set_Space.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Column_set_Space,self.Ptr, value)

