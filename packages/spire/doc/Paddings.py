from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Paddings (  WordAttrCollection) :
    """
    Represents a collection of padding values for a document element.
    """
    @property
    def Left(self)->float:
        """
        Gets or sets the left padding value.
        """
        GetDllLibDoc().Paddings_get_Left.argtypes=[c_void_p]
        GetDllLibDoc().Paddings_get_Left.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Paddings_get_Left,self.Ptr)
        return ret

    @Left.setter
    def Left(self, value:float):
        """
        Sets the left padding value.
        """
        GetDllLibDoc().Paddings_set_Left.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Paddings_set_Left,self.Ptr, value)

    @property
    def Top(self)->float:
        """
        Gets or sets the top padding value.
        """
        GetDllLibDoc().Paddings_get_Top.argtypes=[c_void_p]
        GetDllLibDoc().Paddings_get_Top.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Paddings_get_Top,self.Ptr)
        return ret

    @Top.setter
    def Top(self, value:float):
        """
        Sets the top padding value.
        """
        GetDllLibDoc().Paddings_set_Top.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Paddings_set_Top,self.Ptr, value)

    @property
    def Right(self)->float:
        """
        Gets or sets the right padding value.
        """
        GetDllLibDoc().Paddings_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().Paddings_get_Right.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Paddings_get_Right,self.Ptr)
        return ret

    @Right.setter
    def Right(self, value:float):
        """
        Sets the right padding value.
        """
        GetDllLibDoc().Paddings_set_Right.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Paddings_set_Right,self.Ptr, value)

    @property
    def Bottom(self)->float:
        """
        Gets or sets the bottom padding value.
        """
        GetDllLibDoc().Paddings_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().Paddings_get_Bottom.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Paddings_get_Bottom,self.Ptr)
        return ret

    @Bottom.setter
    def Bottom(self, value:float):
        """
        Sets the bottom padding value.
        """
        GetDllLibDoc().Paddings_set_Bottom.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Paddings_set_Bottom,self.Ptr, value)

    def SetAll(self, value:float):
        """
        Sets all padding values to the specified value.
        """
        GetDllLibDoc().Paddings_set_All.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Paddings_set_All,self.Ptr, value)

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """
        Determines whether the current instance is equal to the specified object.
        """
        intPtrobj:c_void_p = obj.Ptr

        GetDllLibDoc().Paddings_Equals.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paddings_Equals.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Paddings_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,other:'Paddings')->bool:
        """
        Determines whether the current instance is equal to the specified Paddings object.
        """
        intPtrother:c_void_p = other.Ptr

        GetDllLibDoc().Paddings_EqualsO.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paddings_EqualsO.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Paddings_EqualsO,self.Ptr, intPtrother)
        return ret

    @staticmethod
    def LeftKey()->int:
        """
        Gets the constant value for the left key.
        """
        #GetDllLibDoc().Paddings_LeftKey.argtypes=[]
        GetDllLibDoc().Paddings_LeftKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paddings_LeftKey,)
        return ret

    @staticmethod
    def TopKey()->int:
        """
        Gets the constant value for the top key.
        """
        #GetDllLibDoc().Paddings_TopKey.argtypes=[]
        GetDllLibDoc().Paddings_TopKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paddings_TopKey,)
        return ret

    @staticmethod
    def BottomKey()->int:
        """
        Gets the constant value for the bottom key.
        """
        #GetDllLibDoc().Paddings_BottomKey.argtypes=[]
        GetDllLibDoc().Paddings_BottomKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paddings_BottomKey,)
        return ret

    @staticmethod
    def RightKey()->int:
        """
        Gets the constant value for the right key.
        """
        #GetDllLibDoc().Paddings_RightKey.argtypes=[]
        GetDllLibDoc().Paddings_RightKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paddings_RightKey,)
        return ret

