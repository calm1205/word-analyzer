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

class Double (SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        dlllib.Double_Create.restype = c_void_p
        intPtr = CallCFunction(dlllib.Double_Create)
        super(String, self).__init__(intPtr)
    @dispatch
    def __init__(self, value:float):
        dlllib.Double_CreateV.argtypes=[ c_double]
        dlllib.Double_CreateV.restype = c_void_p
        intPtr = CallCFunction(dlllib.Double_CreateV,value)
        super(Double, self).__init__(intPtr)

    @property
    def Value(self)->float:
        """

        """
        dlllib.Double_Value.argtypes=[ c_void_p]
        dlllib.Double_Value.restype=c_double
        ret = CallCFunction(dlllib.Double_Value, self.Ptr)
        return ret

    @staticmethod

    def IsInfinity(d:float)->bool:
        """

        """
        
        dlllib.Double_IsInfinity.argtypes=[ c_double]
        dlllib.Double_IsInfinity.restype=c_bool
        ret = CallCFunction(dlllib.Double_IsInfinity, d)
        return ret

    @staticmethod

    def IsPositiveInfinity(d:float)->bool:
        """

        """
        
        dlllib.Double_IsPositiveInfinity.argtypes=[ c_double]
        dlllib.Double_IsPositiveInfinity.restype=c_bool
        ret = CallCFunction(dlllib.Double_IsPositiveInfinity, d)
        return ret

    @staticmethod

    def IsNegativeInfinity(d:float)->bool:
        """

        """
        
        dlllib.Double_IsNegativeInfinity.argtypes=[ c_double]
        dlllib.Double_IsNegativeInfinity.restype=c_bool
        ret = CallCFunction(dlllib.Double_IsNegativeInfinity, d)
        return ret

    @staticmethod

    def IsNaN(d:float)->bool:
        """

        """
        
        dlllib.Double_IsNaN.argtypes=[ c_double]
        dlllib.Double_IsNaN.restype=c_bool
        ret = CallCFunction(dlllib.Double_IsNaN, d)
        return ret

    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Double_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Double_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.Double_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:float)->int:
        """

        """
        
        dlllib.Double_CompareToV.argtypes=[c_void_p ,c_double]
        dlllib.Double_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.Double_CompareToV,self.Ptr, value)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Double_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Double_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Double_Equals,self.Ptr, intPtrobj)
        return ret

    @staticmethod

    def op_Equality(left:float,right:float)->bool:
        """

        """
        
        dlllib.Double_op_Equality.argtypes=[ c_double,c_double]
        dlllib.Double_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.Double_op_Equality, left,right)
        return ret

    @staticmethod

    def op_Inequality(left:float,right:float)->bool:
        """

        """
        
        dlllib.Double_op_Inequality.argtypes=[ c_double,c_double]
        dlllib.Double_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.Double_op_Inequality, left,right)
        return ret

    @staticmethod

    def op_LessThan(left:float,right:float)->bool:
        """

        """
        
        dlllib.Double_op_LessThan.argtypes=[ c_double,c_double]
        dlllib.Double_op_LessThan.restype=c_bool
        ret = CallCFunction(dlllib.Double_op_LessThan, left,right)
        return ret

    @staticmethod

    def op_GreaterThan(left:float,right:float)->bool:
        """

        """
        
        dlllib.Double_op_GreaterThan.argtypes=[ c_double,c_double]
        dlllib.Double_op_GreaterThan.restype=c_bool
        ret = CallCFunction(dlllib.Double_op_GreaterThan, left,right)
        return ret

    @staticmethod

    def op_LessThanOrEqual(left:float,right:float)->bool:
        """

        """
        
        dlllib.Double_op_LessThanOrEqual.argtypes=[ c_double,c_double]
        dlllib.Double_op_LessThanOrEqual.restype=c_bool
        ret = CallCFunction(dlllib.Double_op_LessThanOrEqual, left,right)
        return ret

    @staticmethod

    def op_GreaterThanOrEqual(left:float,right:float)->bool:
        """

        """
        
        dlllib.Double_op_GreaterThanOrEqual.argtypes=[ c_double,c_double]
        dlllib.Double_op_GreaterThanOrEqual.restype=c_bool
        ret = CallCFunction(dlllib.Double_op_GreaterThanOrEqual, left,right)
        return ret

    @dispatch

    def Equals(self ,obj:float)->bool:
        """

        """
        
        dlllib.Double_EqualsO.argtypes=[c_void_p ,c_double]
        dlllib.Double_EqualsO.restype=c_bool
        ret = CallCFunction(dlllib.Double_EqualsO,self.Ptr, obj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Double_GetHashCode.argtypes=[c_void_p]
        dlllib.Double_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Double_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Double_ToString.argtypes=[c_void_p]
        dlllib.Double_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Double_ToString,self.Ptr))
        return ret


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        
        dlllib.Double_ToStringF.argtypes=[c_void_p ,c_void_p]
        dlllib.Double_ToStringF.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Double_ToStringF,self.Ptr, format))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Double_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Double_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Double_ToStringP,self.Ptr, intPtrprovider)
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
#        dlllib.Double_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.Double_ToStringFP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Double_ToStringFP,self.Ptr, format,intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def Parse(s:str)->float:
        """

        """
        
        dlllib.Double_Parse.argtypes=[ c_void_p]
        dlllib.Double_Parse.restype=c_double
        ret = CallCFunction(dlllib.Double_Parse, s)
        return ret

