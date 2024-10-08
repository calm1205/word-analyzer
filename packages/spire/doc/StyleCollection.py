from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StyleCollection (  DocumentSerializableCollection, IStyleCollection) :
    """
    Represents a collection of styles.
    """

    def get_Item(self ,index:int)->'IStyle':
        """
        Gets the style at the specified index.

        Args:
            index: The index of the style.

        Returns:
            The style at the specified index.
        """
        
        GetDllLibDoc().StyleCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().StyleCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret

    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->IStyle:
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName =="Spire.Doc.Documents.ListStyle"):
            ret = ListStyle(intPtr)
        elif (strName =="Spire.Doc.Documents.ParagraphStyle"):
            ret = ParagraphStyle(intPtr)
        else:
            ret = Style(intPtr)
        return ret


    def Add(self ,style:'IStyle')->int:
        """
        Adds a style to the collection.

        Args:
            style: The style to add.

        Returns:
            The index of the added style.
        """
        intPtrstyle:c_void_p = style.Ptr

        GetDllLibDoc().StyleCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().StyleCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StyleCollection_Add,self.Ptr, intPtrstyle)
        return ret

    def ApplyDocDefaultsToNormalStyle(self):
        """
        Applies the document default paragraph format and character format to the normal style.
        """
        GetDllLibDoc().StyleCollection_ApplyDocDefaultsToNormalStyle.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StyleCollection_ApplyDocDefaultsToNormalStyle,self.Ptr)

    @dispatch

    def FindByName(self ,name:str)->Style:
        """
        Finds a style by name.

        Args:
            name: The name of the style.

        Returns:
            The style with the specified name.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().StyleCollection_FindByName.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().StyleCollection_FindByName.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StyleCollection_FindByName,self.Ptr, namePtr)
        ret = None if intPtr==None else Style(intPtr)
        return ret


    @dispatch

    def FindByName(self ,name:str,styleType:StyleType)->IStyle:
        """
        Finds a style by name and style type.

        Args:
            name: The name of the style.
            styleType: The type of the style.

        Returns:
            The style with the specified name and style type.
        """
        namePtr = StrToPtr(name)
        enumstyleType:c_int = styleType.value

        GetDllLibDoc().StyleCollection_FindByNameNS.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().StyleCollection_FindByNameNS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StyleCollection_FindByNameNS,self.Ptr, namePtr,enumstyleType)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def FindById(self ,styleId:int)->'IStyle':
        """
        Finds a style by id.

        Args:
            styleId: The id of the style.

        Returns:
            The style with the specified id.
        """
        
        GetDllLibDoc().StyleCollection_FindById.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_FindById.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StyleCollection_FindById,self.Ptr, styleId)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def FindByIstd(self ,istd:int)->'IStyle':
        """
        Finds a style by istd.

        Args:
            istd: The istd of the style.

        Returns:
            The style with the specified istd.
        """
        
        GetDllLibDoc().StyleCollection_FindByIstd.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_FindByIstd.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StyleCollection_FindByIstd,self.Ptr, istd)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def FindByIdentifier(self ,sIdentifier:int)->'IStyle':
        """
        Finds a style by identifier.

        Args:
            sIdentifier: The style identifier. The parameter value is the Spire.Doc.Documents.BuiltinStyle enumeration value or the Spire.Doc.Documents.DefaultTableStyle enumeration value.

        Returns:
            The style with the specified identifier.
        """
        
        GetDllLibDoc().StyleCollection_FindByIdentifier.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().StyleCollection_FindByIdentifier.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StyleCollection_FindByIdentifier,self.Ptr, sIdentifier)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret


