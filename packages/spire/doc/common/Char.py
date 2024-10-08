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

class Char (SpireObject) :
    """

    """
    def GetHashCode(self)->int:
        """

        """
        dlllib.Char_GetHashCode.argtypes=[c_void_p]
        dlllib.Char_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Char_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def Equals(self ,obj:SpireObject)->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Char_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Char_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Char_Equals,self.Ptr, intPtrobj)
        return ret

    @dispatch

    def Equals(self ,obj:int)->bool:
        """

        """
        
        dlllib.Char_EqualsO.argtypes=[c_void_p ,c_void_p]
        dlllib.Char_EqualsO.restype=c_bool
        ret = CallCFunction(dlllib.Char_EqualsO,self.Ptr, obj)
        return ret

    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Char_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.Char_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.Char_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:int)->int:
        """

        """
        
        dlllib.Char_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.Char_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.Char_CompareToV,self.Ptr, value)
        return ret

    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.Char_ToString.argtypes=[c_void_p]
        dlllib.Char_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Char_ToString,self.Ptr))
        return ret


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Char_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.Char_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Char_ToStringP,self.Ptr, intPtrprovider)
#        return ret
#


    @staticmethod
    @dispatch

    def ToString(c:int)->str:
        """

        """
        
        dlllib.Char_ToStringC.argtypes=[ c_void_p]
        dlllib.Char_ToStringC.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Char_ToStringC, c))
        return ret


    @staticmethod

    def Parse(s:str)->int:
        """

        """
        
        dlllib.Char_Parse.argtypes=[ c_void_p]
        dlllib.Char_Parse.restype=c_int
        ret = CallCFunction(dlllib.Char_Parse, s)
        return ret

#    @staticmethod
#
#    def TryParse(s:str,result:'Char&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.Char_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.Char_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.Char_TryParse, s,intPtrresult)
#        return ret


    @staticmethod
    @dispatch

    def IsDigit(c:int)->bool:
        """

        """
        
        dlllib.Char_IsDigit.argtypes=[ c_void_p]
        dlllib.Char_IsDigit.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsDigit, c)
        return ret

    @staticmethod
    @dispatch

    def IsLetter(c:int)->bool:
        """

        """
        
        dlllib.Char_IsLetter.argtypes=[ c_void_p]
        dlllib.Char_IsLetter.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLetter, c)
        return ret

    @staticmethod
    @dispatch

    def IsWhiteSpace(c:int)->bool:
        """

        """
        
        dlllib.Char_IsWhiteSpace.argtypes=[ c_void_p]
        dlllib.Char_IsWhiteSpace.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsWhiteSpace, c)
        return ret

    @staticmethod
    @dispatch

    def IsUpper(c:int)->bool:
        """

        """
        
        dlllib.Char_IsUpper.argtypes=[ c_void_p]
        dlllib.Char_IsUpper.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsUpper, c)
        return ret

    @staticmethod
    @dispatch

    def IsLower(c:int)->bool:
        """

        """
        
        dlllib.Char_IsLower.argtypes=[ c_void_p]
        dlllib.Char_IsLower.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLower, c)
        return ret

    @staticmethod
    @dispatch

    def IsPunctuation(c:int)->bool:
        """

        """
        
        dlllib.Char_IsPunctuation.argtypes=[ c_void_p]
        dlllib.Char_IsPunctuation.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsPunctuation, c)
        return ret

    @staticmethod
    @dispatch

    def IsLetterOrDigit(c:int)->bool:
        """

        """
        
        dlllib.Char_IsLetterOrDigit.argtypes=[ c_void_p]
        dlllib.Char_IsLetterOrDigit.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLetterOrDigit, c)
        return ret

    @staticmethod
    @dispatch

    def ToUpper(c:int,culture:CultureInfo)->int:
        """

        """
        intPtrculture:c_void_p = culture.Ptr

        dlllib.Char_ToUpper.argtypes=[ c_void_p,c_void_p]
        dlllib.Char_ToUpper.restype=c_int
        ret = CallCFunction(dlllib.Char_ToUpper, c,intPtrculture)
        return ret

    @staticmethod
    @dispatch

    def ToUpper(c:int)->int:
        """

        """
        
        dlllib.Char_ToUpperC.argtypes=[ c_void_p]
        dlllib.Char_ToUpperC.restype=c_int
        ret = CallCFunction(dlllib.Char_ToUpperC, c)
        return ret

    @staticmethod

    def ToUpperInvariant(c:int)->int:
        """

        """
        
        dlllib.Char_ToUpperInvariant.argtypes=[ c_void_p]
        dlllib.Char_ToUpperInvariant.restype=c_int
        ret = CallCFunction(dlllib.Char_ToUpperInvariant, c)
        return ret

    @staticmethod
    @dispatch

    def ToLower(c:int,culture:CultureInfo)->int:
        """

        """
        intPtrculture:c_void_p = culture.Ptr

        dlllib.Char_ToLower.argtypes=[ c_void_p,c_void_p]
        dlllib.Char_ToLower.restype=c_int
        ret = CallCFunction(dlllib.Char_ToLower, c,intPtrculture)
        return ret

    @staticmethod
    @dispatch

    def ToLower(c:int)->int:
        """

        """
        
        dlllib.Char_ToLowerC.argtypes=[ c_void_p]
        dlllib.Char_ToLowerC.restype=c_int
        ret = CallCFunction(dlllib.Char_ToLowerC, c)
        return ret

    @staticmethod

    def ToLowerInvariant(c:int)->int:
        """

        """
        
        dlllib.Char_ToLowerInvariant.argtypes=[ c_void_p]
        dlllib.Char_ToLowerInvariant.restype=c_int
        ret = CallCFunction(dlllib.Char_ToLowerInvariant, c)
        return ret

