from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class OfficeMath (  ParagraphBase, ICompositeObject) :
    """
    Represents an OfficeMath object in a document.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        :return: The type of the document object.
        """
        GetDllLibDoc().OfficeMath_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().OfficeMath_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ParentParagraph(self)->'Paragraph':
        """
        Gets the parent paragraph.
        :return: The parent paragraph.
        """
        GetDllLibDoc().OfficeMath_get_ParentParagraph.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_get_ParentParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().OfficeMath_get_ParentParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret



    def FromMathMLCode(self ,mathMLCode:str):
        """
        Creates an OfficeMath object from MathML code.
        :param mathMLCode: The MathML code.
        """
        mathMLCodePtr = StrToPtr(mathMLCode)
        GetDllLibDoc().OfficeMath_FromMathMLCode.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().OfficeMath_FromMathMLCode,self.Ptr, mathMLCodePtr)


    def FromLatexMathCode(self ,latexMathCode:str):
        """
        Creates an OfficeMath object from LaTeX math code.
        :param latexMathCode: The LaTeX math code.
        """
        latexMathCodePtr = StrToPtr(latexMathCode)
        GetDllLibDoc().OfficeMath_FromLatexMathCode.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().OfficeMath_FromLatexMathCode,self.Ptr, latexMathCodePtr)

#
#    def SaveAsImage(self ,imageType:'ImageType')->'SKImage':
#        """
#    <summary>
#        Save the OfficeMath object as Image
#    </summary>
#        """
#        enumimageType:c_int = imageType.value
#
#        GetDllLibDoc().OfficeMath_SaveAsImage.argtypes=[c_void_p ,c_int]
#        GetDllLibDoc().OfficeMath_SaveAsImage.restype=c_void_p
#        intPtr = GetDllLibDoc().OfficeMath_SaveAsImage(self.Ptr, enumimageType)
#        ret = None if intPtr==None else SKImage(intPtr)
#        return ret
#



    def ToMathMLCode(self)->str:
        """
        Converts the OfficeMath object to MathML code.
        :return: The MathML code.
        """
        GetDllLibDoc().OfficeMath_ToMathMLCode.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_ToMathMLCode.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().OfficeMath_ToMathMLCode,self.Ptr))
        return ret


    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects of the OfficeMath object.
        :return: The child objects.
        """
        GetDllLibDoc().OfficeMath_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().OfficeMath_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().OfficeMath_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


