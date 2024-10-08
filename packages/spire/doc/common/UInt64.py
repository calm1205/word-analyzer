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

class UInt64 (SpireObject) :
    """

    """
    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.UInt64_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt64_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.UInt64_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:'UInt64')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.UInt64_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt64_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.UInt64_CompareToV,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.UInt64_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt64_Equals.restype=c_bool
        ret = CallCFunction(dlllib.UInt64_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:'UInt64')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.UInt64_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt64_EqualsO.restype=c_bool
        ret = CallCFunction(dlllib.UInt64_EqualsO,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.UInt64_GetHashCode.argtypes=[c_void_p]
        dlllib.UInt64_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.UInt64_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.UInt64_ToString.argtypes=[c_void_p]
        dlllib.UInt64_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.UInt64_ToString,self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt64_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.UInt64_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.UInt64_ToStringP,self.Ptr, intPtrprovider)
#        return ret
#


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.UInt64_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt64_ToStringF.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.UInt64_ToStringF,self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt64_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.UInt64_ToStringFP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.UInt64_ToStringFP,self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->'UInt64':
        """

        """
        
        dlllib.UInt64_Parse.argtypes=[ c_void_p]
        dlllib.UInt64_Parse.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt64_Parse, s)
        ret = None if intPtr==None else UInt64(intPtr)
        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->'UInt64':
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.UInt64_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.UInt64_ParseSS.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt64_ParseSS, s,enumstyle)
#        ret = None if intPtr==None else UInt64(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->'UInt64':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt64_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.UInt64_ParseSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt64_ParseSP, s,intPtrprovider)
#        ret = None if intPtr==None else UInt64(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->'UInt64':
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt64_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.UInt64_ParseSSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt64_ParseSSP, s,enumstyle,intPtrprovider)
#        ret = None if intPtr==None else UInt64(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'UInt64&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.UInt64_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.UInt64_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.UInt64_TryParse, s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'UInt64&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.UInt64_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.UInt64_TryParseSSPR.restype=c_bool
#        ret = CallCFunction(dlllib.UInt64_TryParseSSPR, s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.UInt64_GetTypeCode.argtypes=[c_void_p]
#        dlllib.UInt64_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.UInt64_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod

    def MaxValue()->'UInt64':
        """

        """
        #dlllib.UInt64_MaxValue.argtypes=[]
        dlllib.UInt64_MaxValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt64_MaxValue)
        ret = None if intPtr==None else UInt64(intPtr)
        return ret


    @staticmethod

    def MinValue()->'UInt64':
        """

        """
        #dlllib.UInt64_MinValue.argtypes=[]
        dlllib.UInt64_MinValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt64_MinValue)
        ret = None if intPtr==None else UInt64(intPtr)
        return ret


