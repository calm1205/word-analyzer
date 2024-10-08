from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableRow (  DocumentBase, ICompositeObject) :
    """
    Represents a table row in a document.
    """
    @dispatch
    def __init__(self, document:'IDocument'):
        """
        Initializes a new instance of the TableRow class.
        Args:
            document: The document to which the table row belongs.
        """
        intPdocument:c_void_p =  document.Ptr

        GetDllLibDoc().TableRow_CreateTableRowD.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_CreateTableRowD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_CreateTableRowD,intPdocument)
        super(TableRow, self).__init__(intPtr)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects of the table row.
        Returns:
            The child objects of the table row.
        """
        GetDllLibDoc().TableRow_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        Returns:
            The type of the document object.
        """
        GetDllLibDoc().TableRow_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableRow_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Cells(self)->'CellCollection':
        """
        Gets or sets the cell collection of the table row.
        Returns:
            The cell collection of the table row.
        """
        GetDllLibDoc().TableRow_get_Cells.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_Cells.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_get_Cells,self.Ptr)
        from spire.doc import CellCollection
        ret = None if intPtr==None else CellCollection(intPtr)
        return ret


    @Cells.setter
    def Cells(self, value:'CellCollection'):
        GetDllLibDoc().TableRow_set_Cells.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().TableRow_set_Cells,self.Ptr, value.Ptr)

    @property

    def HeightType(self)->'TableRowHeightType':
        """
        Gets or sets the height type of the table row.
        Returns:
            The height type of the table row.
        """
        GetDllLibDoc().TableRow_get_HeightType.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_HeightType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableRow_get_HeightType,self.Ptr)
        objwraped = TableRowHeightType(ret)
        return objwraped

    @HeightType.setter
    def HeightType(self, value:'TableRowHeightType'):
        GetDllLibDoc().TableRow_set_HeightType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TableRow_set_HeightType,self.Ptr, value.value)

    @property

    def RowFormat(self)->'RowFormat':
        """
        Gets the row format of the table row.
        Returns:
            The row format of the table row.
        """
        GetDllLibDoc().TableRow_get_RowFormat.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_RowFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_get_RowFormat,self.Ptr)
        from spire.doc import RowFormat
        ret = None if intPtr==None else RowFormat(intPtr)
        return ret


    @property
    def Height(self)->float:
        """
        Gets or sets the height of the table row.
        Returns:
            The height of the table row.
        """
        GetDllLibDoc().TableRow_get_Height.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_Height.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TableRow_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        GetDllLibDoc().TableRow_set_Height.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TableRow_set_Height,self.Ptr, value)

    @property
    def IsHeader(self)->bool:
        """
        Gets or sets a value indicating whether the table row is a header.
        Returns:
            True if the table row is a header; otherwise, False.
        """
        GetDllLibDoc().TableRow_get_IsHeader.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_get_IsHeader.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().TableRow_get_IsHeader,self.Ptr)
        return ret

    @IsHeader.setter
    def IsHeader(self, value:bool):
        GetDllLibDoc().TableRow_set_IsHeader.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().TableRow_set_IsHeader,self.Ptr, value)


    def Clone(self)->'TableRow':
        """
        Creates a deep copy of the table row.
        Returns:
            A new instance of the TableRow class that is a deep copy of this instance.
        """
        GetDllLibDoc().TableRow_Clone.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_Clone,self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddCell(self)->TableCell:
        """
        Adds a cell to the table row.
        Returns:
            The added cell.
        """
        GetDllLibDoc().TableRow_AddCell.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_AddCell.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_AddCell,self.Ptr)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @dispatch

    def AddCell(self ,isCopyFormat:bool)->TableCell:
        """
        Adds a cell to the table row.
        Args:
            isCopyFormat: Specifies whether to apply the parent row format to the new cell.
        Returns:
            The added cell.
        """
        
        GetDllLibDoc().TableRow_AddCellI.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().TableRow_AddCellI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableRow_AddCellI,self.Ptr, isCopyFormat)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    def GetRowIndex(self)->int:
        """
        Gets the index of the table row in the owner table.
        Returns:
            The index of the table row in the owner table.
        """
        GetDllLibDoc().TableRow_GetRowIndex.argtypes=[c_void_p]
        GetDllLibDoc().TableRow_GetRowIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableRow_GetRowIndex,self.Ptr)
        return ret

