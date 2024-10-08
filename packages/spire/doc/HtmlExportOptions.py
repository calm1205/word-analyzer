from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class HtmlExportOptions (SpireObject) :
    """
    Represents the options for exporting to HTML.
    """
    @property
    def EPubExportFont(self)->bool:
        """
        Gets or sets a value indicating whether to export the font when exporting to EPUB format.
        """
        GetDllLibDoc().HtmlExportOptions_get_EPubExportFont.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_EPubExportFont.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_EPubExportFont,self.Ptr)
        return ret

    @EPubExportFont.setter
    def EPubExportFont(self, value:bool):
        """
        Sets a value indicating whether to export the font when exporting to EPUB format.
        """
        GetDllLibDoc().HtmlExportOptions_set_EPubExportFont.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_EPubExportFont,self.Ptr, value)

    @property

    def CssStyleSheetType(self)->'CssStyleSheetType':
        """
        Gets or sets the type of the HTML export CSS style sheet.
        """
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetType.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetType,self.Ptr)
        objwraped = CssStyleSheetType(ret)
        return objwraped

    @CssStyleSheetType.setter
    def CssStyleSheetType(self, value:'CssStyleSheetType'):
        """
        Sets the type of the HTML export CSS style sheet.
        """
        GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetType,self.Ptr, value.value)

    @property
    def ImageEmbedded(self)->bool:
        """
        Gets or sets a value indicating whether to embed the image into the HTML code using the Data URI scheme.
        """
        GetDllLibDoc().HtmlExportOptions_get_ImageEmbedded.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_ImageEmbedded.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_ImageEmbedded,self.Ptr)
        return ret

    @ImageEmbedded.setter
    def ImageEmbedded(self, value:bool):
        """
        Sets a value indicating whether to embed the image into the HTML code using the Data URI scheme.
        """
        GetDllLibDoc().HtmlExportOptions_set_ImageEmbedded.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_ImageEmbedded,self.Ptr, value)

    @property
    def IsExportDocumentStyles(self)->bool:
        """
        Gets or sets a value indicating whether to export the document styles to the head.
        """
        GetDllLibDoc().HtmlExportOptions_get_IsExportDocumentStyles.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_IsExportDocumentStyles.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_IsExportDocumentStyles,self.Ptr)
        return ret

    @IsExportDocumentStyles.setter
    def IsExportDocumentStyles(self, value:bool):
        """
        Sets a value indicating whether to export the document styles to the head.
        """
        GetDllLibDoc().HtmlExportOptions_set_IsExportDocumentStyles.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_IsExportDocumentStyles,self.Ptr, value)

    @property

    def CssStyleSheetFileName(self)->str:
        """
        Gets or sets the name of the HTML export CSS style sheet file.
        """
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetFileName.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetFileName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().HtmlExportOptions_get_CssStyleSheetFileName,self.Ptr))
        return ret


    @CssStyleSheetFileName.setter
    def CssStyleSheetFileName(self, value:str):
        """
        Sets the name of the HTML export CSS style sheet file.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetFileName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_CssStyleSheetFileName,self.Ptr, valuePtr)

    @property
    def HasHeadersFooters(self)->bool:
        """
        Gets or sets a value indicating whether to export headers and footers in HTML.
        """
        GetDllLibDoc().HtmlExportOptions_get_HasHeadersFooters.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_HasHeadersFooters.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_HasHeadersFooters,self.Ptr)
        return ret

    @HasHeadersFooters.setter
    def HasHeadersFooters(self, value:bool):
        """
        Sets a value indicating whether to export headers and footers in HTML.
        """
        GetDllLibDoc().HtmlExportOptions_set_HasHeadersFooters.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_HasHeadersFooters,self.Ptr, value)

    @property
    def IsTextInputFormFieldAsText(self)->bool:
        """
        Gets or sets a value indicating whether to export text input form fields as text in HTML.
        """
        GetDllLibDoc().HtmlExportOptions_get_IsTextInputFormFieldAsText.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_IsTextInputFormFieldAsText.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_IsTextInputFormFieldAsText,self.Ptr)
        return ret

    @IsTextInputFormFieldAsText.setter
    def IsTextInputFormFieldAsText(self, value:bool):
        """
        Sets a value indicating whether to export text input form fields as text in HTML.
        """
        GetDllLibDoc().HtmlExportOptions_set_IsTextInputFormFieldAsText.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_IsTextInputFormFieldAsText,self.Ptr, value)

    @property

    def ImagesPath(self)->str:
        """
        Gets or sets the folder for exporting images in HTML.
        """
        GetDllLibDoc().HtmlExportOptions_get_ImagesPath.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_ImagesPath.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().HtmlExportOptions_get_ImagesPath,self.Ptr))
        return ret


    @ImagesPath.setter
    def ImagesPath(self, value:str):
        """
        Sets the folder for exporting images in HTML.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().HtmlExportOptions_set_ImagesPath.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_ImagesPath,self.Ptr, valuePtr)

    @property
    def UseSaveFileRelativePath(self)->bool:
        """
        Gets or sets a value indicating whether the image path is relative to the file save path.
        """
        GetDllLibDoc().HtmlExportOptions_get_UseSaveFileRelativePath.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_UseSaveFileRelativePath.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_UseSaveFileRelativePath,self.Ptr)
        return ret

    @UseSaveFileRelativePath.setter
    def UseSaveFileRelativePath(self, value:bool):
        """
        Sets a value indicating whether the image path is relative to the file save path.
        """
        GetDllLibDoc().HtmlExportOptions_set_UseSaveFileRelativePath.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_UseSaveFileRelativePath,self.Ptr, value)

    @property
    def UseMsoSpace(self)->bool:
        """
        Gets or sets a value indicating whether to use Microsoft Office rules for spacing.
        """
        GetDllLibDoc().HtmlExportOptions_get_UseMsoSpace.argtypes=[c_void_p]
        GetDllLibDoc().HtmlExportOptions_get_UseMsoSpace.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().HtmlExportOptions_get_UseMsoSpace,self.Ptr)
        return ret

    @UseMsoSpace.setter
    def UseMsoSpace(self, value:bool):
        """
        Sets a value indicating whether to use Microsoft Office rules for spacing.
        """
        GetDllLibDoc().HtmlExportOptions_set_UseMsoSpace.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().HtmlExportOptions_set_UseMsoSpace,self.Ptr, value)

