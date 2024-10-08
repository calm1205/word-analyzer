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

class Byte (SpireObject) :
    """

    """
    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Byte_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Byte_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.Byte_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:int)->int:
        """

        """
        
        dlllib.Byte_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.Byte_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.Byte_CompareToV,self.Ptr, value)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Byte_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Byte_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Byte_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:int)->bool:
        """

        """
        
        dlllib.Byte_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.Byte_EqualsO.restype=c_bool
        ret = CallCFunction(dlllib.Byte_EqualsO,self.Ptr, obj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Byte_GetHashCode.argtypes=[c_void_p]
        dlllib.Byte_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Byte_GetHashCode,self.Ptr)
        return ret

    @staticmethod
    @dispatch

    def Parse(s:str)->int:
        """

        """
        
        dlllib.Byte_Parse.argtypes=[ c_void_p]
        dlllib.Byte_Parse.restype=c_int
        ret = CallCFunction(dlllib.Byte_Parse, s)
        return ret

#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->int:
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.Byte_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.Byte_ParseSS.restype=c_int
#        ret = CallCFunction(dlllib.Byte_ParseSS, s,enumstyle)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->int:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Byte_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.Byte_ParseSP.restype=c_int
#        ret = CallCFunction(dlllib.Byte_ParseSP, s,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->int:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Byte_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.Byte_ParseSSP.restype=c_int
#        ret = CallCFunction(dlllib.Byte_ParseSSP, s,enumstyle,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'Byte&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Byte_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Byte_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.Byte_TryParse, s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'Byte&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Byte_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.Byte_TryParseSSPR.restype=c_bool
#        ret = CallCFunction(dlllib.Byte_TryParseSSPR, s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Byte_ToString.argtypes=[c_void_p]
        dlllib.Byte_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Byte_ToString,self.Ptr))
        return ret


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.Byte_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.Byte_ToStringF.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Byte_ToStringF,self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Byte_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Byte_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Byte_ToStringP,self.Ptr, intPtrprovider)
#        return ret
#


#    @dispatch
#
#    def ToString(self ,format:str,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Byte_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Byte_ToStringFP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Byte_ToStringFP,self.Ptr, format,intPtrprovider)
#        return ret
#


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Byte_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Byte_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.Byte_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod
    def MaxValue()->int:
        """

        """
        #dlllib.Byte_MaxValue.argtypes=[]
        dlllib.Byte_MaxValue.restype=c_int
        ret = CallCFunction(dlllib.Byte_MaxValue)
        return ret

    @staticmethod
    def MinValue()->int:
        """

        """
        #dlllib.Byte_MinValue.argtypes=[]
        dlllib.Byte_MinValue.restype=c_int
        ret = CallCFunction(dlllib.Byte_MinValue)
        return ret

