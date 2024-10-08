from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Table (  BodyRegion, IBodyRegion, ITable, ICompositeObject) :
    """
    Represents a table in a document.
    """
    @dispatch
    def __init__(self, doc:'IDocument'):
        """
        Initializes a new instance of the Table class with the specified document.
        :param doc: The document to which the table belongs.
        """	
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Table_CreateTableD.argtypes=[c_void_p]
        GetDllLibDoc().Table_CreateTableD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_CreateTableD,intPdoc)
        super(Table, self).__init__(intPtr)
			
    @dispatch
    def __init__(self, doc:'IDocument', showBorder:bool):
        """
        Initializes a new instance of the Table class with the specified document and showBorder flag.
        :param doc: The document to which the table belongs.
        :param showBorder: A flag indicating whether to show the table border.
        """
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Table_CreateTableDS.argtypes=[c_void_p,c_bool]
        GetDllLibDoc().Table_CreateTableDS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_CreateTableDS,intPdoc,showBorder)
        super(Table, self).__init__(intPtr)
    @dispatch
    def __init__(self, doc:'IDocument', showBorder:bool, lineWidth:float):
        """
        Initializes a new instance of the Table class with the specified document, showBorder flag, and lineWidth.
        :param doc: The document to which the table belongs.
        :param showBorder: A flag indicating whether to show the table border.
        :param lineWidth: The width of the table border.
        """	
        intPdoc:c_void_p =  doc.Ptr

        GetDllLibDoc().Table_CreateTableDSL.argtypes=[c_void_p,c_bool,c_float]
        GetDllLibDoc().Table_CreateTableDSL.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_CreateTableDSL,intPdoc,showBorder,lineWidth)
        super(Table, self).__init__(intPtr)

		
    @property
    def DefaultRowHeight(self)->float:
        """
        Gets or sets the default row height, the unit of measure is point, 1point = 0.3528 mm.
        """
        GetDllLibDoc().Table_get_DefaultRowHeight.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DefaultRowHeight.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Table_get_DefaultRowHeight,self.Ptr)
        return ret

    @DefaultRowHeight.setter
    def DefaultRowHeight(self, value:float):
        """
        Sets the default row height.
        :param value: The default row height to set.
        """
        GetDllLibDoc().Table_set_DefaultRowHeight.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Table_set_DefaultRowHeight,self.Ptr, value)

    @property
    def DefaultColumnsNumber(self)->int:
        """
        Gets or sets the default number of columns in the table.
        """
        GetDllLibDoc().Table_get_DefaultColumnsNumber.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DefaultColumnsNumber.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Table_get_DefaultColumnsNumber,self.Ptr)
        return ret

    @DefaultColumnsNumber.setter
    def DefaultColumnsNumber(self, value:int):
        """
        Sets the default number of columns in the table.
        :param value: The default number of columns to set.
        """
        GetDllLibDoc().Table_set_DefaultColumnsNumber.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Table_set_DefaultColumnsNumber,self.Ptr, value)

    @property
    def DefaultColumnWidth(self)->float:
        """
        Gets or sets the default width of each column.
        """
        GetDllLibDoc().Table_get_DefaultColumnWidth.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DefaultColumnWidth.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Table_get_DefaultColumnWidth,self.Ptr)
        return ret

    @DefaultColumnWidth.setter
    def DefaultColumnWidth(self, value:float):
        """
        Sets the default width of each column.
        :param value: The default column width to set.
        """
        GetDllLibDoc().Table_set_DefaultColumnWidth.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Table_set_DefaultColumnWidth,self.Ptr, value)

    @property

    def ColumnWidth(self)->List[float]:
        """
        Gets or sets the width of each column.
        """
        GetDllLibDoc().Table_get_ColumnWidth.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_ColumnWidth.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().Table_get_ColumnWidth,self.Ptr)
        ret = GetVectorFromArray(intPtrArray, c_float)
        return ret

    @ColumnWidth.setter
    def ColumnWidth(self, value:List[float]):
        """
        Sets the width of each column.
        :param value: The list of column widths to set.
        """
        vCount = len(value)
        ArrayType = c_float * vCount
        vArray = ArrayType()
        for i in range(0, vCount):
            vArray[i] = value[i]
        GetDllLibDoc().Table_set_ColumnWidth.argtypes=[c_void_p, ArrayType, c_int]
        CallCFunction(GetDllLibDoc().Table_set_ColumnWidth,self.Ptr, vArray, vCount)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().Table_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Table_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def Rows(self)->'RowCollection':
        """
        Gets the collection of rows in the table.
        """
        GetDllLibDoc().Table_get_Rows.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_Rows.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_Rows,self.Ptr)
        from spire.doc import RowCollection
        ret = None if intPtr==None else RowCollection(intPtr)
        return ret


    @property

    def TableFormat(self)->'RowFormat':
        """
        Gets the table formatting after ResetCells call.
        """
        GetDllLibDoc().Table_get_TableFormat.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_TableFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_TableFormat,self.Ptr)
        ret = None if intPtr==None else RowFormat(intPtr)
        return ret


    @property

    def PreferredWidth(self)->'PreferredWidth':
        """
        Gets or sets the preferred horizontal width of the table.
        """
        GetDllLibDoc().Table_get_PreferredWidth.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_PreferredWidth.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_PreferredWidth,self.Ptr)
        ret = None if intPtr==None else PreferredWidth(intPtr)
        return ret


    @PreferredWidth.setter
    def PreferredWidth(self, value:'PreferredWidth'):
        """
        Sets the preferred horizontal width of the table.
        :param value: The preferred width to set.
        """
        GetDllLibDoc().Table_set_PreferredWidth.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Table_set_PreferredWidth,self.Ptr, value.Ptr)

    @property

    def TableStyleName(self)->str:
        """
        Gets the name of the table style.
        """
        GetDllLibDoc().Table_get_TableStyleName.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_TableStyleName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Table_get_TableStyleName,self.Ptr))
        return ret


    @property

    def LastCell(self)->'TableCell':
        """
        Gets the last cell in the table.
        """
        GetDllLibDoc().Table_get_LastCell.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_LastCell.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_LastCell,self.Ptr)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @property

    def FirstRow(self)->'TableRow':
        """
        Get the first row of the table.
        """
        GetDllLibDoc().Table_get_FirstRow.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_FirstRow.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_FirstRow,self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @property

    def LastRow(self)->'TableRow':
        """
        Get the last row of the table.
        """
        GetDllLibDoc().Table_get_LastRow.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_LastRow.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_LastRow,self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret



    def get_Item(self ,row:int,column:int)->'TableCell':
        """
        Get a table cell by row and column indexes.
        """
        
        GetDllLibDoc().Table_get_Item.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Table_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_Item,self.Ptr, row,column)
        ret = None if intPtr==None else TableCell(intPtr)
        return ret


    @property
    def Width(self)->float:
        """
        Get the width of the table.
        """
        GetDllLibDoc().Table_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_Width.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Table_get_Width,self.Ptr)
        return ret

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Get the child entities of the table.
        """
        GetDllLibDoc().Table_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property
    def IndentFromLeft(self)->float:
        """
        Get or set the indent from the left for the table.
        """
        GetDllLibDoc().Table_get_IndentFromLeft.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_IndentFromLeft.restype=c_float
        ret = CallCFunction(GetDllLibDoc().Table_get_IndentFromLeft,self.Ptr)
        return ret

    @IndentFromLeft.setter
    def IndentFromLeft(self, value:float):
        GetDllLibDoc().Table_set_IndentFromLeft.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().Table_set_IndentFromLeft,self.Ptr, value)

    @property

    def Title(self)->str:
        """
        Get or set the title of the table.
        """
        GetDllLibDoc().Table_get_Title.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_Title.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Table_get_Title,self.Ptr))
        return ret


    @Title.setter
    def Title(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Table_set_Title.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Table_set_Title,self.Ptr, valuePtr)

    @property

    def TableDescription(self)->str:
        """
        Get or set the description of the table.
        """
        GetDllLibDoc().Table_get_TableDescription.argtypes=[c_void_p]
        GetDllLibDoc().Table_get_TableDescription.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Table_get_TableDescription,self.Ptr))
        return ret


    @TableDescription.setter
    def TableDescription(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Table_set_TableDescription.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Table_set_TableDescription,self.Ptr, valuePtr)


    def AddCaption(self ,name:str,format:'CaptionNumberingFormat',captionPosition:'CaptionPosition')->'IParagraph':
        """
        Add a caption for the current table.
        """
        namePtr = StrToPtr(name)
        enumformat:c_int = format.value
        enumcaptionPosition:c_int = captionPosition.value

        GetDllLibDoc().Table_AddCaption.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        GetDllLibDoc().Table_AddCaption.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_AddCaption,self.Ptr, namePtr,enumformat,enumcaptionPosition)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret



    def Clone(self)->'Table':
        """
        Clone the current table.
        """
        GetDllLibDoc().Table_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Table_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_Clone,self.Ptr)
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @dispatch

    def ResetCells(self ,rowsNum:int,columnsNum:int):
        """
        Reset the number of rows and columns in the table.
        """
        
        GetDllLibDoc().Table_ResetCells.argtypes=[c_void_p ,c_int,c_int]
        CallCFunction(GetDllLibDoc().Table_ResetCells,self.Ptr, rowsNum,columnsNum)

    @dispatch

    def ResetCells(self ,rowsNum:int,columnsNum:int,format:RowFormat,cellWidth:float):
        """
        Resets rows / columns numbers.

        Args:
            rowsNum (int): The rows num.
            columnsNum (int): The columns num.
            format (RowFormat): The format.
            cellWidth (float): Width of the cell.
        """
        intPtrformat:c_void_p = format.Ptr

        GetDllLibDoc().Table_ResetCellsRCFC.argtypes=[c_void_p ,c_int,c_int,c_void_p,c_float]
        CallCFunction(GetDllLibDoc().Table_ResetCellsRCFC,self.Ptr, rowsNum,columnsNum,intPtrformat,cellWidth)


    def ApplyStyle(self ,builtinTableStyle:'DefaultTableStyle'):
        """
        Applies the built-in table style.

        Args:
            builtinTableStyle (DefaultTableStyle): The built-in table style.
        """
        enumbuiltinTableStyle:c_int = builtinTableStyle.value

        GetDllLibDoc().Table_ApplyStyle.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().Table_ApplyStyle,self.Ptr, enumbuiltinTableStyle)

    def ApplyTableStyle(self):
        """
        Applies the table style properties to table and cell.
        """
        GetDllLibDoc().Table_ApplyTableStyle.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Table_ApplyTableStyle,self.Ptr)

    @dispatch

    def AddRow(self)->TableRow:
        """
        Adds a row to table

        Returns:
            TableRow: The added row.
        """
        GetDllLibDoc().Table_AddRow.argtypes=[c_void_p]
        GetDllLibDoc().Table_AddRow.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_AddRow,self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,columnsNum:int)->TableRow:
        """
        Adds a row to table with copy format from the current last row, and then add columnsNum cells to the new row.

        Args:
            columnsNum (int): The number of the count of the new row, it's must be -1 < columnsNum < 64.

        Returns:
            TableRow: The added row.
        """
        
        GetDllLibDoc().Table_AddRowC.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Table_AddRowC.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_AddRowC,self.Ptr, columnsNum)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,isCopyFormat:bool)->TableRow:
        """
        Adds new row to table.

        Args:
            isCopyFormat (bool): Indicates whether copy format from previous row or not.

        Returns:
            TableRow: The added row.
        """
        
        GetDllLibDoc().Table_AddRowI.argtypes=[c_void_p ,c_bool]
        GetDllLibDoc().Table_AddRowI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_AddRowI,self.Ptr, isCopyFormat)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,isCopyFormat:bool,autoPopulateCells:bool)->TableRow:
        """
        Adds a row to table with copy format option.

        Args:
            isCopyFormat (bool): Indicates whether copy format from previous row or not.
            autoPopulateCells (bool): Specifies to populate cells automatically.

        Returns:
            TableRow: The added row.
        """
        
        GetDllLibDoc().Table_AddRowIA.argtypes=[c_void_p ,c_bool,c_bool]
        GetDllLibDoc().Table_AddRowIA.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_AddRowIA,self.Ptr, isCopyFormat,autoPopulateCells)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def AddRow(self ,isCopyFormat:bool,columnsNum:int)->TableRow:
        """
        Adds a row to table with copy format option.

        Args:
            isCopyFormat (bool): Indicates whether copy format from previous row or not.
            columnsNum (int): The number of the count of the new row, it's must be -1 < columnsNum < 64.

        Returns:
            TableRow: The added row.
        """
        
        GetDllLibDoc().Table_AddRowIC.argtypes=[c_void_p ,c_bool,c_int]
        GetDllLibDoc().Table_AddRowIC.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_AddRowIC,self.Ptr, isCopyFormat,columnsNum)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,replace:str)->int:
        """
        Replaces all entries of matchString regular expression with newValue string.

        Args:
            pattern (Regex): The pattern.
            replace (str): Replace text.

        Returns:
            int: The number of replacements made.
        """
        replacePtr = StrToPtr(replace)
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Table_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Table_Replace.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Table_Replace,self.Ptr, intPtrpattern,replacePtr)
        return ret


    @dispatch

    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces by specified matchString string.

        Args:
            given (str): The matchString text.
            replace (str): The newValue text.
            caseSensitive (bool): Specifies case sensitive.
            wholeWord (bool): Specifies to search a whole word.

        Returns:
            int: The number of replacements made.
        """
        givenPtr = StrToPtr(given)
        replacePtr = StrToPtr(replace)
        GetDllLibDoc().Table_ReplaceGRCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Table_ReplaceGRCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Table_ReplaceGRCW,self.Ptr, givenPtr,replacePtr,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,pattern:Regex,textSelection:'TextSelection')->int:
        """
        Replaces by specified pattern.

        Args:
            pattern (Regex): The pattern.
            textSelection (TextSelection): The text selection.

        Returns:
            int: The number of replacements made.
        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Table_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Table_ReplacePT.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Table_ReplacePT,self.Ptr, intPtrpattern,intPtrtextSelection)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,textSelection:'TextSelection',saveFormatting:bool)->int:
        """
        Replaces by specified pattern.

        Args:
            pattern (Regex): The pattern.
            textSelection (TextSelection): The text selection.
            saveFormatting (bool): Specifies save source formatting.

        Returns:
            int: The number of replacements made.
        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Table_ReplacePTS.argtypes=[c_void_p ,c_void_p,c_void_p,c_bool]
        GetDllLibDoc().Table_ReplacePTS.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Table_ReplacePTS,self.Ptr, intPtrpattern,intPtrtextSelection,saveFormatting)
        return ret



    def Find(self ,pattern:'Regex')->'TextSelection':
        """
        Finds text by specified pattern.

        Args:
            pattern: The pattern.

        Returns:
            TextSelection object if found, None otherwise.
        """
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Table_Find.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Table_Find.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Table_Find,self.Ptr, intPtrpattern)
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret




    def ApplyVerticalMerge(self ,columnIndex:int,startRowIndex:int,endRowIndex:int):
        """
        Applies the vertical merge for table cells.

        Args:
            columnIndex: Index of the column.
            startRowIndex: Start index of the row.
            endRowIndex: End index of the row.
        """
        
        GetDllLibDoc().Table_ApplyVerticalMerge.argtypes=[c_void_p ,c_int,c_int,c_int]
        CallCFunction(GetDllLibDoc().Table_ApplyVerticalMerge,self.Ptr, columnIndex,startRowIndex,endRowIndex)


    def ApplyHorizontalMerge(self ,rowIndex:int,startCellIndex:int,endCellIndex:int):
        """
        Applies horizontal merging for cells of table row.

        Args:
            rowIndex: Index of the row.
            startCellIndex: Start index of the cell.
            endCellIndex: End index of the cell.
        """
        
        GetDllLibDoc().Table_ApplyHorizontalMerge.argtypes=[c_void_p ,c_int,c_int,c_int]
        CallCFunction(GetDllLibDoc().Table_ApplyHorizontalMerge,self.Ptr, rowIndex,startCellIndex,endCellIndex)

    def RemoveAbsPosition(self):
        """
        Removes the absolute position data. If table has absolute position in the document,
        all position data will be erased.
        """
        GetDllLibDoc().Table_RemoveAbsPosition.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Table_RemoveAbsPosition,self.Ptr)


    def SetColumnWidth(self ,columnIndex:int,columnWidth:float,columnWidthType:'CellWidthType'):
        """
        Sets the width of all cells in the current column of the table.

        Args:
            columnIndex: Index of the column.
            columnWidth: The column width.
            columnWidthType: The column width type.
        """
        enumcolumnWidthType:c_int = columnWidthType.value

        GetDllLibDoc().Table_SetColumnWidth.argtypes=[c_void_p ,c_int,c_float,c_int]
        CallCFunction(GetDllLibDoc().Table_SetColumnWidth,self.Ptr, columnIndex,columnWidth,enumcolumnWidthType)


    def AutoFit(self ,behavior:'AutoFitBehaviorType'):
        """
        Determines how Microsoft Word resizes a table when the AutoFit feature is used.

        Args:
            behavior: How Word resizes the specified table with the AutoFit feature is used.
        """
        enumbehavior:c_int = behavior.value

        GetDllLibDoc().Table_AutoFit.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().Table_AutoFit,self.Ptr, enumbehavior)

