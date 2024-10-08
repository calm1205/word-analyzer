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

class UInt16 (SpireObject) :
    """

    """
    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.UInt16_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt16_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.UInt16_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:'UInt16')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.UInt16_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt16_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.UInt16_CompareToV,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.UInt16_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt16_Equals.restype=c_bool
        ret = CallCFunction(dlllib.UInt16_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:'UInt16')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.UInt16_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt16_EqualsO.restype=c_bool
        ret = CallCFunction(dlllib.UInt16_EqualsO,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.UInt16_GetHashCode.argtypes=[c_void_p]
        dlllib.UInt16_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.UInt16_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.UInt16_ToString.argtypes=[c_void_p]
        dlllib.UInt16_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.UInt16_ToString,self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt16_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.UInt16_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.UInt16_ToStringP,self.Ptr, intPtrprovider)
#        return ret
#


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.UInt16_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.UInt16_ToStringF.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.UInt16_ToStringF,self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt16_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.UInt16_ToStringFP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.UInt16_ToStringFP,self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->'UInt16':
        """

        """
        
        dlllib.UInt16_Parse.argtypes=[ c_void_p]
        dlllib.UInt16_Parse.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt16_Parse, s)
        ret = None if intPtr==None else UInt16(intPtr)
        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->'UInt16':
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.UInt16_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.UInt16_ParseSS.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt16_ParseSS, s,enumstyle)
#        ret = None if intPtr==None else UInt16(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->'UInt16':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt16_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.UInt16_ParseSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt16_ParseSP, s,intPtrprovider)
#        ret = None if intPtr==None else UInt16(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->'UInt16':
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.UInt16_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.UInt16_ParseSSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.UInt16_ParseSSP, s,enumstyle,intPtrprovider)
#        ret = None if intPtr==None else UInt16(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'UInt16&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.UInt16_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.UInt16_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.UInt16_TryParse, s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'UInt16&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.UInt16_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.UInt16_TryParseSSPR.restype=c_bool
#        ret = CallCFunction(dlllib.UInt16_TryParseSSPR, s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.UInt16_GetTypeCode.argtypes=[c_void_p]
#        dlllib.UInt16_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.UInt16_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod

    def MaxValue()->'UInt16':
        """

        """
        #dlllib.UInt16_MaxValue.argtypes=[]
        dlllib.UInt16_MaxValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt16_MaxValue)
        ret = None if intPtr==None else UInt16(intPtr)
        return ret


    @staticmethod

    def MinValue()->'UInt16':
        """

        """
        #dlllib.UInt16_MinValue.argtypes=[]
        dlllib.UInt16_MinValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.UInt16_MinValue)
        ret = None if intPtr==None else UInt16(intPtr)
        return ret


