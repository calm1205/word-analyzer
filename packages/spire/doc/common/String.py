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

class String (  SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        dlllib.String_Create.restype = c_void_p
        intPtr = CallCFunction(dlllib.String_Create)
        super(String, self).__init__(intPtr)
    @dispatch
    def __init__(self, value:str):
        if __package__ == "spire.presentation.common":
            valuePtr = StrToPtr(value)
            dlllib.String_CreateV.argtypes=[ c_void_p]
            dlllib.String_CreateV.restype = c_void_p
            intPtr = CallCFunction(dlllib.String_CreateV,valuePtr)
            super(String, self).__init__(intPtr)
        else:
            dlllib.String_CreateV.argtypes=[ c_wchar_p]
            dlllib.String_CreateV.restype = c_void_p
            intPtr = CallCFunction(dlllib.String_CreateV,value)
            super(String, self).__init__(intPtr)

    def __str__(self):
        return self.Value

    @property
    def Value(self)->str:
        """

        """
        dlllib.String_Value.argtypes=[ c_void_p]
        dlllib.String_Value.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.String_Value, self.Ptr))
        return ret

#    @staticmethod
#    @dispatch

#    def Join(separator:str,value:List[str])->str:
#        """

#        """
#        #arrayvalue:ArrayTypevalue = ""
#        countvalue = len(value)
#        ArrayTypevalue = c_wchar_p * countvalue
#        arrayvalue = ArrayTypevalue()
#        for i in range(0, countvalue):
#            arrayvalue[i] = value[i]


#        dlllib.String_Join.argtypes=[ c_void_p,ArrayTypevalue,c_int]
#        dlllib.String_Join.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Join, separator,arrayvalue,countvalue)
#        return ret


#    @staticmethod
#    @dispatch

#    def Join(separator:str,values:List[SpireObject])->str:
#        """

#        """
#        #arrayvalues:ArrayTypevalues = ""
#        countvalues = len(values)
#        ArrayTypevalues = c_void_p * countvalues
#        arrayvalues = ArrayTypevalues()
#        for i in range(0, countvalues):
#            arrayvalues[i] = values[i].Ptr


#        dlllib.String_JoinSV.argtypes=[ c_void_p,ArrayTypevalues,c_int]
#        dlllib.String_JoinSV.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_JoinSV, separator,arrayvalues,countvalue)
#        return ret


##    @staticmethod
##    @dispatch
##
##    def Join(separator:str,values:'IEnumerable1')->str:
##        """
##
##        """
##        intPtrvalues:c_void_p = values.Ptr
##
##        dlllib.String_JoinSV1.argtypes=[ c_void_p,c_void_p]
##        dlllib.String_JoinSV1.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_JoinSV1, separator,intPtrvalues)
##        return ret
##


#    @staticmethod
#    @dispatch

#    def Join(separator:str,value:List[str],startIndex:int,count:int)->str:
#        """

#        """
#        #arrayvalue:ArrayTypevalue = ""
#        countvalue = len(value)
#        ArrayTypevalue = c_wchar_p * countvalue
#        arrayvalue = ArrayTypevalue()
#        for i in range(0, countvalue):
#            arrayvalue[i] = value[i]


#        dlllib.String_JoinSVSC.argtypes=[ c_void_p,ArrayTypevalue,c_int,c_int,c_int]
#        dlllib.String_JoinSVSC.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_JoinSVSC, separator,arrayvalue,startIndex,count,countvalue)
#        return ret


#    @dispatch

#    def Equals(self ,obj:SpireObject)->bool:
#        """

#        """
#        intPtrobj:c_void_p = obj.Ptr

#        dlllib.String_Equals.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_Equals.restype=c_bool
#        ret = CallCFunction(dlllib.String_Equals,self.Ptr, intPtrobj)
#        return ret

#    @dispatch

#    def Equals(self ,value:str)->bool:
#        """

#        """
        
#        dlllib.String_EqualsV.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_EqualsV.restype=c_bool
#        ret = CallCFunction(dlllib.String_EqualsV,self.Ptr, value)
#        return ret

##    @dispatch
##
##    def Equals(self ,value:str,comparisonType:'StringComparison')->bool:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_EqualsVC.argtypes=[c_void_p ,c_void_p,c_int]
##        dlllib.String_EqualsVC.restype=c_bool
##        ret = CallCFunction(dlllib.String_EqualsVC,self.Ptr, value,enumcomparisonType)
##        return ret


#    @staticmethod
#    @dispatch

#    def Equals(a:str,b:str)->bool:
#        """

#        """
        
#        dlllib.String_EqualsAB.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_EqualsAB.restype=c_bool
#        ret = CallCFunction(dlllib.String_EqualsAB, a,b)
#        return ret

##    @staticmethod
##    @dispatch
##
##    def Equals(a:str,b:str,comparisonType:'StringComparison')->bool:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_EqualsABC.argtypes=[ c_void_p,c_void_p,c_int]
##        dlllib.String_EqualsABC.restype=c_bool
##        ret = CallCFunction(dlllib.String_EqualsABC, a,b,enumcomparisonType)
##        return ret


#    @staticmethod

#    def op_Equality(a:str,b:str)->bool:
#        """

#        """
        
#        dlllib.String_op_Equality.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_op_Equality.restype=c_bool
#        ret = CallCFunction(dlllib.String_op_Equality, a,b)
#        return ret

#    @staticmethod

#    def op_Inequality(a:str,b:str)->bool:
#        """

#        """
        
#        dlllib.String_op_Inequality.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_op_Inequality.restype=c_bool
#        ret = CallCFunction(dlllib.String_op_Inequality, a,b)
#        return ret

##
##    def CopyTo(self ,sourceIndex:int,destination:'Char[]',destinationIndex:int,count:int):
##        """
##
##        """
##        #arraydestination:ArrayTypedestination = ""
##        countdestination = len(destination)
##        ArrayTypedestination = c_void_p * countdestination
##        arraydestination = ArrayTypedestination()
##        for i in range(0, countdestination):
##            arraydestination[i] = destination[i].Ptr
##
##
##        dlllib.String_CopyTo.argtypes=[c_void_p ,c_int,ArrayTypedestination,c_int,c_int]
##        CallCFunction(dlllib.String_CopyTo,self.Ptr, sourceIndex,arraydestination,destinationIndex,count)


##    @dispatch
##
##    def ToCharArray(self)->List[Char]:
##        """
##
##        """
##        dlllib.String_ToCharArray.argtypes=[c_void_p]
##        dlllib.String_ToCharArray.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_ToCharArray,self.Ptr)
##        ret = GetVectorFromArray(intPtrArray, Char)
##        return ret


