from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
elif __package__ == "spire.xls.common":
    from spire.xls.common import *
elif __package__ == "spire.doc.common":
    from spire.doc.common import *
else :
    from spire.presentation.common import *
#from spire.xls import *
from ctypes import *
import abc

class Encoding (SpireObject) :
    """

    """
#    @staticmethod
#    @dispatch
#
#    def Convert(srcEncoding:'Encoding',dstEncoding:'Encoding',bytes:'Byte[]')->List[Byte]:
#        """
#
#        """
#        intPtrsrcEncoding:c_void_p = srcEncoding.Ptr
#        intPtrdstEncoding:c_void_p = dstEncoding.Ptr
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_Convert.argtypes=[ c_void_p,c_void_p,ArrayTypebytes]
#        dlllib.Encoding_Convert.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_Convert, intPtrsrcEncoding,intPtrdstEncoding,arraybytes)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


#    @staticmethod
#
#    def RegisterProvider(provider:'EncodingProvider'):
#        """
#
#        """
#        intPtrprovider:c_void_p = provider.Ptr
#
#        dlllib.Encoding_RegisterProvider.argtypes=[ c_void_p]
#        CallCFunction(dlllib.Encoding_RegisterProvider, intPtrprovider)


    @staticmethod
    @dispatch

    def GetEncoding(codepage:int)->'Encoding':
        """

        """
        
        dlllib.Encoding_GetEncoding.argtypes=[ c_int]
        dlllib.Encoding_GetEncoding.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_GetEncoding, codepage)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


#    @staticmethod
#    @dispatch
#
#    def GetEncoding(codepage:int,encoderFallback:'EncoderFallback',decoderFallback:'DecoderFallback')->'Encoding':
#        """
#
#        """
#        intPtrencoderFallback:c_void_p = encoderFallback.Ptr
#        intPtrdecoderFallback:c_void_p = decoderFallback.Ptr
#
#        dlllib.Encoding_GetEncodingCED.argtypes=[ c_int,c_void_p,c_void_p]
#        dlllib.Encoding_GetEncodingCED.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Encoding_GetEncodingCED, codepage,intPtrencoderFallback,intPtrdecoderFallback)
#        ret = None if intPtr==None else Encoding(intPtr)
#        return ret
#


    @staticmethod
    @dispatch

    def GetEncoding(name:str)->'Encoding':
        """

        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            namePtr = StrToPtr(name)
            dlllib.Encoding_GetEncodingN.argtypes=[ c_char_p]
            dlllib.Encoding_GetEncodingN.restype=c_void_p
            intPtr = CallCFunction(dlllib.Encoding_GetEncodingN,namePtr)
            ret = None if intPtr==None else Encoding(intPtr)
            return ret
        else:
            dlllib.Encoding_GetEncodingN.argtypes=[ c_void_p]
            dlllib.Encoding_GetEncodingN.restype=c_void_p
            intPtr = CallCFunction(dlllib.Encoding_GetEncodingN, name)
            ret = None if intPtr==None else Encoding(intPtr)
            return ret
        


#    @staticmethod
#    @dispatch
#
#    def GetEncoding(name:str,encoderFallback:'EncoderFallback',decoderFallback:'DecoderFallback')->'Encoding':
#        """
#
#        """
#        intPtrencoderFallback:c_void_p = encoderFallback.Ptr
#        intPtrdecoderFallback:c_void_p = decoderFallback.Ptr
#
#        dlllib.Encoding_GetEncodingNED.argtypes=[ c_void_p,c_void_p,c_void_p]
#        dlllib.Encoding_GetEncodingNED.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Encoding_GetEncodingNED, name,intPtrencoderFallback,intPtrdecoderFallback)
#        ret = None if intPtr==None else Encoding(intPtr)
#        return ret
#


#    @staticmethod
#
#    def GetEncodings()->List['EncodingInfo']:
#        """
#
#        """
#        #dlllib.Encoding_GetEncodings.argtypes=[]
#        dlllib.Encoding_GetEncodings.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetEncodings)
#        ret = GetVectorFromArray(intPtrArray, EncodingInfo)
#        return ret


