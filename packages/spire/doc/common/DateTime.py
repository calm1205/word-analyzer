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

class DateTime (SpireObject) :
    """

    """
    @dispatch
    def __init__(self):
        dlllib.DateTime_CreateDateTime.argtypes=[ c_int,c_int,c_int,c_int,c_int,c_int,c_int]
        dlllib.DateTime_CreateDateTime.restype = c_void_p
        intPtr = CallCFunction(dlllib.DateTime_CreateDateTime,1, 1, 1, 0, 0, 0, 0)
        super(DateTime, self).__init__(intPtr)
    @dispatch
    def __init__(self, year:int, month:int, day:int, hour:int, minute:int, second:int, millisecond:int):
        dlllib.DateTime_CreateDateTime.argtypes=[ c_int,c_int,c_int,c_int,c_int,c_int,c_int]
        dlllib.DateTime_CreateDateTime.restype = c_void_p
        intPtr = CallCFunction(dlllib.DateTime_CreateDateTime,year, month, day, hour, minute, second, millisecond)
        super(DateTime, self).__init__(intPtr)

    def __sub__(self ,other):
        return DateTime.op_Subtraction(self,other)
    def __add__(self ,other):
        return DateTime.op_Addition(self,other)
    def __str__(self):
        return self.ToString()

    def Add(self ,value:'TimeSpan')->'DateTime':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_Add.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_Add.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_Add,self.Ptr, intPtrvalue)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddDays(self ,value:float)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddDays.argtypes=[c_void_p ,c_double]
        dlllib.DateTime_AddDays.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddDays,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddHours(self ,value:float)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddHours.argtypes=[c_void_p ,c_double]
        dlllib.DateTime_AddHours.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddHours,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddMilliseconds(self ,value:float)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddMilliseconds.argtypes=[c_void_p ,c_double]
        dlllib.DateTime_AddMilliseconds.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddMilliseconds,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddMinutes(self ,value:float)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddMinutes.argtypes=[c_void_p ,c_double]
        dlllib.DateTime_AddMinutes.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddMinutes,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddMonths(self ,months:int)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddMonths.argtypes=[c_void_p ,c_int]
        dlllib.DateTime_AddMonths.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddMonths,self.Ptr, months)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddSeconds(self ,value:float)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddSeconds.argtypes=[c_void_p ,c_double]
        dlllib.DateTime_AddSeconds.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddSeconds,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddTicks(self ,value:int)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddTicks.argtypes=[c_void_p ,c_long]
        dlllib.DateTime_AddTicks.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddTicks,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret



    def AddYears(self ,value:int)->'DateTime':
        """

        """
        
        dlllib.DateTime_AddYears.argtypes=[c_void_p ,c_int]
        dlllib.DateTime_AddYears.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_AddYears,self.Ptr, value)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod

    def Compare(t1:'DateTime',t2:'DateTime')->int:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.DateTime_Compare.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_Compare.restype=c_int
        ret = CallCFunction(dlllib.DateTime_Compare, intPtrt1,intPtrt2)
        return ret

    @dispatch

    def CompareTo(self ,value:SpireObject)->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_CompareTo.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_CompareTo.restype=c_int
        ret = CallCFunction(dlllib.DateTime_CompareTo,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def CompareTo(self ,value:'DateTime')->int:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_CompareToV.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_CompareToV.restype=c_int
        ret = CallCFunction(dlllib.DateTime_CompareToV,self.Ptr, intPtrvalue)
        return ret

    @staticmethod

    def DaysInMonth(year:int,month:int)->int:
        """

        """
        
        dlllib.DateTime_DaysInMonth.argtypes=[ c_int,c_int]
        dlllib.DateTime_DaysInMonth.restype=c_int
        ret = CallCFunction(dlllib.DateTime_DaysInMonth, year,month)
        return ret

    @dispatch

    def Equals(self ,value:SpireObject)->bool:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_Equals.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_Equals,self.Ptr, intPtrvalue)
        return ret

    @dispatch

    def Equals(self ,value:'DateTime')->bool:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_EqualsV.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_EqualsV.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_EqualsV,self.Ptr, intPtrvalue)
        return ret

    @staticmethod
    @dispatch

    def Equals(t1:'DateTime',t2:'DateTime')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.DateTime_EqualsTT.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_EqualsTT.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_EqualsTT, intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def FromBinary(dateData:int)->'DateTime':
        """

        """
        
        dlllib.DateTime_FromBinary.argtypes=[ c_long]
        dlllib.DateTime_FromBinary.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_FromBinary, dateData)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod

    def FromFileTime(fileTime:int)->'DateTime':
        """

        """
        
        dlllib.DateTime_FromFileTime.argtypes=[ c_long]
        dlllib.DateTime_FromFileTime.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_FromFileTime, fileTime)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod

    def FromFileTimeUtc(fileTime:int)->'DateTime':
        """

        """
        
        dlllib.DateTime_FromFileTimeUtc.argtypes=[ c_long]
        dlllib.DateTime_FromFileTimeUtc.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_FromFileTimeUtc, fileTime)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod

    def FromOADate(d:float)->'DateTime':
        """

        """
        
        dlllib.DateTime_FromOADate.argtypes=[ c_double]
        dlllib.DateTime_FromOADate.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_FromOADate, d)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    def IsDaylightSavingTime(self)->bool:
        """

        """
        dlllib.DateTime_IsDaylightSavingTime.argtypes=[c_void_p]
        dlllib.DateTime_IsDaylightSavingTime.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_IsDaylightSavingTime,self.Ptr)
        return ret

