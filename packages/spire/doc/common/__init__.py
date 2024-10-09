import os
import platform
from ctypes import *
from typing import TypeVar,Union,Generic,List,Tuple

def LoadLib(path:str):
    whlPath = os.path.abspath(__file__ + '/../../lib/'+ path)
    fileExists = os.path.isfile(whlPath)
    if fileExists:
        return cdll.LoadLibrary(whlPath)
    fileExists = os.path.isfile(path)
    if fileExists:
        return cdll.LoadLibrary(path)

    return None

os_name = platform.system()
os_version = platform.release()
path = os.environ['PATH']
new_path = os.path.abspath(__file__ + '/../../lib/')
os.environ['PATH'] = new_path + os.pathsep + path

if os_name == "Windows":
    lib_pathXls = r'.\Spire.Xls.Base.dll'
    lib_pathDoc = r'.\Spire.Doc.Base.dll'
    lib_pathPdf = r'.\Spire.Pdf.Base.dll'
    lib_pathPpt = r'.\Spire.Presentation.Base.dll'
elif os_name == "Linux":
    lib_pathXls = r'./Spire.Xls.Base.so'
    lib_pathDoc = r'./Spire.Doc.Base.so'
    lib_pathPdf = r'./Spire.Pdf.Base.so'
    lib_pathPpt = r'./Spire.Presentation.Base.so'
elif os_name =="Darwin":
    lib_pathXls = r'./Spire.Xls.Base.dylib'
    lib_pathDoc = r'./Spire.Doc.Base.dylib'
    lib_pathPdf = r'./Spire.Pdf.Base.dylib'
    lib_pathPpt = r'./Spire.Presentation.Base.dylib'
else:
    lib_pathXls = r'./Spire.Xls.Base.dll'
    lib_pathDoc = r'./Spire.Doc.Base.dll'
    lib_pathPdf = r'./Spire.Pdf.Base.dll'
    lib_pathPpt = r'./Spire.Presentation.Base.dll'
dlllibXls = None
dlllibXls = LoadLib(lib_pathXls)
dlllibDoc = LoadLib(lib_pathDoc)
dlllibPdf = LoadLib(lib_pathPdf)
dlllibPpt = LoadLib(lib_pathPpt)
dlllib = dlllibXls
if dlllibXls != None and __package__ == "spire.xls.common":
    dlllib = dlllibXls
elif dlllibDoc != None and __package__ == "spire.doc.common":
    dlllib = dlllibDoc
elif dlllibPdf != None and __package__ == "spire.pdf.common":
    dlllib = dlllibPdf
elif dlllibPpt != None and __package__ == "spire.presentation.common":
    dlllib = dlllibPpt

def GetDllLibXls():
    #if dlllibXls != None:
    #    dlllibXls = LoadLib(lib_pathXls)
    #if dlllibXls != None:
    dlllib = dlllibXls
    return dlllibXls;

def GetDllLibDoc():
    #if dlllibDoc == None:
    #    dlllibDoc = LoadLib(lib_pathDoc)
    #if dlllibDoc != None:
    dlllib = dlllibDoc
    return dlllibDoc;
def GetDllLibPdf():
    #if dlllibPdf == None:
    #    dlllibPdf = LoadLib(lib_pathPdf)
    #if dlllibPdf != None:
    dlllib = dlllibPdf
    return dlllibPdf;
def GetDllLibPpt():
    #if dlllibPpt == None:
    #    dlllibPpt = LoadLib(lib_pathPpt)
    #if dlllibPpt != None:
    dlllib = dlllibPpt
    return dlllibPpt;
def ChangeHandleToXls():
    GetDllLibXls()
def ChangeHandleToDoc():
    GetDllLibDoc()
def ChangeHandleToPdf():
    GetDllLibPdf()
def ChangeHandleToPpt():
    GetDllLibPpt()
    
class SpireException(Exception):
    """Custom Exception"""
    def __init__(self, message="custom exception"):
        self.message = message
        super().__init__(self.message)

def CallCFunction(func, *args, **kwargs):
    if hasattr(func, 'argtypes') and func.argtypes is not None:
        new_argtypes = [c_int if arg == c_bool else arg for arg in func.argtypes]
        func.argtypes = new_argtypes
        
    data = create_string_buffer(sizeof(c_uint64))
    old_value  = 0
    # Write the initial values to the allocated memory
    memmove(data, byref(c_uint64(0)), sizeof(c_uint64))
    args = list(args) +[data]

    result = func(*args, **kwargs)
    modified_value = cast(data, POINTER(c_uint64)).contents.value
    if old_value != modified_value:
        info = PtrToStr(modified_value)
        raise SpireException(info)
    return result

