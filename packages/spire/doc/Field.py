from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Field (  TextRange, IField) :
    """
    Represents a field in a document.
    """
    @dispatch
    def __init__(self, doc: 'IDocument'):
        """
        Initializes a new instance of the Field class.
        Args:
            doc: The document that the field belongs to.
        """
        intPdoc: c_void_p = doc.Ptr

        GetDllLibDoc().Field_CreateFieldD.argtypes=[c_void_p]
        GetDllLibDoc().Field_CreateFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Field_CreateFieldD,intPdoc)
        super(Field, self).__init__(intPtr)

    @property
    def IsLocked(self)->bool:
        """
        Gets or sets the lock property of the field. If the field is locked, the field can't be updated.
        Returns:
            A boolean value indicating whether the field is locked.
        """
        GetDllLibDoc().Field_get_IsLocked.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_IsLocked.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Field_get_IsLocked,self.Ptr)
        return ret

    @IsLocked.setter
    def IsLocked(self, value:bool):
        """
        Sets the lock property of the field.
        Args:
            value: A boolean value indicating whether to lock the field.
        """
        GetDllLibDoc().Field_set_IsLocked.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Field_set_IsLocked,self.Ptr, value)

    @property

    def TextFormat(self)->'TextFormat':
        """
        Gets or sets the regular text format.
        Returns:
            The regular text format.
        """
        GetDllLibDoc().Field_get_TextFormat.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_TextFormat.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Field_get_TextFormat,self.Ptr)
        objwraped = TextFormat(ret)
        return objwraped

    @TextFormat.setter
    def TextFormat(self, value:'TextFormat'):
        """
        Sets the regular text format.
        Args:
            value: The regular text format to set.
        """
        GetDllLibDoc().Field_set_TextFormat.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Field_set_TextFormat,self.Ptr, value.value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        Returns:
            The type of the document object.
        """
        GetDllLibDoc().Field_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Field_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Pattern(self)->str:
        """
        Returns or sets the field pattern.
        Returns:
            The field pattern.
        """
        GetDllLibDoc().Field_get_Pattern.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Pattern.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Field_get_Pattern,self.Ptr))
        return ret


    @Pattern.setter
    def Pattern(self, value:str):
        """
        Sets the field pattern.
        Args:
            value: The field pattern to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Field_set_Pattern.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Field_set_Pattern,self.Ptr, valuePtr)

    @property

    def Value(self)->str:
        """
        Gets the field value.
        Returns:
            The field value.
        """
        GetDllLibDoc().Field_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Value.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Field_get_Value,self.Ptr))
        return ret


    @property

    def Type(self)->'FieldType':
        """
        Returns or sets the field type.
        Returns:
            The field type.
        """
        GetDllLibDoc().Field_get_Type.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Type.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Field_get_Type,self.Ptr)
        objwraped = FieldType(ret)
        return objwraped

    @Type.setter
    def Type(self, value:'FieldType'):
        """
        Sets the field type.
        Args:
            value: The field type to set.
        """
        GetDllLibDoc().Field_set_Type.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Field_set_Type,self.Ptr, value.value)

    @property

    def Code(self)->str:
        """
        Gets or sets the field code.
        Returns:
            The field code.
        """
        GetDllLibDoc().Field_get_Code.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Code.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Field_get_Code,self.Ptr))
        return ret


    @Code.setter
    def Code(self, value:str):
        """
        Sets the field code.
        Args:
            value: The field code to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Field_set_Code.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Field_set_Code,self.Ptr, valuePtr)

    @property

    def Separator(self)->'FieldMark':
        """
        Gets or sets the field separator.
        Returns:
            The field separator.
        """
        GetDllLibDoc().Field_get_Separator.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_Separator.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Field_get_Separator,self.Ptr)
        from spire.doc import FieldMark
        ret = None if intPtr==None else FieldMark(intPtr)
        return ret


    @property

    def End(self)->'FieldMark':
        """
        Gets or sets the field end.
        Returns:
            The field mark, Type of FieldEnd.
        """
        GetDllLibDoc().Field_get_End.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_End.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Field_get_End,self.Ptr)
        from spire.doc import FieldMark
        ret = None if intPtr==None else FieldMark(intPtr)
        return ret


    @End.setter
    def End(self, value:'FieldMark'):
        """
        Sets the field end.
        Args:
            value: The field mark to set, Type of FieldEnd.
        """
        GetDllLibDoc().Field_set_End.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Field_set_End,self.Ptr, value.Ptr)

    @property

    def FieldText(self)->str:
        """
        Gets or sets the field display text information.
        Returns:
            The field display text information.
        """
        GetDllLibDoc().Field_get_FieldText.argtypes=[c_void_p]
        GetDllLibDoc().Field_get_FieldText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Field_get_FieldText,self.Ptr))
        return ret


    @FieldText.setter
    def FieldText(self, value:str):
        """
        Sets the field display text information.
        Args:
            value: The field display text information to set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Field_set_FieldText.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Field_set_FieldText,self.Ptr, valuePtr)

    def Update(self):
        """
        Updates the result of the field.
        Can only be simpler field.
        Direct calls cannot update the NumPages field and Page field, etc.
        """
        GetDllLibDoc().Field_Update.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Field_Update,self.Ptr)

