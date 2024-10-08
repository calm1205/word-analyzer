from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocOleObject(ShapeObject, IDocumentObject):
    """
    Represents an OLE object in a document.
    """
    @property
    def DisplayAsIcon(self)->bool:
        """
        Gets or sets whether the OLEObject is displayed as an Icon or Content.
        If True, the OLEObject is displayed as an icon.
        """
        GetDllLibDoc().DocOleObject_get_DisplayAsIcon.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_DisplayAsIcon.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocOleObject_get_DisplayAsIcon,self.Ptr)
        return ret

    @DisplayAsIcon.setter
    def DisplayAsIcon(self, value:bool):
        """
        Sets whether the OLEObject is displayed as an Icon or Content.
        If True, the OLEObject is displayed as an icon.
        """
        GetDllLibDoc().DocOleObject_set_DisplayAsIcon.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().DocOleObject_set_DisplayAsIcon,self.Ptr, value)

    @property

    def OlePicture(self)->'DocPicture':
        """
        Gets the OLE picture.
        """
        GetDllLibDoc().DocOleObject_get_OlePicture.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_OlePicture.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocOleObject_get_OlePicture,self.Ptr)
        ret = None if intPtr==None else DocPicture(intPtr)
        return ret

    @property
    def DocumentObjectType(self) -> 'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().DocOleObject_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocOleObject_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def Container(self) -> 'Stream':
        """
        Gets the OLE container.
        """
        GetDllLibDoc().DocOleObject_get_Container.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_Container.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocOleObject_get_Container,self.Ptr)
        ret = None if intPtr==None else Stream(intPtr)
        return ret


    @property
    def CharacterFormat(self) -> 'CharacterFormat':
        """
        Gets the character format of the OLE object.
        """
        GetDllLibDoc().DocOleObject_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocOleObject_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret

    @property
    def OleStorageName(self) -> str:
        """
        Gets or sets the name of the OLE Object storage.
        """
        GetDllLibDoc().DocOleObject_get_OleStorageName.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_OleStorageName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocOleObject_get_OleStorageName,self.Ptr))
        return ret


    @OleStorageName.setter
    def OleStorageName(self, value:str):
        """
        Sets the name of the OLE Object storage.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocOleObject_set_OleStorageName.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().DocOleObject_set_OleStorageName,self.Ptr, valuePtr)

    @property
    def LinkPath(self) -> str:
        """
        Gets or sets the link path.
        """
        GetDllLibDoc().DocOleObject_get_LinkPath.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_LinkPath.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocOleObject_get_LinkPath,self.Ptr))
        return ret


    @LinkPath.setter
    def LinkPath(self, value:str):
        """
        Sets the link path.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocOleObject_set_LinkPath.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().DocOleObject_set_LinkPath,self.Ptr, valuePtr)

    @property

    def LinkType(self)->'OleLinkType':
        """
        Gets the type of the OLE object.
        """
        GetDllLibDoc().DocOleObject_get_LinkType.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_LinkType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocOleObject_get_LinkType,self.Ptr)
        objwraped = OleLinkType(ret)
        return objwraped

    @property
    def ProgId(self) -> str:
        """
        Gets the programmatic identifier of the OLE object of an undefined type.
        """
        GetDllLibDoc().DocOleObject_get_ProgId.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_ProgId.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocOleObject_get_ProgId,self.Ptr))
        return ret


    @property

    def ObjectType(self)->str:
        """
        Gets or sets the type of the OLE object.
        """
        GetDllLibDoc().DocOleObject_get_ObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_ObjectType.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocOleObject_get_ObjectType,self.Ptr))
        return ret


    @ObjectType.setter
    def ObjectType(self, value:str):
        """
        Sets the type of the OLE object.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocOleObject_set_ObjectType.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().DocOleObject_set_ObjectType,self.Ptr, valuePtr)

    @property

    def NativeData(self):
        """
        Gets the native data of embedded OLE object.
        """
        GetDllLibDoc().DocOleObject_get_NativeData.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_NativeData.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().DocOleObject_get_NativeData,self.Ptr)
        ret = GetBytesFromArray(intPtrArray)
        return ret


    @property
    def PackageFileName(self) -> str:
        """
        Gets the name of file embedded in the package (only if OleType is "Package").
        """
        GetDllLibDoc().DocOleObject_get_PackageFileName.argtypes=[c_void_p]
        GetDllLibDoc().DocOleObject_get_PackageFileName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocOleObject_get_PackageFileName,self.Ptr))
        return ret


#
#    def SetNativeData(self ,nativeData:'Byte[]'):
#        """
#    <summary>
#        Sets the native data.
#    </summary>
#    <param name="nativeData">The native data.</param>
#        """
#        #arraynativeData:ArrayTypenativeData = ""
#        countnativeData = len(nativeData)
#        ArrayTypenativeData = c_void_p * countnativeData
#        arraynativeData = ArrayTypenativeData()
#        for i in range(0, countnativeData):
#            arraynativeData[i] = nativeData[i].Ptr
#
#
#        GetDllLibDoc().DocOleObject_SetNativeData.argtypes=[c_void_p ,ArrayTypenativeData]
#        GetDllLibDoc().DocOleObject_SetNativeData(self.Ptr, arraynativeData)



    def SetOlePicture(self ,picture:'DocPicture'):
        """
        Sets the OLE picture.
        """
        intPtrpicture:c_void_p = picture.Ptr

        GetDllLibDoc().DocOleObject_SetOlePicture.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().DocOleObject_SetOlePicture,self.Ptr, intPtrpicture)

