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

class Rectangle (SpireObject) :
    """

    """
    @staticmethod

    def FromLTRB(left:int,top:int,right:int,bottom:int)->'Rectangle':
        """

        """
        
        dlllib.Rectangle_FromLTRB.argtypes=[ c_int,c_int,c_int,c_int]
        dlllib.Rectangle_FromLTRB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_FromLTRB, left,top,right,bottom)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


    @property

    def Location(self)->'Point':
        """

        """
        dlllib.Rectangle_get_Location.argtypes=[c_void_p]
        dlllib.Rectangle_get_Location.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_get_Location,self.Ptr)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @property

    def SIZE(self)->'Size':
        """

        """
        dlllib.Rectangle_get_Size.argtypes=[c_void_p]
        dlllib.Rectangle_get_Size.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_get_Size,self.Ptr)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @SIZE.setter
    def SIZE(self, value:'Size'):
        dlllib.Rectangle_set_Size.argtypes=[c_void_p, c_void_p]
        CallCFunction(dlllib.Rectangle_set_Size,self.Ptr, value.Ptr)

    @property
    def X(self)->int:
        """

        """
        dlllib.Rectangle_get_X.argtypes=[c_void_p]
        dlllib.Rectangle_get_X.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_X,self.Ptr)
        return ret

    @X.setter
    def X(self, value:int):
        dlllib.Rectangle_set_X.argtypes=[c_void_p, c_int]
        CallCFunction(dlllib.Rectangle_set_X,self.Ptr, value)

    @property
    def Y(self)->int:
        """

        """
        dlllib.Rectangle_get_Y.argtypes=[c_void_p]
        dlllib.Rectangle_get_Y.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Y,self.Ptr)
        return ret

    @Y.setter
    def Y(self, value:int):
        dlllib.Rectangle_set_Y.argtypes=[c_void_p, c_int]
        CallCFunction(dlllib.Rectangle_set_Y,self.Ptr, value)

    @property
    def Width(self)->int:
        """

        """
        dlllib.Rectangle_get_Width.argtypes=[c_void_p]
        dlllib.Rectangle_get_Width.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:int):
        dlllib.Rectangle_set_Width.argtypes=[c_void_p, c_int]
        CallCFunction(dlllib.Rectangle_set_Width,self.Ptr, value)

    @property
    def Height(self)->int:
        """

        """
        dlllib.Rectangle_get_Height.argtypes=[c_void_p]
        dlllib.Rectangle_get_Height.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:int):
        dlllib.Rectangle_set_Height.argtypes=[c_void_p, c_int]
        CallCFunction(dlllib.Rectangle_set_Height,self.Ptr, value)

    @property
    def Left(self)->int:
        """

        """
        dlllib.Rectangle_get_Left.argtypes=[c_void_p]
        dlllib.Rectangle_get_Left.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Left,self.Ptr)
        return ret

    @property
    def Right(self)->int:
        """

        """
        dlllib.Rectangle_get_Right.argtypes=[c_void_p]
        dlllib.Rectangle_get_Right.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Right,self.Ptr)
        return ret

    @property
    def Bottom(self)->int:
        """

        """
        dlllib.Rectangle_get_Bottom.argtypes=[c_void_p]
        dlllib.Rectangle_get_Bottom.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Bottom,self.Ptr)
        return ret

    @staticmethod

    def op_Equality(left:'Rectangle',right:'Rectangle')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.Rectangle_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.Rectangle_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_op_Equality, intPtrleft,intPtrright)
        return ret

    @staticmethod

    def Truncate(value:'RectangleF')->'Rectangle':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Rectangle_Truncate.argtypes=[ c_void_p]
        dlllib.Rectangle_Truncate.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_Truncate, intPtrvalue)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


    @dispatch

    def Contains(self ,x:int,y:int)->bool:
        """

        """
        
        dlllib.Rectangle_Contains.argtypes=[c_void_p ,c_int,c_int]
        dlllib.Rectangle_Contains.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_Contains,self.Ptr, x,y)
        return ret

    @dispatch

    def Contains(self ,pt:Point)->bool:
        """

        """
        intPtrpt:c_void_p = pt.Ptr

        dlllib.Rectangle_ContainsP.argtypes=[c_void_p ,c_void_p]
        dlllib.Rectangle_ContainsP.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_ContainsP,self.Ptr, intPtrpt)
        return ret

    @dispatch

    def Contains(self ,rect:'Rectangle')->bool:
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.Rectangle_ContainsR.argtypes=[c_void_p ,c_void_p]
        dlllib.Rectangle_ContainsR.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_ContainsR,self.Ptr, intPtrrect)
        return ret

    @dispatch

    def Inflate(self ,width:int,height:int):
        """

        """
        
        dlllib.Rectangle_Inflate.argtypes=[c_void_p ,c_int,c_int]
        CallCFunction(dlllib.Rectangle_Inflate,self.Ptr, width,height)

    @dispatch

    def Intersect(self ,rect:'Rectangle'):
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.Rectangle_Intersect.argtypes=[c_void_p ,c_void_p]
        CallCFunction(dlllib.Rectangle_Intersect,self.Ptr, intPtrrect)

    @staticmethod
    @dispatch

    def Intersect(a:'Rectangle',b:'Rectangle')->'Rectangle':
        """

        """
        intPtra:c_void_p = a.Ptr
        intPtrb:c_void_p = b.Ptr

        dlllib.Rectangle_IntersectAB.argtypes=[ c_void_p,c_void_p]
        dlllib.Rectangle_IntersectAB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_IntersectAB, intPtra,intPtrb)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret



    def IntersectsWith(self ,rect:'Rectangle')->bool:
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.Rectangle_IntersectsWith.argtypes=[c_void_p ,c_void_p]
        dlllib.Rectangle_IntersectsWith.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_IntersectsWith,self.Ptr, intPtrrect)
        return ret

    @staticmethod

    def Union(a:'Rectangle',b:'Rectangle')->'Rectangle':
        """

        """
        intPtra:c_void_p = a.Ptr
        intPtrb:c_void_p = b.Ptr

        dlllib.Rectangle_Union.argtypes=[ c_void_p,c_void_p]
        dlllib.Rectangle_Union.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_Union, intPtra,intPtrb)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


    @Location.setter
    def Location(self, value:'Point'):
        dlllib.Rectangle_set_Location.argtypes=[c_void_p, c_void_p]
        CallCFunction(dlllib.Rectangle_set_Location,self.Ptr, value.Ptr)

    @property
    def Top(self)->int:
        """

        """
        dlllib.Rectangle_get_Top.argtypes=[c_void_p]
        dlllib.Rectangle_get_Top.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_get_Top,self.Ptr)
        return ret

    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.Rectangle_get_IsEmpty.argtypes=[c_void_p]
        dlllib.Rectangle_get_IsEmpty.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_get_IsEmpty,self.Ptr)
        return ret


    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Rectangle_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Rectangle_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_Equals,self.Ptr, intPtrobj)
        return ret

    @staticmethod

    def op_Inequality(left:'Rectangle',right:'Rectangle')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.Rectangle_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.Rectangle_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.Rectangle_op_Inequality, intPtrleft,intPtrright)
        return ret

    @staticmethod

    def Ceiling(value:'RectangleF')->'Rectangle':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Rectangle_Ceiling.argtypes=[ c_void_p]
        dlllib.Rectangle_Ceiling.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_Ceiling, intPtrvalue)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


    @staticmethod

    def Round(value:'RectangleF')->'Rectangle':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Rectangle_Round.argtypes=[ c_void_p]
        dlllib.Rectangle_Round.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_Round, intPtrvalue)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


    def GetHashCode(self)->int:
        """

        """
        dlllib.Rectangle_GetHashCode.argtypes=[c_void_p]
        dlllib.Rectangle_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Rectangle_GetHashCode,self.Ptr)
        return ret

    @dispatch

    def Inflate(self ,size:Size):
        """

        """
        intPtrsize:c_void_p = size.Ptr

        dlllib.Rectangle_InflateS.argtypes=[c_void_p ,c_void_p]
        CallCFunction(dlllib.Rectangle_InflateS,self.Ptr, intPtrsize)

    @staticmethod
    @dispatch

    def Inflate(rect:'Rectangle',x:int,y:int)->'Rectangle':
        """

        """
        intPtrrect:c_void_p = rect.Ptr

        dlllib.Rectangle_InflateRXY.argtypes=[ c_void_p,c_int,c_int]
        dlllib.Rectangle_InflateRXY.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_InflateRXY, intPtrrect,x,y)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


    @dispatch

    def Offset(self ,pos:Point):
        """

        """
        intPtrpos:c_void_p = pos.Ptr

        dlllib.Rectangle_Offset.argtypes=[c_void_p ,c_void_p]
        CallCFunction(dlllib.Rectangle_Offset,self.Ptr, intPtrpos)

    @dispatch

    def Offset(self ,x:int,y:int):
        """

        """
        
        dlllib.Rectangle_OffsetXY.argtypes=[c_void_p ,c_int,c_int]
        CallCFunction(dlllib.Rectangle_OffsetXY,self.Ptr, x,y)


    def ToString(self)->str:
        """

        """
        dlllib.Rectangle_ToString.argtypes=[c_void_p]
        dlllib.Rectangle_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Rectangle_ToString,self.Ptr))
        return ret


    @staticmethod

    def Empty()->'Rectangle':
        """

        """
        #dlllib.Rectangle_Empty.argtypes=[]
        dlllib.Rectangle_Empty.restype=c_void_p
        intPtr = CallCFunction(dlllib.Rectangle_Empty)
        ret = None if intPtr==None else Rectangle(intPtr)
        return ret