##    @dispatch
##
##    def ToCharArray(self ,startIndex:int,length:int)->List[Char]:
##        """
##
##        """
##        
##        dlllib.String_ToCharArraySL.argtypes=[c_void_p ,c_int,c_int]
##        dlllib.String_ToCharArraySL.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_ToCharArraySL,self.Ptr, startIndex,length)
##        ret = GetObjVectorFromArray(intPtrArray, Char)
##        return ret


#    @staticmethod

#    def IsNullOrEmpty(value:str)->bool:
#        """

#        """
        
#        dlllib.String_IsNullOrEmpty.argtypes=[ c_void_p]
#        dlllib.String_IsNullOrEmpty.restype=c_bool
#        ret = CallCFunction(dlllib.String_IsNullOrEmpty, value)
#        return ret

#    @staticmethod

#    def IsNullOrWhiteSpace(value:str)->bool:
#        """

#        """
        
#        dlllib.String_IsNullOrWhiteSpace.argtypes=[ c_void_p]
#        dlllib.String_IsNullOrWhiteSpace.restype=c_bool
#        ret = CallCFunction(dlllib.String_IsNullOrWhiteSpace, value)
#        return ret

#    def GetHashCode(self)->int:
#        """

#        """
#        dlllib.String_GetHashCode.argtypes=[c_void_p]
#        dlllib.String_GetHashCode.restype=c_int
#        ret = CallCFunction(dlllib.String_GetHashCode,self.Ptr)
#        return ret

##    @dispatch
##
##    def Split(self ,separator:'Char[]')->List[str]:
##        """
##
##        """
##        #arrayseparator:ArrayTypeseparator = ""
##        countseparator = len(separator)
##        ArrayTypeseparator = c_void_p * countseparator
##        arrayseparator = ArrayTypeseparator()
##        for i in range(0, countseparator):
##            arrayseparator[i] = separator[i].Ptr
##
##
##        dlllib.String_Split.argtypes=[c_void_p ,ArrayTypeseparator]
##        dlllib.String_Split.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_Split,self.Ptr, arrayseparator)
##        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
##        return ret


##    @dispatch
##
##    def Split(self ,separator:'Char[]',count:int)->List[str]:
##        """
##
##        """
##        #arrayseparator:ArrayTypeseparator = ""
##        countseparator = len(separator)
##        ArrayTypeseparator = c_void_p * countseparator
##        arrayseparator = ArrayTypeseparator()
##        for i in range(0, countseparator):
##            arrayseparator[i] = separator[i].Ptr
##
##
##        dlllib.String_SplitSC.argtypes=[c_void_p ,ArrayTypeseparator,c_int]
##        dlllib.String_SplitSC.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_SplitSC,self.Ptr, arrayseparator,count)
##        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
##        return ret


##    @dispatch
##
##    def Split(self ,separator:'Char[]',options:'StringSplitOptions')->List[str]:
##        """
##
##        """
##        #arrayseparator:ArrayTypeseparator = ""
##        countseparator = len(separator)
##        ArrayTypeseparator = c_void_p * countseparator
##        arrayseparator = ArrayTypeseparator()
##        for i in range(0, countseparator):
##            arrayseparator[i] = separator[i].Ptr
##
##        enumoptions:c_int = options.value
##
##        dlllib.String_SplitSO.argtypes=[c_void_p ,ArrayTypeseparator,c_int]
##        dlllib.String_SplitSO.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_SplitSO,self.Ptr, arrayseparator,enumoptions)
##        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
##        return ret


##    @dispatch
##
##    def Split(self ,separator:'Char[]',count:int,options:'StringSplitOptions')->List[str]:
##        """
##
##        """
##        #arrayseparator:ArrayTypeseparator = ""
##        countseparator = len(separator)
##        ArrayTypeseparator = c_void_p * countseparator
##        arrayseparator = ArrayTypeseparator()
##        for i in range(0, countseparator):
##            arrayseparator[i] = separator[i].Ptr
##
##        enumoptions:c_int = options.value
##
##        dlllib.String_SplitSCO.argtypes=[c_void_p ,ArrayTypeseparator,c_int,c_int]
##        dlllib.String_SplitSCO.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_SplitSCO,self.Ptr, arrayseparator,count,enumoptions)
##        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
##        return ret


##    @dispatch
##
##    def Split(self ,separator:List[str],options:'StringSplitOptions')->List[str]:
##        """
##
##        """
##        #arrayseparator:ArrayTypeseparator = ""
##        countseparator = len(separator)
##        ArrayTypeseparator = c_wchar_p * countseparator
##        arrayseparator = ArrayTypeseparator()
##        for i in range(0, countseparator):
##            arrayseparator[i] = separator[i]
##
##        enumoptions:c_int = options.value
##
##        dlllib.String_SplitSO1.argtypes=[c_void_p ,ArrayTypeseparator,c_int]
##        dlllib.String_SplitSO1.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_SplitSO1,self.Ptr, arrayseparator,enumoptions)
##        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
##        return ret


##    @dispatch
##
##    def Split(self ,separator:List[str],count:int,options:'StringSplitOptions')->List[str]:
##        """
##
##        """
##        #arrayseparator:ArrayTypeseparator = ""
##        countseparator = len(separator)
##        ArrayTypeseparator = c_wchar_p * countseparator
##        arrayseparator = ArrayTypeseparator()
##        for i in range(0, countseparator):
##            arrayseparator[i] = separator[i]
##
##        enumoptions:c_int = options.value
##
##        dlllib.String_SplitSCO1.argtypes=[c_void_p ,ArrayTypeseparator,c_int,c_int]
##        dlllib.String_SplitSCO1.restype=IntPtrArray
##        intPtrArray = CallCFunction(dlllib.String_SplitSCO1,self.Ptr, arrayseparator,count,enumoptions)
##        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
##        return ret


#    @dispatch

#    def Substring(self ,startIndex:int)->str:
#        """

#        """
        
#        dlllib.String_Substring.argtypes=[c_void_p ,c_int]
#        dlllib.String_Substring.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Substring,self.Ptr, startIndex)
#        return ret


#    @dispatch

#    def Substring(self ,startIndex:int,length:int)->str:
#        """

#        """
        
#        dlllib.String_SubstringSL.argtypes=[c_void_p ,c_int,c_int]
#        dlllib.String_SubstringSL.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_SubstringSL,self.Ptr, startIndex,length)
#        return ret


