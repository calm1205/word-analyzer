from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListLevel (  DocumentSerializable) :
    """
    Represents a list level.
    """
    @property

    def NumberAlignment(self)->'ListNumberAlignment':
        """
        Gets or sets the number alignment of the list level.
        """
        GetDllLibDoc().ListLevel_get_NumberAlignment.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_NumberAlignment,self.Ptr)
        objwraped = ListNumberAlignment(ret)
        return objwraped

    @NumberAlignment.setter
    def NumberAlignment(self, value:'ListNumberAlignment'):
        """
        Sets the number alignment of the list level.
        """
        GetDllLibDoc().ListLevel_set_NumberAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ListLevel_set_NumberAlignment,self.Ptr, value.value)

    @property
    def StartAt(self)->int:
        """
        Gets or sets the start number of the list level.
        """
        GetDllLibDoc().ListLevel_get_StartAt.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_StartAt.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_StartAt,self.Ptr)
        return ret

    @StartAt.setter
    def StartAt(self, value:int):
        """
        Sets the start number of the list level.
        """
        GetDllLibDoc().ListLevel_set_StartAt.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ListLevel_set_StartAt,self.Ptr, value)

    @property
    def TabSpaceAfter(self)->float:
        """
        Gets or sets the tab space after the list level.
        """
        GetDllLibDoc().ListLevel_get_TabSpaceAfter.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_TabSpaceAfter.restype=c_float
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_TabSpaceAfter,self.Ptr)
        return ret

    @TabSpaceAfter.setter
    def TabSpaceAfter(self, value:float):
        """
        Sets the tab space after the list level.
        """
        GetDllLibDoc().ListLevel_set_TabSpaceAfter.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().ListLevel_set_TabSpaceAfter,self.Ptr, value)

    @property
    def TextPosition(self)->float:
        """
        Gets or sets the text position of the list level.
        """
        GetDllLibDoc().ListLevel_get_TextPosition.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_TextPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_TextPosition,self.Ptr)
        return ret

    @TextPosition.setter
    def TextPosition(self, value:float):
        """
        Sets the text position of the list level.
        """
        GetDllLibDoc().ListLevel_set_TextPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().ListLevel_set_TextPosition,self.Ptr, value)

    @property

    def NumberPrefix(self)->str:
        """
        Gets or sets the number prefix of the list level.
        """
        GetDllLibDoc().ListLevel_get_NumberPrefix.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberPrefix.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().ListLevel_get_NumberPrefix,self.Ptr))
        return ret


    @NumberPrefix.setter
    def NumberPrefix(self, value:str):
        """
        Sets the number prefix of the list level.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ListLevel_set_NumberPrefix.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().ListLevel_set_NumberPrefix,self.Ptr, valuePtr)

    @property

    def NumberSufix(self)->str:
        """
        Gets or sets the number suffix of the list level.
        """
        GetDllLibDoc().ListLevel_get_NumberSufix.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberSufix.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().ListLevel_get_NumberSufix,self.Ptr))
        return ret


    @NumberSufix.setter
    def NumberSufix(self, value:str):
        """
        Sets the number suffix of the list level.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ListLevel_set_NumberSufix.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().ListLevel_set_NumberSufix,self.Ptr, valuePtr)

    @property

    def BulletCharacter(self)->str:
        """
        Gets or sets the bullet character of the list level.
        """
        GetDllLibDoc().ListLevel_get_BulletCharacter.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_BulletCharacter.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().ListLevel_get_BulletCharacter,self.Ptr))
        return ret


    @BulletCharacter.setter
    def BulletCharacter(self, value:str):
        """
        Sets the bullet character of the list level.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ListLevel_set_BulletCharacter.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().ListLevel_set_BulletCharacter,self.Ptr, valuePtr)

    @property

    def PatternType(self)->'ListPatternType':
        """
        Gets or sets the pattern type of the list level.
        """
        GetDllLibDoc().ListLevel_get_PatternType.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_PatternType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_PatternType,self.Ptr)
        objwraped = ListPatternType(ret)
        return objwraped

    @PatternType.setter
    def PatternType(self, value:'ListPatternType'):
        """
        Sets the pattern type of the list level.
        """
        GetDllLibDoc().ListLevel_set_PatternType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ListLevel_set_PatternType,self.Ptr, value.value)

    @property
    def NoRestartByHigher(self)->bool:
        """
        Gets or sets whether the list level restarts numbering by higher levels.
        """
        GetDllLibDoc().ListLevel_get_NoRestartByHigher.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NoRestartByHigher.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_NoRestartByHigher,self.Ptr)
        return ret

    @NoRestartByHigher.setter
    def NoRestartByHigher(self, value:bool):
        """
        Sets whether the list level restarts numbering by higher levels.
        """
        GetDllLibDoc().ListLevel_set_NoRestartByHigher.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().ListLevel_set_NoRestartByHigher,self.Ptr, value)

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format of the list level.
        """
        GetDllLibDoc().ListLevel_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListLevel_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def ParagraphFormat(self)->'ParagraphFormat':
        """
        Gets the paragraph format of the list level.
        """
        GetDllLibDoc().ListLevel_get_ParagraphFormat.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_ParagraphFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListLevel_get_ParagraphFormat,self.Ptr)
        ret = None if intPtr==None else ParagraphFormat(intPtr)
        return ret


    @property

    def FollowCharacter(self)->'FollowCharacterType':
        """
        Gets or sets the type of character following the number text for the paragraph.
        """
        GetDllLibDoc().ListLevel_get_FollowCharacter.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_FollowCharacter.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_FollowCharacter,self.Ptr)
        objwraped = FollowCharacterType(ret)
        return objwraped

    @FollowCharacter.setter
    def FollowCharacter(self, value:'FollowCharacterType'):
        """
        Sets the type of character following the number text for the paragraph.
        """
        GetDllLibDoc().ListLevel_set_FollowCharacter.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ListLevel_set_FollowCharacter,self.Ptr, value.value)

    @property
    def IsLegalStyleNumbering(self)->bool:
        """
        Gets or sets whether the list level uses legal style numbering.
        """
        GetDllLibDoc().ListLevel_get_IsLegalStyleNumbering.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_IsLegalStyleNumbering.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_IsLegalStyleNumbering,self.Ptr)
        return ret

    @IsLegalStyleNumbering.setter
    def IsLegalStyleNumbering(self, value:bool):
        """
        Sets whether the list level uses legal style numbering.
        """
        GetDllLibDoc().ListLevel_set_IsLegalStyleNumbering.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().ListLevel_set_IsLegalStyleNumbering,self.Ptr, value)

    @property
    def NumberPosition(self)->float:
        """
        Gets or sets the number position of the list level.
        """
        GetDllLibDoc().ListLevel_get_NumberPosition.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_NumberPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_NumberPosition,self.Ptr)
        return ret

    @NumberPosition.setter
    def NumberPosition(self, value:float):
        GetDllLibDoc().ListLevel_set_NumberPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().ListLevel_set_NumberPosition,self.Ptr, value)

    @property
    def UsePrevLevelPattern(self)->bool:
        """

        """
        GetDllLibDoc().ListLevel_get_UsePrevLevelPattern.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_get_UsePrevLevelPattern.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ListLevel_get_UsePrevLevelPattern,self.Ptr)
        return ret

    @UsePrevLevelPattern.setter
    def UsePrevLevelPattern(self, value:bool):
        GetDllLibDoc().ListLevel_set_UsePrevLevelPattern.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().ListLevel_set_UsePrevLevelPattern,self.Ptr, value)


    def GetListItemText(self ,listItemIndex:int,listType:'ListType')->str:
        """

        """
        enumlistType:c_int = listType.value

        GetDllLibDoc().ListLevel_GetListItemText.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().ListLevel_GetListItemText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().ListLevel_GetListItemText,self.Ptr, listItemIndex,enumlistType))
        return ret



    def Clone(self)->'ListLevel':
        """

        """
        GetDllLibDoc().ListLevel_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ListLevel_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListLevel_Clone,self.Ptr)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


