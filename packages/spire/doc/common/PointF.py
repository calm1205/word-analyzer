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

class PointF (SpireObject) :
    @dispatch
    def __init__(self, x:float, y:float):
        dlllib.PointF_CreateXY.argtypes=[c_float,c_float]
        dlllib.PointF_CreateXY.restype = c_void_p
        intPtr = CallCFunction(dlllib.PointF_CreateXY,x, y)
        super(PointF, self).__init__(intPtr)
    """

    """
    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.PointF_get_IsEmpty.argtypes=[c_void_p]
        dlllib.PointF_get_IsEmpty.restype=c_bool
        ret = CallCFunction(dlllib.PointF_get_IsEmpty,self.Ptr)
        return ret

    @property
    def X(self)->float:
        """

        """
        dlllib.PointF_get_X.argtypes=[c_void_p]
        dlllib.PointF_get_X.restype=c_float
        ret = CallCFunction(dlllib.PointF_get_X,self.Ptr)
        return ret

    @X.setter
    def X(self, value:float):
        dlllib.PointF_set_X.argtypes=[c_void_p, c_float]
        CallCFunction(dlllib.PointF_set_X,self.Ptr, value)

    @property
    def Y(self)->float:
        """

        """
        dlllib.PointF_get_Y.argtypes=[c_void_p]
        dlllib.PointF_get_Y.restype=c_float
        ret = CallCFunction(dlllib.PointF_get_Y,self.Ptr)
        return ret

    @Y.setter
    def Y(self, value:float):
        dlllib.PointF_set_Y.argtypes=[c_void_p, c_float]
        CallCFunction(dlllib.PointF_set_Y,self.Ptr, value)

    @staticmethod
    @dispatch

    def op_Addition(pt:'PointF',sz:Size)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_op_Addition.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_op_Addition.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_op_Addition, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod
    @dispatch

    def op_Subtraction(pt:'PointF',sz:Size)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_op_Subtraction.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_op_Subtraction.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_op_Subtraction, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod
    @dispatch

    def op_Addition(pt:'PointF',sz:SizeF)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_op_AdditionPS.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_op_AdditionPS.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_op_AdditionPS, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod
    @dispatch

    def op_Subtraction(pt:'PointF',sz:SizeF)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_op_SubtractionPS.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_op_SubtractionPS.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_op_SubtractionPS, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod

    def op_Equality(left:'PointF',right:'PointF')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.PointF_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.PointF_op_Equality, intPtrleft,intPtrright)
        return ret

    @staticmethod

    def op_Inequality(left:'PointF',right:'PointF')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.PointF_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.PointF_op_Inequality, intPtrleft,intPtrright)
        return ret

    @staticmethod
    @dispatch

    def Add(pt:'PointF',sz:Size)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_Add.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_Add.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_Add, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod
    @dispatch

    def Subtract(pt:'PointF',sz:Size)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_Subtract.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_Subtract.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_Subtract, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod
    @dispatch

    def Add(pt:'PointF',sz:SizeF)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_AddPS.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_AddPS.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_AddPS, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @staticmethod
    @dispatch

    def Subtract(pt:'PointF',sz:SizeF)->'PointF':
        """

        """
        intPtrpt:c_void_p = pt.Ptr
        intPtrsz:c_void_p = sz.Ptr

        dlllib.PointF_SubtractPS.argtypes=[ c_void_p,c_void_p]
        dlllib.PointF_SubtractPS.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_SubtractPS, intPtrpt,intPtrsz)
        ret = None if intPtr==None else PointF(intPtr)
        return ret



    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.PointF_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.PointF_Equals.restype=c_bool
        ret = CallCFunction(dlllib.PointF_Equals,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.PointF_GetHashCode.argtypes=[c_void_p]
        dlllib.PointF_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.PointF_GetHashCode,self.Ptr)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.PointF_ToString.argtypes=[c_void_p]
        dlllib.PointF_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.PointF_ToString,self.Ptr))
        return ret


    @staticmethod

    def Empty()->'PointF':
        """

        """
        #dlllib.PointF_Empty.argtypes=[]
        dlllib.PointF_Empty.restype=c_void_p
        intPtr = CallCFunction(dlllib.PointF_Empty)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