#
#    def GetPreamble(self)->List['Byte']:
#        """
#
#        """
#        dlllib.Encoding_GetPreamble.argtypes=[c_void_p]
#        dlllib.Encoding_GetPreamble.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetPreamble,self.Ptr)
#        ret = GetVectorFromArray(intPtrArray, Byte)
#        return ret


    @property

    def BodyName(self)->str:
        """

        """
        dlllib.Encoding_get_BodyName.argtypes=[c_void_p]
        dlllib.Encoding_get_BodyName.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Encoding_get_BodyName,self.Ptr))
        return ret


    @property

    def HeaderName(self)->str:
        """

        """
        dlllib.Encoding_get_HeaderName.argtypes=[c_void_p]
        dlllib.Encoding_get_HeaderName.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Encoding_get_HeaderName,self.Ptr))
        return ret


    @property

    def WebName(self)->str:
        """

        """
        dlllib.Encoding_get_WebName.argtypes=[c_void_p]
        dlllib.Encoding_get_WebName.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Encoding_get_WebName,self.Ptr))
        return ret


    @property
    def WindowsCodePage(self)->int:
        """

        """
        dlllib.Encoding_get_WindowsCodePage.argtypes=[c_void_p]
        dlllib.Encoding_get_WindowsCodePage.restype=c_int
        ret = CallCFunction(dlllib.Encoding_get_WindowsCodePage,self.Ptr)
        return ret

    @property
    def IsBrowserDisplay(self)->bool:
        """

        """
        dlllib.Encoding_get_IsBrowserDisplay.argtypes=[c_void_p]
        dlllib.Encoding_get_IsBrowserDisplay.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_get_IsBrowserDisplay,self.Ptr)
        return ret

    @property
    def IsBrowserSave(self)->bool:
        """

        """
        dlllib.Encoding_get_IsBrowserSave.argtypes=[c_void_p]
        dlllib.Encoding_get_IsBrowserSave.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_get_IsBrowserSave,self.Ptr)
        return ret

    @property
    def IsMailNewsDisplay(self)->bool:
        """

        """
        dlllib.Encoding_get_IsMailNewsDisplay.argtypes=[c_void_p]
        dlllib.Encoding_get_IsMailNewsDisplay.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_get_IsMailNewsDisplay,self.Ptr)
        return ret

    @property
    def IsMailNewsSave(self)->bool:
        """

        """
        dlllib.Encoding_get_IsMailNewsSave.argtypes=[c_void_p]
        dlllib.Encoding_get_IsMailNewsSave.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_get_IsMailNewsSave,self.Ptr)
        return ret

    @property
    def IsSingleByte(self)->bool:
        """

        """
        dlllib.Encoding_get_IsSingleByte.argtypes=[c_void_p]
        dlllib.Encoding_get_IsSingleByte.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_get_IsSingleByte,self.Ptr)
        return ret

#    @property
#
#    def EncoderFallback(self)->'EncoderFallback':
#        """
#
#        """
#        dlllib.Encoding_get_EncoderFallback.argtypes=[c_void_p]
#        dlllib.Encoding_get_EncoderFallback.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Encoding_get_EncoderFallback,self.Ptr)
#        ret = None if intPtr==None else EncoderFallback(intPtr)
#        return ret
#


#    @EncoderFallback.setter
#    def EncoderFallback(self, value:'EncoderFallback'):
#        dlllib.Encoding_set_EncoderFallback.argtypes=[c_void_p, c_void_p]
#        CallCFunction(dlllib.Encoding_set_EncoderFallback,self.Ptr, value.Ptr)


#    @property
#
#    def DecoderFallback(self)->'DecoderFallback':
#        """
#
#        """
#        dlllib.Encoding_get_DecoderFallback.argtypes=[c_void_p]
#        dlllib.Encoding_get_DecoderFallback.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Encoding_get_DecoderFallback,self.Ptr)
#        ret = None if intPtr==None else DecoderFallback(intPtr)
#        return ret
#