#    @staticmethod
#
#    def SpecifyKind(value:'DateTime',kind:'DateTimeKind')->'DateTime':
#        """
#
#        """
#        intPtrvalue:c_void_p = value.Ptr
#        enumkind:c_int = kind.value
#
#        dlllib.DateTime_SpecifyKind.argtypes=[ c_void_p,c_int]
#        dlllib.DateTime_SpecifyKind.restype=c_void_p
#        intPtr = CallCFunction(dlllib.DateTime_SpecifyKind, intPtrvalue,enumkind)
#        ret = None if intPtr==None else DateTime(intPtr)
#        return ret
#


    def ToBinary(self)->int:
        """

        """
        dlllib.DateTime_ToBinary.argtypes=[c_void_p]
        dlllib.DateTime_ToBinary.restype=c_long
        ret = CallCFunction(dlllib.DateTime_ToBinary,self.Ptr)
        return ret

    @property

    def Date(self)->'DateTime':
        """

        """
        dlllib.DateTime_get_Date.argtypes=[c_void_p]
        dlllib.DateTime_get_Date.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_get_Date,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @property
    def Day(self)->int:
        """

        """
        dlllib.DateTime_get_Day.argtypes=[c_void_p]
        dlllib.DateTime_get_Day.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Day,self.Ptr)
        return ret

#    @property
#
#    def DayOfWeek(self)->'DayOfWeek':
#        """
#
#        """
#        dlllib.DateTime_get_DayOfWeek.argtypes=[c_void_p]
#        dlllib.DateTime_get_DayOfWeek.restype=c_int
#        ret = CallCFunction(dlllib.DateTime_get_DayOfWeek,self.Ptr)
#        objwraped = DayOfWeek(ret)
#        return objwraped


    @property
    def DayOfYear(self)->int:
        """

        """
        dlllib.DateTime_get_DayOfYear.argtypes=[c_void_p]
        dlllib.DateTime_get_DayOfYear.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_DayOfYear,self.Ptr)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.DateTime_GetHashCode.argtypes=[c_void_p]
        dlllib.DateTime_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.DateTime_GetHashCode,self.Ptr)
        return ret

    @property
    def Hour(self)->int:
        """

        """
        dlllib.DateTime_get_Hour.argtypes=[c_void_p]
        dlllib.DateTime_get_Hour.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Hour,self.Ptr)
        return ret