#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.Char_GetTypeCode.argtypes=[c_void_p]
#        dlllib.Char_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.Char_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


    @staticmethod
    @dispatch

    def IsControl(c:int)->bool:
        """

        """
        
        dlllib.Char_IsControl.argtypes=[ c_void_p]
        dlllib.Char_IsControl.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsControl, c)
        return ret

    @staticmethod
    @dispatch

    def IsControl(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsControlSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsControlSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsControlSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsDigit(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsDigitSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsDigitSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsDigitSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsLetter(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsLetterSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsLetterSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLetterSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsLetterOrDigit(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsLetterOrDigitSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsLetterOrDigitSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLetterOrDigitSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsLower(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsLowerSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsLowerSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLowerSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsNumber(c:int)->bool:
        """

        """
        
        dlllib.Char_IsNumber.argtypes=[ c_void_p]
        dlllib.Char_IsNumber.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsNumber, c)
        return ret

    @staticmethod
    @dispatch

    def IsNumber(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsNumberSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsNumberSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsNumberSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsPunctuation(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsPunctuationSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsPunctuationSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsPunctuationSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsSeparator(c:int)->bool:
        """

        """
        
        dlllib.Char_IsSeparator.argtypes=[ c_void_p]
        dlllib.Char_IsSeparator.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSeparator, c)
        return ret

    @staticmethod
    @dispatch

    def IsSeparator(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsSeparatorSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsSeparatorSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSeparatorSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsSurrogate(c:int)->bool:
        """

        """
        
        dlllib.Char_IsSurrogate.argtypes=[ c_void_p]
        dlllib.Char_IsSurrogate.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSurrogate, c)
        return ret

    @staticmethod
    @dispatch

    def IsSurrogate(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsSurrogateSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsSurrogateSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSurrogateSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsSymbol(c:int)->bool:
        """

        """
        
        dlllib.Char_IsSymbol.argtypes=[ c_void_p]
        dlllib.Char_IsSymbol.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSymbol, c)
        return ret

    @staticmethod
    @dispatch

    def IsSymbol(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsSymbolSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsSymbolSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSymbolSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsUpper(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsUpperSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsUpperSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsUpperSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsWhiteSpace(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsWhiteSpaceSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsWhiteSpaceSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsWhiteSpaceSI, s,index)
        return ret

#    @staticmethod
#    @dispatch
#
#    def GetUnicodeCategory(c:int)->UnicodeCategory:
#        """
#
#        """
#        
#        dlllib.Char_GetUnicodeCategory.argtypes=[ c_void_p]
#        dlllib.Char_GetUnicodeCategory.restype=c_int
#        ret = CallCFunction(dlllib.Char_GetUnicodeCategory, c)
#        objwraped = UnicodeCategory(ret)
#        return objwraped


#    @staticmethod
#    @dispatch
#
#    def GetUnicodeCategory(s:str,index:int)->UnicodeCategory:
#        """
#
#        """
#        
#        dlllib.Char_GetUnicodeCategorySI.argtypes=[ c_void_p,c_int]
#        dlllib.Char_GetUnicodeCategorySI.restype=c_int
#        ret = CallCFunction(dlllib.Char_GetUnicodeCategorySI, s,index)
#        objwraped = UnicodeCategory(ret)
#        return objwraped


    @staticmethod
    @dispatch

    def GetNumericValue(c:int)->float:
        """

        """
        
        dlllib.Char_GetNumericValue.argtypes=[ c_void_p]
        dlllib.Char_GetNumericValue.restype=c_double
        ret = CallCFunction(dlllib.Char_GetNumericValue, c)
        return ret

    @staticmethod
    @dispatch

    def GetNumericValue(s:str,index:int)->float:
        """

        """
        
        dlllib.Char_GetNumericValueSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_GetNumericValueSI.restype=c_double
        ret = CallCFunction(dlllib.Char_GetNumericValueSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsHighSurrogate(c:int)->bool:
        """

        """
        
        dlllib.Char_IsHighSurrogate.argtypes=[ c_void_p]
        dlllib.Char_IsHighSurrogate.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsHighSurrogate, c)
        return ret

    @staticmethod
    @dispatch

    def IsHighSurrogate(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsHighSurrogateSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsHighSurrogateSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsHighSurrogateSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsLowSurrogate(c:int)->bool:
        """

        """
        
        dlllib.Char_IsLowSurrogate.argtypes=[ c_void_p]
        dlllib.Char_IsLowSurrogate.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLowSurrogate, c)
        return ret

    @staticmethod
    @dispatch

    def IsLowSurrogate(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsLowSurrogateSI.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsLowSurrogateSI.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsLowSurrogateSI, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsSurrogatePair(s:str,index:int)->bool:
        """

        """
        
        dlllib.Char_IsSurrogatePair.argtypes=[ c_void_p,c_int]
        dlllib.Char_IsSurrogatePair.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSurrogatePair, s,index)
        return ret

    @staticmethod
    @dispatch

    def IsSurrogatePair(highSurrogate:int,lowSurrogate:int)->bool:
        """

        """
        
        dlllib.Char_IsSurrogatePairHL.argtypes=[ c_void_p,c_void_p]
        dlllib.Char_IsSurrogatePairHL.restype=c_bool
        ret = CallCFunction(dlllib.Char_IsSurrogatePairHL, highSurrogate,lowSurrogate)
        return ret

    @staticmethod

    def ConvertFromUtf32(utf32:int)->str:
        """

        """
        
        dlllib.Char_ConvertFromUtf32.argtypes=[ c_int]
        dlllib.Char_ConvertFromUtf32.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Char_ConvertFromUtf32, utf32))
        return ret


    @staticmethod
    @dispatch

    def ConvertToUtf32(highSurrogate:int,lowSurrogate:int)->int:
        """

        """
        
        dlllib.Char_ConvertToUtf32.argtypes=[ c_void_p,c_void_p]
        dlllib.Char_ConvertToUtf32.restype=c_int
        ret = CallCFunction(dlllib.Char_ConvertToUtf32, highSurrogate,lowSurrogate)
        return ret

    @staticmethod
    @dispatch

    def ConvertToUtf32(s:str,index:int)->int:
        """

        """
        
        dlllib.Char_ConvertToUtf32SI.argtypes=[ c_void_p,c_int]
        dlllib.Char_ConvertToUtf32SI.restype=c_int
        ret = CallCFunction(dlllib.Char_ConvertToUtf32SI, s,index)
        return ret

    @staticmethod
    def MaxValue()->int:
        """

        """
        #dlllib.Char_MaxValue.argtypes=[]
        dlllib.Char_MaxValue.restype=c_int
        ret = CallCFunction(dlllib.Char_MaxValue)
        return ret

    @staticmethod
    def MinValue()->int:
        """

        """
        #dlllib.Char_MinValue.argtypes=[]
        dlllib.Char_MinValue.restype=c_int
        ret = CallCFunction(dlllib.Char_MinValue)
        return ret

