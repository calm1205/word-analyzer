from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class FormatBase (  DocumentSerializable) :
    """
    Base class for formatting.
    """
    @property
    def IsDefault(self)->bool:
        """
        Gets a value indicating whether format is default.

        Returns:
            bool: True if format is default; otherwise, False.
        """
        GetDllLibDoc().FormatBase_get_IsDefault.argtypes=[c_void_p]
        GetDllLibDoc().FormatBase_get_IsDefault.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().FormatBase_get_IsDefault,self.Ptr)
        return ret


    def HasKey(self ,key:int)->bool:
        """
        Checks if Key exists.

        Args:
            key (int): The key.

        Returns:
            bool: True if the specified key has key, False otherwise.
        """
        
        GetDllLibDoc().FormatBase_HasKey.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().FormatBase_HasKey.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().FormatBase_HasKey,self.Ptr, key)
        return ret

    def ClearFormatting(self):
        """
        Clears the formatting.
        """
        GetDllLibDoc().FormatBase_ClearFormatting.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().FormatBase_ClearFormatting,self.Ptr)

    def ClearBackground(self):
        """
        Clears the background.
        """
        GetDllLibDoc().FormatBase_ClearBackground.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().FormatBase_ClearBackground,self.Ptr)