#    @property
#
#    def Kind(self)->'DateTimeKind':
#        """
#
#        """
#        dlllib.DateTime_get_Kind.argtypes=[c_void_p]
#        dlllib.DateTime_get_Kind.restype=c_int
#        ret = CallCFunction(dlllib.DateTime_get_Kind,self.Ptr)
#        objwraped = DateTimeKind(ret)
#        return objwraped


    @property
    def Millisecond(self)->int:
        """

        """
        dlllib.DateTime_get_Millisecond.argtypes=[c_void_p]
        dlllib.DateTime_get_Millisecond.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Millisecond,self.Ptr)
        return ret

    @property
    def Minute(self)->int:
        """

        """
        dlllib.DateTime_get_Minute.argtypes=[c_void_p]
        dlllib.DateTime_get_Minute.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Minute,self.Ptr)
        return ret

    @property
    def Month(self)->int:
        """

        """
        dlllib.DateTime_get_Month.argtypes=[c_void_p]
        dlllib.DateTime_get_Month.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Month,self.Ptr)
        return ret

    @staticmethod

    def get_Now()->'DateTime':
        """

        """
        #dlllib.DateTime_get_Now.argtypes=[]
        dlllib.DateTime_get_Now.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_get_Now)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod

    def get_UtcNow()->'DateTime':
        """

        """
        #dlllib.DateTime_get_UtcNow.argtypes=[]
        dlllib.DateTime_get_UtcNow.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_get_UtcNow)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @property
    def Second(self)->int:
        """

        """
        dlllib.DateTime_get_Second.argtypes=[c_void_p]
        dlllib.DateTime_get_Second.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Second,self.Ptr)
        return ret

    @property
    def Ticks(self)->int:
        """

        """
        dlllib.DateTime_get_Ticks.argtypes=[c_void_p]
        dlllib.DateTime_get_Ticks.restype=c_long
        ret = CallCFunction(dlllib.DateTime_get_Ticks,self.Ptr)
        return ret

    @property

    def TimeOfDay(self)->'TimeSpan':
        """

        """
        dlllib.DateTime_get_TimeOfDay.argtypes=[c_void_p]
        dlllib.DateTime_get_TimeOfDay.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_get_TimeOfDay,self.Ptr)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def get_Today()->'DateTime':
        """

        """
        #dlllib.DateTime_get_Today.argtypes=[]
        dlllib.DateTime_get_Today.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_get_Today)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @property
    def Year(self)->int:
        """

        """
        dlllib.DateTime_get_Year.argtypes=[c_void_p]
        dlllib.DateTime_get_Year.restype=c_int
        ret = CallCFunction(dlllib.DateTime_get_Year,self.Ptr)
        return ret

    @staticmethod

    def IsLeapYear(year:int)->bool:
        """

        """
        
        dlllib.DateTime_IsLeapYear.argtypes=[ c_int]
        dlllib.DateTime_IsLeapYear.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_IsLeapYear, year)
        return ret

    @staticmethod
    @dispatch

    def Parse(s:str)->'DateTime':
        """

        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            sPtr = StrToPtr(s)
            dlllib.DateTime_Parse.argtypes=[ c_char_p]
            dlllib.DateTime_Parse.restype=c_void_p
            intPtr = CallCFunction(dlllib.DateTime_Parse,sPtr)
            ret = None if intPtr==None else DateTime(intPtr)
            return ret
        else:
            dlllib.DateTime_Parse.argtypes=[ c_void_p]
            dlllib.DateTime_Parse.restype=c_void_p
            intPtr = CallCFunction(dlllib.DateTime_Parse, s)
            ret = None if intPtr==None else DateTime(intPtr)
            return ret
        


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider')->'DateTime':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.DateTime_ParseSP.argtypes=[ c_void_p,c_void_p]
#        dlllib.DateTime_ParseSP.restype=c_void_p
#        intPtr = CallCFunction(dlllib.DateTime_ParseSP, s,intPtrprovider)
#        ret = None if intPtr==None else DateTime(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def ParseExact(s:str,format:str,provider:'IFormatProvider')->'DateTime':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.DateTime_ParseExact.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.DateTime_ParseExact.restype=c_void_p
#        intPtr = CallCFunction(dlllib.DateTime_ParseExact, s,format,intPtrprovider)
#        ret = None if intPtr==None else DateTime(intPtr)
#        return ret
#


    @dispatch

    def Subtract(self ,value:'DateTime')->TimeSpan:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_Subtract.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_Subtract.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_Subtract,self.Ptr, intPtrvalue)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @dispatch

    def Subtract(self ,value:TimeSpan)->'DateTime':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.DateTime_SubtractV.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_SubtractV.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_SubtractV,self.Ptr, intPtrvalue)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    def ToOADate(self)->float:
        """

        """
        dlllib.DateTime_ToOADate.argtypes=[c_void_p]
        dlllib.DateTime_ToOADate.restype=c_double
        ret = CallCFunction(dlllib.DateTime_ToOADate,self.Ptr)
        return ret

    def ToFileTime(self)->int:
        """

        """
        dlllib.DateTime_ToFileTime.argtypes=[c_void_p]
        dlllib.DateTime_ToFileTime.restype=c_long
        ret = CallCFunction(dlllib.DateTime_ToFileTime,self.Ptr)
        return ret

    def ToFileTimeUtc(self)->int:
        """

        """
        dlllib.DateTime_ToFileTimeUtc.argtypes=[c_void_p]
        dlllib.DateTime_ToFileTimeUtc.restype=c_long
        ret = CallCFunction(dlllib.DateTime_ToFileTimeUtc,self.Ptr)
        return ret


    def ToLocalTime(self)->'DateTime':
        """

        """
        dlllib.DateTime_ToLocalTime.argtypes=[c_void_p]
        dlllib.DateTime_ToLocalTime.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_ToLocalTime,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @dispatch

    def ToString(self)->str:
        """

        """
        dlllib.DateTime_ToString.argtypes=[c_void_p]
        dlllib.DateTime_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.DateTime_ToString,self.Ptr))
        return ret


    @dispatch

    def ToString(self ,format:str)->str:
        """

        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            formatPtr = StrToPtr(format)
            dlllib.DateTime_ToStringF.argtypes=[c_void_p ,c_char_p]
            dlllib.DateTime_ToStringF.restype=c_void_p
            ret = PtrToStr(CallCFunction(dlllib.DateTime_ToStringF,self.Ptr, formatPtr))
            return ret
        else:
            dlllib.DateTime_ToStringF.argtypes=[c_void_p ,c_void_p]
            dlllib.DateTime_ToStringF.restype=c_void_p
            ret = PtrToStr(CallCFunction(dlllib.DateTime_ToStringF,self.Ptr, format))
            return ret
        


