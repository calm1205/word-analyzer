from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellFormat(WordAttrCollection):
    """
    Represents the format of a cell in a table.
    """

    @property
    def Borders(self) -> 'Borders':
        """
        Gets the borders of the cell.
        """
        GetDllLibDoc().CellFormat_get_Borders.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_Borders.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CellFormat_get_Borders,self.Ptr)
        ret = None if intPtr==None else Borders(intPtr)
        return ret

    @property
    def Paddings(self) -> 'Paddings':
        """
        Gets the paddings of the cell.
        """
        GetDllLibDoc().CellFormat_get_Paddings.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_Paddings.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CellFormat_get_Paddings,self.Ptr)
        ret = None if intPtr==None else Paddings(intPtr)
        return ret

    @property
    def VerticalAlignment(self) -> 'VerticalAlignment':
        """
        Gets or sets the vertical alignment of the cell.
        """
        GetDllLibDoc().CellFormat_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_VerticalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_VerticalAlignment,self.Ptr)
        objwraped = VerticalAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'VerticalAlignment'):
        GetDllLibDoc().CellFormat_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CellFormat_set_VerticalAlignment,self.Ptr, value.value)

    @property

    def BackColor(self)->'Color':
        """
        Gets or sets the background color of the cell.
        """
        GetDllLibDoc().CellFormat_get_BackColor.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_BackColor.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().CellFormat_get_BackColor,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @BackColor.setter
    def BackColor(self, value:'Color'):
        GetDllLibDoc().CellFormat_set_BackColor.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().CellFormat_set_BackColor,self.Ptr, value.Ptr)

    @property

    def VerticalMerge(self)->'CellMerge':
        """
        Gets or sets the vertical merging of the cell.
        """
        GetDllLibDoc().CellFormat_get_VerticalMerge.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_VerticalMerge.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_VerticalMerge,self.Ptr)
        objwraped = CellMerge(ret)
        return objwraped

    @VerticalMerge.setter
    def VerticalMerge(self, value:'CellMerge'):
        GetDllLibDoc().CellFormat_set_VerticalMerge.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CellFormat_set_VerticalMerge,self.Ptr, value.value)

    @property

    def HorizontalMerge(self)->'CellMerge':
        """
        Gets or sets the horizontal merging of the cell.
        """
        GetDllLibDoc().CellFormat_get_HorizontalMerge.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_HorizontalMerge.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_HorizontalMerge,self.Ptr)
        objwraped = CellMerge(ret)
        return objwraped

    @HorizontalMerge.setter
    def HorizontalMerge(self, value:'CellMerge'):
        GetDllLibDoc().CellFormat_set_HorizontalMerge.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CellFormat_set_HorizontalMerge,self.Ptr, value.value)

    @property
    def TextWrap(self)->bool:
        """
        Gets or sets a value indicating whether text should wrap in the cell.
        """
        GetDllLibDoc().CellFormat_get_TextWrap.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_TextWrap.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_TextWrap,self.Ptr)
        return ret

    @TextWrap.setter
    def TextWrap(self, value:bool):
        GetDllLibDoc().CellFormat_set_TextWrap.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().CellFormat_set_TextWrap,self.Ptr, value)

    @property
    def FitText(self)->bool:
        """
        Gets or sets the fit text option of the cell.
        """
        GetDllLibDoc().CellFormat_get_FitText.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_FitText.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_FitText,self.Ptr)
        return ret

    @FitText.setter
    def FitText(self, value:bool):
        GetDllLibDoc().CellFormat_set_FitText.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().CellFormat_set_FitText,self.Ptr, value)

    @property

    def TextDirection(self)->'TextDirection':
        """
        Gets or sets the text direction of the cell.
        """
        GetDllLibDoc().CellFormat_get_TextDirection.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_TextDirection.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_TextDirection,self.Ptr)
        objwraped = TextDirection(ret)
        return objwraped

    @TextDirection.setter
    def TextDirection(self, value:'TextDirection'):
        GetDllLibDoc().CellFormat_set_TextDirection.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().CellFormat_set_TextDirection,self.Ptr, value.value)

    @property
    def SamePaddingsAsTable(self)->bool:
        """
        Gets or sets whether to use the same paddings as the table.
        """
        GetDllLibDoc().CellFormat_get_SamePaddingsAsTable.argtypes=[c_void_p]
        GetDllLibDoc().CellFormat_get_SamePaddingsAsTable.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().CellFormat_get_SamePaddingsAsTable,self.Ptr)
        return ret

    @SamePaddingsAsTable.setter
    def SamePaddingsAsTable(self, value:bool):
        GetDllLibDoc().CellFormat_set_SamePaddingsAsTable.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().CellFormat_set_SamePaddingsAsTable,self.Ptr, value)

    def ClearBackground(self):
        """
        Clears the background of the cell.
        """
        GetDllLibDoc().CellFormat_ClearBackground.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().CellFormat_ClearBackground,self.Ptr)