##    @dispatch
##
##    def Trim(self ,trimChars:'Char[]')->str:
##        """
##
##        """
##        #arraytrimChars:ArrayTypetrimChars = ""
##        counttrimChars = len(trimChars)
##        ArrayTypetrimChars = c_void_p * counttrimChars
##        arraytrimChars = ArrayTypetrimChars()
##        for i in range(0, counttrimChars):
##            arraytrimChars[i] = trimChars[i].Ptr
##
##
##        dlllib.String_Trim.argtypes=[c_void_p ,ArrayTypetrimChars]
##        dlllib.String_Trim.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_Trim,self.Ptr, arraytrimChars)
##        return ret
##


##
##    def TrimStart(self ,trimChars:'Char[]')->str:
##        """
##
##        """
##        #arraytrimChars:ArrayTypetrimChars = ""
##        counttrimChars = len(trimChars)
##        ArrayTypetrimChars = c_void_p * counttrimChars
##        arraytrimChars = ArrayTypetrimChars()
##        for i in range(0, counttrimChars):
##            arraytrimChars[i] = trimChars[i].Ptr
##
##
##        dlllib.String_TrimStart.argtypes=[c_void_p ,ArrayTypetrimChars]
##        dlllib.String_TrimStart.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_TrimStart,self.Ptr, arraytrimChars)
##        return ret
##


##
##    def TrimEnd(self ,trimChars:'Char[]')->str:
##        """
##
##        """
##        #arraytrimChars:ArrayTypetrimChars = ""
##        counttrimChars = len(trimChars)
##        ArrayTypetrimChars = c_void_p * counttrimChars
##        arraytrimChars = ArrayTypetrimChars()
##        for i in range(0, counttrimChars):
##            arraytrimChars[i] = trimChars[i].Ptr
##
##
##        dlllib.String_TrimEnd.argtypes=[c_void_p ,ArrayTypetrimChars]
##        dlllib.String_TrimEnd.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_TrimEnd,self.Ptr, arraytrimChars)
##        return ret
##


#    @dispatch
#    def IsNormalized(self)->bool:
#        """

#        """
#        dlllib.String_IsNormalized.argtypes=[c_void_p]
#        dlllib.String_IsNormalized.restype=c_bool
#        ret = CallCFunction(dlllib.String_IsNormalized,self.Ptr)
#        return ret

##    @dispatch
##
##    def IsNormalized(self ,normalizationForm:'NormalizationForm')->bool:
##        """
##
##        """
##        enumnormalizationForm:c_int = normalizationForm.value
##
##        dlllib.String_IsNormalizedN.argtypes=[c_void_p ,c_int]
##        dlllib.String_IsNormalizedN.restype=c_bool
##        ret = CallCFunction(dlllib.String_IsNormalizedN,self.Ptr, enumnormalizationForm)
##        return ret


#    @dispatch

#    def Normalize(self)->str:
#        """

#        """
#        dlllib.String_Normalize.argtypes=[c_void_p]
#        dlllib.String_Normalize.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Normalize,self.Ptr)
#        return ret


##    @dispatch
##
##    def Normalize(self ,normalizationForm:'NormalizationForm')->str:
##        """
##
##        """
##        enumnormalizationForm:c_int = normalizationForm.value
##
##        dlllib.String_NormalizeN.argtypes=[c_void_p ,c_int]
##        dlllib.String_NormalizeN.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_NormalizeN,self.Ptr, enumnormalizationForm)
##        return ret
##


#    @staticmethod
#    @dispatch

#    def Compare(strA:str,strB:str)->int:
#        """

#        """
        
#        dlllib.String_Compare.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_Compare.restype=c_int
#        ret = CallCFunction(dlllib.String_Compare, strA,strB)
#        return ret

#    @staticmethod
#    @dispatch

#    def Compare(strA:str,strB:str,ignoreCase:bool)->int:
#        """

#        """
        
#        dlllib.String_CompareSSI.argtypes=[ c_void_p,c_void_p,c_bool]
#        dlllib.String_CompareSSI.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareSSI, strA,strB,ignoreCase)
#        return ret

##    @staticmethod
##    @dispatch
##
##    def Compare(strA:str,strB:str,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_CompareSSC.argtypes=[ c_void_p,c_void_p,c_int]
##        dlllib.String_CompareSSC.restype=c_int
##        ret = CallCFunction(dlllib.String_CompareSSC, strA,strB,enumcomparisonType)
##        return ret


##    @staticmethod
##    @dispatch
##
##    def Compare(strA:str,strB:str,culture:CultureInfo,options:'CompareOptions')->int:
##        """
##
##        """
##        intPtrculture:c_void_p = culture.Ptr
##        enumoptions:c_int = options.value
##
##        dlllib.String_CompareSSCO.argtypes=[ c_void_p,c_void_p,c_void_p,c_int]
##        dlllib.String_CompareSSCO.restype=c_int
##        ret = CallCFunction(dlllib.String_CompareSSCO, strA,strB,intPtrculture,enumoptions)
##        return ret


#    @staticmethod
#    @dispatch

#    def Compare(strA:str,strB:str,ignoreCase:bool,culture:CultureInfo)->int:
#        """

#        """
#        intPtrculture:c_void_p = culture.Ptr

#        dlllib.String_CompareSSIC.argtypes=[ c_void_p,c_void_p,c_bool,c_void_p]
#        dlllib.String_CompareSSIC.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareSSIC, strA,strB,ignoreCase,intPtrculture)
#        return ret

#    @staticmethod
#    @dispatch

#    def Compare(strA:str,indexA:int,strB:str,indexB:int,length:int)->int:
#        """

#        """
        
#        dlllib.String_CompareSISIL.argtypes=[ c_void_p,c_int,c_void_p,c_int,c_int]
#        dlllib.String_CompareSISIL.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareSISIL, strA,indexA,strB,indexB,length)
#        return ret

#    @staticmethod
#    @dispatch

#    def Compare(strA:str,indexA:int,strB:str,indexB:int,length:int,ignoreCase:bool)->int:
#        """

#        """
        
#        dlllib.String_CompareSISILI.argtypes=[ c_void_p,c_int,c_void_p,c_int,c_int,c_bool]
#        dlllib.String_CompareSISILI.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareSISILI, strA,indexA,strB,indexB,length,ignoreCase)
#        return ret

#    @staticmethod
#    @dispatch

#    def Compare(strA:str,indexA:int,strB:str,indexB:int,length:int,ignoreCase:bool,culture:CultureInfo)->int:
#        """

#        """
#        intPtrculture:c_void_p = culture.Ptr