#    @dispatch
#
#    def ToString(self ,provider:'IFormatProvider')->str:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.DateTime_ToStringP.argtypes=[c_void_p ,c_void_p]
#        dlllib.DateTime_ToStringP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.DateTime_ToStringP,self.Ptr, intPtrprovider)
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
#        dlllib.DateTime_ToStringFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.DateTime_ToStringFP.restype=c_wchar_p
#        ret = CallCFunction(dlllib.DateTime_ToStringFP,self.Ptr, format,intPtrprovider)
#        return ret
#



    def ToUniversalTime(self)->'DateTime':
        """

        """
        dlllib.DateTime_ToUniversalTime.argtypes=[c_void_p]
        dlllib.DateTime_ToUniversalTime.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_ToUniversalTime,self.Ptr)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,result:'DateTime&')->bool:
#        """
#
#        """
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.DateTime_TryParse.argtypes=[ c_void_p,c_void_p]
#        dlllib.DateTime_TryParse.restype=c_bool
#        ret = CallCFunction(dlllib.DateTime_TryParse, s,intPtrresult)
#        return ret


    @staticmethod

    def op_Addition(d:'DateTime',t:'TimeSpan')->'DateTime':
        """

        """
        intPtrd:c_void_p = d.Ptr
        intPtrt:c_void_p = t.Ptr

        dlllib.DateTime_op_Addition.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_Addition.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_op_Addition, intPtrd,intPtrt)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod
    @dispatch

    def op_Subtraction(d:'DateTime',t:TimeSpan)->'DateTime':
        """

        """
        intPtrd:c_void_p = d.Ptr
        intPtrt:c_void_p = t.Ptr

        dlllib.DateTime_op_Subtraction.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_Subtraction.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_op_Subtraction, intPtrd,intPtrt)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod
    @dispatch

    def op_Subtraction(d1:'DateTime',d2:'DateTime')->TimeSpan:
        """

        """
        intPtrd1:c_void_p = d1.Ptr
        intPtrd2:c_void_p = d2.Ptr

        dlllib.DateTime_op_SubtractionDD.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_SubtractionDD.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_op_SubtractionDD, intPtrd1,intPtrd2)
        ret = None if intPtr==None else TimeSpan(intPtr)
        return ret


    @staticmethod

    def op_Equality(d1:'DateTime',d2:'DateTime')->bool:
        """

        """
        intPtrd1:c_void_p = d1.Ptr
        intPtrd2:c_void_p = d2.Ptr

        dlllib.DateTime_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_op_Equality, intPtrd1,intPtrd2)
        return ret

    @staticmethod

    def op_Inequality(d1:'DateTime',d2:'DateTime')->bool:
        """

        """
        intPtrd1:c_void_p = d1.Ptr
        intPtrd2:c_void_p = d2.Ptr

        dlllib.DateTime_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_op_Inequality, intPtrd1,intPtrd2)
        return ret

    @staticmethod

    def op_LessThan(t1:'DateTime',t2:'DateTime')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.DateTime_op_LessThan.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_LessThan.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_op_LessThan, intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_LessThanOrEqual(t1:'DateTime',t2:'DateTime')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.DateTime_op_LessThanOrEqual.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_LessThanOrEqual.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_op_LessThanOrEqual, intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_GreaterThan(t1:'DateTime',t2:'DateTime')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.DateTime_op_GreaterThan.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_GreaterThan.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_op_GreaterThan, intPtrt1,intPtrt2)
        return ret

    @staticmethod

    def op_GreaterThanOrEqual(t1:'DateTime',t2:'DateTime')->bool:
        """

        """
        intPtrt1:c_void_p = t1.Ptr
        intPtrt2:c_void_p = t2.Ptr

        dlllib.DateTime_op_GreaterThanOrEqual.argtypes=[ c_void_p,c_void_p]
        dlllib.DateTime_op_GreaterThanOrEqual.restype=c_bool
        ret = CallCFunction(dlllib.DateTime_op_GreaterThanOrEqual, intPtrt1,intPtrt2)
        return ret

    @dispatch

    def GetDateTimeFormats(self)->List[str]:
        """

        """
        dlllib.DateTime_GetDateTimeFormats.argtypes=[c_void_p]
        dlllib.DateTime_GetDateTimeFormats.restype=IntPtrArray
        intPtrArray = CallCFunction(dlllib.DateTime_GetDateTimeFormats,self.Ptr)
        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
        return ret

