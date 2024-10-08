from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class StructureDocumentTagRow (  TableRow, IStructureDocument) :
    """
    Represents a row in a structured document tag.
    """
    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the entity.
        """
        GetDllLibDoc().StructureDocumentTagRow_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagRow_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().StructureDocumentTagRow_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def SDTProperties(self)->'SDTProperties':
        """
        Gets the structured document tag properties.
        """
        GetDllLibDoc().StructureDocumentTagRow_get_SDTProperties.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagRow_get_SDTProperties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagRow_get_SDTProperties,self.Ptr)
        ret = None if intPtr==None else SDTProperties(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Gets character format for the break symbol.
        """
        GetDllLibDoc().StructureDocumentTagRow_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagRow_get_BreakCharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagRow_get_BreakCharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child object.
        """
        GetDllLibDoc().StructureDocumentTagRow_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagRow_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagRow_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def Cells(self)->'CellCollection':
        """
        Returns or sets cell collection.
        """
        GetDllLibDoc().StructureDocumentTagRow_get_Cells.argtypes=[c_void_p]
        GetDllLibDoc().StructureDocumentTagRow_get_Cells.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().StructureDocumentTagRow_get_Cells,self.Ptr)
        ret = None if intPtr==None else CellCollection(intPtr)
        return ret


    @Cells.setter
    def Cells(self, value:'CellCollection'):
        GetDllLibDoc().StructureDocumentTagRow_set_Cells.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTagRow_set_Cells,self.Ptr, value.Ptr)

    def UpdateDataBinding(self):
        """
        Updates the data binding of the row.
        """
        GetDllLibDoc().StructureDocumentTagRow_UpdateDataBinding.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().StructureDocumentTagRow_UpdateDataBinding,self.Ptr)