#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles')->float:
#        """
#
#        """
#        enumstyle:c_int = style.value
#
#        dlllib.Double_ParseSS.argtypes=[ c_void_p,c_int]
#        dlllib.Double_ParseSS.restype=c_double
#        ret = CallCFunction(dlllib.Double_ParseSS, s,enumstyle)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->float:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Double_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.Double_ParseSP.restype=c_double
#        ret = CallCFunction(dlllib.Double_ParseSP, s,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,style:'NumberStyles',provider:'IFormatProvider')->float:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Double_ParseSSP.argtypes=[ c_void_p,c_int,c_void_p]
#        dlllib.Double_ParseSSP.restype=c_double
#        ret = CallCFunction(dlllib.Double_ParseSSP, s,enumstyle,intPtrprovider)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'Double&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Double_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Double_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.Double_TryParse, s,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,style:'NumberStyles',provider:'IFormatProvider',result:'Double&')->bool:
#        """
#
#        """
#        enumstyle:c_int = style.value
#        intPtrprovider:c_void_p = provider.Ptr
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Double_TryParseSSPR.argtypes=[ c_void_p,c_int,c_void_p,c_void_p]
#        dlllib.Double_TryParseSSPR.restype=c_bool
#        ret = CallCFunction(dlllib.Double_TryParseSSPR, s,enumstyle,intPtrprovider,intPtrresult)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Double_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Double_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.Double_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod
    def MinValue()->float:
        """

        """
        #dlllib.Double_MinValue.argtypes=[]
        dlllib.Double_MinValue.restype=c_double
        ret = CallCFunction(dlllib.Double_MinValue)
        return ret

    @staticmethod
    def MaxValue()->float:
        """

        """
        #dlllib.Double_MaxValue.argtypes=[]
        dlllib.Double_MaxValue.restype=c_double
        ret = CallCFunction(dlllib.Double_MaxValue)
        return ret

    @staticmethod
    def Epsilon()->float:
        """

        """
        #dlllib.Double_Epsilon.argtypes=[]
        dlllib.Double_Epsilon.restype=c_double
        ret = CallCFunction(dlllib.Double_Epsilon)
        return ret

    @staticmethod
    def NegativeInfinity()->float:
        """

        """
        #dlllib.Double_NegativeInfinity.argtypes=[]
        dlllib.Double_NegativeInfinity.restype=c_double
        ret = CallCFunction(dlllib.Double_NegativeInfinity)
        return ret

    @staticmethod
    def PositiveInfinity()->float:
        """

        """
        #dlllib.Double_PositiveInfinity.argtypes=[]
        dlllib.Double_PositiveInfinity.restype=c_double
        ret = CallCFunction(dlllib.Double_PositiveInfinity)
        return ret

    @staticmethod
    def NaN()->float:
        """

        """
        #dlllib.Double_NaN.argtypes=[]
        dlllib.Double_NaN.restype=c_double
        ret = CallCFunction(dlllib.Double_NaN)
        return ret

