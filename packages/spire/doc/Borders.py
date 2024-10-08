from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Borders (  WordAttrCollection) :
    """
    Represents a collection of four borders. <see cref="!:Spire.Doc.Border" />
    """
    @property
    def NoBorder(self)->bool:
        """
        Gets whether the border exists
        """
        GetDllLibDoc().Borders_get_NoBorder.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_NoBorder.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Borders_get_NoBorder,self.Ptr)
        return ret

    @property

    def Left(self)->'Border':
        """
        Gets left border.
        """
        GetDllLibDoc().Borders_get_Left.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_Left.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_Left,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def Top(self)->'Border':
        """
        Gets top border.
        """
        GetDllLibDoc().Borders_get_Top.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_Top.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_Top,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property
    def Right(self) -> 'Border':
        """
        Gets right border.
        """
        GetDllLibDoc().Borders_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_Right.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_Right,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def Bottom(self)->'Border':
        """
        Gets bottom border.
        """
        GetDllLibDoc().Borders_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_Bottom.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_Bottom,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def Vertical(self)->'Border':
        """
        Gets vertical border.
        """
        GetDllLibDoc().Borders_get_Vertical.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_Vertical.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_Vertical,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def Horizontal(self)->'Border':
        """
        Gets horizontal border.
        """
        GetDllLibDoc().Borders_get_Horizontal.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_Horizontal.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_Horizontal,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def DiagonalDown(self)->'Border':
        """
        Gets diagonal border from top left corner to bottom right corner.
        """
        GetDllLibDoc().Borders_get_DiagonalDown.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_DiagonalDown.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_DiagonalDown,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret


    @property

    def DiagonalUp(self)->'Border':
        """
        Gets diagonal border from bottom left corner to top right corner.
        """
        GetDllLibDoc().Borders_get_DiagonalUp.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_DiagonalUp.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_get_DiagonalUp,self.Ptr)
        ret = None if intPtr==None else Border(intPtr)
        return ret

    
    def Color(self, value:'Color'):
        GetDllLibDoc().Borders_set_Color.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Borders_set_Color,self.Ptr, value.Ptr)

    
    def LineWidth(self, value:float):
        GetDllLibDoc().Borders_set_LineWidth.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Borders_set_LineWidth,self.Ptr, value)

    def SetOnlyLineWidth(self, lineWidth: float):
        """
        Sets only line width.
        """
        
        GetDllLibDoc().Borders_SetOnlyLineWidth.argtypes=[c_void_p ,c_float]
        CallCFunction(GetDllLibDoc().Borders_SetOnlyLineWidth,self.Ptr, lineWidth)

    
    def BorderType(self, value:'BorderStyle'):
        GetDllLibDoc().Borders_set_BorderType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Borders_set_BorderType,self.Ptr, value.value)

    def Space(self, value:float):
        GetDllLibDoc().Borders_set_Space.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Borders_set_Space,self.Ptr, value)

    def IsShadow(self, value:bool):
        GetDllLibDoc().Borders_set_IsShadow.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Borders_set_IsShadow,self.Ptr, value)

    @property
    def IsDefault(self)->bool:
        """
        Gets a value indicating whether format is default.
        <value>
        <c>true</c> if format is default; otherwise,<c>false</c>.</value>&gt;
        """
        GetDllLibDoc().Borders_get_IsDefault.argtypes=[c_void_p]
        GetDllLibDoc().Borders_get_IsDefault.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Borders_get_IsDefault,self.Ptr)
        return ret


    def Clone(self)->'Borders':
        """
        Clones self.
        <returns></returns>
        """
        GetDllLibDoc().Borders_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Borders_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Borders_Clone,self.Ptr)
        ret = None if intPtr==None else Borders(intPtr)
        return ret



    @staticmethod
    def LeftKey()->int:
        """
        Gets the left key.
        """
        #GetDllLibDoc().Borders_LeftKey.argtypes=[]
        GetDllLibDoc().Borders_LeftKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_LeftKey,)
        return ret

    @staticmethod
    def TopKey()->int:
        """
        Gets the top key.
        """
        #GetDllLibDoc().Borders_TopKey.argtypes=[]
        GetDllLibDoc().Borders_TopKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_TopKey,)
        return ret

    @staticmethod
    def BottomKey()->int:
        """
        Gets the bottom key.
        """
        #GetDllLibDoc().Borders_BottomKey.argtypes=[]
        GetDllLibDoc().Borders_BottomKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_BottomKey,)
        return ret

    @staticmethod
    def RightKey()->int:
        """
        Gets the right key.
        """
        #GetDllLibDoc().Borders_RightKey.argtypes=[]
        GetDllLibDoc().Borders_RightKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_RightKey,)
        return ret

    @staticmethod
    def VerticalKey()->int:
        """
        Gets the vertical key.
        """
        #GetDllLibDoc().Borders_VerticalKey.argtypes=[]
        GetDllLibDoc().Borders_VerticalKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_VerticalKey,)
        return ret

    @staticmethod
    def HorizontalKey()->int:
        """
        Gets the horizontal key.
        """
        #GetDllLibDoc().Borders_HorizontalKey.argtypes=[]
        GetDllLibDoc().Borders_HorizontalKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_HorizontalKey,)
        return ret

    @staticmethod
    def DiagonalDownKey()->int:
        """
        Gets the diagonal down key.
        """
        #GetDllLibDoc().Borders_DiagonalDownKey.argtypes=[]
        GetDllLibDoc().Borders_DiagonalDownKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_DiagonalDownKey,)
        return ret

    @staticmethod
    def DiagonalUpKey()->int:
        """
        Gets the diagonal up key.
        """
        #GetDllLibDoc().Borders_DiagonalUpKey.argtypes=[]
        GetDllLibDoc().Borders_DiagonalUpKey.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Borders_DiagonalUpKey,)
        return ret