#    @DecoderFallback.setter
#    def DecoderFallback(self, value:'DecoderFallback'):
#        dlllib.Encoding_set_DecoderFallback.argtypes=[c_void_p, c_void_p]
#        CallCFunction(dlllib.Encoding_set_DecoderFallback,self.Ptr, value.Ptr)



    def Clone(self)->'SpireObject':
        """

        """
        dlllib.Encoding_Clone.argtypes=[c_void_p]
        dlllib.Encoding_Clone.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_Clone,self.Ptr)
        ret = None if intPtr==None else SpireObject(intPtr)
        return ret


    @property
    def IsReadOnly(self)->bool:
        """

        """
        dlllib.Encoding_get_IsReadOnly.argtypes=[c_void_p]
        dlllib.Encoding_get_IsReadOnly.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_get_IsReadOnly,self.Ptr)
        return ret

    @staticmethod

    def get_ASCII()->'Encoding':
        """

        """
        #dlllib.Encoding_get_ASCII.argtypes=[]
        dlllib.Encoding_get_ASCII.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_ASCII)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


#    @dispatch
#
#    def GetByteCount(self ,chars:'Char[]')->int:
#        """
#
#        """
#        #arraychars:ArrayTypechars = ""
#        countchars = len(chars)
#        ArrayTypechars = c_void_p * countchars
#        arraychars = ArrayTypechars()
#        for i in range(0, countchars):
#            arraychars[i] = chars[i].Ptr
#
#
#        dlllib.Encoding_GetByteCount.argtypes=[c_void_p ,ArrayTypechars]
#        dlllib.Encoding_GetByteCount.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetByteCount,self.Ptr, arraychars)
#        return ret


    @dispatch

    def GetByteCount(self ,s:str)->int:
        """

        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            sPtr = StrToPtr(s)
            dlllib.Encoding_GetByteCountS.argtypes=[c_void_p ,c_char_p]
            dlllib.Encoding_GetByteCountS.restype=c_int
            ret = CallCFunction(dlllib.Encoding_GetByteCountS,self.Ptr, sPtr)
            return ret
        else:
            dlllib.Encoding_GetByteCountS.argtypes=[c_void_p ,c_void_p]
            dlllib.Encoding_GetByteCountS.restype=c_int
            ret = CallCFunction(dlllib.Encoding_GetByteCountS,self.Ptr, s)
            return ret
        

#    @dispatch
#
#    def GetByteCount(self ,chars:'Char*',count:int)->int:
#        """
#
#        """
#        intPtrchars:c_void_p = chars.Ptr
#
#        dlllib.Encoding_GetByteCountCC.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.Encoding_GetByteCountCC.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetByteCountCC,self.Ptr, intPtrchars,count)
#        return ret


#    @dispatch
#
#    def GetBytes(self ,chars:'Char[]')->List[Byte]:
#        """
#
#        """
#        #arraychars:ArrayTypechars = ""
#        countchars = len(chars)
#        ArrayTypechars = c_void_p * countchars
#        arraychars = ArrayTypechars()
#        for i in range(0, countchars):
#            arraychars[i] = chars[i].Ptr
#
#
#        dlllib.Encoding_GetBytes.argtypes=[c_void_p ,ArrayTypechars]
#        dlllib.Encoding_GetBytes.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetBytes,self.Ptr, arraychars)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


#    @dispatch
#
#    def GetBytes(self ,chars:'Char[]',index:int,count:int)->List[Byte]:
#        """
#
#        """
#        #arraychars:ArrayTypechars = ""
#        countchars = len(chars)
#        ArrayTypechars = c_void_p * countchars
#        arraychars = ArrayTypechars()
#        for i in range(0, countchars):
#            arraychars[i] = chars[i].Ptr
#
#
#        dlllib.Encoding_GetBytesCIC.argtypes=[c_void_p ,ArrayTypechars,c_int,c_int]
#        dlllib.Encoding_GetBytesCIC.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetBytesCIC,self.Ptr, arraychars,index,count)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


#    @dispatch
#
#    def GetBytes(self ,s:str)->List[Byte]:
#        """
#
#        """
#        
#        dlllib.Encoding_GetBytesS.argtypes=[c_void_p ,c_void_p]
#        dlllib.Encoding_GetBytesS.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetBytesS,self.Ptr, s)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


