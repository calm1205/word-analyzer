from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class TableCell (  Body, IDocumentObject) :
    """
    Represents a cell in a table.
    """
    @dispatch
    def __init__(self, document:'IDocument'):
        """
        Initializes a new instance of the TableCell class.
        Args:
            document: The document that the cell belongs to.
        """
        intPdocument:c_void_p = document.Ptr

        GetDllLibDoc().TableCell_CreateTableCellD.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_CreateTableCellD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableCell_CreateTableCellD,intPdocument)
        super(TableCell, self).__init__(intPtr)

    @property

    def GridSpan(self)->int:
        """
        Gets the number of columns that the cell spans.
        Returns:
            The number of columns that the cell spans.
        """
        GetDllLibDoc().TableCell_get_GridSpan.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_GridSpan.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableCell_get_GridSpan,self.Ptr)
        return intPtr


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        Returns:
            The type of the document object.
        """
        GetDllLibDoc().TableCell_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCell_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def OwnerRow(self)->'TableRow':
        """
        Gets the owner row of the cell.
        Returns:
            The owner row of the cell.
        """
        GetDllLibDoc().TableCell_get_OwnerRow.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_OwnerRow.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableCell_get_OwnerRow,self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @property

    def CellFormat(self)->'CellFormat':
        """
        Gets the cell format.
        Returns:
            The cell format.
        """
        GetDllLibDoc().TableCell_get_CellFormat.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_CellFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableCell_get_CellFormat,self.Ptr)
        from spire.doc import CellFormat
        ret = None if intPtr==None else CellFormat(intPtr)
        return ret


    @property
    def Width(self)->float:
        """
        Gets the width of the cell.
        Returns:
            The width of the cell.
        """
        GetDllLibDoc().TableCell_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_Width.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TableCell_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        """
        Sets the width of the cell.
        Args:
            value: The width of the cell.
        """
        GetDllLibDoc().TableCell_set_Width.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TableCell_set_Width,self.Ptr, value)

    @property

    def CellWidthType(self)->'CellWidthType':
        """
        Gets the width type of the cell.
        Returns:
            The width type of the cell.
        """
        GetDllLibDoc().TableCell_get_CellWidthType.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_CellWidthType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCell_get_CellWidthType,self.Ptr)
        objwraped = CellWidthType(ret)
        return objwraped

    @CellWidthType.setter
    def CellWidthType(self, value:'CellWidthType'):
        """
        Sets the width type of the cell.
        Args:
            value: The width type of the cell.
        """
        GetDllLibDoc().TableCell_set_CellWidthType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().TableCell_set_CellWidthType,self.Ptr, value.value)

    @property
    def Scaling(self)->float:
        """
        Gets or sets the cell scaling.
        Returns:
            The cell scaling.
        """
        GetDllLibDoc().TableCell_get_Scaling.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_get_Scaling.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TableCell_get_Scaling,self.Ptr)
        return ret

    @Scaling.setter
    def Scaling(self, value:float):
        """
        Sets the cell scaling.
        Args:
            value: The cell scaling.
        """
        GetDllLibDoc().TableCell_set_Scaling.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().TableCell_set_Scaling,self.Ptr, value)


    def Clone(self)->'DocumentObject':
        """
        Creates a new TableCell object that is a copy of the current instance.
        Returns:
            A new TableCell object that is a copy of this instance.
        """
        GetDllLibDoc().TableCell_Clone.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().TableCell_Clone,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


    def GetCellIndex(self)->int:
        """
        Gets the index of the cell in the row.
        Returns:
            The index of the cell in the row.
        """
        GetDllLibDoc().TableCell_GetCellIndex.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_GetCellIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCell_GetCellIndex,self.Ptr)
        return ret


    def SetCellWidth(self ,width:float,widthType:'CellWidthType'):
        """
        Sets the width and type of the cell.
        Args:
            width: The width of the cell.
            widthType: The width type of the cell.
        """
        enumwidthType:c_int = widthType.value

        GetDllLibDoc().TableCell_SetCellWidth.argtypes=[c_void_p ,c_float,c_int]
        CallCFunction(GetDllLibDoc().TableCell_SetCellWidth,self.Ptr, width,enumwidthType)

    def GetCellWidth(self)->float:
        """
        Gets the width of the cell.
        Returns:
            The width of the cell.
        """
        GetDllLibDoc().TableCell_GetCellWidth.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_GetCellWidth.restype=c_float
        ret = CallCFunction(GetDllLibDoc().TableCell_GetCellWidth,self.Ptr)
        return ret


    def GetCellWidthType(self)->'CellWidthType':
        """
        Gets the width type of the cell.
        Returns:
            The width type of the cell.
        """
        GetDllLibDoc().TableCell_GetCellWidthType.argtypes=[c_void_p]
        GetDllLibDoc().TableCell_GetCellWidthType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().TableCell_GetCellWidthType,self.Ptr)
        objwraped = CellWidthType(ret)
        return objwraped


    def SplitCell(self ,columnNum:int,rowNum:int):
        """
        Splits the cell into two or more cells.
        Args:
            columnNum: The number of columns to split. Must be greater than or equal to 1.
            rowNum: The number of rows to split. Must be greater than or equal to 1.
        """
        
        GetDllLibDoc().TableCell_SplitCell.argtypes=[c_void_p ,c_int,c_int]
        CallCFunction(GetDllLibDoc().TableCell_SplitCell,self.Ptr, columnNum,rowNum)

