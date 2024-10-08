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

class Size (SpireObject) :
    """

    """
    @staticmethod

    def op_Implicit(p:'Size')->'SizeF':
        """

        """
        intPtrp:c_void_p = p.Ptr

        dlllib.Size_op_Implicit.argtypes=[ c_void_p]
        dlllib.Size_op_Implicit.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_op_Implicit, intPtrp)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @staticmethod

    def op_Addition(sz1:'Size',sz2:'Size')->'Size':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.Size_op_Addition.argtypes=[ c_void_p,c_void_p]
        dlllib.Size_op_Addition.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_op_Addition, intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def op_Subtraction(sz1:'Size',sz2:'Size')->'Size':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.Size_op_Subtraction.argtypes=[ c_void_p,c_void_p]
        dlllib.Size_op_Subtraction.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_op_Subtraction, intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def op_Equality(sz1:'Size',sz2:'Size')->bool:
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.Size_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.Size_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.Size_op_Equality, intPtrsz1,intPtrsz2)
        return ret

    @staticmethod

    def op_Inequality(sz1:'Size',sz2:'Size')->bool:
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.Size_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.Size_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.Size_op_Inequality, intPtrsz1,intPtrsz2)
        return ret

    @staticmethod

    def op_Explicit(size:'Size')->'Point':
        """

        """
        intPtrsize:c_void_p = size.Ptr

        dlllib.Size_op_Explicit.argtypes=[ c_void_p]
        dlllib.Size_op_Explicit.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_op_Explicit, intPtrsize)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.Size_get_IsEmpty.argtypes=[c_void_p]
        dlllib.Size_get_IsEmpty.restype=c_bool
        ret = CallCFunction(dlllib.Size_get_IsEmpty,self.Ptr)
        return ret

    @property
    def Width(self)->int:
        """

        """
        dlllib.Size_get_Width.argtypes=[c_void_p]
        dlllib.Size_get_Width.restype=c_int
        ret = CallCFunction(dlllib.Size_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:int):
        dlllib.Size_set_Width.argtypes=[c_void_p, c_int]
        CallCFunction(dlllib.Size_set_Width,self.Ptr, value)

    @property
    def Height(self)->int:
        """

        """
        dlllib.Size_get_Height.argtypes=[c_void_p]
        dlllib.Size_get_Height.restype=c_int
        ret = CallCFunction(dlllib.Size_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:int):
        dlllib.Size_set_Height.argtypes=[c_void_p, c_int]
        CallCFunction(dlllib.Size_set_Height,self.Ptr, value)

    @staticmethod

    def Add(sz1:'Size',sz2:'Size')->'Size':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.Size_Add.argtypes=[ c_void_p,c_void_p]
        dlllib.Size_Add.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_Add, intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def Ceiling(value:'SizeF')->'Size':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Size_Ceiling.argtypes=[ c_void_p]
        dlllib.Size_Ceiling.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_Ceiling, intPtrvalue)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def Subtract(sz1:'Size',sz2:'Size')->'Size':
        """

        """
        intPtrsz1:c_void_p = sz1.Ptr
        intPtrsz2:c_void_p = sz2.Ptr

        dlllib.Size_Subtract.argtypes=[ c_void_p,c_void_p]
        dlllib.Size_Subtract.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_Subtract, intPtrsz1,intPtrsz2)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def Truncate(value:'SizeF')->'Size':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Size_Truncate.argtypes=[ c_void_p]
        dlllib.Size_Truncate.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_Truncate, intPtrvalue)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @staticmethod

    def Round(value:'SizeF')->'Size':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Size_Round.argtypes=[ c_void_p]
        dlllib.Size_Round.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_Round, intPtrvalue)
        ret = None if intPtr==None else Size(intPtr)
        return ret



    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Size_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Size_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Size_Equals,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Size_GetHashCode.argtypes=[c_void_p]
        dlllib.Size_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Size_GetHashCode,self.Ptr)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.Size_ToString.argtypes=[c_void_p]
        dlllib.Size_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Size_ToString,self.Ptr))
        return ret


    @staticmethod

    def Empty()->'Size':
        """

        """
        #dlllib.Size_Empty.argtypes=[]
        dlllib.Size_Empty.restype=c_void_p
        intPtr = CallCFunction(dlllib.Size_Empty)
        ret = None if intPtr==None else Size(intPtr)
        return ret


