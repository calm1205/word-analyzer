from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocumentProperty (SpireObject) :
    """
    Represents a document property.
    """
    @property

    def Name(self)->str:
        """
        Gets the name of the document property.
        """
        GetDllLibDoc().DocumentProperty_get_Name.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_get_Name.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocumentProperty_get_Name,self.Ptr))
        return ret


    @property

    def Value(self)->'SpireObject':
        """
        Gets the value of the document property.
        """
        GetDllLibDoc().DocumentProperty_get_Value.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_get_Value.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentProperty_get_Value,self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    @Value.setter
    def Value(self, value:'SpireObject'):
        """
        Sets the value of the document property.
        """
        GetDllLibDoc().DocumentProperty_set_Value.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().DocumentProperty_set_Value,self.Ptr, value.Ptr)

    @property

    def ValueType(self)->'PropertyValueType':
        """
        Gets the value type of the document property.
        """
        GetDllLibDoc().DocumentProperty_get_ValueType.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_get_ValueType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentProperty_get_ValueType,self.Ptr)
        objwraped = PropertyValueType(ret)
        return objwraped

    @property

    def ClipboardData(self)->'ClipboardData':
        """
        Gets the clipboard data of the document property.
        """
        GetDllLibDoc().DocumentProperty_get_ClipboardData.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_get_ClipboardData.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentProperty_get_ClipboardData,self.Ptr)
        ret = None if intPtr==None else ClipboardData(intPtr)
        return ret


    @ClipboardData.setter
    def ClipboardData(self, value:'ClipboardData'):
        """
        Sets the clipboard data of the document property.
        """
        GetDllLibDoc().DocumentProperty_set_ClipboardData.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().DocumentProperty_set_ClipboardData,self.Ptr, value.Ptr)

    def ToBool(self)->bool:
        """
        Converts the document property to a boolean value.
        """
        GetDllLibDoc().DocumentProperty_ToBool.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_ToBool.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocumentProperty_ToBool,self.Ptr)
        return ret


    def ToDateTime(self)->'DateTime':
        """
        Converts the document property to a DateTime object.
        """
        GetDllLibDoc().DocumentProperty_ToDateTime.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_ToDateTime.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentProperty_ToDateTime,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    def ToFloat(self)->float:
        """
        Converts the document property to a float value.
        """
        GetDllLibDoc().DocumentProperty_ToFloat.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_ToFloat.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocumentProperty_ToFloat,self.Ptr)
        return ret

    def ToDouble(self)->float:
        """
        Converts the document property to a double value.
        """
        GetDllLibDoc().DocumentProperty_ToDouble.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_ToDouble.restype=c_double
        ret = CallCFunction(GetDllLibDoc().DocumentProperty_ToDouble,self.Ptr)
        return ret

    def ToInt(self)->int:
        """
        Converts the document property to an integer value.
        """
        GetDllLibDoc().DocumentProperty_ToInt.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_ToInt.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocumentProperty_ToInt,self.Ptr)
        return ret


    def ToString(self)->str:
        """
        Converts the document property to a string value.
        """
        GetDllLibDoc().DocumentProperty_ToString.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocumentProperty_ToString,self.Ptr))
        return ret


#
#    def ToByteArray(self)->List['Byte']:
#        """
#
#        """
#        GetDllLibDoc().DocumentProperty_ToByteArray.argtypes=[c_void_p]
#        GetDllLibDoc().DocumentProperty_ToByteArray.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().DocumentProperty_ToByteArray(self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret



    def Clone(self)->'DocumentProperty':
        """
        Clones the document property.
        """
        GetDllLibDoc().DocumentProperty_Clone.argtypes=[c_void_p]
        GetDllLibDoc().DocumentProperty_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocumentProperty_Clone,self.Ptr)
        ret = None if intPtr==None else DocumentProperty(intPtr)
        return ret
