from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class LOGFONT (SpireObject) :
    """
    Represents a LOGFONT object.
    """

    def ToString(self)->str:
        """
        Converts the LOGFONT object to a string.
        
        Returns:
            str: The string representation of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_ToString.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().LOGFONT_ToString,self.Ptr))
        return ret


    def lfHeight(self)->int:
        """
        Gets the height of the LOGFONT object.
        
        Returns:
            int: The height of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfHeight.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfHeight.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfHeight,self.Ptr)
        return ret

    def lfWidth(self)->int:
        """
        Gets the width of the LOGFONT object.
        
        Returns:
            int: The width of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfWidth.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfWidth.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfWidth,self.Ptr)
        return ret

    def lfEscapement(self)->int:
        """
        Gets the escapement of the LOGFONT object.
        
        Returns:
            int: The escapement of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfEscapement.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfEscapement.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfEscapement,self.Ptr)
        return ret

    def lfOrientation(self)->int:
        """
        Gets the orientation of the LOGFONT object.
        
        Returns:
            int: The orientation of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfOrientation.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfOrientation.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfOrientation,self.Ptr)
        return ret


    def lfWeight(self)->'FontWeight':
        """
        Gets the weight of the LOGFONT object.
        
        Returns:
            FontWeight: The weight of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfWeight.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfWeight.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfWeight,self.Ptr)
        objwraped = FontWeight(ret)
        return objwraped

    def lfItalic(self)->bool:
        """
        Checks if the LOGFONT object is italic.
        
        Returns:
            bool: True if the LOGFONT object is italic, False otherwise.
        """
        GetDllLibDoc().LOGFONT_lfItalic.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfItalic.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfItalic,self.Ptr)
        return ret

    def lfUnderline(self)->bool:
        """
        Checks if the LOGFONT object is underlined.
        
        Returns:
            bool: True if the LOGFONT object is underlined, False otherwise.
        """
        GetDllLibDoc().LOGFONT_lfUnderline.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfUnderline.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfUnderline,self.Ptr)
        return ret

    def lfStrikeOut(self)->bool:
        """
        Checks if the LOGFONT object has a strikeout.
        
        Returns:
            bool: True if the LOGFONT object has a strikeout, False otherwise.
        """
        GetDllLibDoc().LOGFONT_lfStrikeOut.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfStrikeOut.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfStrikeOut,self.Ptr)
        return ret


    def lfCharSet(self)->'FontCharSet':
        """
        Gets the character set of the LOGFONT object.
        
        Returns:
            FontCharSet: The character set of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfCharSet.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfCharSet.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfCharSet,self.Ptr)
        objwraped = FontCharSet(ret)
        return objwraped


    def lfOutPrecision(self)->'FontPrecision':
        """
        Gets the output precision of the LOGFONT object.
        
        Returns:
            FontPrecision: The output precision of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfOutPrecision.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfOutPrecision.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfOutPrecision,self.Ptr)
        objwraped = FontPrecision(ret)
        return objwraped


    def lfClipPrecision(self)->'FontClipPrecision':
        """
        Gets the clipping precision of the LOGFONT object.
        
        Returns:
            FontClipPrecision: The clipping precision of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfClipPrecision.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfClipPrecision.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfClipPrecision,self.Ptr)
        objwraped = FontClipPrecision(ret)
        return objwraped


    def lfQuality(self)->'FontQuality':
        """
        Gets the quality of the LOGFONT object.
        
        Returns:
            FontQuality: The quality of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfQuality.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfQuality.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfQuality,self.Ptr)
        objwraped = FontQuality(ret)
        return objwraped


    def lfPitchAndFamily(self)->'FontPitchAndFamily':
        """
        Gets the pitch and family of the LOGFONT object.
        
        Returns:
            FontPitchAndFamily: The pitch and family of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfPitchAndFamily.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfPitchAndFamily.restype=c_int
        ret = CallCFunction(GetDllLibDoc().LOGFONT_lfPitchAndFamily,self.Ptr)
        objwraped = FontPitchAndFamily(ret)
        return objwraped


    def lfFaceName(self)->str:
        """
        Gets the face name of the LOGFONT object.
        
        Returns:
            str: The face name of the LOGFONT object.
        """
        GetDllLibDoc().LOGFONT_lfFaceName.argtypes=[c_void_p]
        GetDllLibDoc().LOGFONT_lfFaceName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().LOGFONT_lfFaceName,self.Ptr))
        return ret