#        dlllib.String_CompareSISILIC.argtypes=[ c_void_p,c_int,c_void_p,c_int,c_int,c_bool,c_void_p]
#        dlllib.String_CompareSISILIC.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareSISILIC, strA,indexA,strB,indexB,length,ignoreCase,intPtrculture)
#        return ret

##    @staticmethod
##    @dispatch
##
##    def Compare(strA:str,indexA:int,strB:str,indexB:int,length:int,culture:CultureInfo,options:'CompareOptions')->int:
##        """
##
##        """
##        intPtrculture:c_void_p = culture.Ptr
##        enumoptions:c_int = options.value
##
##        dlllib.String_CompareSISILCO.argtypes=[ c_void_p,c_int,c_void_p,c_int,c_int,c_void_p,c_int]
##        dlllib.String_CompareSISILCO.restype=c_int
##        ret = CallCFunction(dlllib.String_CompareSISILCO, strA,indexA,strB,indexB,length,intPtrculture,enumoptions)
##        return ret


##    @staticmethod
##    @dispatch
##
##    def Compare(strA:str,indexA:int,strB:str,indexB:int,length:int,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_CompareSISILC.argtypes=[ c_void_p,c_int,c_void_p,c_int,c_int,c_int]
##        dlllib.String_CompareSISILC.restype=c_int
##        ret = CallCFunction(dlllib.String_CompareSISILC, strA,indexA,strB,indexB,length,enumcomparisonType)
##        return ret


#    @dispatch

#    def CompareTo(self ,value:SpireObject)->int:
#        """

#        """
#        intPtrvalue:c_void_p = value.Ptr

#        dlllib.String_CompareTo.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_CompareTo.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareTo,self.Ptr, intPtrvalue)
#        return ret

#    @dispatch

#    def CompareTo(self ,strB:str)->int:
#        """

#        """
        
#        dlllib.String_CompareToS.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_CompareToS.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareToS,self.Ptr, strB)
#        return ret

#    @staticmethod
#    @dispatch

#    def CompareOrdinal(strA:str,strB:str)->int:
#        """

#        """
        
#        dlllib.String_CompareOrdinal.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_CompareOrdinal.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareOrdinal, strA,strB)
#        return ret

#    @staticmethod
#    @dispatch

#    def CompareOrdinal(strA:str,indexA:int,strB:str,indexB:int,length:int)->int:
#        """

#        """
        
#        dlllib.String_CompareOrdinalSISIL.argtypes=[ c_void_p,c_int,c_void_p,c_int,c_int]
#        dlllib.String_CompareOrdinalSISIL.restype=c_int
#        ret = CallCFunction(dlllib.String_CompareOrdinalSISIL, strA,indexA,strB,indexB,length)
#        return ret


#    def Contains(self ,value:str)->bool:
#        """

#        """
        
#        dlllib.String_Contains.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_Contains.restype=c_bool
#        ret = CallCFunction(dlllib.String_Contains,self.Ptr, value)
#        return ret

#    @dispatch

#    def EndsWith(self ,value:str)->bool:
#        """

#        """
        
#        dlllib.String_EndsWith.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_EndsWith.restype=c_bool
#        ret = CallCFunction(dlllib.String_EndsWith,self.Ptr, value)
#        return ret

##    @dispatch
##
##    def EndsWith(self ,value:str,comparisonType:'StringComparison')->bool:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_EndsWithVC.argtypes=[c_void_p ,c_void_p,c_int]
##        dlllib.String_EndsWithVC.restype=c_bool
##        ret = CallCFunction(dlllib.String_EndsWithVC,self.Ptr, value,enumcomparisonType)
##        return ret


#    @dispatch

#    def EndsWith(self ,value:str,ignoreCase:bool,culture:CultureInfo)->bool:
#        """

#        """
#        intPtrculture:c_void_p = culture.Ptr

#        dlllib.String_EndsWithVIC.argtypes=[c_void_p ,c_void_p,c_bool,c_void_p]
#        dlllib.String_EndsWithVIC.restype=c_bool
#        ret = CallCFunction(dlllib.String_EndsWithVIC,self.Ptr, value,ignoreCase,intPtrculture)
#        return ret

#    @dispatch

#    def IndexOf(self ,value:int)->int:
#        """

#        """
        
#        dlllib.String_IndexOf.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_IndexOf.restype=c_int
#        ret = CallCFunction(dlllib.String_IndexOf,self.Ptr, value)
#        return ret

#    @dispatch

#    def IndexOf(self ,value:int,startIndex:int)->int:
#        """

#        """
        
#        dlllib.String_IndexOfVS.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.String_IndexOfVS.restype=c_int
#        ret = CallCFunction(dlllib.String_IndexOfVS,self.Ptr, value,startIndex)
#        return ret

##    @dispatch
##
##    def IndexOfAny(self ,anyOf:'Char[]')->int:
##        """
##
##        """
##        #arrayanyOf:ArrayTypeanyOf = ""
##        countanyOf = len(anyOf)
##        ArrayTypeanyOf = c_void_p * countanyOf
##        arrayanyOf = ArrayTypeanyOf()
##        for i in range(0, countanyOf):
##            arrayanyOf[i] = anyOf[i].Ptr
##
##
##        dlllib.String_IndexOfAny.argtypes=[c_void_p ,ArrayTypeanyOf]
##        dlllib.String_IndexOfAny.restype=c_int
##        ret = CallCFunction(dlllib.String_IndexOfAny,self.Ptr, arrayanyOf)
##        return ret


##    @dispatch
##
##    def IndexOfAny(self ,anyOf:'Char[]',startIndex:int)->int:
##        """
##
##        """
##        #arrayanyOf:ArrayTypeanyOf = ""
##        countanyOf = len(anyOf)
##        ArrayTypeanyOf = c_void_p * countanyOf
##        arrayanyOf = ArrayTypeanyOf()
##        for i in range(0, countanyOf):
##            arrayanyOf[i] = anyOf[i].Ptr
##
##
##        dlllib.String_IndexOfAnyAS.argtypes=[c_void_p ,ArrayTypeanyOf,c_int]
##        dlllib.String_IndexOfAnyAS.restype=c_int
##        ret = CallCFunction(dlllib.String_IndexOfAnyAS,self.Ptr, arrayanyOf,startIndex)
##        return ret


#    @dispatch

#    def IndexOf(self ,value:str)->int:
#        """

#        """
        
#        dlllib.String_IndexOfV.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_IndexOfV.restype=c_int
#        ret = CallCFunction(dlllib.String_IndexOfV,self.Ptr, value)
#        return ret

#    @dispatch

#    def IndexOf(self ,value:str,startIndex:int)->int:
#        """

#        """
        
