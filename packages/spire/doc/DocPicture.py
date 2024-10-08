from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class DocPicture(ShapeObject, IPicture):
#class DocPicture (  ShapeObject, IDocumentObject,IPicture) :
    """
    Represents a picture in a document.
    """

    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the DocPicture class.

        Args:
            doc (IDocument): The document to which the picture belongs.
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().DocPicture_CreateDocPictureD.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_CreateDocPictureD.restype = c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocPicture_CreateDocPictureD,intPdoc)
        super(DocPicture, self).__init__(intPtr)

    @property
    def Rotation(self) -> float:
        """
        Gets or sets the rotation of the picture.

        Returns:
            float: The rotation of the picture.
        """
        GetDllLibDoc().DocPicture_get_Rotation.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Rotation.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_Rotation,self.Ptr)
        return ret

    @Rotation.setter
    def Rotation(self, value:float):
        """
        Sets the rotation of the picture.

        Args:
            value (float): The rotation value to set.
        """
        GetDllLibDoc().DocPicture_set_Rotation.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_Rotation,self.Ptr, value)

    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.

        Returns:
            DocumentObjectType: The type of the document object.
        """
        GetDllLibDoc().DocPicture_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property
    def Height(self)->float:
        """
        Gets or sets the height of the picture.

        Returns:
            float: The height of the picture.
        """
        GetDllLibDoc().DocPicture_get_Height.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Height.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_Height,self.Ptr)
        return ret

    @Height.setter
    def Height(self, value:float):
        """
        Sets the height of the picture.

        Args:
            value (float): The height value to set.
        """
        GetDllLibDoc().DocPicture_set_Height.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_Height,self.Ptr, value)

    @property
    def Width(self)->float:
        """
        Gets or sets the width of the picture.

        Returns:
            float: The width of the picture.
        """
        GetDllLibDoc().DocPicture_get_Width.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Width.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_Width,self.Ptr)
        return ret

    @Width.setter
    def Width(self, value:float):
        """
        Sets the width of the picture.

        Args:
            value (float): The width value to set.
        """
        GetDllLibDoc().DocPicture_set_Width.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_Width,self.Ptr, value)

    @property
    def HeightScale(self)->float:
        """
        Gets or sets the height scale of the picture.

        Returns:
            float: The height scale of the picture.
        """
        GetDllLibDoc().DocPicture_get_HeightScale.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HeightScale.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_HeightScale,self.Ptr)
        return ret

    @HeightScale.setter
    def HeightScale(self, value:float):
        """
        Sets the height scale of the picture.

        Args:
            value (float): The height scale value to set.
        """
        GetDllLibDoc().DocPicture_set_HeightScale.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_HeightScale,self.Ptr, value)

    @property
    def WidthScale(self)->float:
        """
        Gets or sets the width scale of the picture.

        Returns:
            float: The width scale of the picture.
        """
        GetDllLibDoc().DocPicture_get_WidthScale.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_WidthScale.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_WidthScale,self.Ptr)
        return ret

    @WidthScale.setter
    def WidthScale(self, value:float):
        """
        Sets the width scale of the picture.

        Args:
            value (float): The width scale value to set.
        """
        GetDllLibDoc().DocPicture_set_WidthScale.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_WidthScale,self.Ptr, value)

    @dispatch

    def SetScale(self ,scaleFactor:float):
        """
        Scales the image by the specified scale factor.

        Args:
            scaleFactor (float): The scale factor to apply.
        """
        
        GetDllLibDoc().DocPicture_SetScale.argtypes=[c_void_p ,c_float]
        CallCFunction(GetDllLibDoc().DocPicture_SetScale,self.Ptr, scaleFactor)

    @dispatch

    def SetScale(self ,heightFactor:float,widthFactor:float):
        """
        Scales the image by the specified height and width factors.

        Args:
            heightFactor (float): The height factor to apply.
            widthFactor (float): The width factor to apply.
        """
        
        GetDllLibDoc().DocPicture_SetScaleHW.argtypes=[c_void_p ,c_float,c_float]
        CallCFunction(GetDllLibDoc().DocPicture_SetScaleHW,self.Ptr, heightFactor,widthFactor)

    @property

    def ImageBytes(self):
        """
        Gets the image byte array.

        Returns:
            bytes: The image byte array.
        """
        GetDllLibDoc().DocPicture_get_ImageBytes.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_ImageBytes.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().DocPicture_get_ImageBytes,self.Ptr)
        ret = GetBytesFromArray(intPtrArray)
        return ret


    @property
    def GrayScale(self)->bool:
        """
        Gets or sets a value indicating whether the picture is in grayscale.

        Returns:
            bool: True if the picture is in grayscale, False otherwise.
        """
        GetDllLibDoc().DocPicture_get_GrayScale.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_GrayScale.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_GrayScale,self.Ptr)
        return ret

    @GrayScale.setter
    def GrayScale(self, value:bool):
        """
        Sets a value indicating whether the picture is in grayscale.

        Args:
            value (bool): True to set the picture to grayscale, False otherwise.
        """
        GetDllLibDoc().DocPicture_set_GrayScale.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().DocPicture_set_GrayScale,self.Ptr, value)

    @property
    def BiLevel(self)->bool:
        """
        Gets or sets a value indicating whether the picture is in bi-level.

        Returns:
            bool: True if the picture is in bi-level, False otherwise.
        """
        GetDllLibDoc().DocPicture_get_BiLevel.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_BiLevel.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_BiLevel,self.Ptr)
        return ret

    @BiLevel.setter
    def BiLevel(self, value:bool):
        """
        Sets a value indicating whether the picture is in bi-level.

        Args:
            value (bool): True to set the picture to bi-level, False otherwise.
        """
        GetDllLibDoc().DocPicture_set_BiLevel.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().DocPicture_set_BiLevel,self.Ptr, value)

    @property
    def Brightness(self)->float:
        """
        Gets or sets the brightness of the picture.

        Returns:
            float: The brightness of the picture.
        """
        GetDllLibDoc().DocPicture_get_Brightness.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Brightness.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_Brightness,self.Ptr)
        return ret

    @Brightness.setter
    def Brightness(self, value:float):
        """
        Sets the brightness of the picture.

        Args:
            value (float): The brightness value to set.
        """
        GetDllLibDoc().DocPicture_set_Brightness.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_Brightness,self.Ptr, value)

    @property
    def Contrast(self)->float:
        """
        Gets or sets the contrast of the picture.

        Returns:
            float: The contrast of the picture.
        """
        GetDllLibDoc().DocPicture_get_Contrast.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Contrast.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_Contrast,self.Ptr)
        return ret

    @Contrast.setter
    def Contrast(self, value:float):
        """
        Sets the contrast of the picture.

        Args:
            value (float): The contrast value to set.
        """
        GetDllLibDoc().DocPicture_set_Contrast.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_Contrast,self.Ptr, value)

    @property

    def Color(self)->'PictureColor':
        """
        Gets picture color.
        """
        GetDllLibDoc().DocPicture_get_Color.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Color.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_Color,self.Ptr)
        objwraped = PictureColor(ret)
        return objwraped

    @Color.setter
    def Color(self, value:'PictureColor'):
        """
        Sets picture color.
        """
        GetDllLibDoc().DocPicture_set_Color.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_Color,self.Ptr, value.value)

    @property

    def TransparentColor(self)->'Color':
        """
        Gets transparent color.
        """
        GetDllLibDoc().DocPicture_get_TransparentColor.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_TransparentColor.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocPicture_get_TransparentColor,self.Ptr)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @TransparentColor.setter
    def TransparentColor(self, value:'Color'):
        """
        Sets transparent color.
        """
        GetDllLibDoc().DocPicture_set_TransparentColor.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().DocPicture_set_TransparentColor,self.Ptr, value.Ptr)

    @property
    def IsCrop(self)->bool:
        """
    Gets whether the picture object is cropped.
    """
        GetDllLibDoc().DocPicture_get_IsCrop.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_IsCrop.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_IsCrop,self.Ptr)
        return ret

    @property

    def HorizontalOrigin(self)->'HorizontalOrigin':
        """
        Gets horizontal origin of the picture.
        """
        GetDllLibDoc().DocPicture_get_HorizontalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HorizontalOrigin.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_HorizontalOrigin,self.Ptr)
        objwraped = HorizontalOrigin(ret)
        return objwraped

    @HorizontalOrigin.setter
    def HorizontalOrigin(self, value:'HorizontalOrigin'):
        """
        Sets horizontal origin of the picture.
        """
        GetDllLibDoc().DocPicture_set_HorizontalOrigin.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_HorizontalOrigin,self.Ptr, value.value)

    @property

    def VerticalOrigin(self)->'VerticalOrigin':
        """
        Gets absolute horizontal position of the picture.
        """
        GetDllLibDoc().DocPicture_get_VerticalOrigin.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_VerticalOrigin.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_VerticalOrigin,self.Ptr)
        objwraped = VerticalOrigin(ret)
        return objwraped

    @VerticalOrigin.setter
    def VerticalOrigin(self, value:'VerticalOrigin'):
        """
        Sets absolute horizontal position of the picture.
        """
        GetDllLibDoc().DocPicture_set_VerticalOrigin.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_VerticalOrigin,self.Ptr, value.value)

    @property
    def HorizontalPosition(self)->float:
        """
        Gets absolute horizontal position of the picture.
        """
        GetDllLibDoc().DocPicture_get_HorizontalPosition.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HorizontalPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_HorizontalPosition,self.Ptr)
        return ret

    @HorizontalPosition.setter
    def HorizontalPosition(self, value:float):
        """
        Sets absolute horizontal position of the picture.
        """
        GetDllLibDoc().DocPicture_set_HorizontalPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_HorizontalPosition,self.Ptr, value)

    @property
    def VerticalPosition(self)->float:
        """
        Gets absolute vertical position of the picture.
        """
        GetDllLibDoc().DocPicture_get_VerticalPosition.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_VerticalPosition.restype=c_float
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_VerticalPosition,self.Ptr)
        return ret

    @VerticalPosition.setter
    def VerticalPosition(self, value:float):
        """
        Sets absolute vertical position of the picture.
        """
        GetDllLibDoc().DocPicture_set_VerticalPosition.argtypes=[c_void_p, c_float]
        CallCFunction(GetDllLibDoc().DocPicture_set_VerticalPosition,self.Ptr, value)

    @property

    def TextWrappingStyle(self)->'TextWrappingStyle':
        """
        Gets text wrapping style of the picture.
        """
        GetDllLibDoc().DocPicture_get_TextWrappingStyle.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_TextWrappingStyle.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_TextWrappingStyle,self.Ptr)
        objwraped = TextWrappingStyle(ret)
        return objwraped

    @TextWrappingStyle.setter
    def TextWrappingStyle(self, value:'TextWrappingStyle'):
        """
        Sets text wrapping style of the picture.
        """
        GetDllLibDoc().DocPicture_set_TextWrappingStyle.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_TextWrappingStyle,self.Ptr, value.value)

    @property

    def TextWrappingType(self)->'TextWrappingType':
        """
        Gets text wrapping type of the picture.
        """
        GetDllLibDoc().DocPicture_get_TextWrappingType.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_TextWrappingType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_TextWrappingType,self.Ptr)
        objwraped = TextWrappingType(ret)
        return objwraped

    @TextWrappingType.setter
    def TextWrappingType(self, value:'TextWrappingType'):
        """
        Sets the text wrapping type of the picture.
        :param value: The text wrapping type to be set.
        """
        GetDllLibDoc().DocPicture_set_TextWrappingType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_TextWrappingType,self.Ptr, value.value)

    @property

    def HorizontalAlignment(self)->'ShapeHorizontalAlignment':
        """
        Gets the horizontal alignment of the picture.
        :return: The horizontal alignment of the picture.
        """
        GetDllLibDoc().DocPicture_get_HorizontalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_HorizontalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_HorizontalAlignment,self.Ptr)
        objwraped = ShapeHorizontalAlignment(ret)
        return objwraped

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value:'ShapeHorizontalAlignment'):
        """
        Sets the horizontal alignment of the picture.
        :param value: The horizontal alignment to be set.
        """
        GetDllLibDoc().DocPicture_set_HorizontalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_HorizontalAlignment,self.Ptr, value.value)

    @property

    def VerticalAlignment(self)->'ShapeVerticalAlignment':
        """
        Gets the vertical alignment of the picture.
        :return: The vertical alignment of the picture.
        """
        GetDllLibDoc().DocPicture_get_VerticalAlignment.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_VerticalAlignment.restype=c_int
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_VerticalAlignment,self.Ptr)
        objwraped = ShapeVerticalAlignment(ret)
        return objwraped

    @VerticalAlignment.setter
    def VerticalAlignment(self, value:'ShapeVerticalAlignment'):
        """
        Sets the vertical alignment of the picture.
        :param value: The vertical alignment to be set.
        """
        GetDllLibDoc().DocPicture_set_VerticalAlignment.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().DocPicture_set_VerticalAlignment,self.Ptr, value.value)

    @property
    def IsUnderText(self)->bool:
        """
        Gets whether the picture is below the text.
        :return: True if the picture is below the text, False otherwise.
        """
        GetDllLibDoc().DocPicture_get_IsUnderText.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_IsUnderText.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_IsUnderText,self.Ptr)
        return ret

    @IsUnderText.setter
    def IsUnderText(self, value:bool):
        """
        Sets whether the picture is below the text.
        :param value: True if the picture is below the text, False otherwise.
        """
        GetDllLibDoc().DocPicture_set_IsUnderText.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().DocPicture_set_IsUnderText,self.Ptr, value)

    @property

    def CharacterFormat(self)->'CharacterFormat':
        """
        Gets the character format of the shape object.
        :return: The character format of the shape object.
        """
        GetDllLibDoc().DocPicture_get_CharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_CharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocPicture_get_CharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def Title(self)->str:
        """
        Gets the title of the picture.
        :return: The title of the picture.
        """
        GetDllLibDoc().DocPicture_get_Title.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_Title.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().DocPicture_get_Title,self.Ptr))
        return ret


    @Title.setter
    def Title(self, value:str):
        """
        Sets the title of the picture.
        :param value: The title to be set.
        """
        valuePtr = StrToPtr(value)
        GetDllLibDoc().DocPicture_set_Title.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().DocPicture_set_Title,self.Ptr, valuePtr)

    @property
    def LayoutInCell(self)->bool:
        """
        Gets whether a picture in a table is displayed inside or outside the table.
        :return: True if the picture is displayed inside the table, False otherwise.
        """
        GetDllLibDoc().DocPicture_get_LayoutInCell.argtypes=[c_void_p]
        GetDllLibDoc().DocPicture_get_LayoutInCell.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().DocPicture_get_LayoutInCell,self.Ptr)
        return ret

    @LayoutInCell.setter
    def LayoutInCell(self, value:bool):
        """
        Sets whether a picture in a table is displayed inside or outside the table.
        :param value: True if the picture is displayed inside the table, False otherwise.
        """
        GetDllLibDoc().DocPicture_set_LayoutInCell.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().DocPicture_set_LayoutInCell,self.Ptr, value)

    @dispatch

    def LoadImage(self ,imgFile:str):
        """
        Loads the image from a file.
        :param imgFile: The path of the image file.
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().DocPicture_LoadImageI.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().DocPicture_LoadImageI,self.Ptr, imgFilePtr)

    @dispatch

    def LoadImage(self ,imgStream:Stream):
        """
        Loads the image from a stream.
        :param imgStream: The stream containing the image data.
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().DocPicture_LoadImageI1.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().DocPicture_LoadImageI1,self.Ptr, intPtrimgStream)

    @dispatch

    def LoadImage(self ,imageBytes:bytes):
        """
        Loads the image from a byte array.
        :param imageBytes: The byte array containing the image data.
        """
        #arrayimageBytes:ArrayTypeimageBytes = ""
        list_address:c_void_p = cast((c_ubyte * len(imageBytes)).from_buffer_copy(imageBytes),c_void_p)
        length:c_int = len(imageBytes)

        GetDllLibDoc().DocPicture_LoadImageI11.argtypes=[c_void_p ,c_void_p,c_int]
        CallCFunction(GetDllLibDoc().DocPicture_LoadImageI11,self.Ptr,list_address, length)



    def ReplaceImage(self ,imageBytes:bytes,bIsKeepRation:bool):
        """
        Replaces the image with a new image.
        :param imageBytes: The byte array containing the new image data.
        :param bIsKeepRation: True to keep the original aspect ratio of the image, False otherwise.
        """
        #arrayimageBytes:ArrayTypeimageBytes = ""
        list_address:c_void_p = cast((c_ubyte * len(imageBytes)).from_buffer_copy(imageBytes),c_void_p)
        length:c_int = len(imageBytes)

        GetDllLibDoc().DocPicture_ReplaceImage.argtypes=[c_void_p ,c_void_p,c_int,c_bool]
        CallCFunction(GetDllLibDoc().DocPicture_ReplaceImage,self.Ptr, list_address,length,bIsKeepRation)



    def AddCaption(self ,name:str,numberingFormat:'CaptionNumberingFormat',captionPosition:'CaptionPosition')->'IParagraph':
        """
        Adds a caption for the current picture.
        :param name: The name of the caption.
        :param numberingFormat: The numbering format of the caption.
        :param captionPosition: The position of the caption.
        :return: The paragraph object representing the added caption.
        """
        namePtr = StrToPtr(name)
        enumformat:c_int = numberingFormat.value
        enumcaptionPosition:c_int = captionPosition.value

        GetDllLibDoc().DocPicture_AddCaption.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        GetDllLibDoc().DocPicture_AddCaption.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().DocPicture_AddCaption,self.Ptr, namePtr,enumformat,enumcaptionPosition)
        #ret = None if intPtr==None else IParagraph(intPtr)
        from spire.doc import Paragraph
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