#    @dispatch
#
#    def GetBytes(self ,s:str,charIndex:int,charCount:int,bytes:'Byte[]',byteIndex:int)->int:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetBytesSCCBB.argtypes=[c_void_p ,c_void_p,c_int,c_int,ArrayTypebytes,c_int]
#        dlllib.Encoding_GetBytesSCCBB.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetBytesSCCBB,self.Ptr, s,charIndex,charCount,arraybytes,byteIndex)
#        return ret


#    @dispatch
#
#    def GetCharCount(self ,bytes:'Byte[]')->int:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetCharCount.argtypes=[c_void_p ,ArrayTypebytes]
#        dlllib.Encoding_GetCharCount.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetCharCount,self.Ptr, arraybytes)
#        return ret


#    @dispatch
#
#    def GetCharCount(self ,bytes:'Byte*',count:int)->int:
#        """
#
#        """
#        intPtrbytes:c_void_p = bytes.Ptr
#
#        dlllib.Encoding_GetCharCountBC.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.Encoding_GetCharCountBC.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetCharCountBC,self.Ptr, intPtrbytes,count)
#        return ret


#    @dispatch
#
#    def GetChars(self ,bytes:'Byte[]')->List[Char]:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetChars.argtypes=[c_void_p ,ArrayTypebytes]
#        dlllib.Encoding_GetChars.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetChars,self.Ptr, arraybytes)
#        ret = GetObjVectorFromArray(intPtrArray, Char)
#        return ret


#    @dispatch
#
#    def GetChars(self ,bytes:'Byte[]',index:int,count:int)->List[Char]:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetCharsBIC.argtypes=[c_void_p ,ArrayTypebytes,c_int,c_int]
#        dlllib.Encoding_GetCharsBIC.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_GetCharsBIC,self.Ptr, arraybytes,index,count)
#        ret = GetObjVectorFromArray(intPtrArray, Char)
#        return ret


#    @dispatch
#
#    def GetString(self ,bytes:'Byte*',byteCount:int)->str:
#        """
#
#        """
#        intPtrbytes:c_void_p = bytes.Ptr
#
#        dlllib.Encoding_GetString.argtypes=[c_void_p ,c_void_p,c_int]
#        dlllib.Encoding_GetString.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Encoding_GetString,self.Ptr, intPtrbytes,byteCount)
#        return ret
#


    @property
    def CodePage(self)->int:
        """

        """
        dlllib.Encoding_get_CodePage.argtypes=[c_void_p]
        dlllib.Encoding_get_CodePage.restype=c_int
        ret = CallCFunction(dlllib.Encoding_get_CodePage,self.Ptr)
        return ret

    @dispatch
    def IsAlwaysNormalized(self)->bool:
        """

        """
        dlllib.Encoding_IsAlwaysNormalized.argtypes=[c_void_p]
        dlllib.Encoding_IsAlwaysNormalized.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_IsAlwaysNormalized,self.Ptr)
        return ret

#    @dispatch
#
#    def IsAlwaysNormalized(self ,form:'NormalizationForm')->bool:
#        """
#
#        """
#        enumform:c_int = form.value
#
#        dlllib.Encoding_IsAlwaysNormalizedF.argtypes=[c_void_p ,c_int]
#        dlllib.Encoding_IsAlwaysNormalizedF.restype=c_bool
#        ret = CallCFunction(dlllib.Encoding_IsAlwaysNormalizedF,self.Ptr, enumform)
#        return ret


#
#    def GetDecoder(self)->'Decoder':
#        """
#
#        """
#        dlllib.Encoding_GetDecoder.argtypes=[c_void_p]
#        dlllib.Encoding_GetDecoder.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Encoding_GetDecoder,self.Ptr)
#        ret = None if intPtr==None else Decoder(intPtr)
#        return ret
#


    @staticmethod

    def get_Default()->'Encoding':
        """

        """
        #dlllib.Encoding_get_Default.argtypes=[]
        dlllib.Encoding_get_Default.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_Default)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


#
#    def GetEncoder(self)->'Encoder':
#        """
#
#        """
#        dlllib.Encoding_GetEncoder.argtypes=[c_void_p]
#        dlllib.Encoding_GetEncoder.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Encoding_GetEncoder,self.Ptr)
#        ret = None if intPtr==None else Encoder(intPtr)
#        return ret
#


