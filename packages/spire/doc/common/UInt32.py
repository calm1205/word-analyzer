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

class UInt32 (SpireObject) :
    """

    """
    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.UInt32_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt32_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.UInt32_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:'UInt32')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.UInt32_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt32_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.UInt32_CompareToV,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.UInt32_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt32_Equals.restype=c_bool
        ret = CallCFunction(dlllib.UInt32_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:'UInt32')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.UInt32_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt32_EqualsO.restype=c_bool
        ret = CallCFunction(dlllib.UInt32_EqualsO,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.UInt32_GetHashCode.argtypes=[c_void_p]
        dlllib.UInt32_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.UInt32_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.UInt32_ToString.argtypes=[c_void_p]
        dlllib.UInt32_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.UInt32_ToString,self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt32_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.UInt32_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.UInt32_ToStringP,self.Ptr, intPtrprovider)
#        return ret
#


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.UInt32_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt32_ToStringF.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.UInt32_ToStringF,self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt32_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.UInt32_ToStringFP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.UInt32_ToStringFP,self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->'UInt32':
        """

        """
        
        dlllib.UInt32_Parse.argtypes=[ c_void_p]
        dlllib.UInt32_Parse.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt32_Parse, s)
        ret = None if intPtr==None else UInt32(intPtr)
        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->'UInt32':
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.UInt32_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.UInt32_ParseSS.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt32_ParseSS, s,enumstyle)
#        ret = None if intPtr==None else UInt32(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->'UInt32':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt32_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.UInt32_ParseSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt32_ParseSP, s,intPtrprovider)
#        ret = None if intPtr==None else UInt32(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->'UInt32':
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt32_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.UInt32_ParseSSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt32_ParseSSP, s,enumstyle,intPtrprovider)
#        ret = None if intPtr==None else UInt32(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'UInt32&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.UInt32_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.UInt32_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.UInt32_TryParse, s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'UInt32&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.UInt32_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.UInt32_TryParseSSPR.restype=c_bool
#        ret = CallCFunction(dlllib.UInt32_TryParseSSPR, s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.UInt32_GetTypeCode.argtypes=[c_void_p]
#        dlllib.UInt32_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.UInt32_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod

    def MaxValue()->'UInt32':
        """

        """
        #dlllib.UInt32_MaxValue.argtypes=[]
        dlllib.UInt32_MaxValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt32_MaxValue)
        ret = None if intPtr==None else UInt32(intPtr)
        return ret


    @staticmethod

    def MinValue()->'UInt32':
        """

        """
        #dlllib.UInt32_MinValue.argtypes=[]
        dlllib.UInt32_MinValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt32_MinValue)
        ret = None if intPtr==None else UInt32(intPtr)
        return ret