#    @dispatch
#
#    def GetDateTimeFormats(self ,provider:'IFormatProvider')->List[str]:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.DateTime_GetDateTimeFormatsP.argtypes=[c_void_p ,c_void_p]
#        dlllib.DateTime_GetDateTimeFormatsP.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.DateTime_GetDateTimeFormatsP,self.Ptr, intPtrprovider)
#        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
#        return ret


    @dispatch

    def GetDateTimeFormats(self ,format:int)->List[str]:
        """

        """
        
        dlllib.DateTime_GetDateTimeFormatsF.argtypes=[c_void_p ,c_void_p]
        dlllib.DateTime_GetDateTimeFormatsF.restype=IntPtrArray
        intPtrArray = CallCFunction(dlllib.DateTime_GetDateTimeFormatsF,self.Ptr, format)
        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
        return ret

#    @dispatch
#
#    def GetDateTimeFormats(self ,format:int,provider:'IFormatProvider')->List[str]:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.DateTime_GetDateTimeFormatsFP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        dlllib.DateTime_GetDateTimeFormatsFP.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.DateTime_GetDateTimeFormatsFP,self.Ptr, format,intPtrprovider)
#        ret = GetVectorFromArray(intPtrArray, c_wchar_p)
#        return ret


#
#    def GetTypeCode(self)->'TypeCode':
#        """
#
#        """
#        dlllib.DateTime_GetTypeCode.argtypes=[c_void_p]
#        dlllib.DateTime_GetTypeCode.restype=c_int
#        ret = CallCFunction(dlllib.DateTime_GetTypeCode,self.Ptr)
#        objwraped = TypeCode(ret)
#        return objwraped


#    @staticmethod
#    @dispatch
#
#    def Parse(s:str,provider:'IFormatProvider',styles:'DateTimeStyles')->'DateTime':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#        enumstyles:c_int = styles.value
#
#        dlllib.DateTime_ParseSPS.argtypes=[ c_void_p,c_void_p,c_int]
#        dlllib.DateTime_ParseSPS.restype=c_void_p
#        intPtr = CallCFunction(dlllib.DateTime_ParseSPS, s,intPtrprovider,enumstyles)
#        ret = None if intPtr==None else DateTime(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def ParseExact(s:str,format:str,provider:'IFormatProvider',style:'DateTimeStyles')->'DateTime':
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#        enumstyle:c_int = style.value
#
#        dlllib.DateTime_ParseExactSFPS.argtypes=[ c_void_p,c_void_p,c_void_p,c_int]
#        dlllib.DateTime_ParseExactSFPS.restype=c_void_p
#        intPtr = CallCFunction(dlllib.DateTime_ParseExactSFPS, s,format,intPtrprovider,enumstyle)
#        ret = None if intPtr==None else DateTime(intPtr)
#        return ret
#