#    @dispatch
#
#    def GetString(self ,bytes:'Byte[]')->str:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetStringB.argtypes=[c_void_p ,ArrayTypebytes]
#        dlllib.Encoding_GetStringB.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Encoding_GetStringB,self.Ptr, arraybytes)
#        return ret
#


#    @dispatch
#
#    def GetString(self ,bytes:'Byte[]',index:int,count:int)->str:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetStringBIC.argtypes=[c_void_p ,ArrayTypebytes,c_int,c_int]
#        dlllib.Encoding_GetStringBIC.restype=c_wchar_p
#        ret = CallCFunction(dlllib.Encoding_GetStringBIC,self.Ptr, arraybytes,index,count)
#        return ret
#


    @staticmethod

    def get_Unicode()->'Encoding':
        """

        """
        #dlllib.Encoding_get_Unicode.argtypes=[]
        dlllib.Encoding_get_Unicode.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_Unicode)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


    @staticmethod

    def get_BigEndianUnicode()->'Encoding':
        """

        """
        #dlllib.Encoding_get_BigEndianUnicode.argtypes=[]
        dlllib.Encoding_get_BigEndianUnicode.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_BigEndianUnicode)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


    @staticmethod

    def get_UTF7()->'Encoding':
        """

        """
        #dlllib.Encoding_get_UTF7.argtypes=[]
        dlllib.Encoding_get_UTF7.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_UTF7)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


    @staticmethod

    def get_UTF8()->'Encoding':
        """

        """
        #dlllib.Encoding_get_UTF8.argtypes=[]
        dlllib.Encoding_get_UTF8.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_UTF8)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret


    @staticmethod

    def get_UTF32()->'Encoding':
        """

        """
        #dlllib.Encoding_get_UTF32.argtypes=[]
        dlllib.Encoding_get_UTF32.restype=c_void_p
        intPtr = CallCFunction(dlllib.Encoding_get_UTF32)
        ret = None if intPtr==None else Encoding(intPtr)
        return ret



    def Equals(self ,value:'SpireObject')->bool:
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        dlllib.Encoding_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Encoding_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Encoding_Equals,self.Ptr, intPtrvalue)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Encoding_GetHashCode.argtypes=[c_void_p]
        dlllib.Encoding_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Encoding_GetHashCode,self.Ptr)
        return ret

#    @staticmethod
#    @dispatch
#
#    def Convert(srcEncoding:'Encoding',dstEncoding:'Encoding',bytes:'Byte[]',index:int,count:int)->List[Byte]:
#        """
#
#        """
#        intPtrsrcEncoding:c_void_p = srcEncoding.Ptr
#        intPtrdstEncoding:c_void_p = dstEncoding.Ptr
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_ConvertSDBIC.argtypes=[ c_void_p,c_void_p,ArrayTypebytes,c_int,c_int]
#        dlllib.Encoding_ConvertSDBIC.restype=IntPtrArray
#        intPtrArray = CallCFunction(dlllib.Encoding_ConvertSDBIC, intPtrsrcEncoding,intPtrdstEncoding,arraybytes,index,count)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


    @property

    def EncodingName(self)->str:
        """

        """
        dlllib.Encoding_get_EncodingName.argtypes=[c_void_p]
        dlllib.Encoding_get_EncodingName.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Encoding_get_EncodingName,self.Ptr))
        return ret


#    @dispatch
#
#    def GetByteCount(self ,chars:'Char[]',index:int,count:int)->int:
#        """
#
#        """
#        #arraychars:ArrayTypechars = ""
#        countchars = len(chars)
#        ArrayTypechars = c_void_p * countchars
#        arraychars = ArrayTypechars()
#        for i in range(0, countchars):
#            arraychars[i] = chars[i].Ptr
#
#
#        dlllib.Encoding_GetByteCountCIC.argtypes=[c_void_p ,ArrayTypechars,c_int,c_int]
#        dlllib.Encoding_GetByteCountCIC.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetByteCountCIC,self.Ptr, arraychars,index,count)
#        return ret