#        dlllib.String_IndexOfVS1.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.String_IndexOfVS1.restype=c_int
#        ret = CallCFunction(dlllib.String_IndexOfVS1,self.Ptr, value,startIndex)
#        return ret

#    @dispatch

#    def IndexOf(self ,value:str,startIndex:int,count:int)->int:
#        """

#        """
        
#        dlllib.String_IndexOfVSC.argtypes=[c_void_p ,c_void_p,c_int,c_int]
#        dlllib.String_IndexOfVSC.restype=c_int
#        ret = CallCFunction(dlllib.String_IndexOfVSC,self.Ptr, value,startIndex,count)
#        return ret

##    @dispatch
##
##    def IndexOf(self ,value:str,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_IndexOfVC.argtypes=[c_void_p ,c_void_p,c_int]
##        dlllib.String_IndexOfVC.restype=c_int
##        ret = CallCFunction(dlllib.String_IndexOfVC,self.Ptr, value,enumcomparisonType)
##        return ret


##    @dispatch
##
##    def IndexOf(self ,value:str,startIndex:int,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_IndexOfVSC1.argtypes=[c_void_p ,c_void_p,c_int,c_int]
##        dlllib.String_IndexOfVSC1.restype=c_int
##        ret = CallCFunction(dlllib.String_IndexOfVSC1,self.Ptr, value,startIndex,enumcomparisonType)
##        return ret


##    @dispatch
##
##    def IndexOf(self ,value:str,startIndex:int,count:int,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_IndexOfVSCC.argtypes=[c_void_p ,c_void_p,c_int,c_int,c_int]
##        dlllib.String_IndexOfVSCC.restype=c_int
##        ret = CallCFunction(dlllib.String_IndexOfVSCC,self.Ptr, value,startIndex,count,enumcomparisonType)
##        return ret


#    @dispatch

#    def LastIndexOf(self ,value:int)->int:
#        """

#        """
        
#        dlllib.String_LastIndexOf.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_LastIndexOf.restype=c_int
#        ret = CallCFunction(dlllib.String_LastIndexOf,self.Ptr, value)
#        return ret

#    @dispatch

#    def LastIndexOf(self ,value:int,startIndex:int)->int:
#        """

#        """
        
#        dlllib.String_LastIndexOfVS.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.String_LastIndexOfVS.restype=c_int
#        ret = CallCFunction(dlllib.String_LastIndexOfVS,self.Ptr, value,startIndex)
#        return ret

##    @dispatch
##
##    def LastIndexOfAny(self ,anyOf:'Char[]')->int:
##        """
##
##        """
##        #arrayanyOf:ArrayTypeanyOf = ""
##        countanyOf = len(anyOf)
##        ArrayTypeanyOf = c_void_p * countanyOf
##        arrayanyOf = ArrayTypeanyOf()
##        for i in range(0, countanyOf):
##            arrayanyOf[i] = anyOf[i].Ptr
##
##
##        dlllib.String_LastIndexOfAny.argtypes=[c_void_p ,ArrayTypeanyOf]
##        dlllib.String_LastIndexOfAny.restype=c_int
##        ret = CallCFunction(dlllib.String_LastIndexOfAny,self.Ptr, arrayanyOf)
##        return ret


##    @dispatch
##
##    def LastIndexOfAny(self ,anyOf:'Char[]',startIndex:int)->int:
##        """
##
##        """
##        #arrayanyOf:ArrayTypeanyOf = ""
##        countanyOf = len(anyOf)
##        ArrayTypeanyOf = c_void_p * countanyOf
##        arrayanyOf = ArrayTypeanyOf()
##        for i in range(0, countanyOf):
##            arrayanyOf[i] = anyOf[i].Ptr
##
##
##        dlllib.String_LastIndexOfAnyAS.argtypes=[c_void_p ,ArrayTypeanyOf,c_int]
##        dlllib.String_LastIndexOfAnyAS.restype=c_int
##        ret = CallCFunction(dlllib.String_LastIndexOfAnyAS,self.Ptr, arrayanyOf,startIndex)
##        return ret


#    @dispatch

#    def LastIndexOf(self ,value:str)->int:
#        """

#        """
        
#        dlllib.String_LastIndexOfV.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_LastIndexOfV.restype=c_int
#        ret = CallCFunction(dlllib.String_LastIndexOfV,self.Ptr, value)
#        return ret

#    @dispatch

#    def LastIndexOf(self ,value:str,startIndex:int)->int:
#        """

#        """
        
#        dlllib.String_LastIndexOfVS1.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.String_LastIndexOfVS1.restype=c_int
#        ret = CallCFunction(dlllib.String_LastIndexOfVS1,self.Ptr, value,startIndex)
#        return ret

#    @dispatch

#    def LastIndexOf(self ,value:str,startIndex:int,count:int)->int:
#        """

#        """
        
#        dlllib.String_LastIndexOfVSC.argtypes=[c_void_p ,c_void_p,c_int,c_int]
#        dlllib.String_LastIndexOfVSC.restype=c_int
#        ret = CallCFunction(dlllib.String_LastIndexOfVSC,self.Ptr, value,startIndex,count)
#        return ret

##    @dispatch
##
##    def LastIndexOf(self ,value:str,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_LastIndexOfVC.argtypes=[c_void_p ,c_void_p,c_int]
##        dlllib.String_LastIndexOfVC.restype=c_int
##        ret = CallCFunction(dlllib.String_LastIndexOfVC,self.Ptr, value,enumcomparisonType)
##        return ret


##    @dispatch
##
##    def LastIndexOf(self ,value:str,startIndex:int,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_LastIndexOfVSC1.argtypes=[c_void_p ,c_void_p,c_int,c_int]
##        dlllib.String_LastIndexOfVSC1.restype=c_int
##        ret = CallCFunction(dlllib.String_LastIndexOfVSC1,self.Ptr, value,startIndex,enumcomparisonType)
##        return ret


##    @dispatch
##
##    def LastIndexOf(self ,value:str,startIndex:int,count:int,comparisonType:'StringComparison')->int:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_LastIndexOfVSCC.argtypes=[c_void_p ,c_void_p,c_int,c_int,c_int]
##        dlllib.String_LastIndexOfVSCC.restype=c_int
##        ret = CallCFunction(dlllib.String_LastIndexOfVSCC,self.Ptr, value,startIndex,count,enumcomparisonType)
##        return ret


#    @dispatch

#    def PadLeft(self ,totalWidth:int)->str:
#        """

#        """
        
#        dlllib.String_PadLeft.argtypes=[c_void_p ,c_int]
#        dlllib.String_PadLeft.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_PadLeft,self.Ptr, totalWidth)
#        return ret


