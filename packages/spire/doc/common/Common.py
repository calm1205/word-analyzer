import abc
import ctypes
from typing import TypeVar, Union, Generic, List,Tuple
from enum import Enum
from plum import dispatch
from ctypes import *

if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *

class IntPtrArray(Structure):
    _fields_ = [
        ('size',c_int),
        ('data',(c_uint)*20)
    ]
class IntPtrWithTypeName(Structure):
    _fields_ = [
        ('intPtr',(c_uint)*2),
        ('typeName', c_void_p)
    ]

def PtrToStr(valuePtr:c_void_p):
    if valuePtr != None :
        resultStr = ctypes.string_at(valuePtr).decode('utf-8')
        ReleasePtr(valuePtr)
        return resultStr
    else :
        return None
def StrToPtr(value):
    if value != None and isinstance(value,str):
        utf8Bytes = value.encode('utf-8')
        utf8StrPoint = ctypes.c_char_p(utf8Bytes)
        return utf8StrPoint
    else :
        return value

def GetIntPtrArray(intPtrArray:IntPtrArray):
    ret = []
    size = intPtrArray.size
    if(size == 0):
        return ret
    r0 = intPtrArray.data[0] + (intPtrArray.data[1]<<32)
    if(size <= 10):
        ret.append(r0)
        for i in range(1,size):
            ret.append(intPtrArray.data[i*2] + (intPtrArray.data[i*2+1]<<32))
    else:
        r = cast(r0, POINTER(c_void_p))
        for i in range(0,size):
            ret.append(r[i])

    return ret

def GetByteArray(intPtrArray:IntPtrArray):
    ret = []
    size = intPtrArray.size
    if(size == 0):
        return ret
    r0 = intPtrArray.data[0] + (intPtrArray.data[1]<<32)
    r = cast(r0, POINTER(c_void_p))
    for i in range(0,size):
        ret.append(r[i])

    return ret

T = TypeVar("T")
def GetVectorFromArray(intPtrArray:IntPtrArray, t):
    ret:List = []
    #obj = self.__orig_bases__[0].__args__[0]
    #intPtr = GetByteArray(intPtrArr);
    size = intPtrArray.size
    if(size == 0):
        return ret
    r0 = intPtrArray.data[0] + (intPtrArray.data[1]<<32)
    r = cast(r0, POINTER(t))
    for i in range(0,size):
        ret.append(r[i])
    return ret

def GetStrVectorFromArray(intPtrArray:IntPtrArray,t):
    ret:List = []
    size = intPtrArray.size
    if(size == 0):
        return ret
    r0 = intPtrArray.data[0] + (intPtrArray.data[1]<<32)
    r = cast(r0, POINTER(t))
    for i in range(0,size):
        ret.append(PtrToStr(r[i]))
    return ret

def GetObjVectorFromArray(intPtrArray:IntPtrArray, t):
    ret:List = []
    arr = GetIntPtrArray(intPtrArray)
    size = intPtrArray.size
    if(size == 0):
        return ret
    for i in range(0,size):
        obj = t(arr[i])
        ret.append(obj)
    return ret

def GetIntValue(ptr:c_void_p, valueName:str, paraValues:str)->int:
    if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
        valueNamePtr = StrToPtr(valueName)
        paraValuesPtr = StrToPtr(paraValues)
        dlllib.Spire_GetIntValue.argtypes=[c_void_p, c_char_p, c_char_p]
        dlllib.Spire_GetIntValue.restype=c_int
        ret = CallCFunction(dlllib.Spire_GetIntValue,ptr, valueNamePtr, paraValuesPtr)
        return ret
    else:
        dlllib.Spire_GetIntValue.argtypes=[c_void_p, c_wchar_p, c_wchar_p]
        dlllib.Spire_GetIntValue.restype=c_int
        ret = CallCFunction(dlllib.Spire_GetIntValue,ptr, valueName, paraValues)
        return ret
    
def GetObjIntPtr(ptr:c_void_p, valueName:str, paraValues:str)->c_void_p:
    if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
        valueNamePtr = StrToPtr(valueName)
        paraValuesPtr = StrToPtr(paraValues)
        dlllib.Spire_GetIntValue.argtypes=[c_void_p, c_char_p, c_char_p]
        dlllib.Spire_GetIntValue.restype=c_void_p
        ret = CallCFunction(dlllib.Spire_GetIntPtr,ptr,valueNamePtr, paraValuesPtr)
        return ret
    else:
        dlllib.Spire_GetIntValue.argtypes=[c_void_p, c_wchar_p, c_wchar_p]
        dlllib.Spire_GetIntValue.restype=c_void_p
        ret = CallCFunction(dlllib.Spire_GetIntPtr,ptr, valueName, paraValues)
        return ret
    

def GetBytesFromArray(intPtrArray:IntPtrArray):
    ret:List = []
    size = intPtrArray.size
    if(size == 0):
        return ret
    r0 = intPtrArray.data[0] + (intPtrArray.data[1]<<32)
    r = cast(r0, POINTER(c_ubyte))
    for i in range(0,size):
        ret.append(r[i])
    return bytes(ret)

def ReleasePtr(intPtr):
    dlllib.Spire_FreeHandle.argtypes=[c_void_p]
    CallCFunction(dlllib.Spire_FreeHandle,intPtr)
