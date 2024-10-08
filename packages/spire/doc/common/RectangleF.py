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

class RectangleF (SpireObject) :

    @dispatch
    def __init__(self, x:float, y:float, width:float, height:float):
        dlllib.RectangleF_CreateXYWH.argtypes=[c_float,c_float,c_float,c_float]
        dlllib.RectangleF_CreateXYWH.restype = c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_CreateXYWH,x, y, width, height)
        super(RectangleF, self).__init__(intPtr)

    @dispatch
    def __init__(self, location:PointF,size:SizeF):
        ptrPoint:c_void_p = location.Ptr
        ptrSize:c_void_p = size.Ptr

        dlllib.RectangleF_CreateLS.argtypes=[c_void_p,c_void_p]
        dlllib.RectangleF_CreateLS.restype = c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_CreateLS,ptrPoint,ptrSize)
        super(RectangleF, self).__init__(intPtr)
    """

    """
    @property

    def Location(self)->'PointF':
        """

        """
        dlllib.RectangleF_get_Location.argtypes=[c_void_p]
        dlllib.RectangleF_get_Location.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_get_Location,self.Ptr)
        ret = None if intPtr==None else PointF(intPtr)
        return ret


    @property

    def Size(self)->'SizeF':
        """

        """
        dlllib.RectangleF_get_Size.argtypes=[c_void_p]
        dlllib.RectangleF_get_Size.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_get_Size,self.Ptr)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @property
    def Right(self)->float:
        """

        """
        dlllib.RectangleF_get_Right.argtypes=[c_void_p]
        dlllib.RectangleF_get_Right.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Right,self.Ptr)
        return ret

    @property
    def Bottom(self)->float:
        """

        """
        dlllib.RectangleF_get_Bottom.argtypes=[c_void_p]
        dlllib.RectangleF_get_Bottom.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Bottom,self.Ptr)
        return ret

    @dispatch

    def Inflate(self ,x:float,y:float):
        """

        """
        
        dlllib.RectangleF_Inflate.argtypes=[c_void_p ,c_float,c_float]
        CallCFunction(dlllib.RectangleF_Inflate,self.Ptr, x,y)

    @staticmethod

    def Union(a:'RectangleF',b:'RectangleF')->'RectangleF':
        """

        """
        intPtra:c_void_p = a.Ptr
        intPtrb:c_void_p = b.Ptr

        dlllib.RectangleF_Union.argtypes=[ c_void_p,c_void_p]
        dlllib.RectangleF_Union.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_Union, intPtra,intPtrb)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


    @staticmethod

    def op_Implicit(r:'Rectangle')->'RectangleF':
        """

        """
        intPtrr:c_void_p = r.Ptr

        dlllib.RectangleF_op_Implicit.argtypes=[ c_void_p]
        dlllib.RectangleF_op_Implicit.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_op_Implicit, intPtrr)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


    @staticmethod

    def FromLTRB(left:float,top:float,right:float,bottom:float)->'RectangleF':
        """

        """
        
        dlllib.RectangleF_FromLTRB.argtypes=[ c_float,c_float,c_float,c_float]
        dlllib.RectangleF_FromLTRB.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_FromLTRB, left,top,right,bottom)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


    @Location.setter
    def Location(self, value:'PointF'):
        dlllib.RectangleF_set_Location.argtypes=[c_void_p, c_void_p]
        CallCFunction(dlllib.RectangleF_set_Location,self.Ptr, value.Ptr)

    @Size.setter
    def Size(self, value:'SizeF'):
        dlllib.RectangleF_set_Size.argtypes=[c_void_p, c_void_p]
        CallCFunction(dlllib.RectangleF_set_Size,self.Ptr, value.Ptr)

    @property
    def X(self)->float:
        """

        """
        dlllib.RectangleF_get_X.argtypes=[c_void_p]
        dlllib.RectangleF_get_X.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_X,self.Ptr)
        return ret

    @X.setter
    def X(self, value:float):
        dlllib.RectangleF_set_X.argtypes=[c_void_p, c_float]
        CallCFunction(dlllib.RectangleF_set_X,self.Ptr, value)

    @property
    def Y(self)->float:
        """

        """
        dlllib.RectangleF_get_Y.argtypes=[c_void_p]
        dlllib.RectangleF_get_Y.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Y,self.Ptr)
        return ret

    @Y.setter
    def Y(self, value:float):
        dlllib.RectangleF_set_Y.argtypes=[c_void_p, c_float]
        CallCFunction(dlllib.RectangleF_set_Y,self.Ptr, value)

    @property
    def Width(self)->float:
        """

        """
        dlllib.RectangleF_get_Width.argtypes=[c_void_p]
        dlllib.RectangleF_get_Width.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        dlllib.RectangleF_set_Width.argtypes=[c_void_p, c_float]
        CallCFunction(dlllib.RectangleF_set_Width,self.Ptr, value)

    @property
    def Height(self)->float:
        """

        """
        dlllib.RectangleF_get_Height.argtypes=[c_void_p]
        dlllib.RectangleF_get_Height.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        dlllib.RectangleF_set_Height.argtypes=[c_void_p, c_float]
        CallCFunction(dlllib.RectangleF_set_Height,self.Ptr, value)

    @property
    def Left(self)->float:
        """

        """
        dlllib.RectangleF_get_Left.argtypes=[c_void_p]
        dlllib.RectangleF_get_Left.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Left,self.Ptr)
        return ret

    @property
    def Top(self)->float:
        """

        """
        dlllib.RectangleF_get_Top.argtypes=[c_void_p]
        dlllib.RectangleF_get_Top.restype=c_float
        ret = CallCFunction(dlllib.RectangleF_get_Top,self.Ptr)
        return ret

    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.RectangleF_get_IsEmpty.argtypes=[c_void_p]
        dlllib.RectangleF_get_IsEmpty.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_get_IsEmpty,self.Ptr)
        return ret


    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.RectangleF_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.RectangleF_Equals.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_Equals,self.Ptr, intPtrobj)
        return ret

    @staticmethod

    def op_Equality(left:'RectangleF',right:'RectangleF')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.RectangleF_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.RectangleF_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_op_Equality, intPtrleft,intPtrright)
        return ret

    @staticmethod

    def op_Inequality(left:'RectangleF',right:'RectangleF')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.RectangleF_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.RectangleF_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_op_Inequality, intPtrleft,intPtrright)
        return ret

    @dispatch

    def Contains(self ,x:float,y:float)->bool:
        """

        """
        
        dlllib.RectangleF_Contains.argtypes=[c_void_p ,c_float,c_float]
        dlllib.RectangleF_Contains.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_Contains,self.Ptr, x,y)
        return ret

    @dispatch

    def Contains(self ,pt:PointF)->bool:
        """

        """
        intPtrpt:c_void_p = pt.Ptr

        dlllib.RectangleF_ContainsP.argtypes=[c_void_p ,c_void_p]
        dlllib.RectangleF_ContainsP.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_ContainsP,self.Ptr, intPtrpt)
        return ret

    @dispatch

    def Contains(self ,rect:'RectangleF')->bool:
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.RectangleF_ContainsR.argtypes=[c_void_p ,c_void_p]
        dlllib.RectangleF_ContainsR.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_ContainsR,self.Ptr, intPtrrect)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.RectangleF_GetHashCode.argtypes=[c_void_p]
        dlllib.RectangleF_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.RectangleF_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def Inflate(self ,size:SizeF):
        """

        """
        intPtrsize:c_void_p = size.Ptr

        dlllib.RectangleF_InflateS.argtypes=[c_void_p ,c_void_p]
        CallCFunction(dlllib.RectangleF_InflateS,self.Ptr, intPtrsize)

    @staticmethod
    @dispatch

    def Inflate(rect:'RectangleF',x:float,y:float)->'RectangleF':
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.RectangleF_InflateRXY.argtypes=[ c_void_p,c_float,c_float]
        dlllib.RectangleF_InflateRXY.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_InflateRXY, intPtrrect,x,y)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


    @dispatch

    def Intersect(self ,rect:'RectangleF'):
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.RectangleF_Intersect.argtypes=[c_void_p ,c_void_p]
        CallCFunction(dlllib.RectangleF_Intersect,self.Ptr, intPtrrect)

    @staticmethod
    @dispatch

    def Intersect(a:'RectangleF',b:'RectangleF')->'RectangleF':
        """

        """
        intPtra:c_void_p = a.Ptr
        intPtrb:c_void_p = b.Ptr

        dlllib.RectangleF_IntersectAB.argtypes=[ c_void_p,c_void_p]
        dlllib.RectangleF_IntersectAB.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_IntersectAB, intPtra,intPtrb)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret



    def IntersectsWith(self ,rect:'RectangleF')->bool:
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.RectangleF_IntersectsWith.argtypes=[c_void_p ,c_void_p]
        dlllib.RectangleF_IntersectsWith.restype=c_bool
        ret = CallCFunction(dlllib.RectangleF_IntersectsWith,self.Ptr, intPtrrect)
        return ret

    @dispatch

    def Offset(self ,pos:PointF):
        """

        """
        intPtrpos:c_void_p = pos.Ptr

        dlllib.RectangleF_Offset.argtypes=[c_void_p ,c_void_p]
        CallCFunction(dlllib.RectangleF_Offset,self.Ptr, intPtrpos)

    @dispatch

    def Offset(self ,x:float,y:float):
        """

        """
        
        dlllib.RectangleF_OffsetXY.argtypes=[c_void_p ,c_float,c_float]
        CallCFunction(dlllib.RectangleF_OffsetXY,self.Ptr, x,y)


    def ToString(self)->str:
        """

        """
        dlllib.RectangleF_ToString.argtypes=[c_void_p]
        dlllib.RectangleF_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.RectangleF_ToString,self.Ptr))
        return ret


    @staticmethod

    def Empty()->'RectangleF':
        """

        """
        #dlllib.RectangleF_Empty.argtypes=[]
        dlllib.RectangleF_Empty.restype=c_void_p
        intPtr = CallCFunction(dlllib.RectangleF_Empty)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