#    @dispatch
#
#    def GetBytes(self ,chars:'Char[]',charIndex:int,charCount:int,bytes:'Byte[]',byteIndex:int)->int:
#        """
#
#        """
#        #arraychars:ArrayTypechars = ""
#        countchars = len(chars)
#        ArrayTypechars = c_void_p * countchars
#        arraychars = ArrayTypechars()
#        for i in range(0, countchars):
#            arraychars[i] = chars[i].Ptr
#
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetBytesCCCBB.argtypes=[c_void_p ,ArrayTypechars,c_int,c_int,ArrayTypebytes,c_int]
#        dlllib.Encoding_GetBytesCCCBB.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetBytesCCCBB,self.Ptr, arraychars,charIndex,charCount,arraybytes,byteIndex)
#        return ret


#    @dispatch
#
#    def GetBytes(self ,chars:'Char*',charCount:int,bytes:'Byte*',byteCount:int)->int:
#        """
#
#        """
#        intPtrchars:c_void_p = chars.Ptr
#        intPtrbytes:c_void_p = bytes.Ptr
#
#        dlllib.Encoding_GetBytesCCBB.argtypes=[c_void_p ,c_void_p,c_int,c_void_p,c_int]
#        dlllib.Encoding_GetBytesCCBB.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetBytesCCBB,self.Ptr, intPtrchars,charCount,intPtrbytes,byteCount)
#        return ret


#    @dispatch
#
#    def GetCharCount(self ,bytes:'Byte[]',index:int,count:int)->int:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#
#        dlllib.Encoding_GetCharCountBIC.argtypes=[c_void_p ,ArrayTypebytes,c_int,c_int]
#        dlllib.Encoding_GetCharCountBIC.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetCharCountBIC,self.Ptr, arraybytes,index,count)
#        return ret


#    @dispatch
#
#    def GetChars(self ,bytes:'Byte[]',byteIndex:int,byteCount:int,chars:'Char[]',charIndex:int)->int:
#        """
#
#        """
#        #arraybytes:ArrayTypebytes = ""
#        countbytes = len(bytes)
#        ArrayTypebytes = c_void_p * countbytes
#        arraybytes = ArrayTypebytes()
#        for i in range(0, countbytes):
#            arraybytes[i] = bytes[i].Ptr
#
#        #arraychars:ArrayTypechars = ""
#        countchars = len(chars)
#        ArrayTypechars = c_void_p * countchars
#        arraychars = ArrayTypechars()
#        for i in range(0, countchars):
#            arraychars[i] = chars[i].Ptr
#
#
#        dlllib.Encoding_GetCharsBBBCC.argtypes=[c_void_p ,ArrayTypebytes,c_int,c_int,ArrayTypechars,c_int]
#        dlllib.Encoding_GetCharsBBBCC.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetCharsBBBCC,self.Ptr, arraybytes,byteIndex,byteCount,arraychars,charIndex)
#        return ret


#    @dispatch
#
#    def GetChars(self ,bytes:'Byte*',byteCount:int,chars:'Char*',charCount:int)->int:
#        """
#
#        """
#        intPtrbytes:c_void_p = bytes.Ptr
#        intPtrchars:c_void_p = chars.Ptr
#
#        dlllib.Encoding_GetCharsBBCC.argtypes=[c_void_p ,c_void_p,c_int,c_void_p,c_int]
#        dlllib.Encoding_GetCharsBBCC.restype=c_int
#        ret = CallCFunction(dlllib.Encoding_GetCharsBBCC,self.Ptr, intPtrbytes,byteCount,intPtrchars,charCount)
#        return ret



    def GetMaxByteCount(self ,charCount:int)->int:
        """

        """
        
        dlllib.Encoding_GetMaxByteCount.argtypes=[c_void_p ,c_int]
        dlllib.Encoding_GetMaxByteCount.restype=c_int
        ret = CallCFunction(dlllib.Encoding_GetMaxByteCount,self.Ptr, charCount)
        return ret


    def GetMaxCharCount(self ,byteCount:int)->int:
        """

        """
        
        dlllib.Encoding_GetMaxCharCount.argtypes=[c_void_p ,c_int]
        dlllib.Encoding_GetMaxCharCount.restype=c_int
        ret = CallCFunction(dlllib.Encoding_GetMaxCharCount,self.Ptr, byteCount)
        return ret

