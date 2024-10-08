from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ShapeObject (  Shape, IDocumentObject) :
    """
    Represents a shape object in a document.
    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        """
        Initializes a new instance of the ShapeObject class with the specified document.
        :param doc: The document to which the shape object belongs.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().ShapeObject_CreateShapeObjectD.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_CreateShapeObjectD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_CreateShapeObjectD,intPdoc)
        super(ShapeObject, self).__init__(intPtr)

    @dispatch
    def __init__(self, doc:'IDocument', shapeType:ShapeType):
        """
        Initializes a new instance of the ShapeObject class with the specified document and shape type.
        :param doc: The document to which the shape object belongs.
        :param shapeType: The type of the shape object.
        """
        intPdoc:c_void_p =  doc.Ptr
        iTypeshapeType:c_int = shapeType.value

        GetDllLibDoc().ShapeObject_CreateShapeObjectDS.argtypes = [c_void_p,c_int]
        GetDllLibDoc().ShapeObject_CreateShapeObjectDS.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_CreateShapeObjectDS,intPdoc,iTypeshapeType)
        super(ShapeObject, self).__init__(intPtr)

    @property

    def Chart(self)->'Chart':
        """
        Gets the chart object associated with this shape.
        :return: The chart object associated with this shape.
        """
        GetDllLibDoc().ShapeObject_get_Chart.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_Chart.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_get_Chart,self.Ptr)
        ret = None if intPtr==None else Chart(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        :return: The type of the document object.
        """
        GetDllLibDoc().ShapeObject_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeObject_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format of the shape object.
        :return: The character format of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def FillColor(self)->'Color':
        """
        Gets the fill color of the shape object.
        :return: The fill color of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_FillColor.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_FillColor.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_get_FillColor,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @FillColor.setter
    def FillColor(self, value:'Color'):
        """
        Sets the fill color of the shape object.
        :param value: The fill color to set.
        """
        GetDllLibDoc().ShapeObject_set_FillColor.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().ShapeObject_set_FillColor,self.Ptr, value.Ptr)

    #@FillTransparency.setter
    def FillTransparency(self, value:float):
        """
        Sets the fill transparency of the shape object.
        :param value: The fill transparency to set.
        """
        GetDllLibDoc().ShapeObject_set_FillTransparency.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeObject_set_FillTransparency,self.Ptr, value)

    @property
    def StrokeWeight(self)->float:
        """
        Gets the stroke weight of the shape object.
        :return: The stroke weight of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_StrokeWeight.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_StrokeWeight.restype=c_double
        ret = CallCFunction(GetDllLibDoc().ShapeObject_get_StrokeWeight,self.Ptr)
        return ret

    @StrokeWeight.setter
    def StrokeWeight(self, value:float):
        """
        Sets the stroke weight of the shape object.
        :param value: The stroke weight to set.
        """
        GetDllLibDoc().ShapeObject_set_StrokeWeight.argtypes=[c_void_p, c_double]
        CallCFunction(GetDllLibDoc().ShapeObject_set_StrokeWeight,self.Ptr, value)

    @property

    def StrokeColor(self)->'Color':
        """
        Gets the stroke color of the shape object.
        :return: The stroke color of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_StrokeColor.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_StrokeColor.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_get_StrokeColor,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @StrokeColor.setter
    def StrokeColor(self, value:'Color'):
        """
        Sets the stroke color of the shape object.
        :param value: The stroke color to set.
        """
        GetDllLibDoc().ShapeObject_set_StrokeColor.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().ShapeObject_set_StrokeColor,self.Ptr, value.Ptr)

    @property

    def LineStyle(self)->'ShapeLineStyle':
        """
        Gets the line style of the shape object.
        :return: The line style of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_LineStyle.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_LineStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeObject_get_LineStyle,self.Ptr)
        objwraped = ShapeLineStyle(ret)
        return objwraped

    @LineStyle.setter
    def LineStyle(self, value:'ShapeLineStyle'):
        """
        Sets the line style of the shape object.
        :param value: The line style to set.
        """
        GetDllLibDoc().ShapeObject_set_LineStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeObject_set_LineStyle,self.Ptr, value.value)

    @property

    def LineDashing(self)->'LineDashing':
        """
        Gets the line dashing of the shape object.
        :return: The line dashing of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_LineDashing.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_LineDashing.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ShapeObject_get_LineDashing,self.Ptr)
        objwraped = LineDashing(ret)
        return objwraped

    @LineDashing.setter
    def LineDashing(self, value:'LineDashing'):
        """
        Sets the line dashing of the shape object.
        :param value: The line dashing to set.
        """
        GetDllLibDoc().ShapeObject_set_LineDashing.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ShapeObject_set_LineDashing,self.Ptr, value.value)

    @property

    def WordArt(self)->'WordArt':
        """
        Gets the word art associated with this shape.
        :return: The word art associated with this shape.
        """
        GetDllLibDoc().ShapeObject_get_WordArt.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_WordArt.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_get_WordArt,self.Ptr)
        from spire.doc import WordArt
        ret = None if intPtr==None else WordArt(intPtr)
        return ret


    @property
    def ExtrusionEnabled(self)->bool:
        """
        Gets a value indicating whether extrusion is enabled for the shape object.
        :return: True if extrusion is enabled for the shape object; otherwise, False.
        """
        GetDllLibDoc().ShapeObject_get_ExtrusionEnabled.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_ExtrusionEnabled.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ShapeObject_get_ExtrusionEnabled,self.Ptr)
        return ret

    @property
    def ShadowEnabled(self)->bool:
        """
        Gets a value indicating whether shadow is enabled for the shape object.
        :return: True if shadow is enabled for the shape object; otherwise, False.
        """
        GetDllLibDoc().ShapeObject_get_ShadowEnabled.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_ShadowEnabled.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().ShapeObject_get_ShadowEnabled,self.Ptr)
        return ret

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects of the shape object.
        :return: The child objects of the shape object.
        """
        GetDllLibDoc().ShapeObject_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().ShapeObject_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ShapeObject_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