#    @dispatch

#    def PadLeft(self ,totalWidth:int,paddingChar:int)->str:
#        """

#        """
        
#        dlllib.String_PadLeftTP.argtypes=[c_void_p ,c_int,c_void_p]
#        dlllib.String_PadLeftTP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_PadLeftTP,self.Ptr, totalWidth,paddingChar)
#        return ret


#    @dispatch

#    def PadRight(self ,totalWidth:int)->str:
#        """

#        """
        
#        dlllib.String_PadRight.argtypes=[c_void_p ,c_int]
#        dlllib.String_PadRight.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_PadRight,self.Ptr, totalWidth)
#        return ret


#    @dispatch

#    def PadRight(self ,totalWidth:int,paddingChar:int)->str:
#        """

#        """
        
#        dlllib.String_PadRightTP.argtypes=[c_void_p ,c_int,c_void_p]
#        dlllib.String_PadRightTP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_PadRightTP,self.Ptr, totalWidth,paddingChar)
#        return ret


#    @dispatch

#    def StartsWith(self ,value:str)->bool:
#        """

#        """
        
#        dlllib.String_StartsWith.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_StartsWith.restype=c_bool
#        ret = CallCFunction(dlllib.String_StartsWith,self.Ptr, value)
#        return ret

##    @dispatch
##
##    def StartsWith(self ,value:str,comparisonType:'StringComparison')->bool:
##        """
##
##        """
##        enumcomparisonType:c_int = comparisonType.value
##
##        dlllib.String_StartsWithVC.argtypes=[c_void_p ,c_void_p,c_int]
##        dlllib.String_StartsWithVC.restype=c_bool
##        ret = CallCFunction(dlllib.String_StartsWithVC,self.Ptr, value,enumcomparisonType)
##        return ret


#    @dispatch

#    def StartsWith(self ,value:str,ignoreCase:bool,culture:CultureInfo)->bool:
#        """

#        """
#        intPtrculture:c_void_p = culture.Ptr

#        dlllib.String_StartsWithVIC.argtypes=[c_void_p ,c_void_p,c_bool,c_void_p]
#        dlllib.String_StartsWithVIC.restype=c_bool
#        ret = CallCFunction(dlllib.String_StartsWithVIC,self.Ptr, value,ignoreCase,intPtrculture)
#        return ret

#    @dispatch

#    def ToLower(self)->str:
#        """

#        """
#        dlllib.String_ToLower.argtypes=[c_void_p]
#        dlllib.String_ToLower.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToLower,self.Ptr)
#        return ret


#    @dispatch

#    def ToLower(self ,culture:CultureInfo)->str:
#        """

#        """
#        intPtrculture:c_void_p = culture.Ptr

#        dlllib.String_ToLowerC.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_ToLowerC.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToLowerC,self.Ptr, intPtrculture)
#        return ret



#    def ToLowerInvariant(self)->str:
#        """

#        """
#        dlllib.String_ToLowerInvariant.argtypes=[c_void_p]
#        dlllib.String_ToLowerInvariant.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToLowerInvariant,self.Ptr)
#        return ret


#    @dispatch

#    def ToUpper(self)->str:
#        """

#        """
#        dlllib.String_ToUpper.argtypes=[c_void_p]
#        dlllib.String_ToUpper.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToUpper,self.Ptr)
#        return ret


#    @dispatch

#    def ToUpper(self ,culture:CultureInfo)->str:
#        """

#        """
#        intPtrculture:c_void_p = culture.Ptr

#        dlllib.String_ToUpperC.argtypes=[c_void_p ,c_void_p]
#        dlllib.String_ToUpperC.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToUpperC,self.Ptr, intPtrculture)
#        return ret



#    def ToUpperInvariant(self)->str:
#        """

#        """
#        dlllib.String_ToUpperInvariant.argtypes=[c_void_p]
#        dlllib.String_ToUpperInvariant.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToUpperInvariant,self.Ptr)
#        return ret


#    @dispatch

#    def ToString(self)->str:
#        """

#        """
#        dlllib.String_ToString.argtypes=[c_void_p]
#        dlllib.String_ToString.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ToString,self.Ptr)
#        return ret


##    @dispatch
##
##    def ToString(self ,provider:'IFormatProvider')->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##
##        dlllib.String_ToStringP.argtypes=[c_void_p ,c_void_p]
##        dlllib.String_ToStringP.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_ToStringP,self.Ptr, intPtrprovider)
##        return ret
##



#    def Clone(self)->'SpireObject':
#        """

#        """
#        dlllib.String_Clone.argtypes=[c_void_p]
#        dlllib.String_Clone.restype=c_void_p
#        intPtr = CallCFunction(dlllib.String_Clone,self.Ptr)
#        ret = None if intPtr==None else SpireObject(intPtr)
#        return ret


#    @dispatch

#    def Trim(self)->str:
#        """

#        """
#        dlllib.String_Trim1.argtypes=[c_void_p]
#        dlllib.String_Trim1.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Trim1,self.Ptr)
#        return ret



#    def Insert(self ,startIndex:int,value:str)->str:
#        """

#        """
        
#        dlllib.String_Insert.argtypes=[c_void_p ,c_int,c_void_p]
#        dlllib.String_Insert.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Insert,self.Ptr, startIndex,value)
#        return ret


#    @dispatch

#    def Replace(self ,oldChar:int,newChar:int)->str:
#        """

#        """
        
#        dlllib.String_Replace.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.String_Replace.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Replace,self.Ptr, oldChar,newChar)
#        return ret


#    @dispatch

#    def Replace(self ,oldValue:str,newValue:str)->str:
#        """

#        """
        
#        dlllib.String_ReplaceON.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.String_ReplaceON.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ReplaceON,self.Ptr, oldValue,newValue)
#        return ret


#    @dispatch

#    def Remove(self ,startIndex:int,count:int)->str:
#        """

#        """
        
#        dlllib.String_Remove.argtypes=[c_void_p ,c_int,c_int]
#        dlllib.String_Remove.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Remove,self.Ptr, startIndex,count)
#        return ret


#    @dispatch

#    def Remove(self ,startIndex:int)->str:
#        """

#        """
        
#        dlllib.String_RemoveS.argtypes=[c_void_p ,c_int]
#        dlllib.String_RemoveS.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_RemoveS,self.Ptr, startIndex)
#        return ret


#    @staticmethod
#    @dispatch

#    def Format(format:str,arg0:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr

#        dlllib.String_Format.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_Format.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Format, format,intPtrarg0)
#        return ret


#    @staticmethod
#    @dispatch