#    @staticmethod
#    @dispatch
#
#    def ParseExact(s:str,formats:List[str],provider:'IFormatProvider',style:'DateTimeStyles')->'DateTime':
#        """
#
#        """
#        #arrayformats:ArrayTypeformats = ""
#        countformats = len(formats)
#        ArrayTypeformats = c_wchar_p * countformats
#        arrayformats = ArrayTypeformats()
#        for i in range(0, countformats):
#            arrayformats[i] = formats[i]
#
#        intPtrprovider:c_void_p = provider.Ptr
#        enumstyle:c_int = style.value
#
#        dlllib.DateTime_ParseExactSFPS1.argtypes=[ c_void_p,ArrayTypeformats,c_void_p,c_int]
#        dlllib.DateTime_ParseExactSFPS1.restype=c_void_p
#        intPtr = CallCFunction(dlllib.DateTime_ParseExactSFPS1, s,arrayformats,intPtrprovider,enumstyle)
#        ret = None if intPtr==None else DateTime(intPtr)
#        return ret
#



    def ToLongDateString(self)->str:
        """

        """
        dlllib.DateTime_ToLongDateString.argtypes=[c_void_p]
        dlllib.DateTime_ToLongDateString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.DateTime_ToLongDateString,self.Ptr))
        return ret



    def ToLongTimeString(self)->str:
        """

        """
        dlllib.DateTime_ToLongTimeString.argtypes=[c_void_p]
        dlllib.DateTime_ToLongTimeString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.DateTime_ToLongTimeString,self.Ptr))
        return ret



    def ToShortTimeString(self)->str:
        """

        """
        dlllib.DateTime_ToShortTimeString.argtypes=[c_void_p]
        dlllib.DateTime_ToShortTimeString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.DateTime_ToShortTimeString,self.Ptr))
        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParseExact(s:str,format:str,provider:'IFormatProvider',style:'DateTimeStyles',result:'DateTime&')->bool:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#        enumstyle:c_int = style.value
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.DateTime_TryParseExact.argtypes=[ c_void_p,c_void_p,c_void_p,c_int,c_void_p]
#        dlllib.DateTime_TryParseExact.restype=c_bool
#        ret = CallCFunction(dlllib.DateTime_TryParseExact, s,format,intPtrprovider,enumstyle,intPtrresult)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParseExact(s:str,formats:List[str],provider:'IFormatProvider',style:'DateTimeStyles',result:'DateTime&')->bool:
#        """
#
#        """
#        #arrayformats:ArrayTypeformats = ""
#        countformats = len(formats)
#        ArrayTypeformats = c_wchar_p * countformats
#        arrayformats = ArrayTypeformats()
#        for i in range(0, countformats):
#            arrayformats[i] = formats[i]
#
#        intPtrprovider:c_void_p = provider.Ptr
#        enumstyle:c_int = style.value
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.DateTime_TryParseExactSFPSR.argtypes=[ c_void_p,ArrayTypeformats,c_void_p,c_int,c_void_p]
#        dlllib.DateTime_TryParseExactSFPSR.restype=c_bool
#        ret = CallCFunction(dlllib.DateTime_TryParseExactSFPSR, s,arrayformats,intPtrprovider,enumstyle,intPtrresult)
#        return ret



    def ToShortDateString(self)->str:
        """

        """
        dlllib.DateTime_ToShortDateString.argtypes=[c_void_p]
        dlllib.DateTime_ToShortDateString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.DateTime_ToShortDateString,self.Ptr))
        return ret


#    @staticmethod
#    @dispatch
#
#    def TryParse(s:str,provider:'IFormatProvider',styles:'DateTimeStyles',result:'DateTime&')->bool:
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#        enumstyles:c_int = styles.value
#        intPtrresult:c_void_p = result.Ptr
#
#        dlllib.DateTime_TryParseSPSR.argtypes=[ c_void_p,c_void_p,c_int,c_void_p]
#        dlllib.DateTime_TryParseSPSR.restype=c_bool
#        ret = CallCFunction(dlllib.DateTime_TryParseSPSR, s,intPtrprovider,enumstyles,intPtrresult)
#        return ret


    @staticmethod

    def MinValue()->'DateTime':
        """

        """
        #dlllib.DateTime_MinValue.argtypes=[]
        dlllib.DateTime_MinValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_MinValue)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


    @staticmethod

    def MaxValue()->'DateTime':
        """

        """
        #dlllib.DateTime_MaxValue.argtypes=[]
        dlllib.DateTime_MaxValue.restype=c_void_p
        intPtr = CallCFunction(dlllib.DateTime_MaxValue)
        ret = None if intPtr==None else DateTime(intPtr)
        return ret