if __package__ == "spire.pdf.common" :
    from spire.pdf.common.SpireObject import SpireObject

    from spire.pdf.common.Common import IntPtrArray
    from spire.pdf.common.Common import GetObjVectorFromArray
    from spire.pdf.common.Common import GetVectorFromArray
    from spire.pdf.common.Common import GetStrVectorFromArray
    from spire.pdf.common.Common import GetIntPtrArray
    from spire.pdf.common.Common import GetByteArray
    from spire.pdf.common.Common import GetIntValue
    from spire.pdf.common.Common import GetBytesFromArray
    from spire.pdf.common.Common import PtrToStr
    from spire.pdf.common.Common import ReleasePtr

    from spire.pdf.common.RegexOptions import RegexOptions
    from spire.pdf.common.CultureInfo import CultureInfo
    from spire.pdf.common.Boolean import Boolean
    from spire.pdf.common.Byte import Byte
    from spire.pdf.common.Char import Char
    from spire.pdf.common.Int16 import Int16
    from spire.pdf.common.Int32 import Int32
    from spire.pdf.common.Int64 import Int64
    from spire.pdf.common.PixelFormat import PixelFormat
    from spire.pdf.common.Size import Size
    from spire.pdf.common.SizeF import SizeF
    from spire.pdf.common.Point import Point
    from spire.pdf.common.PointF import PointF
    from spire.pdf.common.Rectangle import Rectangle
    from spire.pdf.common.RectangleF import RectangleF
    from spire.pdf.common.Single import Single
    from spire.pdf.common.TimeSpan import TimeSpan
    from spire.pdf.common.UInt16 import UInt16
    from spire.pdf.common.UInt32 import UInt32
    from spire.pdf.common.UInt64 import UInt64
    from spire.pdf.common.Stream import Stream
    from spire.pdf.common.License import License
    from spire.pdf.common.Color import Color
    from spire.pdf.common.DateTime import DateTime
    from spire.pdf.common.Double import Double
    from spire.pdf.common.EmfType import EmfType
    from spire.pdf.common.Encoding import Encoding
    from spire.pdf.common.FontStyle import FontStyle
    from spire.pdf.common.GraphicsUnit import GraphicsUnit
    from spire.pdf.common.ICollection import ICollection
    from spire.pdf.common.IDictionary import IDictionary
    from spire.pdf.common.IEnumerable import IEnumerable
    from spire.pdf.common.IEnumerator import IEnumerator
    from spire.pdf.common.IList import IList
    from spire.pdf.common.String import String
    from spire.pdf.common.Regex import Regex
elif __package__ == "spire.xls.common" :
    from spire.xls.common.SpireObject import SpireObject

    from spire.xls.common.Common import IntPtrArray
    from spire.xls.common.Common import GetObjVectorFromArray
    from spire.xls.common.Common import GetVectorFromArray
    from spire.xls.common.Common import GetIntPtrArray
    from spire.xls.common.Common import GetByteArray
    from spire.xls.common.Common import GetIntValue
    from spire.xls.common.Common import GetBytesFromArray
    from spire.xls.common.Common import PtrToStr
    from spire.xls.common.Common import ReleasePtr

    from spire.xls.common.RegexOptions import RegexOptions
    from spire.xls.common.CultureInfo import CultureInfo
    from spire.xls.common.Boolean import Boolean
    from spire.xls.common.Byte import Byte
    from spire.xls.common.Char import Char
    from spire.xls.common.Int16 import Int16
    from spire.xls.common.Int32 import Int32
    from spire.xls.common.Int64 import Int64
    from spire.xls.common.PixelFormat import PixelFormat
    from spire.xls.common.Size import Size
    from spire.xls.common.SizeF import SizeF
    from spire.xls.common.Point import Point
    from spire.xls.common.PointF import PointF
    from spire.xls.common.Rectangle import Rectangle
    from spire.xls.common.RectangleF import RectangleF
    from spire.xls.common.Single import Single
    from spire.xls.common.TimeSpan import TimeSpan
    from spire.xls.common.UInt16 import UInt16
    from spire.xls.common.UInt32 import UInt32
    from spire.xls.common.UInt64 import UInt64
    from spire.xls.common.Stream import Stream
    from spire.xls.common.License import License
    from spire.xls.common.Color import Color
    from spire.xls.common.DateTime import DateTime
    from spire.xls.common.Double import Double
    from spire.xls.common.EmfType import EmfType
    from spire.xls.common.Encoding import Encoding
    from spire.xls.common.FontStyle import FontStyle
    from spire.xls.common.GraphicsUnit import GraphicsUnit
    from spire.xls.common.ICollection import ICollection
    from spire.xls.common.IDictionary import IDictionary
    from spire.xls.common.IEnumerable import IEnumerable
    from spire.xls.common.IEnumerator import IEnumerator
    from spire.xls.common.IList import IList
    from spire.xls.common.String import String
    from spire.xls.common.Regex import Regex