#    def Format(format:str,arg0:SpireObject,arg1:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr
#        intPtrarg1:c_void_p = arg1.Ptr

#        dlllib.String_FormatFAA.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.String_FormatFAA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_FormatFAA, format,intPtrarg0,intPtrarg1)
#        return ret


#    @staticmethod
#    @dispatch

#    def Format(format:str,arg0:SpireObject,arg1:SpireObject,arg2:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr
#        intPtrarg1:c_void_p = arg1.Ptr
#        intPtrarg2:c_void_p = arg2.Ptr

#        dlllib.String_FormatFAAA.argtypes=[ c_void_p,c_void_p,c_void_p,c_void_p]
#        dlllib.String_FormatFAAA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_FormatFAAA, format,intPtrarg0,intPtrarg1,intPtrarg2)
#        return ret


##    @staticmethod
##    @dispatch
##
##    def Format(provider:'IFormatProvider',format:str,arg0:SpireObject)->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##        intPtrarg0:c_void_p = arg0.Ptr
##
##        dlllib.String_FormatPFA.argtypes=[ c_void_p,c_void_p,c_void_p]
##        dlllib.String_FormatPFA.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_FormatPFA, intPtrprovider,format,intPtrarg0)
##        return ret
##


##    @staticmethod
##    @dispatch
##
##    def Format(provider:'IFormatProvider',format:str,arg0:SpireObject,arg1:SpireObject)->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##        intPtrarg0:c_void_p = arg0.Ptr
##        intPtrarg1:c_void_p = arg1.Ptr
##
##        dlllib.String_FormatPFAA.argtypes=[ c_void_p,c_void_p,c_void_p,c_void_p]
##        dlllib.String_FormatPFAA.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_FormatPFAA, intPtrprovider,format,intPtrarg0,intPtrarg1)
##        return ret
##


##    @staticmethod
##    @dispatch
##
##    def Format(provider:'IFormatProvider',format:str,arg0:SpireObject,arg1:SpireObject,arg2:SpireObject)->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##        intPtrarg0:c_void_p = arg0.Ptr
##        intPtrarg1:c_void_p = arg1.Ptr
##        intPtrarg2:c_void_p = arg2.Ptr
##
##        dlllib.String_FormatPFAAA.argtypes=[ c_void_p,c_void_p,c_void_p,c_void_p,c_void_p]
##        dlllib.String_FormatPFAAA.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_FormatPFAAA, intPtrprovider,format,intPtrarg0,intPtrarg1,intPtrarg2)
##        return ret
##


#    @staticmethod

#    def Copy(str:str)->str:
#        """

#        """
        
#        dlllib.String_Copy.argtypes=[ c_void_p]
#        dlllib.String_Copy.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Copy, str)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(arg0:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr

#        dlllib.String_Concat.argtypes=[ c_void_p]
#        dlllib.String_Concat.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Concat, intPtrarg0)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(arg0:SpireObject,arg1:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr
#        intPtrarg1:c_void_p = arg1.Ptr

#        dlllib.String_ConcatAA.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_ConcatAA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatAA, intPtrarg0,intPtrarg1)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(arg0:SpireObject,arg1:SpireObject,arg2:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr
#        intPtrarg1:c_void_p = arg1.Ptr
#        intPtrarg2:c_void_p = arg2.Ptr

#        dlllib.String_ConcatAAA.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.String_ConcatAAA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatAAA, intPtrarg0,intPtrarg1,intPtrarg2)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(arg0:SpireObject,arg1:SpireObject,arg2:SpireObject,arg3:SpireObject)->str:
#        """

#        """
#        intPtrarg0:c_void_p = arg0.Ptr
#        intPtrarg1:c_void_p = arg1.Ptr
#        intPtrarg2:c_void_p = arg2.Ptr
#        intPtrarg3:c_void_p = arg3.Ptr

#        dlllib.String_ConcatAAAA.argtypes=[ c_void_p,c_void_p,c_void_p,c_void_p]
#        dlllib.String_ConcatAAAA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatAAAA, intPtrarg0,intPtrarg1,intPtrarg2,intPtrarg3)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(args:List[SpireObject])->str:
#        """

#        """
#        #arrayargs:ArrayTypeargs = ""
#        countargs = len(args)
#        ArrayTypeargs = c_void_p * countargs
#        arrayargs = ArrayTypeargs()
#        for i in range(0, countargs):
#            arrayargs[i] = args[i].Ptr


#        dlllib.String_ConcatA.argtypes=[ ArrayTypeargs,c_int]
#        dlllib.String_ConcatA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatA, arrayargs,countargs)
#        return ret


##    @staticmethod
##    @dispatch
##
##    def Concat(values:'IEnumerable1')->str:
##        """
##
##        """
##        intPtrvalues:c_void_p = values.Ptr
##
##        dlllib.String_ConcatV.argtypes=[ c_void_p]
##        dlllib.String_ConcatV.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_ConcatV, intPtrvalues)
##        return ret
##


#    @staticmethod
#    @dispatch

#    def Concat(str0:str,str1:str)->str:
#        """

#        """
        
#        dlllib.String_ConcatSS.argtypes=[ c_void_p,c_void_p]
#        dlllib.String_ConcatSS.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatSS, str0,str1)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(str0:str,str1:str,str2:str)->str:
#        """

#        """
        
#        dlllib.String_ConcatSSS.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.String_ConcatSSS.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatSSS, str0,str1,str2)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(str0:str,str1:str,str2:str,str3:str)->str:
#        """

#        """
        
#        dlllib.String_ConcatSSSS.argtypes=[ c_void_p,c_void_p,c_void_p,c_void_p]
#        dlllib.String_ConcatSSSS.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatSSSS, str0,str1,str2,str3)
#        return ret


#    @staticmethod
#    @dispatch

#    def Concat(values:List[str])->str:
#        """

#        """
#        #arrayvalues:ArrayTypevalues = ""
#        countvalues = len(values)
#        ArrayTypevalues = c_wchar_p * countvalues
#        arrayvalues = ArrayTypevalues()
#        for i in range(0, countvalues):
#            arrayvalues[i] = values[i]


#        dlllib.String_ConcatV1.argtypes=[ ArrayTypevalues,c_int]
#        dlllib.String_ConcatV1.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_ConcatV1, arrayvalues,countvalues)
#        return ret


#    @staticmethod

#    def Intern(str:str)->str:
#        """

#        """
        
#        dlllib.String_Intern.argtypes=[ c_void_p]
#        dlllib.String_Intern.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Intern, str)
#        return ret


#    @staticmethod

#    def IsInterned(str:str)->str:
#        """

