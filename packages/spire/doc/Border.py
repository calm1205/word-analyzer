from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Border(AttrCollection):
    """
    Represents a border.
    """
    @property

    def Color(self)->'Color':
        """
        Gets the color of the border.
        """
        GetDllLibDoc().Border_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_Color.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Border_get_Color,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @Color.setter
    def Color(self, value:'Color'):
        """
        Sets the color of the border.
        """
        GetDllLibDoc().Border_set_Color.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Border_set_Color,self.Ptr, value.Ptr)

    @property
    def LineWidth(self)->float:
        """
        Gets the width of the border.
        """
        GetDllLibDoc().Border_get_LineWidth.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_LineWidth.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Border_get_LineWidth,self.Ptr)
        return ret

    @LineWidth.setter
    def LineWidth(self, value:float):
        """
        Sets the width of the border.
        """
        GetDllLibDoc().Border_set_LineWidth.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Border_set_LineWidth,self.Ptr, value)

    @property

    def BorderType(self)->'BorderStyle':
        """
        Gets the style of the border.
        """
        GetDllLibDoc().Border_get_BorderType.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_BorderType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Border_get_BorderType,self.Ptr)
        objwraped = BorderStyle(ret)
        return objwraped

    @BorderType.setter
    def BorderType(self, value:'BorderStyle'):
        """
        Sets the style of the border.
        """
        GetDllLibDoc().Border_set_BorderType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Border_set_BorderType,self.Ptr, value.value)

    @property
    def Space(self)->float:
        """
        Gets the width of space to maintain between the border and text within the border.
        """
        GetDllLibDoc().Border_get_Space.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_Space.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Border_get_Space,self.Ptr)
        return ret

    @Space.setter
    def Space(self, value:float):
        """
        Sets the width of space to maintain between the border and text within the border.
        """
        GetDllLibDoc().Border_set_Space.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Border_set_Space,self.Ptr, value)

    @property
    def Shadow(self)->bool:
        """
        Gets a value indicating whether the border should be drawn with shadow.
        """
        GetDllLibDoc().Border_get_Shadow.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_Shadow.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Border_get_Shadow,self.Ptr)
        return ret

    @Shadow.setter
    def Shadow(self, value:bool):
        """
        Sets a value indicating whether the border should be drawn with shadow.
        """
        GetDllLibDoc().Border_set_Shadow.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Border_set_Shadow,self.Ptr, value)

    @property
    def IsDefault(self)->bool:
        """
        Gets a value indicating whether the format is default.
        """
        GetDllLibDoc().Border_get_IsDefault.argtypes=[c_void_p]
        GetDllLibDoc().Border_get_IsDefault.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Border_get_IsDefault,self.Ptr)
        return ret


    def InitFormatting(self ,color:'Color',lineWidth:float,borderType:'BorderStyle',shadow:bool):
        """
        Initializes the border style.
        """
        intPtrcolor: c_void_p = color.Ptr
        enumborderType: c_int = borderType.value

        GetDllLibDoc().Border_InitFormatting.argtypes=[c_void_p ,c_void_p,c_float,c_int,c_bool]
        CallCFunction(GetDllLibDoc().Border_InitFormatting,self.Ptr, intPtrcolor,lineWidth,enumborderType,shadow)

