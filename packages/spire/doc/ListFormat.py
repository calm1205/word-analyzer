from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListFormat (  WordAttrCollection) :
    """
    Represents the formatting of a list in a document.
    """
    @property
    def ListLevelNumber(self)->int:
        """
        Returns or sets the list nesting level.
        """
        GetDllLibDoc().ListFormat_get_ListLevelNumber.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_ListLevelNumber.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListFormat_get_ListLevelNumber,self.Ptr)
        return ret

    @ListLevelNumber.setter
    def ListLevelNumber(self, value:int):
        GetDllLibDoc().ListFormat_set_ListLevelNumber.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ListFormat_set_ListLevelNumber,self.Ptr, value)

    @property

    def ListType(self)->'ListType':
        """
        Gets the type of the list.
        """
        GetDllLibDoc().ListFormat_get_ListType.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_ListType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListFormat_get_ListType,self.Ptr)
        objwraped = ListType(ret)
        return objwraped

    @property
    def IsRestartNumbering(self)->bool:
        """
        Returns or sets whether numbering of the list must restart from the previous list.
        """
        GetDllLibDoc().ListFormat_get_IsRestartNumbering.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_IsRestartNumbering.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ListFormat_get_IsRestartNumbering,self.Ptr)
        return ret

    @IsRestartNumbering.setter
    def IsRestartNumbering(self, value:bool):
        GetDllLibDoc().ListFormat_set_IsRestartNumbering.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().ListFormat_set_IsRestartNumbering,self.Ptr, value)

    @property

    def CustomStyleName(self)->str:
        """
        Gets the name of the custom style.
        """
        GetDllLibDoc().ListFormat_get_CustomStyleName.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_CustomStyleName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().ListFormat_get_CustomStyleName,self.Ptr))
        return ret


    @property

    def CurrentListStyle(self)->'ListStyle':
        """
        Gets the paragraph's list style.
        """
        GetDllLibDoc().ListFormat_get_CurrentListStyle.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_CurrentListStyle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListFormat_get_CurrentListStyle,self.Ptr)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret


    @property

    def CurrentListLevel(self)->'ListLevel':
        """
        Gets the paragraph's ListLevel.
        """
        GetDllLibDoc().ListFormat_get_CurrentListLevel.argtypes=[c_void_p]
        GetDllLibDoc().ListFormat_get_CurrentListLevel.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListFormat_get_CurrentListLevel,self.Ptr)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


    def IncreaseIndentLevel(self):
        """
        Increase the level of indentation.
        """
        GetDllLibDoc().ListFormat_IncreaseIndentLevel.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ListFormat_IncreaseIndentLevel,self.Ptr)

    def DecreaseIndentLevel(self):
        """
        Decrease the level of indentation.
        """
        GetDllLibDoc().ListFormat_DecreaseIndentLevel.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ListFormat_DecreaseIndentLevel,self.Ptr)

    def ContinueListNumbering(self):
        """
        Continue the last list.
        """
        GetDllLibDoc().ListFormat_ContinueListNumbering.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ListFormat_ContinueListNumbering,self.Ptr)


    def ApplyStyle(self ,styleName:str):
        """
        Apply a list style.

        Args:
            styleName: The name of the list style.
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().ListFormat_ApplyStyle.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().ListFormat_ApplyStyle,self.Ptr, styleNamePtr)

    def ApplyBulletStyle(self):
        """
        Apply the default bullet style for the current paragraph.
        """
        GetDllLibDoc().ListFormat_ApplyBulletStyle.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ListFormat_ApplyBulletStyle,self.Ptr)

    def ApplyNumberedStyle(self):
        """
        Apply the default numbered style for the current paragraph.
        """
        GetDllLibDoc().ListFormat_ApplyNumberedStyle.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ListFormat_ApplyNumberedStyle,self.Ptr)

    def RemoveList(self):
        """
        Remove the list from the current paragraph.
        """
        GetDllLibDoc().ListFormat_RemoveList.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().ListFormat_RemoveList,self.Ptr)

