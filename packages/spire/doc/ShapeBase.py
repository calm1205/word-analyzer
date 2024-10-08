from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeBase (  ParagraphBase) :
    """
    Base class for shapes.
    """
    @property
    def HasImage(self)->bool:
        """
        Check if the shape has an image.
        """
        GetDllLibDoc().ShapeBase_get_HasImage.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_HasImage.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_HasImage,self.Ptr)
        return ret

    @property
    def VerticalPosition(self)->float:
        """
        Get the vertical position of the shape.
        """
        GetDllLibDoc().ShapeBase_get_VerticalPosition.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_VerticalPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_VerticalPosition,self.Ptr)
        return ret

    @VerticalPosition.setter
    def VerticalPosition(self, value:float):
        """
        Set the vertical position of the shape.
        """
        GetDllLibDoc().ShapeBase_set_VerticalPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().ShapeBase_set_VerticalPosition,self.Ptr, value)

    @property
    def Right(self)->float:
        """
        Get the right position of the shape.
        """
        GetDllLibDoc().ShapeBase_get_Right.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_Right.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_Right,self.Ptr)
        return ret

    @property
    def Bottom(self)->float:
        """
        Get the bottom position of the shape.
        """
        GetDllLibDoc().ShapeBase_get_Bottom.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_Bottom.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_Bottom,self.Ptr)
        return ret

    @property
    def Width(self)->float:
        """
        Get the width of the shape.
        """
        GetDllLibDoc().ShapeBase_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_Width.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        """
        Set the width of the shape.
        """
        GetDllLibDoc().ShapeBase_set_Width.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_Width,self.Ptr, value)

    @property
    def Height(self)->float:
        """
        Get the height of the shape.
        """
        GetDllLibDoc().ShapeBase_get_Height.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_Height.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        """
        Set the height of the shape.
        """
        GetDllLibDoc().ShapeBase_set_Height.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_Height,self.Ptr, value)

    @property
    def DistanceTop(self)->float:
        """
        Get the distance from the top of the shape.
        """
        GetDllLibDoc().ShapeBase_get_DistanceTop.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_DistanceTop.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_DistanceTop,self.Ptr)
        return ret

    @DistanceTop.setter
    def DistanceTop(self, value:float):
        """
        Set the distance from the top of the shape.
        """
        GetDllLibDoc().ShapeBase_set_DistanceTop.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_DistanceTop,self.Ptr, value)

    @property
    def DistanceBottom(self)->float:
        """
        Get the distance from the bottom of the shape.
        """
        GetDllLibDoc().ShapeBase_get_DistanceBottom.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_DistanceBottom.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_DistanceBottom,self.Ptr)
        return ret

    @DistanceBottom.setter
    def DistanceBottom(self, value:float):
        """
        Set the distance from the bottom of the shape.
        """
        GetDllLibDoc().ShapeBase_set_DistanceBottom.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_DistanceBottom,self.Ptr, value)

    @property
    def DistanceLeft(self)->float:
        """
        Get the distance from the left of the shape.
        """
        GetDllLibDoc().ShapeBase_get_DistanceLeft.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_DistanceLeft.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_DistanceLeft,self.Ptr)
        return ret

    @DistanceLeft.setter
    def DistanceLeft(self, value:float):
        """
        Set the distance from the left of the shape.
        """
        GetDllLibDoc().ShapeBase_set_DistanceLeft.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_DistanceLeft,self.Ptr, value)

    @property
    def DistanceRight(self)->float:
        """
        Get the distance from the right of the shape.
        """
        GetDllLibDoc().ShapeBase_get_DistanceRight.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_DistanceRight.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_DistanceRight,self.Ptr)
        return ret

    @DistanceRight.setter
    def DistanceRight(self, value:float):
        """
        Set the distance from the right of the shape.
        """
        GetDllLibDoc().ShapeBase_set_DistanceRight.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_DistanceRight,self.Ptr, value)

    @property
    def Rotation(self)->float:
        """
        Get the rotation of the shape.
        """
        GetDllLibDoc().ShapeBase_get_Rotation.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_Rotation.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_Rotation,self.Ptr)
        return ret

    @Rotation.setter
    def Rotation(self, value:float):
        GetDllLibDoc().ShapeBase_set_Rotation.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeBase_set_Rotation,self.Ptr, value)

    @property
    def ZOrder(self)->int:
        """

        """
        GetDllLibDoc().ShapeBase_get_ZOrder.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_ZOrder.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_ZOrder,self.Ptr)
        return ret

    @ZOrder.setter
    def ZOrder(self, value:int):
        GetDllLibDoc().ShapeBase_set_ZOrder.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_ZOrder,self.Ptr, value)


    def AdjustWithEffects(self ,source:'RectangleF')->'RectangleF':
        """

        """
        intPtrsource:c_void_p = source.Ptr

        GetDllLibDoc().ShapeBase_AdjustWithEffects.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ShapeBase_AdjustWithEffects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_AdjustWithEffects,self.Ptr, intPtrsource)
        ret = None if intPtr==None else RectangleF(intPtr)
        return ret


    @property

    def ShapeType(self)->'ShapeType':
        """

        """
        GetDllLibDoc().ShapeBase_get_ShapeType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_ShapeType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_ShapeType,self.Ptr)
        objwraped = ShapeType(ret)
        return objwraped

    @property

    def HorizontalOrigin(self)->'HorizontalOrigin':
        """

        """
        GetDllLibDoc().ShapeBase_get_HorizontalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_HorizontalOrigin.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_HorizontalOrigin,self.Ptr)
        objwraped = HorizontalOrigin(ret)
        return objwraped

    @HorizontalOrigin.setter
    def HorizontalOrigin(self, value:'HorizontalOrigin'):
        GetDllLibDoc().ShapeBase_set_HorizontalOrigin.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_HorizontalOrigin,self.Ptr, value.value)

    @property

    def VerticalOrigin(self)->'VerticalOrigin':
        """

        """
        GetDllLibDoc().ShapeBase_get_VerticalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_VerticalOrigin.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_VerticalOrigin,self.Ptr)
        objwraped = VerticalOrigin(ret)
        return objwraped

    @VerticalOrigin.setter
    def VerticalOrigin(self, value:'VerticalOrigin'):
        GetDllLibDoc().ShapeBase_set_VerticalOrigin.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_VerticalOrigin,self.Ptr, value.value)

    @property

    def HorizontalAlignment(self)->'ShapeHorizontalAlignment':
        """

        """
        GetDllLibDoc().ShapeBase_get_HorizontalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_HorizontalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_HorizontalAlignment,self.Ptr)
        objwraped = ShapeHorizontalAlignment(ret)
        return objwraped

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value:'ShapeHorizontalAlignment'):
        GetDllLibDoc().ShapeBase_set_HorizontalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_HorizontalAlignment,self.Ptr, value.value)

    @property

    def VerticalAlignment(self)->'ShapeVerticalAlignment':
        """

        """
        GetDllLibDoc().ShapeBase_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_VerticalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_VerticalAlignment,self.Ptr)
        objwraped = ShapeVerticalAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'ShapeVerticalAlignment'):
        GetDllLibDoc().ShapeBase_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_VerticalAlignment,self.Ptr, value.value)

    @property

    def WrapType(self)->'TextWrappingStyle':
        """

        """
        GetDllLibDoc().ShapeBase_get_WrapType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_WrapType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_WrapType,self.Ptr)
        objwraped = TextWrappingStyle(ret)
        return objwraped

    @WrapType.setter
    def WrapType(self, value:'TextWrappingStyle'):
        GetDllLibDoc().ShapeBase_set_WrapType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_WrapType,self.Ptr, value.value)

    @property

    def TextWrappingStyle(self)->'TextWrappingStyle':
        """

        """
        GetDllLibDoc().ShapeBase_get_TextWrappingStyle.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_TextWrappingStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_TextWrappingStyle,self.Ptr)
        objwraped = TextWrappingStyle(ret)
        return objwraped

    @TextWrappingStyle.setter
    def TextWrappingStyle(self, value:'TextWrappingStyle'):
        GetDllLibDoc().ShapeBase_set_TextWrappingStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_TextWrappingStyle,self.Ptr, value.value)

    @property

    def TextWrappingType(self)->'TextWrappingType':
        """

        """
        GetDllLibDoc().ShapeBase_get_TextWrappingType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_TextWrappingType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_TextWrappingType,self.Ptr)
        objwraped = TextWrappingType(ret)
        return objwraped

    @TextWrappingType.setter
    def TextWrappingType(self, value:'TextWrappingType'):
        GetDllLibDoc().ShapeBase_set_TextWrappingType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_set_TextWrappingType,self.Ptr, value.value)

    @property

    def CoordOrigin(self)->'Point':
        """

        """
        GetDllLibDoc().ShapeBase_get_CoordOrigin.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_CoordOrigin.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_get_CoordOrigin,self.Ptr)
        ret = None if intPtr==None else Point(intPtr)
        return ret


    @CoordOrigin.setter
    def CoordOrigin(self, value:'Point'):
        GetDllLibDoc().ShapeBase_set_CoordOrigin.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().ShapeBase_set_CoordOrigin,self.Ptr, value.Ptr)

    @property

    def CoordSize(self)->'Size':
        """

        """
        GetDllLibDoc().ShapeBase_get_CoordSize.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_CoordSize.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_get_CoordSize,self.Ptr)
        ret = None if intPtr==None else Size(intPtr)
        return ret


    @CoordSize.setter
    def CoordSize(self, value:'Size'):
        GetDllLibDoc().ShapeBase_set_CoordSize.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().ShapeBase_set_CoordSize,self.Ptr, value.Ptr)

    @property
    def IsSignatureLine(self)->bool:
        """

        """
        GetDllLibDoc().ShapeBase_get_IsSignatureLine.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_IsSignatureLine.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_IsSignatureLine,self.Ptr)
        return ret

    @property

    def Size(self)->'SizeF':
        """

        """
        GetDllLibDoc().ShapeBase_get_Size.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_Size.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_get_Size,self.Ptr)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret



    def GetDirectShapeAttr(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().ShapeBase_GetDirectShapeAttr.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_GetDirectShapeAttr.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_GetDirectShapeAttr,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def FetchInheritedShapeAttr(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().ShapeBase_FetchInheritedShapeAttr.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_FetchInheritedShapeAttr.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_FetchInheritedShapeAttr,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def FetchShapeAttr(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().ShapeBase_FetchShapeAttr.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_FetchShapeAttr.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_FetchShapeAttr,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def SetShapeAttr(self ,key:int,value:'SpireObject'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().ShapeBase_SetShapeAttr.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().ShapeBase_SetShapeAttr,self.Ptr, key,intPtrvalue)


    def RemoveShapeAttr(self ,key:int):
        """

        """
        
        GetDllLibDoc().ShapeBase_RemoveShapeAttr.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_RemoveShapeAttr,self.Ptr, key)


    def GetDirectShapeAttribute(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().ShapeBase_GetDirectShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_GetDirectShapeAttribute.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_GetDirectShapeAttribute,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def GetInheritedShapeAttribute(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().ShapeBase_GetInheritedShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_GetInheritedShapeAttribute.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_GetInheritedShapeAttribute,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def GetShapeAttribute(self ,key:int)->'SpireObject':
        """

        """
        
        GetDllLibDoc().ShapeBase_GetShapeAttribute.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_GetShapeAttribute.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_GetShapeAttribute,self.Ptr, key)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret



    def SetShapeAttribute(self ,key:int,value:'SpireObject'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().ShapeBase_SetShapeAttribute.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().ShapeBase_SetShapeAttribute,self.Ptr, key,intPtrvalue)


    def RemoveShapeAttribute(self ,key:int):
        """

        """
        
        GetDllLibDoc().ShapeBase_RemoveShapeAttribute.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_RemoveShapeAttribute,self.Ptr, key)


    def HasKey(self ,key:int)->bool:
        """

        """
        
        GetDllLibDoc().ShapeBase_HasKey.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ShapeBase_HasKey.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ShapeBase_HasKey,self.Ptr, key)
        return ret


    def LocalToParent(self ,value:'PointF')->'PointF':
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().ShapeBase_LocalToParent.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().ShapeBase_LocalToParent.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_LocalToParent,self.Ptr, intPtrvalue)
        ret = None if intPtr==None else PointF(intPtr)
        return ret



    def SetShapeType(self ,shapeType:'ShapeType'):
        """

        """
        enumshapeType:c_int = shapeType.value

        GetDllLibDoc().ShapeBase_SetShapeType.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().ShapeBase_SetShapeType,self.Ptr, enumshapeType)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects of the entity.
        """
        GetDllLibDoc().ShapeBase_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeBase_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def AlternativeText(self)->str:
        """
        Gets or sets the alternative text. 
        """
        GetDllLibDoc().ShapeBase_get_AlternativeText.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_AlternativeText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().ShapeBase_get_AlternativeText,self.Ptr))
        return ret


    @AlternativeText.setter
    def AlternativeText(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().ShapeBase_set_AlternativeText.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().ShapeBase_set_AlternativeText,self.Ptr, valuePtr)

    @property
    def HorizontalPosition(self)->float:
        """

        """
        GetDllLibDoc().ShapeBase_get_HorizontalPosition.argtypes=[c_void_p]
        GetDllLibDoc().ShapeBase_get_HorizontalPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().ShapeBase_get_HorizontalPosition,self.Ptr)
        return ret

    @HorizontalPosition.setter
    def HorizontalPosition(self, value:float):
        GetDllLibDoc().ShapeBase_set_HorizontalPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().ShapeBase_set_HorizontalPosition,self.Ptr, value)