#        """
        
#        dlllib.String_IsInterned.argtypes=[ c_void_p]
#        dlllib.String_IsInterned.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_IsInterned, str)
#        return ret


##
##    def GetTypeCode(self)->'TypeCode':
##        """
##
##        """
##        dlllib.String_GetTypeCode.argtypes=[c_void_p]
##        dlllib.String_GetTypeCode.restype=c_int
##        ret = CallCFunction(dlllib.String_GetTypeCode,self.Ptr)
##        objwraped = TypeCode(ret)
##        return objwraped


##
##    def GetEnumerator(self)->'CharEnumerator':
##        """
##
##        """
##        dlllib.String_GetEnumerator.argtypes=[c_void_p]
##        dlllib.String_GetEnumerator.restype=c_void_p
##        intPtr = CallCFunction(dlllib.String_GetEnumerator,self.Ptr)
##        ret = None if intPtr==None else CharEnumerator(intPtr)
##        return ret
##


##    @staticmethod
##    @dispatch
##
##    def Join(separator:str,values:'IEnumerable1')->str:
##        """
##
##        """
##        intPtrvalues:c_void_p = values.Ptr
##
##        dlllib.String_JoinSV11.argtypes=[ c_void_p,c_void_p]
##        dlllib.String_JoinSV11.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_JoinSV11, separator,intPtrvalues)
##        return ret
##



#    def get_Chars(self ,index:int)->int:
#        """

#        """
        
#        dlllib.String_get_Chars.argtypes=[c_void_p ,c_int]
#        dlllib.String_get_Chars.restype=c_int
#        ret = CallCFunction(dlllib.String_get_Chars,self.Ptr, index)
#        return ret

#    @property
#    def Length(self)->int:
#        """

#        """
#        dlllib.String_get_Length.argtypes=[c_void_p]
#        dlllib.String_get_Length.restype=c_int
#        ret = CallCFunction(dlllib.String_get_Length,self.Ptr)
#        return ret

##    @staticmethod
##    @dispatch
##
##    def Concat(values:'IEnumerable1')->str:
##        """
##
##        """
##        intPtrvalues:c_void_p = values.Ptr
##
##        dlllib.String_ConcatV11.argtypes=[ c_void_p]
##        dlllib.String_ConcatV11.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_ConcatV11, intPtrvalues)
##        return ret
##


#    @dispatch

#    def IndexOf(self ,value:int,startIndex:int,count:int)->int:
#        """

#        """
        
#        dlllib.String_IndexOfVSC11.argtypes=[c_void_p ,c_void_p,c_int,c_int]
#        dlllib.String_IndexOfVSC11.restype=c_int
#        ret = CallCFunction(dlllib.String_IndexOfVSC11,self.Ptr, value,startIndex,count)
#        return ret

##    @dispatch
##
##    def IndexOfAny(self ,anyOf:'Char[]',startIndex:int,count:int)->int:
##        """
##
##        """
##        #arrayanyOf:ArrayTypeanyOf = ""
##        countanyOf = len(anyOf)
##        ArrayTypeanyOf = c_void_p * countanyOf
##        arrayanyOf = ArrayTypeanyOf()
##        for i in range(0, countanyOf):
##            arrayanyOf[i] = anyOf[i].Ptr
##
##
##        dlllib.String_IndexOfAnyASC.argtypes=[c_void_p ,ArrayTypeanyOf,c_int,c_int]
##        dlllib.String_IndexOfAnyASC.restype=c_int
##        ret = CallCFunction(dlllib.String_IndexOfAnyASC,self.Ptr, arrayanyOf,startIndex,count)
##        return ret


#    @dispatch

#    def LastIndexOf(self ,value:int,startIndex:int,count:int)->int:
#        """

#        """
        
#        dlllib.String_LastIndexOfVSC11.argtypes=[c_void_p ,c_void_p,c_int,c_int]
#        dlllib.String_LastIndexOfVSC11.restype=c_int
#        ret = CallCFunction(dlllib.String_LastIndexOfVSC11,self.Ptr, value,startIndex,count)
#        return ret

##    @dispatch
##
##    def LastIndexOfAny(self ,anyOf:'Char[]',startIndex:int,count:int)->int:
##        """
##
##        """
##        #arrayanyOf:ArrayTypeanyOf = ""
##        countanyOf = len(anyOf)
##        ArrayTypeanyOf = c_void_p * countanyOf
##        arrayanyOf = ArrayTypeanyOf()
##        for i in range(0, countanyOf):
##            arrayanyOf[i] = anyOf[i].Ptr
##
##
##        dlllib.String_LastIndexOfAnyASC.argtypes=[c_void_p ,ArrayTypeanyOf,c_int,c_int]
##        dlllib.String_LastIndexOfAnyASC.restype=c_int
##        ret = CallCFunction(dlllib.String_LastIndexOfAnyASC,self.Ptr, arrayanyOf,startIndex,count)
##        return ret


#    @staticmethod
#    @dispatch

#    def Format(format:str,args:List[SpireObject])->str:
#        """

#        """
#        #arrayargs:ArrayTypeargs = ""
#        countargs = len(args)
#        ArrayTypeargs = c_void_p * countargs
#        arrayargs = ArrayTypeargs()
#        for i in range(0, countargs):
#            arrayargs[i] = args[i].Ptr


#        dlllib.String_FormatFA.argtypes=[ c_void_p,ArrayTypeargs,c_int]
#        dlllib.String_FormatFA.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_FormatFA, format,arrayargs,countargs)
#        return ret


##    @staticmethod
##    @dispatch
##
##    def Format(provider:'IFormatProvider',format:str,args:List[SpireObject])->str:
##        """
##
##        """
##        intPtrprovider:c_void_p = provider.Ptr
##        #arrayargs:ArrayTypeargs = ""
##        countargs = len(args)
##        ArrayTypeargs = c_void_p * countargs
##        arrayargs = ArrayTypeargs()
##        for i in range(0, countargs):
##            arrayargs[i] = args[i].Ptr
##
##
##        dlllib.String_FormatPFA1.argtypes=[ c_void_p,c_void_p,ArrayTypeargs]
##        dlllib.String_FormatPFA1.restype=c_wchar_p
##        ret = CallCFunction(dlllib.String_FormatPFA1, intPtrprovider,format,arrayargs)
##        return ret
##


#    @staticmethod

#    def Empty()->str:
#        """

#        """
#        #dlllib.String_Empty.argtypes=[]
#        dlllib.String_Empty.restype=c_wchar_p
#        ret = CallCFunction(dlllib.String_Empty)
#        return ret


