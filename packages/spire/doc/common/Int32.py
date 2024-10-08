from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

class Int32 (SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        dlllib.Int32_Create.restype = c_void_p
        intPtr = CallCFunction(dlllib.Int32_Create)
        super(String, self).__init__(intPtr)
    @dispatch
    def __init__(self, value:int):
        dlllib.Int32_CreateV.argtypes=[ c_int]
        dlllib.Int32_CreateV.restype = c_void_p
        intPtr = CallCFunction(dlllib.Int32_CreateV,value)
        super(Int32, self).__init__(intPtr)

    def __str__(self):
        return str(self.Value)

    @property
    def Value(self)->int:
        """

        """
        dlllib.Int32_Value.argtypes=[ c_void_p]
        dlllib.Int32_Value.restype=c_int
        ret = CallCFunction(dlllib.Int32_Value, self.Ptr)
        return ret
#    @dispatch

#    def CompareTo(self ,value:SpireObject)->int:
#        """

#        """
#        intPtrvalue:c_void_p = value.Ptr

#        dlllib.Int32_CompareTo.argtypes=[c_void_p ,c_void_p]
#        dlllib.Int32_CompareTo.restype=c_int
#        ret = CallCFunction(dlllib.Int32_CompareTo,self.Ptr, intPtrvalue)
#        return ret

#    @dispatch

#    def CompareTo(self ,value:int)->int:
#        """

#        """
        
#        dlllib.Int32_CompareToV.argtypes=[c_void_p ,c_int]
#        dlllib.Int32_CompareToV.restype=c_int
#        ret = CallCFunction(dlllib.Int32_CompareToV,self.Ptr, value)
#        return ret

#    @dispatch

#    def Equals(self ,obj:SpireObject)->bool:
#        """

#        """
#        intPtrobj:c_void_p = obj.Ptr

#        dlllib.Int32_Equals.argtypes=[c_void_p ,c_void_p]
#        dlllib.Int32_Equals.restype=c_bool
#        ret = CallCFunction(dlllib.Int32_Equals,self.Ptr, intPtrobj)
#        return ret

#    @dispatch

#    def Equals(self ,obj:int)->bool:
#        """

#        """
        
#        dlllib.Int32_EqualsO.argtypes=[c_void_p ,c_int]
#        dlllib.Int32_EqualsO.restype=c_bool
#        ret = CallCFunction(dlllib.Int32_EqualsO,self.Ptr, obj)
#        return ret

#    def GetHashCode(self)->int:
#        """

#        """
#        dlllib.Int32_GetHashCode.argtypes=[c_void_p]
#        dlllib.Int32_GetHashCode.restype=c_int
#        ret = CallCFunction(dlllib.Int32_GetHashCode,self.Ptr)
#        return ret

#    @dispatch

#    def ToString(self)->str:
#        """

#        """
#        dlllib.Int32_ToString.argtypes=[c_void_p]
#        dlllib.Int32_ToString.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Int32_ToString,self.Ptr)
#        return ret


#    @dispatch

#    def ToString(self ,format:str)->str:
#        """

#        """
        
#        dlllib.Int32_ToStringF.argtypes=[c_void_p ,c_void_p]
#        dlllib.Int32_ToStringF.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Int32_ToStringF,self.Ptr, format)
#        return ret


##    @dispatch
##
##    def ToString(self ,provider:'IFormatProvider')->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##
##        dlllib.Int32_ToStringP.argtypes=[c_void_p ,c_void_p]
##        dlllib.Int32_ToStringP.restype=c_wchar_p
##        ret = CallCFunction(dlllib.Int32_ToStringP,self.Ptr, intPtrprovider)
##        return ret
##


##    @dispatch
##
##    def ToString(self ,format:str,provider:'IFormatProvider')->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##
##        dlllib.Int32_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
##        dlllib.Int32_ToStringFP.restype=c_wchar_p
##        ret = CallCFunction(dlllib.Int32_ToStringFP,self.Ptr, format,intPtrprovider)
##        return ret
##


#    @staticmethod
#    @dispatch

#    def Parse(s:str)->int:
#        """

#        """
        
#        dlllib.Int32_Parse.argtypes=[ c_void_p]
#        dlllib.Int32_Parse.restype=c_int
#        ret = CallCFunction(dlllib.Int32_Parse, s)
#        return ret

##    @staticmethod
##    @dispatch
##
##    def Parse(s:str,style:'NumberStyles')->int:
##        """
##
##        """
##        enumstyle:c_int = style.value
##
##        dlllib.Int32_ParseSS.argtypes=[ c_void_p,c_int]
##        dlllib.Int32_ParseSS.restype=c_int
##        ret = CallCFunction(dlllib.Int32_ParseSS, s,enumstyle)
##        return ret


##    @staticmethod
##    @dispatch
##
##    def Parse(s:str,provider:'IFormatProvider')->int:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##
##        dlllib.Int32_ParseSP.argtypes=[ c_void_p,c_void_p]
##        dlllib.Int32_ParseSP.restype=c_int
##        ret = CallCFunction(dlllib.Int32_ParseSP, s,intPtrprovider)
##        return ret


##    @staticmethod
##    @dispatch
##
##    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->int:
##        """
##
##        """
##        enumstyle:c_int = style.value
##        intPtrprovider:c_void_p = provider.Ptr
##
##        dlllib.Int32_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
##        dlllib.Int32_ParseSSP.restype=c_int
##        ret = CallCFunction(dlllib.Int32_ParseSSP, s,enumstyle,intPtrprovider)
##        return ret


##    @staticmethod
##    @dispatch
##
##    def TryParse(s:str,result:'Int32&')->bool:
##        """
##
##        """
##        intPtrresult:c_void_p = result.Ptr
##
##        dlllib.Int32_TryParse.argtypes=[ c_void_p,c_void_p]
##        dlllib.Int32_TryParse.restype=c_bool
##        ret = CallCFunction(dlllib.Int32_TryParse, s,intPtrresult)
##        return ret


##    @staticmethod
##    @dispatch
##
##    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'Int32&')->bool:
##        """
##
##        """
##        enumstyle:c_int = style.value
##        intPtrprovider:c_void_p = provider.Ptr
##        intPtrresult:c_void_p = result.Ptr
##
##        dlllib.Int32_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
##        dlllib.Int32_TryParseSSPR.restype=c_bool
##        ret = CallCFunction(dlllib.Int32_TryParseSSPR, s,enumstyle,intPtrprovider,intPtrresult)
##        return ret


##
##    def GetTypeCode(self)->'TypeCode':
##        """
##
##        """
##        dlllib.Int32_GetTypeCode.argtypes=[c_void_p]
##        dlllib.Int32_GetTypeCode.restype=c_int
##        ret = CallCFunction(dlllib.Int32_GetTypeCode,self.Ptr)
##        objwraped = TypeCode(ret)
##        return objwraped


#    @staticmethod
#    def MaxValue()->int:
#        """

#        """
#        #dlllib.Int32_MaxValue.argtypes=[]
#        dlllib.Int32_MaxValue.restype=c_int
#        ret = CallCFunction(dlllib.Int32_MaxValue)
#        return ret

#    @staticmethod
#    def MinValue()->int:
#        """

#        """
#        #dlllib.Int32_MinValue.argtypes=[]
#        dlllib.Int32_MinValue.restype=c_int
#        ret = CallCFunction(dlllib.Int32_MinValue)
#        return ret

