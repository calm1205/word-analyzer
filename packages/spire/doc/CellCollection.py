from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class CellCollection(DocumentObjectCollection):
    """
    Represents a collection of TableCell objects.
    """

    def get_Item(self ,index:int)->'TableCell':
        """
        Retrieves the TableCell at the specified index.
        
        Args:
            index: The index of the TableCell to retrieve.
        
        Returns:
            The TableCell at the specified index.
        """
        
        GetDllLibDoc().CellCollection_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().CellCollection_get_Item.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().CellCollection_get_Item,self.Ptr, index)
        ret = None if intPtr==None else self._create(intPtr)
        return ret

    def _create(self, intPtrWithTypeName: IntPtrWithTypeName) -> 'TableCell':
        """
        Creates a TableCell object from the given IntPtrWithTypeName.
        
        Args:
            intPtrWithTypeName: The IntPtrWithTypeName to create the TableCell from.
        
        Returns:
            The created TableCell object.
        """
        ret = None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Documents.StructureDocumentTagCell"):
            ret = StructureDocumentTagCell(intPtr)
        else:
            ret = TableCell(intPtr)
        return ret


    def Add(self ,cell:'TableCell')->int:
        """
        Adds the specified cell to the collection.
        
        Args:
            cell: The cell to add.
        
        Returns:
            The index at which the cell was added.
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_Add.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CellCollection_Add.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CellCollection_Add,self.Ptr, intPtrcell)
        return ret


    def Insert(self ,index:int,cell:'TableCell'):
        """
        Inserts the specified table cell into the collection at the specified index.
        
        Args:
            index: The index at which to insert the cell.
            cell: The cell to insert.
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_Insert.argtypes=[c_void_p ,c_int,c_void_p]
        CallCFunction(GetDllLibDoc().CellCollection_Insert,self.Ptr, index,intPtrcell)


    def IndexOf(self ,cell:'TableCell')->int:
        """
        Returns the index of the specified cell in the collection.
        
        Args:
            cell: The cell to find the index of.
        
        Returns:
            The index of the cell in the collection.
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_IndexOf.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().CellCollection_IndexOf.restype=c_int
        ret = CallCFunction(GetDllLibDoc().CellCollection_IndexOf,self.Ptr, intPtrcell)
        return ret


    def Remove(self ,cell:'TableCell'):
        """
        Removes the specified cell from the collection.
        
        Args:
            cell: The cell to remove.
        """
        intPtrcell:c_void_p = cell.Ptr

        GetDllLibDoc().CellCollection_Remove.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().CellCollection_Remove,self.Ptr, intPtrcell)


    def RemoveAt(self ,index:int):
        """
        Removes the document object at the specified index from the collection.
        
        Args:
            index: The index of the document object to remove.
        """
        
        GetDllLibDoc().CellCollection_RemoveAt.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().CellCollection_RemoveAt,self.Ptr, index)

