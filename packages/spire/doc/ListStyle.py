from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class ListStyle (  Style, IStyle) :
    """
    Represents a list style.
    """
    @dispatch
    def __init__(self, doc:IDocument, listType:ListType):
        """
        Initializes a new instance of the ListStyle class.

        Args:
            doc (IDocument): The document.
            listType (ListType): The type of the list.
        """
        intPdoc:c_void_p =  doc.Ptr
        iTypelistType:c_int = listType.value

        GetDllLibDoc().ListStyle_CreateListStyleDL.argtypes=[c_void_p,c_int]
        GetDllLibDoc().ListStyle_CreateListStyleDL.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyle_CreateListStyleDL,intPdoc,iTypelistType)
        super(ListStyle, self).__init__(intPtr)

    @property

    def ListType(self)->'ListType':
        """
        Gets or sets the type of the list.

        Returns:
            ListType: The type of the list.
        """
        GetDllLibDoc().ListStyle_get_ListType.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_get_ListType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListStyle_get_ListType,self.Ptr)
        objwraped = ListType(ret)
        return objwraped

    @ListType.setter
    def ListType(self, value:'ListType'):
        """
        Sets the type of the list.

        Args:
            value (ListType): The type of the list.
        """
        GetDllLibDoc().ListStyle_set_ListType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().ListStyle_set_ListType,self.Ptr, value.value)

    @property

    def Levels(self)->'ListLevelCollection':
        """
        Gets the levels of the list.

        Returns:
            ListLevelCollection: The levels of the list.
        """
        GetDllLibDoc().ListStyle_get_Levels.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_get_Levels.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyle_get_Levels,self.Ptr)
        ret = None if intPtr==None else ListLevelCollection(intPtr)
        return ret


    @property

    def StyleType(self)->'StyleType':
        """
        Gets the type of the style.

        Returns:
            StyleType: The type of the style.
        """
        GetDllLibDoc().ListStyle_get_StyleType.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_get_StyleType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().ListStyle_get_StyleType,self.Ptr)
        objwraped = StyleType(ret)
        return objwraped

    @staticmethod

    def CreateEmptyListStyle(doc:'IDocument',listType:'ListType',isOneLevelList:bool)->'ListStyle':
        """
        Creates an empty list style.

        Args:
            doc (IDocument): The document.
            listType (ListType): The type of the list.
            isOneLevelList (bool): Indicates whether the list has only one level.

        Returns:
            ListStyle: The created empty list style.
        """
        intPtrdoc:c_void_p = doc.Ptr
        enumlistType:c_int = listType.value

        GetDllLibDoc().ListStyle_CreateEmptyListStyle.argtypes=[ c_void_p,c_int,c_bool]
        GetDllLibDoc().ListStyle_CreateEmptyListStyle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyle_CreateEmptyListStyle, intPtrdoc,enumlistType,isOneLevelList)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret



    def Clone(self)->'IStyle':
        """
        Clones the list style.

        Returns:
            IStyle: The cloned list style.
        """
        GetDllLibDoc().ListStyle_Clone.argtypes=[c_void_p]
        GetDllLibDoc().ListStyle_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyle_Clone,self.Ptr)
        ret = None if intPtr==None else IStyle(intPtr)
        return ret



    def GetNearLevel(self ,levelNumber:int)->'ListLevel':
        """
        Gets the nearest level to the specified level number.

        Args:
            levelNumber (int): The level number.

        Returns:
            ListLevel: The nearest level to the specified level number.
        """
        
        GetDllLibDoc().ListStyle_GetNearLevel.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().ListStyle_GetNearLevel.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().ListStyle_GetNearLevel,self.Ptr, levelNumber)
        ret = None if intPtr==None else ListLevel(intPtr)
        return ret