elif __package__ == "spire.doc.common" :
    from spire.doc.common.SpireObject import SpireObject

    from spire.doc.common.Common import IntPtrArray
    from spire.doc.common.Common import GetObjVectorFromArray
    from spire.doc.common.Common import GetVectorFromArray
    from spire.doc.common.Common import GetStrVectorFromArray
    from spire.doc.common.Common import GetIntPtrArray
    from spire.doc.common.Common import GetByteArray
    from spire.doc.common.Common import GetIntValue
    from spire.doc.common.Common import GetBytesFromArray
    from spire.doc.common.Common import PtrToStr
    from spire.doc.common.Common import StrToPtr
    from spire.doc.common.Common import ReleasePtr

    from spire.doc.common.RegexOptions import RegexOptions
    from spire.doc.common.CultureInfo import CultureInfo
    from spire.doc.common.Boolean import Boolean
    from spire.doc.common.Byte import Byte
    from spire.doc.common.Char import Char
    from spire.doc.common.Int16 import Int16
    from spire.doc.common.Int32 import Int32
    from spire.doc.common.Int64 import Int64
    from spire.doc.common.PixelFormat import PixelFormat
    from spire.doc.common.Size import Size
    from spire.doc.common.SizeF import SizeF
    from spire.doc.common.Point import Point
    from spire.doc.common.PointF import PointF
    from spire.doc.common.Rectangle import Rectangle
    from spire.doc.common.RectangleF import RectangleF
    from spire.doc.common.Single import Single
    from spire.doc.common.TimeSpan import TimeSpan
    from spire.doc.common.UInt16 import UInt16
    from spire.doc.common.UInt32 import UInt32
    from spire.doc.common.UInt64 import UInt64
    from spire.doc.common.Stream import Stream
    from spire.doc.common.License import License
    from spire.doc.common.Color import Color
    from spire.doc.common.DateTime import DateTime
    from spire.doc.common.Double import Double
    from spire.doc.common.EmfType import EmfType
    from spire.doc.common.Encoding import Encoding
    from spire.doc.common.FontStyle import FontStyle
    from spire.doc.common.GraphicsUnit import GraphicsUnit
    from spire.doc.common.ICollection import ICollection
    from spire.doc.common.IDictionary import IDictionary
    from spire.doc.common.IEnumerable import IEnumerable
    from spire.doc.common.IEnumerator import IEnumerator
    from spire.doc.common.IList import IList
    from spire.doc.common.String import String
    from spire.doc.common.Regex import Regex
else :
    from spire.presentation.common.SpireObject import SpireObject

    from spire.presentation.common.Common import IntPtrArray
    from spire.presentation.common.Common import GetObjVectorFromArray
    from spire.presentation.common.Common import GetVectorFromArray
    from spire.presentation.common.Common import GetIntPtrArray
    from spire.presentation.common.Common import GetByteArray
    from spire.presentation.common.Common import GetIntValue
    from spire.presentation.common.Common import GetBytesFromArray
    from spire.presentation.common.Common import GetStrVectorFromArray
    from spire.presentation.common.Common import PtrToStr
    from spire.presentation.common.Common import StrToPtr
    from spire.presentation.common.Common import ReleasePtr

    from spire.presentation.common.RegexOptions import RegexOptions
    from spire.presentation.common.CultureInfo import CultureInfo
    from spire.presentation.common.Boolean import Boolean
    from spire.presentation.common.Byte import Byte
    from spire.presentation.common.Char import Char
    from spire.presentation.common.Int16 import Int16
    from spire.presentation.common.Int32 import Int32
    from spire.presentation.common.Int64 import Int64
    from spire.presentation.common.PixelFormat import PixelFormat
    from spire.presentation.common.Size import Size
    from spire.presentation.common.SizeF import SizeF
    from spire.presentation.common.Point import Point
    from spire.presentation.common.PointF import PointF
    from spire.presentation.common.Rectangle import Rectangle
    from spire.presentation.common.RectangleF import RectangleF
    from spire.presentation.common.Single import Single
    from spire.presentation.common.TimeSpan import TimeSpan
    from spire.presentation.common.UInt16 import UInt16
    from spire.presentation.common.UInt32 import UInt32
    from spire.presentation.common.UInt64 import UInt64
    from spire.presentation.common.Stream import Stream
    from spire.presentation.common.License import License
    from spire.presentation.common.Color import Color
    from spire.presentation.common.DateTime import DateTime
    from spire.presentation.common.Double import Double
    from spire.presentation.common.EmfType import EmfType
    from spire.presentation.common.Encoding import Encoding
    from spire.presentation.common.FontStyle import FontStyle
    from spire.presentation.common.GraphicsUnit import GraphicsUnit
    from spire.presentation.common.ICollection import ICollection
    from spire.presentation.common.IDictionary import IDictionary
    from spire.presentation.common.IEnumerable import IEnumerable
    from spire.presentation.common.IEnumerator import IEnumerator
    from spire.presentation.common.IList import IList
    from spire.presentation.common.String import String
    from spire.presentation.common.Regex import Regex