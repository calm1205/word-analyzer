from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class PageSetup (  DocumentSerializable) :
    """
    Represents the page setup of a document.
    """
    @property
    def DefaultTabWidth(self)->float:
        """
        Gets or sets the length of the auto tab.

        Returns:
            float: The length of the auto tab.
        """
        GetDllLibDoc().PageSetup_get_DefaultTabWidth.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_DefaultTabWidth.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_DefaultTabWidth,self.Ptr)
        return ret

    @DefaultTabWidth.setter
    def DefaultTabWidth(self, value:float):
        """
        Sets the length of the auto tab.

        Args:
            value (float): The length of the auto tab.
        """
        GetDllLibDoc().PageSetup_set_DefaultTabWidth.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().PageSetup_set_DefaultTabWidth,self.Ptr, value)

    @property

    def PageSize(self)->'SizeF':
        """
        Gets or sets the page size in points.

        Returns:
            SizeF: The page size.
        """
        GetDllLibDoc().PageSetup_get_PageSize.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageSize.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PageSetup_get_PageSize,self.Ptr)
        ret = None if intPtr==None else SizeF(intPtr)
        return ret


    @PageSize.setter
    def PageSize(self, value:'SizeF'):
        """
        Sets the page size in points.

        Args:
            value (SizeF): The page size.
        """
        GetDllLibDoc().PageSetup_set_PageSize.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageSize,self.Ptr, value.Ptr)

    @property

    def Orientation(self)->'PageOrientation':
        """
        Gets or sets the orientation of the page.

        Returns:
            PageOrientation: The page orientation.
        """
        GetDllLibDoc().PageSetup_get_Orientation.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Orientation.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_Orientation,self.Ptr)
        objwraped = PageOrientation(ret)
        return objwraped

    @Orientation.setter
    def Orientation(self, value:'PageOrientation'):
        """
        Sets the orientation of the page.

        Args:
            value (PageOrientation): The page orientation.
        """
        GetDllLibDoc().PageSetup_set_Orientation.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_Orientation,self.Ptr, value.value)

    @property

    def VerticalAlignment(self)->'PageAlignment':
        """
        Gets or sets the vertical alignment.

        Returns:
            PageAlignment: The vertical alignment.
        """
        GetDllLibDoc().PageSetup_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_VerticalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_VerticalAlignment,self.Ptr)
        objwraped = PageAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'PageAlignment'):
        """
        Sets the vertical alignment.

        Args:
            value (PageAlignment): The vertical alignment.
        """
        GetDllLibDoc().PageSetup_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_VerticalAlignment,self.Ptr, value.value)

    @property

    def Margins(self)->'MarginsF':
        """
        Gets or sets the page margins in points.

        Returns:
            MarginsF: The page margins.
        """
        GetDllLibDoc().PageSetup_get_Margins.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Margins.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PageSetup_get_Margins,self.Ptr)
        ret = None if intPtr==None else MarginsF(intPtr)
        return ret


    @Margins.setter
    def Margins(self, value:'MarginsF'):
        """
        Sets the page margins in points.

        Args:
            value (MarginsF): The page margins.
        """
        GetDllLibDoc().PageSetup_set_Margins.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().PageSetup_set_Margins,self.Ptr, value.Ptr)

    @property
    def Gutter(self)->float:
        """
        Gets or sets the extra space added to the margin for document binding in points.

        Returns:
            float: The gutter space.
        """
        GetDllLibDoc().PageSetup_get_Gutter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Gutter.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_Gutter,self.Ptr)
        return ret

    @Gutter.setter
    def Gutter(self, value:float):
        """
        Sets the extra space added to the margin for document binding in points.

        Args:
            value (float): The gutter space.
        """
        GetDllLibDoc().PageSetup_set_Gutter.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().PageSetup_set_Gutter,self.Ptr, value)

    @property
    def HeaderDistance(self)->float:
        """
        Gets or sets the height of the header in points.

        Returns:
            float: The header height.
        """
        GetDllLibDoc().PageSetup_get_HeaderDistance.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_HeaderDistance.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_HeaderDistance,self.Ptr)
        return ret

    @HeaderDistance.setter
    def HeaderDistance(self, value:float):
        """
        Sets the height of the header in points.

        Args:
            value (float): The header height.
        """
        GetDllLibDoc().PageSetup_set_HeaderDistance.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().PageSetup_set_HeaderDistance,self.Ptr, value)

    @property
    def FooterDistance(self)->float:
        """
        Gets or sets the footer height in points.

        Returns:
            float: The footer height.
        """
        GetDllLibDoc().PageSetup_get_FooterDistance.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_FooterDistance.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_FooterDistance,self.Ptr)
        return ret

    @FooterDistance.setter
    def FooterDistance(self, value:float):
        """
        Sets the footer height in points.

        Args:
            value (float): The footer height.
        """
        GetDllLibDoc().PageSetup_set_FooterDistance.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().PageSetup_set_FooterDistance,self.Ptr, value)

    @property
    def ClientWidth(self)->float:
        """
        Gets the width of the client area.

        Returns:
            float: The width of the client area.
        """
        GetDllLibDoc().PageSetup_get_ClientWidth.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_ClientWidth.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_ClientWidth,self.Ptr)
        return ret

    @property
    def ClientHeight(self)->float:
        """
        Gets the height of the client area.

        Returns:
            float: The height of the client area.
        """
        GetDllLibDoc().PageSetup_get_ClientHeight.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_ClientHeight.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_ClientHeight,self.Ptr)
        return ret

    @property
    def DifferentFirstPageHeaderFooter(self)->bool:
        """
        Gets or sets a value indicating whether the current section has a different header/footer for the first page.

        Returns:
            bool: True if the current section has a different header/footer for the first page; otherwise, False.
        """
        GetDllLibDoc().PageSetup_get_DifferentFirstPageHeaderFooter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_DifferentFirstPageHeaderFooter.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_DifferentFirstPageHeaderFooter,self.Ptr)
        return ret

    @DifferentFirstPageHeaderFooter.setter
    def DifferentFirstPageHeaderFooter(self, value:bool):
        """
        Sets a value indicating whether the current section has a different header/footer for the first page.

        Args:
            value (bool): True if the current section has a different header/footer for the first page; otherwise, False.
        """
        GetDllLibDoc().PageSetup_set_DifferentFirstPageHeaderFooter.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_DifferentFirstPageHeaderFooter,self.Ptr, value)

    @property
    def DifferentOddAndEvenPagesHeaderFooter(self)->bool:
        """
        Gets or sets a value indicating whether the document has different headers and footers for odd-numbered and even-numbered pages.

        Returns:
            bool: True if the document has different headers and footers for odd-numbered and even-numbered pages; otherwise, False.
        """
        GetDllLibDoc().PageSetup_get_DifferentOddAndEvenPagesHeaderFooter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_DifferentOddAndEvenPagesHeaderFooter.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_DifferentOddAndEvenPagesHeaderFooter,self.Ptr)
        return ret

    @DifferentOddAndEvenPagesHeaderFooter.setter
    def DifferentOddAndEvenPagesHeaderFooter(self, value:bool):
        """
        Sets whether the header and footer on odd and even pages are different.
        """
        GetDllLibDoc().PageSetup_set_DifferentOddAndEvenPagesHeaderFooter.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_DifferentOddAndEvenPagesHeaderFooter,self.Ptr, value)

    @property

    def LineNumberingRestartMode(self)->'LineNumberingRestartMode':
        """
        Returns or sets the line numbering mode.
        """
        GetDllLibDoc().PageSetup_get_LineNumberingRestartMode.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingRestartMode.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_LineNumberingRestartMode,self.Ptr)
        objwraped = LineNumberingRestartMode(ret)
        return objwraped

    @LineNumberingRestartMode.setter
    def LineNumberingRestartMode(self, value:'LineNumberingRestartMode'):
        """
        Sets the line numbering mode.
        """
        GetDllLibDoc().PageSetup_set_LineNumberingRestartMode.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_LineNumberingRestartMode,self.Ptr, value.value)

    @property
    def LineNumberingStep(self)->int:
        """
        Gets or sets the line numbering step.
        """
        GetDllLibDoc().PageSetup_get_LineNumberingStep.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingStep.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_LineNumberingStep,self.Ptr)
        return ret

    @LineNumberingStep.setter
    def LineNumberingStep(self, value:int):
        """
        Sets the line numbering step.
        """
        GetDllLibDoc().PageSetup_set_LineNumberingStep.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_LineNumberingStep,self.Ptr, value)

    @property
    def LineNumberingStartValue(self)->int:
        """
        Gets or sets the line numbering start value.
        """
        GetDllLibDoc().PageSetup_get_LineNumberingStartValue.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingStartValue.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_LineNumberingStartValue,self.Ptr)
        return ret

    @LineNumberingStartValue.setter
    def LineNumberingStartValue(self, value:int):
        """
        Sets the line numbering start value.
        """
        GetDllLibDoc().PageSetup_set_LineNumberingStartValue.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_LineNumberingStartValue,self.Ptr, value)

    @property
    def LineNumberingDistanceFromText(self)->float:
        """
        Gets or sets the distance from text in line numbering.
        """
        GetDllLibDoc().PageSetup_get_LineNumberingDistanceFromText.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LineNumberingDistanceFromText.restype=c_float
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_LineNumberingDistanceFromText,self.Ptr)
        return ret

    @LineNumberingDistanceFromText.setter
    def LineNumberingDistanceFromText(self, value:float):
        """
        Sets the distance from text in line numbering.
        """
        GetDllLibDoc().PageSetup_set_LineNumberingDistanceFromText.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().PageSetup_set_LineNumberingDistanceFromText,self.Ptr, value)

    @property

    def PageBordersApplyType(self)->'PageBordersApplyType':
        """
        Gets or sets the value that determines on which pages the border is applied.
        """
        GetDllLibDoc().PageSetup_get_PageBordersApplyType.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBordersApplyType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_PageBordersApplyType,self.Ptr)
        objwraped = PageBordersApplyType(ret)
        return objwraped

    @PageBordersApplyType.setter
    def PageBordersApplyType(self, value:'PageBordersApplyType'):
        """
        Sets the value that determines on which pages the border is applied.
        """
        GetDllLibDoc().PageSetup_set_PageBordersApplyType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageBordersApplyType,self.Ptr, value.value)

    @property

    def PageBorderOffsetFrom(self)->'PageBorderOffsetFrom':
        """
        Gets or sets the position of the page border.
        """
        GetDllLibDoc().PageSetup_get_PageBorderOffsetFrom.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBorderOffsetFrom.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_PageBorderOffsetFrom,self.Ptr)
        objwraped = PageBorderOffsetFrom(ret)
        return objwraped

    @PageBorderOffsetFrom.setter
    def PageBorderOffsetFrom(self, value:'PageBorderOffsetFrom'):
        """
        Sets the position of the page border.
        """
        GetDllLibDoc().PageSetup_set_PageBorderOffsetFrom.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageBorderOffsetFrom,self.Ptr, value.value)

    @property
    def IsFrontPageBorder(self)->bool:
        """
        Gets or sets a value indicating whether this instance is a front page border.
        """
        GetDllLibDoc().PageSetup_get_IsFrontPageBorder.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_IsFrontPageBorder.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_IsFrontPageBorder,self.Ptr)
        return ret

    @IsFrontPageBorder.setter
    def IsFrontPageBorder(self, value:bool):
        """
        Sets a value indicating whether this instance is a front page border.
        """
        GetDllLibDoc().PageSetup_set_IsFrontPageBorder.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_IsFrontPageBorder,self.Ptr, value)

    @property
    def PageBorderIncludeHeader(self)->bool:
        """
        Gets or sets a value indicating whether the page border includes the header.
        If the page border is not measured from the text extents using a value of text in the PageBorderOffsetFrom, then it can be ignored.
        """
        GetDllLibDoc().PageSetup_get_PageBorderIncludeHeader.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBorderIncludeHeader.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_PageBorderIncludeHeader,self.Ptr)
        return ret

    @PageBorderIncludeHeader.setter
    def PageBorderIncludeHeader(self, value:bool):
        """
        Sets a value indicating whether the page border includes the header.
        If the page border is not measured from the text extents using a value of text in the PageBorderOffsetFrom, then it can be ignored.
        """
        GetDllLibDoc().PageSetup_set_PageBorderIncludeHeader.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageBorderIncludeHeader,self.Ptr, value)

    @property
    def PageBorderIncludeFooter(self)->bool:
        """
        Gets or sets a value indicating whether the page border includes the footer.
        If the page border is not measured from the text extents using a value of text in the PageBorderOffsetFrom, then it can be ignored.
        """
        GetDllLibDoc().PageSetup_get_PageBorderIncludeFooter.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageBorderIncludeFooter.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_PageBorderIncludeFooter,self.Ptr)
        return ret

    @PageBorderIncludeFooter.setter
    def PageBorderIncludeFooter(self, value:bool):
        """
        Sets a value indicating whether the page border includes the footer.
        If the page border is not measured from the text extents using a value of text in the PageBorderOffsetFrom, then it can be ignored.
        """
        GetDllLibDoc().PageSetup_set_PageBorderIncludeFooter.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageBorderIncludeFooter,self.Ptr, value)

    @property

    def Borders(self)->'Borders':
        """
        Gets the page borders collection.
        """
        GetDllLibDoc().PageSetup_get_Borders.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Borders.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().PageSetup_get_Borders,self.Ptr)
        ret = None if intPtr==None else Borders(intPtr)
        return ret


    @property
    def Bidi(self)->bool:
        """
        Gets or sets whether section contains right-to-left text.
        :return: bool
        """
        GetDllLibDoc().PageSetup_get_Bidi.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_Bidi.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_Bidi,self.Ptr)
        return ret

    @Bidi.setter
    def Bidi(self, value:bool):
        """
        Sets whether section contains right-to-left text.
        :param value: bool
        :return: None
        """
        GetDllLibDoc().PageSetup_set_Bidi.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_Bidi,self.Ptr, value)

    @property
    def EqualColumnWidth(self)->bool:
        """
        Gets or sets a value indicating whether equal column width.
        :return: bool
        """
        GetDllLibDoc().PageSetup_get_EqualColumnWidth.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_EqualColumnWidth.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_EqualColumnWidth,self.Ptr)
        return ret

    @EqualColumnWidth.setter
    def EqualColumnWidth(self, value:bool):
        """
        Sets a value indicating whether equal column width.
        :param value: bool
        :return: None
        """
        GetDllLibDoc().PageSetup_set_EqualColumnWidth.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_EqualColumnWidth,self.Ptr, value)

    @property

    def PageNumberStyle(self)->'PageNumberStyle':
        """
        Gets or sets the page number style.
        :return: PageNumberStyle
        """
        GetDllLibDoc().PageSetup_get_PageNumberStyle.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageNumberStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_PageNumberStyle,self.Ptr)
        objwraped = PageNumberStyle(ret)
        return objwraped

    @PageNumberStyle.setter
    def PageNumberStyle(self, value:'PageNumberStyle'):
        """
        Sets the page number style.
        :param value: PageNumberStyle
        :return: None
        """
        GetDllLibDoc().PageSetup_set_PageNumberStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageNumberStyle,self.Ptr, value.value)

    @property
    def PageStartingNumber(self)->int:
        """
        Gets or sets the page starting number.
        :return: int
        """
        GetDllLibDoc().PageSetup_get_PageStartingNumber.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_PageStartingNumber.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_PageStartingNumber,self.Ptr)
        return ret

    @PageStartingNumber.setter
    def PageStartingNumber(self, value:int):
        """
        Sets the page starting number.
        :param value: int
        :return: None
        """
        GetDllLibDoc().PageSetup_set_PageStartingNumber.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_PageStartingNumber,self.Ptr, value)

    @property
    def RestartPageNumbering(self)->bool:
        """
        Gets or sets a value indicating whether to restart page numbering.
        :return: bool
        """
        GetDllLibDoc().PageSetup_get_RestartPageNumbering.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_RestartPageNumbering.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_RestartPageNumbering,self.Ptr)
        return ret

    @RestartPageNumbering.setter
    def RestartPageNumbering(self, value:bool):
        """
        Sets a value indicating whether to restart page numbering.
        :param value: bool
        :return: None
        """
        GetDllLibDoc().PageSetup_set_RestartPageNumbering.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_RestartPageNumbering,self.Ptr, value)

    @property

    def GridType(self)->'GridPitchType':
        """
        Gets or Sets the grid type of this section.
        :return: GridPitchType
        """
        GetDllLibDoc().PageSetup_get_GridType.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_GridType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_GridType,self.Ptr)
        objwraped = GridPitchType(ret)
        return objwraped

    @GridType.setter
    def GridType(self, value:'GridPitchType'):
        """
        Sets the grid type of this section.
        :param value: GridPitchType
        :return: None
        """
        GetDllLibDoc().PageSetup_set_GridType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_GridType,self.Ptr, value.value)

    @property
    def LinesPerPage(self)->int:
        """
        Gets or sets the number of lines per page in the document grid.
        :return: int
        """
        GetDllLibDoc().PageSetup_get_LinesPerPage.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_LinesPerPage.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_LinesPerPage,self.Ptr)
        return ret

    @LinesPerPage.setter
    def LinesPerPage(self, value:int):
        """
        Sets the number of lines per page in the document grid.
        :param value: int
        :return: None
        """
        GetDllLibDoc().PageSetup_set_LinesPerPage.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_LinesPerPage,self.Ptr, value)

    @property
    def ColumnsLineBetween(self)->bool:
        """
        Gets or sets the value specifies if a vertical line is draw between each of the text columns in the this section.
        :return: bool
        """
        GetDllLibDoc().PageSetup_get_ColumnsLineBetween.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_ColumnsLineBetween.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_ColumnsLineBetween,self.Ptr)
        return ret

    @ColumnsLineBetween.setter
    def ColumnsLineBetween(self, value:bool):
        """
        Sets the value specifies if a vertical line is draw between each of the text columns in the this section.
        :param value: bool
        :return: None
        """
        GetDllLibDoc().PageSetup_set_ColumnsLineBetween.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().PageSetup_set_ColumnsLineBetween,self.Ptr, value)

    @property

    def CharacterSpacingControl(self)->'CharacterSpacing':
        """
        Character Spacing Control.
        :return: CharacterSpacing
        """
        GetDllLibDoc().PageSetup_get_CharacterSpacingControl.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_get_CharacterSpacingControl.restype=c_int
        ret = CallCFunction(GetDllLibDoc().PageSetup_get_CharacterSpacingControl,self.Ptr)
        objwraped = CharacterSpacing(ret)
        return objwraped

    @CharacterSpacingControl.setter
    def CharacterSpacingControl(self, value:'CharacterSpacing'):
        """
        Sets the Character Spacing Control.
        :param value: CharacterSpacing
        :return: None
        """
        GetDllLibDoc().PageSetup_set_CharacterSpacingControl.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().PageSetup_set_CharacterSpacingControl,self.Ptr, value.value)


    def InsertPageNumbers(self ,fromTopPage:bool,horizontalAlignment:'PageNumberAlignment'):
        """
        Inserts the page numbers.
        :param fromTopPage: bool
        :param horizontalAlignment: PageNumberAlignment
        :return: None
        """
        enumhorizontalAlignment:c_int = horizontalAlignment.value

        GetDllLibDoc().PageSetup_InsertPageNumbers.argtypes=[c_void_p ,c_bool,c_int]
        CallCFunction(GetDllLibDoc().PageSetup_InsertPageNumbers,self.Ptr, fromTopPage,enumhorizontalAlignment)


    def ToString(self)->str:
        """
        :return: str
        """
        GetDllLibDoc().PageSetup_ToString.argtypes=[c_void_p]
        GetDllLibDoc().PageSetup_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().PageSetup_ToString,self.Ptr))
        return ret


