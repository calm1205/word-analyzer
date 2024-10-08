from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Document (  DocumentContainer, IDocument, ICompositeObject) :
    """
    Represents a document.
    """

    @dispatch
    def __init__(self, stream:Stream, password:str, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified stream, password, and useNewEngine flag.

        Args:
            stream (Stream): The stream to create the document from.
            password (str): The password to open the document.
            useNewEngine (bool): A flag indicating whether to use the new engine.

        Returns:
            None
        """
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr;

        GetDllLibDoc().Document_CreateDocumentSPU.argtypes=[c_void_p,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSPU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSPU,intPstream,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, password:str):
        """
        Initializes a new instance of the Document class with the specified stream, file format, and password.

        Args:
            stream (Stream): The stream to create the document from.
            fileFormat (FileFormat): The file format of the document.
            password (str): The password to open the document.

        Returns:
            None
        """
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr;
        iTypetype:c_int = fileFormat.value;

        GetDllLibDoc().Document_CreateDocumentSTP.argtypes=[c_void_p,c_int,c_char_p]
        GetDllLibDoc().Document_CreateDocumentSTP.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSTP,intPstream,iTypetype,passwordPtr)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, password:str, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified stream, file format, password, and useNewEngine flag.

        Args:
            stream (Stream): The stream to create the document from.
            fileFormat (FileFormat): The file format of the document.
            password (str): The password to open the document.
            useNewEngine (bool): A flag indicating whether to use the new engine.

        Returns:
            None
        """
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr;
        iTypetype:c_int = fileFormat.value;

        GetDllLibDoc().Document_CreateDocumentSTPU.argtypes=[c_void_p,c_int,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSTPU.restype=c_void_p
        intPtr =GetDllLibDoc().Document_CreateDocumentSTPU(intPstream,iTypetype,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str):
        """
        Initializes a new instance of the Document class with the specified file name.

        Args:
            fileName (str): The name of the file to create the document from.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_CreateDocumentF.argtypes=[c_char_p]
        GetDllLibDoc().Document_CreateDocumentF.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentF,fileNamePtr)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified file name and useNewEngine flag.

        Args:
            fileName (str): The name of the file to create the document from.
            useNewEngine (bool): A flag indicating whether to use the new engine.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_CreateDocumentFU.argtypes=[c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentFU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFU,fileNamePtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, password:str):
        """
        Initializes a new instance of the Document class with the specified file name and password.

        Args:
            fileName (str): The name of the file to create the document from.
            password (str): The password to open the document.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        GetDllLibDoc().Document_CreateDocumentFP.argtypes=[c_char_p,c_char_p]
        GetDllLibDoc().Document_CreateDocumentFP.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFP,fileNamePtr,passwordPtr)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, password:str, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified file name, password, and useNewEngine flag.

        Args:
            fileName (str): The name of the file to create the document from.
            password (str): The password to open the document.
            useNewEngine (bool): A flag indicating whether to use the new engine.

        Returns:
            None
        """

        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        GetDllLibDoc().Document_CreateDocumentFPU.argtypes=[c_char_p,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentFPU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFPU,fileNamePtr,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat):
        """
        Initializes a new instance of the Document class with the specified file name and file format.

        Args:
            fileName (str): The name of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentFT.argtypes=[c_char_p,c_int]
        GetDllLibDoc().Document_CreateDocumentFT.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFT,fileNamePtr,iTypetype)
        super(Document, self).__init__(intPtr)


    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified file name, file format, and useNewEngine flag.

        Args:
            fileName (str): The name of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            useNewEngine (bool): A flag indicating whether to use the new engine.

        Returns:
            None
        """

        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentFTU.argtypes=[c_char_p,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentFTU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFTU,fileNamePtr,iTypetype,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, validationType:XHTMLValidationType):
        """
        Initializes a new instance of the Document class with the specified file name, file format, and validation type.

        Args:
            fileName (str): The name of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            validationType (XHTMLValidationType): The validation type of the document.

        Returns:
            None
        """

        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentFTV.argtypes=[c_char_p,c_int,c_int]
        GetDllLibDoc().Document_CreateDocumentFTV.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFTV,fileNamePtr,iTypetype,iTypevalidationType)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, validationType:XHTMLValidationType, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified file name, file format, validation type, and useNewEngine flag.

        Args:
            fileName (str): The name of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            validationType (XHTMLValidationType): The validation type of the document.
            useNewEngine (bool): A flag indicating whether to use the new engine.

        Returns:
            None
        """

        fileNamePtr = StrToPtr(fileName)
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentFTVU.argtypes=[c_char_p,c_int,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentFTVU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFTVU,fileNamePtr,iTypetype,iTypevalidationType,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, password:str):
        """
        Initializes a new instance of the Document class with the specified file name, file format, and password.

        Args:
            fileName (str): The name of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            password (str): The password to open the document.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentFTP.argtypes=[c_char_p,c_int,c_char_p]
        GetDllLibDoc().Document_CreateDocumentFTP.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFTP,fileNamePtr,iTypetype,passwordPtr);
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, fileName:str, fileFormat:FileFormat, password:str, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified file name, file format, password, and useNewEngine.

        Args:
            fileName (str): The name of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            password (str): The password to open the document.
            useNewEngine(bool): Specify whether to use the new engine.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        iTypetype:c_int = fileFormat.value
    
        GetDllLibDoc().Document_CreateDocumentFTPU.argtypes=[c_char_p,c_int,c_char_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentFTPU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentFTPU,fileNamePtr,iTypetype,passwordPtr,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, validationType:XHTMLValidationType):
        """
        Initializes a new instance of the Document class with the specified stream, file format, and validationType.

        Args:
            stream (Stream): The stream of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            validationType (XHTMLValidationType): Represents XHTML validation.

        Returns:
            None
        """
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentSTV.argtypes=[c_void_p,c_int,c_int]
        GetDllLibDoc().Document_CreateDocumentSTV.restype=c_void_p
        intPtr =GetDllLibDoc().Document_CreateDocumentSTV(intPstream,iTypetype,iTypevalidationType)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, validationType:XHTMLValidationType, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified stream, file format, validationType, and useNewEngine.

        Args:
            stream (Stream): The stream of the file to create the document from.
            fileFormat (FileFormat): The file format of the document.
            validationType (XHTMLValidationType): Represents XHTML validation.
            useNewEngine(bool): Specify whether to use the new engine.

        Returns:
            None
        """
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value
        iTypevalidationType:c_int = validationType.value

        GetDllLibDoc().Document_CreateDocumentSTVU.argtypes=[c_void_p,c_int,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentSTVU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSTVU,intPstream,iTypetype,iTypevalidationType,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self):
        """
        Initializes a new instance of the Document class with no params.

        Returns:
            None
        """
        GetDllLibDoc().Document_CreateDocument.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocument,)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified useNewEngine.

        Args:
            useNewEngine(bool): Specify whether to use the new engine.

        Returns:
            None
        """
        GetDllLibDoc().Document_CreateDocumentU.argtypes=[c_bool]
        GetDllLibDoc().Document_CreateDocumentU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentU,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified stream, and useNewEngine.

        Args:
            stream (Stream): The stream of the file to create the document from.
            useNewEngine(bool): Specify whether to use the new engine.

        Returns:
            None
        """
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentSU.argtypes=[c_void_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSU,intPstream,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream):
        """
        Initializes a new instance of the Document class with the specified stream.

        Args:
            stream (Stream): The stream of the file to create the document from.

        Returns:
            None
        """
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentS.argtypes=[c_void_p]
        GetDllLibDoc().Document_CreateDocumentS.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentS,intPstream)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, useNewEngine:bool):
        """
        Initializes a new instance of the Document class with the specified stream, and useNewEngine.

        Args:
            stream (Stream): The stream of the file to create the document from.
            useNewEngine(bool): Specify whether to use the new engine.

        Returns:
            None
        """
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentSU.argtypes=[c_void_p,c_bool]
        GetDllLibDoc().Document_CreateDocumentSU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSU,intPstream,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream,  fileFormat:FileFormat):
        """
            Initializes a new instance of the Document class with a stream and a file format.
        """
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value
        GetDllLibDoc().Document_CreateDocumentST.argtypes=[c_void_p,c_int]
        GetDllLibDoc().Document_CreateDocumentST.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentST,intPstream,iTypetype)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, fileFormat:FileFormat, useNewEngine:bool):
        """
            Initializes a new instance of the Document class with a stream, a file format, and a flag indicating whether to use the new engine.
        """
        intPstream:c_void_p = stream.Ptr
        iTypetype:c_int = fileFormat.value

        GetDllLibDoc().Document_CreateDocumentSTU.argtypes=[c_void_p,c_int,c_bool]
        GetDllLibDoc().Document_CreateDocumentSTU.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSTU,intPstream,iTypetype,useNewEngine)
        super(Document, self).__init__(intPtr)

    @dispatch
    def __init__(self, stream:Stream, password:str):
        """
            Initializes a new instance of the Document class with a stream and a password.
        """
        passwordPtr = StrToPtr(password)
        intPstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_CreateDocumentSP.argtypes=[c_void_p,c_char_p]
        GetDllLibDoc().Document_CreateDocumentSP.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateDocumentSP,intPstream,passwordPtr)
        super(Document, self).__init__(intPtr)

    @property
    def ForceTableRelayout(self)->bool:
        """
            Gets or sets a value indicating whether to force table relayout.
        """
        GetDllLibDoc().Document_get_ForceTableRelayout.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ForceTableRelayout.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_ForceTableRelayout,self.Ptr)
        return ret

    @ForceTableRelayout.setter
    def ForceTableRelayout(self, value:bool):
        """
            Sets a value indicating whether to force table relayout.
        """
        GetDllLibDoc().Document_set_ForceTableRelayout.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_ForceTableRelayout,self.Ptr, value)

    def ClearMacros(self):
        """
            Removes the macros from the document.
        """
        GetDllLibDoc().Document_ClearMacros.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_ClearMacros,self.Ptr)


    def SetDateTimeOfUnitTest(self ,dateTime:'DateTime'):
        """
            Sets date and time of the unit test.
            For unit testing use only.
        """
        intPtrdateTime:c_void_p = dateTime.Ptr

        GetDllLibDoc().Document_SetDateTimeOfUnitTest.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_SetDateTimeOfUnitTest,self.Ptr, intPtrdateTime)

    def ResetPageLayoutCache(self):
        """
            Reset the page layout cache data of the new engine.
        """
        GetDllLibDoc().Document_ResetPageLayoutCache.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_ResetPageLayoutCache,self.Ptr)

    def UpdateTableLayout(self):
        """
            Update table grid before saving the document when using the new engine.
        """
        GetDllLibDoc().Document_UpdateTableLayout.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_UpdateTableLayout,self.Ptr)



    def SaveToOnlineBin(self ,fileName:str)->bool:
        """
            Saves the document in Spire.Online format.
        """
        fileNamePtr = StrToPtr(fileName)
        
        GetDllLibDoc().Document_SaveToOnlineBin.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_SaveToOnlineBin.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_SaveToOnlineBin,self.Ptr, fileNamePtr)
        return ret

    @dispatch

    def SaveToStream(self ,stream:Stream,paramList:ToPdfParameterList):
        """
            Saves the document into stream with the specified parameters.
        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrparamList:c_void_p = paramList.Ptr

        GetDllLibDoc().Document_SaveToStream.argtypes=[c_void_p ,c_void_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_SaveToStream,self.Ptr, intPtrstream,intPtrparamList)

    @dispatch

    def LoadFromStream(self ,stream:Stream,fileFormat:FileFormat,validationType:XHTMLValidationType):
        """
            Opens the HTML document from stream with the specified file format and validation type.
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value
        enumvalidationType:c_int = validationType.value

        GetDllLibDoc().Document_LoadFromStream.argtypes=[c_void_p ,c_void_p,c_int,c_int]
        CallCFunction(GetDllLibDoc().Document_LoadFromStream,self.Ptr, intPtrstream,enumfileFormat,enumvalidationType)

    @dispatch

    def LoadFromStream(self ,stream:Stream,fileFormat:FileFormat):
        """
            Opens the document from stream in Xml or Microsoft Word format.
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromStreamSF.argtypes=[c_void_p ,c_void_p,c_int]
        CallCFunction(GetDllLibDoc().Document_LoadFromStreamSF,self.Ptr, intPtrstream,enumfileFormat)

    @dispatch

    def LoadFromStream(self ,stream:Stream,fileFormat:FileFormat,password:str):
        """
        Loads document from stream with specified file format and password.

        Args:
            stream (Stream): The stream.
            fileFormat (FileFormat): The file format.
            password (str): The password.

        Returns:
            None
        """
        passwordPtr = StrToPtr(password)
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromStreamSFP.argtypes=[c_void_p ,c_void_p,c_int,c_char_p]
        CallCFunction(GetDllLibDoc().Document_LoadFromStreamSFP,self.Ptr, intPtrstream,enumfileFormat,passwordPtr)

    @dispatch

    def SaveToStream(self ,stream:Stream,fileFormat:FileFormat,certificatePath:str,securePassword:str):
        """
        Saves document to stream and digitally sign, Only DOC and DOCX are supported.

        Args:
            stream (Stream): The stream.
            fileFormat (FileFormat): The file format.
            certificatePath (str): Path to the file certificate.
            securePassword (str): Password of the certificate.

        Returns:
            None
        """
        certificatePathPtr = StrToPtr(certificatePath)
        securePasswordPtr = StrToPtr(securePassword)
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToStreamSFCS.argtypes=[c_void_p ,c_void_p,c_int,c_char_p,c_char_p]
        CallCFunction(GetDllLibDoc().Document_SaveToStreamSFCS,self.Ptr, intPtrstream,enumfileFormat,certificatePathPtr,securePasswordPtr)

#    @dispatch
#
#    def SaveToStream(self ,stream:Stream,fileFormat:FileFormat,certificateData:'Byte[]',securePassword:str):
#        """
#    <summary>
#        Saves document to stream and digitally sign, Only DOC and DOCX are supported.
#    </summary>
#    <param name="stream">The stream.</param>
#    <param name="fileFormat">The file format.</param>
#    <param name="certificateData">The certificate data.</param>
#    <param name="securePassword">Password of the certificate.</param>
#        """
#        intPtrstream:c_void_p = stream.Ptr
#        enumfileFormat:c_int = fileFormat.value
#        #arraycertificateData:ArrayTypecertificateData = ""
#        countcertificateData = len(certificateData)
#        ArrayTypecertificateData = c_void_p * countcertificateData
#        arraycertificateData = ArrayTypecertificateData()
#        for i in range(0, countcertificateData):
#            arraycertificateData[i] = certificateData[i].Ptr
#
#
#        GetDllLibDoc().Document_SaveToStreamSFCS1.argtypes=[c_void_p ,c_void_p,c_int,ArrayTypecertificateData,c_wchar_p]
#        GetDllLibDoc().Document_SaveToStreamSFCS1(self.Ptr, intPtrstream,enumfileFormat,arraycertificateData,securePassword)


    @dispatch

    def SaveToFile(self ,fileName:str,fileFormat:FileFormat,certificatePath:str,securePassword:str):
        """
        Saves document to file and digitally sign, Only DOC and DOCX are supported.

        Args:
            fileName (str): The file.
            fileFormat (FileFormat): The file format.
            certificatePath (str): Path to the file certificate.
            securePassword (str): Password of the certificate.

        Returns:
            None
        """
        fileNamePtr = StrToPtr(fileName)
        certificatePathPtr = StrToPtr(certificatePath)
        securePasswordPtr = StrToPtr(securePassword)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToFile.argtypes=[c_void_p ,c_char_p,c_int,c_char_p,c_char_p]
        CallCFunction(GetDllLibDoc().Document_SaveToFile,self.Ptr, fileNamePtr,enumfileFormat,certificatePathPtr,securePasswordPtr)

#    @dispatch
#
#    def SaveToFile(self ,fileName:str,fileFormat:FileFormat,certificateData:'Byte[]',securePassword:str):
#        """
#    <summary>
#        Saves document to file and digitally sign, Only DOC and DOCX are supported.
#    </summary>
#    <param name="stream">The file.</param>
#    <param name="fileFormat">The file format.</param>
#    <param name="certificateData">The certificate data.</param>
#    <param name="securePassword">Password of the certificate.</param>
#        """
#        enumfileFormat:c_int = fileFormat.value
#        #arraycertificateData:ArrayTypecertificateData = ""
#        countcertificateData = len(certificateData)
#        ArrayTypecertificateData = c_void_p * countcertificateData
#        arraycertificateData = ArrayTypecertificateData()
#        for i in range(0, countcertificateData):
#            arraycertificateData[i] = certificateData[i].Ptr
#
#
#        GetDllLibDoc().Document_SaveToFileFFCS.argtypes=[c_void_p ,c_wchar_p,c_int,ArrayTypecertificateData,c_wchar_p]
#        GetDllLibDoc().Document_SaveToFileFFCS(self.Ptr, fileName,enumfileFormat,arraycertificateData,securePassword)


    @dispatch

    def SaveToStream(self ,stream:Stream,fileFormat:FileFormat):
        """
        Saves the document into stream in Xml or Microsoft Word format.

        Args:
            stream (Stream): The stream.
            fileFormat (FileFormat): The file format.

        Returns:
            None
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToStreamSF.argtypes=[c_void_p ,c_void_p,c_int]
        CallCFunction(GetDllLibDoc().Document_SaveToStreamSF,self.Ptr, intPtrstream,enumfileFormat)

    @dispatch

    def SaveToFile(self ,stream:Stream,fileFormat:FileFormat):
        """
        Saves the document into stream in Xml or Microsoft Word format.

        Args:
            stream (Stream): The stream.
            fileFormat (FileFormat): The file format.

        Returns:
            None
        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToFileSF.argtypes=[c_void_p ,c_void_p,c_int]
        CallCFunction(GetDllLibDoc().Document_SaveToFileSF,self.Ptr, intPtrstream,enumfileFormat)

    def Close(self):
        """
        Closes this instance.

        Returns:
            None
        """
        GetDllLibDoc().Document_Close.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_Close,self.Ptr)

    def Dispose(self):
        """
        Prerforms application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

        Returns:
            None
        """
        GetDllLibDoc().Document_Dispose.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_Dispose,self.Ptr)

#    @dispatch
#
#    def SaveToImages(self ,type:ImageType)->List[SKImage]:
#        """
#    <summary>
#        Save the whole document into images
#    </summary>
#    <param name="type">The ImageType</param>
#    <returns>Return the images</returns>
#        """
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Document_SaveToImages.argtypes=[c_void_p ,c_int]
#        GetDllLibDoc().Document_SaveToImages.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SaveToImages(self.Ptr, enumtype)
#        ret = GetObjVectorFromArray(intPtrArray, SKImage)
#        return ret


#    @dispatch
#
#    def SaveToImages(self ,pageIndex:int,pageCount:int,type:ImageType)->List[SKImage]:
#        """
#    <summary>
#        Save the specified range of pages into images
#    </summary>
#    <param name="pageIndex">Page index (Zero based)</param>
#    <param name="pageCount">Number of pages</param>
#    <param name="type">The ImageType</param>
#    <returns>Return the images</returns>
#        """
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Document_SaveToImagesPPT.argtypes=[c_void_p ,c_int,c_int,c_int]
#        GetDllLibDoc().Document_SaveToImagesPPT.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SaveToImagesPPT(self.Ptr, pageIndex,pageCount,enumtype)
#        ret = GetObjVectorFromArray(intPtrArray, SKImage)
#        return ret


#    @dispatch
#
#    def SaveToImages(self ,pageIndex:int,type:ImageType)->SKImage:
#        """
#    <summary>
#        Save the specified page into image
#    </summary>
#    <param name="pageIndex">Page index</param>
#    <param name="type"> The ImageType</param>
#    <returns>Returns the image</returns>
#        """
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Document_SaveToImagesPT.argtypes=[c_void_p ,c_int,c_int]
#        GetDllLibDoc().Document_SaveToImagesPT.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_SaveToImagesPT(self.Ptr, pageIndex,enumtype)
#        ret = None if intPtr==None else SKImage(intPtr)
#        return ret
#


#    @dispatch
#
#    def SaveToImages(self ,type:ImageType,toImageOption:ToImageOption)->List[SKImage]:
#        """
#    <summary>
#        Save the specified page into image
#    </summary>
#    <param name="type">The ImageType</param>
#    <param name="toImageOption"></param>
#    <returns>Returns the image array</returns>
#        """
#        enumtype:c_int = type.value
#        intPtrtoImageOption:c_void_p = toImageOption.Ptr
#
#        GetDllLibDoc().Document_SaveToImagesTT.argtypes=[c_void_p ,c_int,c_void_p]
#        GetDllLibDoc().Document_SaveToImagesTT.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SaveToImagesTT(self.Ptr, enumtype,intPtrtoImageOption)
#        ret = GetObjVectorFromArray(intPtrArray, SKImage)
#        return ret


    @dispatch
    def SaveImageToStreams(self ,pageIndex:int,pageCount:int,type:ImageType)->List[Stream]:
        """
        Save the specified range of pages as image return streams. 
        The default is PNG format image.

        Args:
            pageIndex (int): Index of the page.
            pageCount (int): The page count.
            type (ImageType): The type.

        Returns:
            List[Stream]: The streams.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_SaveImageToStreamsPPI.argtypes=[c_void_p ,c_int,c_int,c_int]
        GetDllLibDoc().Document_SaveImageToStreamsPPI.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().Document_SaveImageToStreamsPPI,self.Ptr, pageIndex,pageCount,enumtype)
        ret = GetObjVectorFromArray(intPtrArray, Stream)
        return ret


    @dispatch

    def SaveImageToStreams(self ,pageIndex:int,type:ImageType)->Stream:
        """
        Save the specified page as image return stream.
        The default is PNG format image.

        Args:
            pageIndex (int): Index of the page.
            type (ImageType): The type.

        Returns:
            Stream: The stream.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_SaveImageToStreamsPI.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Document_SaveImageToStreamsPI.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_SaveImageToStreamsPI,self.Ptr, pageIndex,enumtype)
        ret = None if intPtr==None else Stream(intPtr)
        return ret


    @dispatch

    def SaveImageToStreams(self ,type:ImageType)->List[Stream]:
        """
        Save the specified page as image return streams.
        The default is PNG format image.

        Args:
            type (ImageType): The type.

        Returns:
            List[Stream]: The streams.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_SaveImageToStreamsI.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_SaveImageToStreamsI.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().Document_SaveImageToStreamsI,self.Ptr, enumtype)
        ret = GetObjVectorFromArray(intPtrArray, Stream)
        return ret


#    @dispatch
#
#    def FindPattern(self ,pattern:'Regex')->TextSelection:
#        """
#    <summary>
#        Finds and returns entry of specified regular expression along with formatting.
#    </summary>
#    <param name="pattern">regex pattern</param>
#    <returns>Found text selection</returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPattern.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_FindPattern.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_FindPattern(self.Ptr, intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


#    @dispatch
#
#    def FindPatternInLine(self ,pattern:'Regex')->List[TextSelection]:
#        """
#    <summary>
#        Finds the first entry of specified pattern in single-line mode.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <returns></returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPatternInLine.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_FindPatternInLine.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindPatternInLine(self.Ptr, intPtrpattern)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


    @dispatch

    def FindString(self ,stringValue:str,caseSensitive:bool,wholeWord:bool):
        """
        Finds and returns string along with formatting.

        Args:
            stringValue (str): The string to find.
            caseSensitive (bool): If set to True, use case sensitive search.
            wholeWord (bool): If it search the whole word, set to True.

        Returns:
            TextSelection: The found text selection.
        """
        stringValuePtr = StrToPtr(stringValue)
        GetDllLibDoc().Document_FindString.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_FindString.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_FindString,self.Ptr, stringValuePtr,caseSensitive,wholeWord)
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret


#    @dispatch
#
#    def FindStringInLine(self ,given:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#    <summary>
#        Finds the first entry of matchString text in single-line mode.
#    </summary>
#    <param name="matchString">The string to find.</param>
#    <param name="caseSensitive">if set to <c>true</c> use case sensitive search.</param>
#    <param name="wholeWord">if it search the whole word, set to <c>true</c>.</param>
#    <returns></returns>
#        """
#        
#        GetDllLibDoc().Document_FindStringInLine.argtypes=[c_void_p ,c_wchar_p,c_bool,c_bool]
#        GetDllLibDoc().Document_FindStringInLine.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindStringInLine(self.Ptr, given,caseSensitive,wholeWord)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


#    @dispatch
#
    def FindAllPattern(self ,pattern:'Regex')->List[TextSelection]:
        """
        Returns all entries of matchString regex.

        Args:
            pattern (Regex): The regex pattern.

        Returns:
            List[TextSelection]: The found text selections.
        """
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Document_FindAllPattern.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Document_FindAllPattern.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().Document_FindAllPattern,self.Ptr, intPtrpattern)
        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
        return ret


#    @dispatch
#
#    def FindAllPattern(self ,pattern:'Regex',isAdvancedSearch:bool)->List[TextSelection]:
#        """
#    <summary>
#        Returns all entries of matchString regex.
#    </summary>
#    <param name="pattern"></param>
#    <param name="isAdvancedSearch"></param>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindAllPatternPI.argtypes=[c_void_p ,c_void_p,c_bool]
#        GetDllLibDoc().Document_FindAllPatternPI.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindAllPatternPI(self.Ptr, intPtrpattern,isAdvancedSearch)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


#
    def FindAllString(self ,matchString:str,caseSensitive:bool,wholeWord:bool)->List['TextSelection']:
        """
        Returns all entries of matchString string, taking into consideration caseSensitive
        and wholeWord options.
        :param matchString: The string to match.
        :param caseSensitive: If True, the match is case sensitive.
        :param wholeWord: If True, the match must be a whole word.
        :return: A list of TextSelection objects.
        """

        matchStringPtr = StrToPtr(matchString)
        GetDllLibDoc().Document_FindAllString.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_FindAllString.restype=IntPtrArray
        intPtrArray = CallCFunction(GetDllLibDoc().Document_FindAllString,self.Ptr, matchStringPtr,caseSensitive,wholeWord)
        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
        return ret


    @dispatch
    def Replace(self ,pattern:Regex,replace:str)->int:
        """
        Replaces all entries of matchString regular expression with newValue string.
        :param pattern: The regular expression pattern to match.
        :param replace: The string to replace the matched pattern with.
        :return: The number of replacements made.
        """

        intPtrpattern:c_void_p = pattern.Ptr
        replacePtr = StrToPtr(replace)

        GetDllLibDoc().Document_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Document_Replace.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_Replace,self.Ptr, intPtrpattern,replacePtr)
        return ret


    @dispatch

    def Replace(self ,matchString:str,newValue:str,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces all entries of matchString string with newValue string, taking into
        consideration caseSensitive and wholeWord options.
        :param matchString: The string to match.
        :param newValue: The string to replace the matched string with.
        :param caseSensitive: If True, the match is case sensitive.
        :param wholeWord: If True, the match must be a whole word.
        :return: The number of replacements made.
        """
        matchStringPtr = StrToPtr(matchString)
        newValuePtr = StrToPtr(newValue)
        GetDllLibDoc().Document_ReplaceMNCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceMNCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_ReplaceMNCW,self.Ptr, matchStringPtr,newValuePtr,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,matchString:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces all entries of matchString string with TextSelection, taking into
        consideration caseSensitive and wholeWord options.
        :param matchString: The string to match.
        :param textSelection: The TextSelection object to replace the matched string with.
        :param caseSensitive: If True, the match is case sensitive.
        :param wholeWord: If True, the match must be a whole word.
        :return: The number of replacements made.
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Document_ReplaceMTCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceMTCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_ReplaceMTCW,self.Ptr, matchStringPtr,intPtrtextSelection,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def Replace(self ,pattern:'Regex',textSelection:TextSelection)->int:
#        """
#    <summary>
#        Replaces all entries of matchString regular expression with TextRangesHolder.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <param name="textSelection">The text selection.</param>
#    <returns></returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrtextSelection:c_void_p = textSelection.Ptr
#
#        GetDllLibDoc().Document_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_ReplacePT.restype=c_int
#        ret = GetDllLibDoc().Document_ReplacePT(self.Ptr, intPtrpattern,intPtrtextSelection)
#        return ret



    def CloneWebSettingsTo(self ,destDoc:'Document'):
        """
        Clone Websettings to other document.
        :param destDoc: The destination Document object.
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneWebSettingsTo.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CloneWebSettingsTo,self.Ptr, intPtrdestDoc)

    @dispatch

    def Replace(self ,matchString:str,matchDoc:IDocument,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces the specified matchString.
        :param matchString: The string to match.
        :param matchDoc: The IDocument object to replace the matched string with.
        :param caseSensitive: If True, the match is case sensitive.
        :param wholeWord: If True, the match must be a whole word.
        :return: The number of replacements made.
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrmatchDoc:c_void_p = matchDoc.Ptr

        GetDllLibDoc().Document_ReplaceMMCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceMMCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_ReplaceMMCW,self.Ptr, matchStringPtr,intPtrmatchDoc,caseSensitive,wholeWord)
        return ret

    @dispatch
    def UpdateWordCount(self):
        """
        Update Paragraphs count, Word count and Character count.
        """
        GetDllLibDoc().Document_UpdateWordCount.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_UpdateWordCount,self.Ptr)

#    @dispatch
#
#    def UpdateWordCount(self ,splitchar:'Char[]'):
#        """
#    <summary>
#        Update Paragraphs count, Word count and Character count.
#    </summary>
#    <param name="splitchar">The word separator. </param>
#        """
#        #arraysplitchar:ArrayTypesplitchar = ""
#        countsplitchar = len(splitchar)
#        ArrayTypesplitchar = c_void_p * countsplitchar
#        arraysplitchar = ArrayTypesplitchar()
#        for i in range(0, countsplitchar):
#            arraysplitchar[i] = splitchar[i].Ptr
#
#
#        GetDllLibDoc().Document_UpdateWordCountS.argtypes=[c_void_p ,ArrayTypesplitchar]
#        GetDllLibDoc().Document_UpdateWordCountS(self.Ptr, arraysplitchar)


#    @dispatch
#
#    def UpdateWordCount(self ,splitchar:'Char[]',includeTbFnEn:bool):
#        """
#    <summary>
#        Update Paragraphs count, Word count and Character count.
#    </summary>
#    <param name="splitchar">The word separator.</param>
#    <param name="includeTbFnEn">The include text boxes,footnotes and endnotes.</param>
#        """
#        #arraysplitchar:ArrayTypesplitchar = ""
#        countsplitchar = len(splitchar)
#        ArrayTypesplitchar = c_void_p * countsplitchar
#        arraysplitchar = ArrayTypesplitchar()
#        for i in range(0, countsplitchar):
#            arraysplitchar[i] = splitchar[i].Ptr
#
#
#        GetDllLibDoc().Document_UpdateWordCountSI.argtypes=[c_void_p ,ArrayTypesplitchar,c_bool]
#        GetDllLibDoc().Document_UpdateWordCountSI(self.Ptr, arraysplitchar,includeTbFnEn)



    def CheckProtectionPassWord(self ,password:str)->bool:
        """
        Checks if the entered password is the same as the permission protection password.

        Args:
            password: The password to check.

        Returns:
            True if the password is correct, False otherwise.
        """
        passwordPtr = StrToPtr(password)
        
        GetDllLibDoc().Document_CheckProtectionPassWord.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_CheckProtectionPassWord.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_CheckProtectionPassWord,self.Ptr, passwordPtr)
        return ret

    def GetPageCount(self)->int:
        """
        Gets the total number of pages for the document.

        Returns:
            The total number of pages.
        """
        GetDllLibDoc().Document_GetPageCount.argtypes=[c_void_p]
        GetDllLibDoc().Document_GetPageCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_GetPageCount,self.Ptr)
        return ret

    @dispatch
    def UpdateTableOfContents(self):
        """
        Updates the Table of Contents in the document.
        """
        GetDllLibDoc().Document_UpdateTableOfContents.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_UpdateTableOfContents,self.Ptr)

    @dispatch
    
    def UpdateTableOfContents(self ,toc:TableOfContent):
        """
        Updates the specified Table of Contents in the document.

        Args:
            toc: The specified Table of Contents.
        """
        intPtrtoc:c_void_p = toc.Ptr

        GetDllLibDoc().Document_UpdateTableOfContentsT.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_UpdateTableOfContentsT,self.Ptr, intPtrtoc)

    @dispatch
    def UpdateTOCPageNumbers(self):
        """
        Updates the Table of Contents page numbers in the document.
        """
        GetDllLibDoc().Document_UpdateTOCPageNumbers.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_UpdateTOCPageNumbers,self.Ptr)

    @dispatch

    def UpdateTOCPageNumbers(self ,toc:'TableOfContent'):
        """
        Updates the specified Table of Contents page numbers in the document.

        Args:
            toc: The specified Table of Contents.
        """
        intPtrtoc:c_void_p = toc.Ptr

        GetDllLibDoc().Document_UpdateTOCPageNumbersT.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_UpdateTOCPageNumbersT,self.Ptr, intPtrtoc)

    @dispatch

    def Compare(self ,document:'Document',author:str):
        """
        Compares this document with another document.

        Args:
            document: The document to compare.
            author: The author to use for revisions.
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr

        GetDllLibDoc().Document_Compare.argtypes=[c_void_p ,c_void_p,c_char_p]
        CallCFunction(GetDllLibDoc().Document_Compare,self.Ptr, intPtrdocument,authorPtr)

    @dispatch

    def Compare(self ,document:'Document',author:str,options:CompareOptions):
        """
        Compares this document with another document.

        Args:
            document: The document to compare.
            author: The author to use for revisions.
            options: The comparison parameters.
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr
        intPtroptions:c_void_p = options.Ptr

        GetDllLibDoc().Document_CompareDAO.argtypes=[c_void_p ,c_void_p,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CompareDAO,self.Ptr, intPtrdocument,authorPtr,intPtroptions)

    @dispatch

    def Compare(self ,document:'Document',author:str,dateTime:DateTime):
        """
        Compares this document with another document.

        Args:
            document: The document to compare.
            author: The author to use for revisions.
            dateTime: The date and time to use for revisions.
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr
        intPtrdateTime:c_void_p = dateTime.Ptr

        GetDllLibDoc().Document_CompareDAD.argtypes=[c_void_p ,c_void_p,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CompareDAD,self.Ptr, intPtrdocument,authorPtr,intPtrdateTime)

    @dispatch

    def Compare(self ,document:'Document',author:str,dateTime:DateTime,options:CompareOptions):
        """
        Compares this document with another document.

        Args:
            document: The document to compare.
            author: The author to use for revisions.
            dateTime: The date and time to use for revisions.
            options: The comparison parameters.
        """
        authorPtr = StrToPtr(author)
        intPtrdocument:c_void_p = document.Ptr
        intPtrdateTime:c_void_p = dateTime.Ptr
        intPtroptions:c_void_p = options.Ptr

        GetDllLibDoc().Document_CompareDADO.argtypes=[c_void_p ,c_void_p,c_char_p,c_void_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CompareDADO,self.Ptr, intPtrdocument,authorPtr,intPtrdateTime,intPtroptions)

    @dispatch

    def ReplaceInLine(self ,matchString:str,newValue:str,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces all occurrences of matchString text with newValue text in single-line mode.

        Args:
            matchString: The matchString.
            newValue: The newValue.
            caseSensitive: If True, the replacement is case sensitive.
            wholeWord: If True, only whole words will be replaced.

        Returns:
            The number of replacements made.
        """
        matchStringPtr = StrToPtr(matchString)
        newValuePtr = StrToPtr(newValue)
        GetDllLibDoc().Document_ReplaceInLine.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceInLine.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_ReplaceInLine,self.Ptr, matchStringPtr,newValuePtr,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def ReplaceInLine(self ,pattern:'Regex',newValue:str)->int:
#        """
#    <summary>
#        Replaces all entries with specified pattern with newValue text in single-line mode.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <param name="newValue">The newValue.</param>
#    <returns></returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_ReplaceInLinePN.argtypes=[c_void_p ,c_void_p,c_wchar_p]
#        GetDllLibDoc().Document_ReplaceInLinePN.restype=c_int
#        ret = GetDllLibDoc().Document_ReplaceInLinePN(self.Ptr, intPtrpattern,newValue)
#        return ret


    @dispatch

    def ReplaceInLine(self ,matchString:str,matchSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces the matchString text with matchSelection in single-line mode.

        Args:
            matchString: The matchString.
            matchSelection: The matchSelection.
            caseSensitive: If True, the replacement is case sensitive.
            wholeWord: If True, only whole words will be replaced.

        Returns:
            The number of replacements made.
        """
        matchStringPtr = StrToPtr(matchString)
        intPtrmatchSelection:c_void_p = matchSelection.Ptr

        GetDllLibDoc().Document_ReplaceInLineMMCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Document_ReplaceInLineMMCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_ReplaceInLineMMCW,self.Ptr, matchStringPtr,intPtrmatchSelection,caseSensitive,wholeWord)
        return ret

#    @dispatch
#
#    def ReplaceInLine(self ,pattern:'Regex',matchSelection:TextSelection)->int:
#        """
#    <summary>
#        Replaces the matchString pattern with matchSelection in single-line mode.
#    </summary>
#    <param name="pattern">The pattern.</param>
#    <param name="matchSelection">The matchSelection.</param>
#    <returns>The number of performed replaces.</returns>
#        """
#        intPtrpattern:c_void_p = pattern.Ptr
#        intPtrmatchSelection:c_void_p = matchSelection.Ptr
#
#        GetDllLibDoc().Document_ReplaceInLinePM.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_ReplaceInLinePM.restype=c_int
#        ret = GetDllLibDoc().Document_ReplaceInLinePM(self.Ptr, intPtrpattern,intPtrmatchSelection)
#        return ret


    @dispatch

    def FindString(self ,start:BodyRegion,matchString:str,caseSensitive:bool,wholeWord:bool)->TextSelection:
        """
        Finds the next entry of matchString string, taking into consideration caseSensitive
        and wholeWord options.

        Args:
            start: Search starts.
            matchString: The string to find.
            caseSensitive: If it specifies case sensitive search, set to True.
            wholeWord: If it search for the whole word, set to True.

        Returns:
            The TextSelection object.

        """
        matchStringPtr = StrToPtr(matchString)
        intPtrstart:c_void_p = start.Ptr

        GetDllLibDoc().Document_FindStringSMCW.argtypes=[c_void_p ,c_void_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Document_FindStringSMCW.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_FindStringSMCW,self.Ptr, intPtrstart,matchStringPtr,caseSensitive,wholeWord)
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret


#    @dispatch
#
#    def FindPattern(self ,start:BodyRegion,pattern:'Regex')->TextSelection:
#        """
#    <summary>
#        Finds the next entry of matchString pattern.
#    </summary>
#    <param name="start">Search starts</param>
#    <param name="pattern">The pattern.</param>
#    <returns></returns>
#        """
#        intPtrstart:c_void_p = start.Ptr
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPatternSP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_FindPatternSP.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_FindPatternSP(self.Ptr, intPtrstart,intPtrpattern)
#        ret = None if intPtr==None else TextSelection(intPtr)
#        return ret
#


#    @dispatch
#
#    def FindStringInLine(self ,start:BodyRegion,matchString:str,caseSensitive:bool,wholeWord:bool)->List[TextSelection]:
#        """
#    <summary>
#        Finds the next matchString text starting from specified using single-line mode.
#    </summary>
#    <param name="start">Search start.</param>
#    <param name="matchString">The matchString.</param>
#    <param name="caseSensitive">if it is case sensitive search, set to <c>true</c>.</param>
#    <param name="wholeWord">if it search for whole word, set to <c>true</c> .</param>
#    <returns></returns>
#        """
#        intPtrstart:c_void_p = start.Ptr
#
#        GetDllLibDoc().Document_FindStringInLineSMCW.argtypes=[c_void_p ,c_void_p,c_wchar_p,c_bool,c_bool]
#        GetDllLibDoc().Document_FindStringInLineSMCW.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindStringInLineSMCW(self.Ptr, intPtrstart,matchString,caseSensitive,wholeWord)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


#    @dispatch
#
#    def FindPatternInLine(self ,start:BodyRegion,pattern:'Regex')->List[TextSelection]:
#        """
#    <summary>
#        Finds the text which fit the specified pattern starting from start.
#            using single-line mode.
#    </summary>
#    <param name="start">Search start.</param>
#    <param name="pattern">The pattern.</param>
#    <returns></returns>
#        """
#        intPtrstart:c_void_p = start.Ptr
#        intPtrpattern:c_void_p = pattern.Ptr
#
#        GetDllLibDoc().Document_FindPatternInLineSP.argtypes=[c_void_p ,c_void_p,c_void_p]
#        GetDllLibDoc().Document_FindPatternInLineSP.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_FindPatternInLineSP(self.Ptr, intPtrstart,intPtrpattern)
#        ret = GetObjVectorFromArray(intPtrArray, TextSelection)
#        return ret


    def ResetFindState(self):
        """
        Resets the FindPattern.
        """
        GetDllLibDoc().Document_ResetFindState.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_ResetFindState,self.Ptr)


    def CreateParagraphItem(self ,itemType:'ParagraphItemType')->'ParagraphBase':
        """
        Creates new paragraph item instance.

        Args:
            itemType: Paragraph item type.

        Returns:
            The ParagraphBase object.

        """
        enumitemType:c_int = itemType.value

        GetDllLibDoc().Document_CreateParagraphItem.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_CreateParagraphItem.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateParagraphItem,self.Ptr, enumitemType)
        ret = None if intPtr==None else self._createParagraphItemByType(intPtr)
        return ret

    def _createParagraphItemByType(self, intPtrWithTypeName:IntPtrWithTypeName)->ParagraphBase:
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Break"):
            from spire.doc import Break
            ret = Break(intPtr)
        elif(strName == "Spire.Doc.Fields.TextRange"):
            from spire.doc import TextRange
            ret = TextRange(intPtr)
        elif(strName == "Spire.Doc.Fields.DocPicture"):
            from spire.doc import DocPicture
            ret = DocPicture(intPtr)
        elif(strName == "Spire.Doc.BookmarkStart"):
            from spire.doc import BookmarkStart
            ret = BookmarkStart(intPtr)
        elif(strName == "Spire.Doc.BookmarkEnd"):
            from spire.doc import BookmarkEnd
            ret = BookmarkEnd(intPtr)
        elif(strName == "Spire.Doc.Fields.Field"):
            from spire.doc import Field
            ret = Field(intPtr)
        elif(strName == "Spire.Doc.Fields.TextBox"):
            from spire.doc import TextBox
            ret = TextBox(intPtr)
        elif(strName == "Spire.Doc.Fields.MergeField"):
            from spire.doc import MergeField
            ret = MergeField(intPtr)
        #elif(strName == "Spire.Doc.Fields.EmbedField"):
        #  ret = EmbedField(intPtr)
        elif(strName == "Spire.Doc.Fields.Symbol"):
            from spire.doc import Symbol
            ret = Symbol(intPtr)
        elif(strName == "Spire.Doc.Fields.FieldMark"):
            from spire.doc import FieldMark
            ret = FieldMark(intPtr)
        elif(strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif(strName == "Spire.Doc.Fields.Comment"):
            from spire.doc import Comment
            ret = Comment(intPtr)
        elif(strName == "Spire.Doc.Documents.CommentMark"):
            from spire.doc import CommentMark
            ret = CommentMark(intPtr)
        elif(strName == "Spire.Doc.Fields.Footnote"):
            from spire.doc import Footnote
            ret = Footnote(intPtr)
        elif(strName == "Spire.Doc.Fields.ShapeObject"):
            from spire.doc import ShapeObject
            ret = ShapeObject(intPtr)
        elif(strName == "Spire.Doc.Fields.ShapeGroup"):
            from spire.doc import ShapeGroup
            ret = ShapeGroup(intPtr)
        elif(strName == "Spire.Doc.Fields.TableOfContent"):
            from spire.doc import TableOfContent
            ret = TableOfContent(intPtr)
        elif(strName == "Spire.Doc.Fields.DocOleObject"):
            from spire.doc import DocOleObject
            ret = DocOleObject(intPtr)
        else:
            ret = ParagraphBase(intPtr)
        return ret

    def CreateParagraph(self)->'Paragraph':
        """
        Creates a new paragraph in the document.

        Returns:
            Paragraph: The newly created paragraph.
        """
        GetDllLibDoc().Document_CreateParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Document_CreateParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_CreateParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    def CreateMinialDocument(self):
        """
        Creates a minimal document with one empty section and one empty paragraph.

        Returns:
            None
        """
        GetDllLibDoc().Document_CreateMinialDocument.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_CreateMinialDocument,self.Ptr)


    def AddSection(self)->'Section':
        """
        Adds a new section to the document.

        Returns:
            Section: The newly added section.
        """
        GetDllLibDoc().Document_AddSection.argtypes=[c_void_p]
        GetDllLibDoc().Document_AddSection.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_AddSection,self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret



    def AddParagraphStyle(self ,styleName:str)->'ParagraphStyle':
        """
        Adds a new paragraph style to the document.

        Args:
            styleName (str): The name of the paragraph style.

        Returns:
            ParagraphStyle: The newly added paragraph style.
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().Document_AddParagraphStyle.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Document_AddParagraphStyle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_AddParagraphStyle,self.Ptr, styleNamePtr)
        ret = None if intPtr==None else ParagraphStyle(intPtr)
        return ret



    def AddListStyle(self ,listType:'ListType',styleName:str)->'ListStyle':
        """
        Adds a new list style to the document.

        Args:
            listType (ListType): The type of the list.
            styleName (str): The name of the paragraph style.

        Returns:
            ListStyle: The newly added list style.
        """
        styleNamePtr = StrToPtr(styleName)
        enumlistType:c_int = listType.value

        GetDllLibDoc().Document_AddListStyle.argtypes=[c_void_p ,c_int,c_char_p]
        GetDllLibDoc().Document_AddListStyle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_AddListStyle,self.Ptr, enumlistType,styleNamePtr)
        ret = None if intPtr==None else ListStyle(intPtr)
        return ret



    def GetText(self)->str:
        """
        Gets the text of the document.

        Returns:
            str: The text of the document.
        """
        GetDllLibDoc().Document_GetText.argtypes=[c_void_p]
        GetDllLibDoc().Document_GetText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Document_GetText,self.Ptr))
        return ret


#    @staticmethod
#    @dispatch
#
#    def Sign(sourceStream:Stream,certificatePath:str,securePassword:str)->List[Byte]:
#        """
#    <summary>
#         Create digitally signed word document.
#             Digital signature of documents support only DOC and DOCX formats.
#    </summary>
#    <param name="sourceStream">Source file stream</param>
#    <param name="certificatePath">Path to the file certificate</param>
#    <param name="securePassword">Password of the certificate.</param>
#    <returns>Bytes of signed word document </returns>
#        """
#        intPtrsourceStream:c_void_p = sourceStream.Ptr
#
#        GetDllLibDoc().Document_Sign.argtypes=[ c_void_p,c_wchar_p,c_wchar_p]
#        GetDllLibDoc().Document_Sign.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_Sign( intPtrsourceStream,certificatePath,securePassword)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret


#    @staticmethod
#    @dispatch
#
#    def Sign(sourceStream:Stream,certificateData:'Byte[]',securePassword:str)->List[Byte]:
#        """
#    <summary>
#        Create digitally signed word document.
#            Digital signature of documents support only DOC and DOCX formats.
#    </summary>
#    <param name="sourceStream">Source file stream.</param>
#    <param name="certificateData">the certificate data.</param>
#    <param name="securePassword">Password of the certificate.</param>
#    <returns>Bytes of signed word document</returns>
#        """
#        intPtrsourceStream:c_void_p = sourceStream.Ptr
#        #arraycertificateData:ArrayTypecertificateData = ""
#        countcertificateData = len(certificateData)
#        ArrayTypecertificateData = c_void_p * countcertificateData
#        arraycertificateData = ArrayTypecertificateData()
#        for i in range(0, countcertificateData):
#            arraycertificateData[i] = certificateData[i].Ptr
#
#
#        GetDllLibDoc().Document_SignSCS.argtypes=[ c_void_p,ArrayTypecertificateData,c_wchar_p]
#        GetDllLibDoc().Document_SignSCS.restype=IntPtrArray
#        intPtrArray = GetDllLibDoc().Document_SignSCS( intPtrsourceStream,arraycertificateData,securePassword)
#        ret = GetObjVectorFromArray(intPtrArray, Byte)
#        return ret



    def Clone(self)->'Document':
        """
        Clones the document.

        Returns:
            Document: The cloned document.
        """
        GetDllLibDoc().Document_Clone.argtypes=[c_void_p]
        GetDllLibDoc().Document_Clone.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_Clone,self.Ptr)
        ret = None if intPtr==None else Document(intPtr)
        return ret



    def CloneDefaultStyleTo(self ,destDoc:'Document'):
        """
        Clones the default style of the current document to the destination document.

        Args:
            destDoc (Document): The destination document.

        Returns:
            None
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneDefaultStyleTo.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CloneDefaultStyleTo,self.Ptr, intPtrdestDoc)


    def CloneThemesTo(self ,destDoc:'Document'):
        """
        Clones the theme style of the current document to the destination document.

        Args:
            destDoc (Document): The destination document.

        Returns:
            None
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneThemesTo.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CloneThemesTo,self.Ptr, intPtrdestDoc)


    def CloneCompatibilityTo(self ,destDoc:'Document'):
        """
        Clones the compatibility settings of the current document to the destination document.

        Args:
            destDoc (Document): The destination document.

        Returns:
            None
        """
        intPtrdestDoc:c_void_p = destDoc.Ptr

        GetDllLibDoc().Document_CloneCompatibilityTo.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_CloneCompatibilityTo,self.Ptr, intPtrdestDoc)


    def ImportSection(self ,section:'ISection'):
        """
        Imports a section into the document.

        Args:
            section (ISection): The section to be imported.

        Returns:
            None
        """
        intPtrsection:c_void_p = section.Ptr

        GetDllLibDoc().Document_ImportSection.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_ImportSection,self.Ptr, intPtrsection)

    @dispatch

    def ImportContent(self ,doc:IDocument):
        """
        Imports all content into the document.

        Args:
            doc (IDocument): The document to import.
        """
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Document_ImportContent.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_ImportContent,self.Ptr, intPtrdoc)

    @dispatch

    def ImportContent(self ,doc:IDocument,importStyles:bool):
        """
        Imports all content into the document.

        Args:
            doc (IDocument): The document to import.
            importStyles (bool): If document styles with the same names should also be imported, set to True.
        """
        intPtrdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Document_ImportContentDI.argtypes=[c_void_p ,c_void_p,c_bool]
        CallCFunction(GetDllLibDoc().Document_ImportContentDI,self.Ptr, intPtrdoc,importStyles)


    def AddStyle(self ,builtinStyle:'BuiltinStyle')->'Style':
        """
        Adds a style to the document style.

        Args:
            builtinStyle (BuiltinStyle): The built-in style to add.

        Returns:
            Style: The added style.
        """
        enumbuiltinStyle:c_int = builtinStyle.value

        GetDllLibDoc().Document_AddStyle.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Document_AddStyle.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().Document_AddStyle,self.Ptr, enumbuiltinStyle)
        ret = None if intPtr==None else self._create(intPtr)
        return ret


    def _create(self,intPtrWithTypeName:IntPtrWithTypeName)->'Style':

        ret= None
        if intPtrWithTypeName == None :
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Documents.ListStyle"):
            ret = ListStyle(intPtr)
        elif(strName == "Spire.Doc.Documents.ParagraphStyle"):
            from spire.doc import ParagraphStyle
            ret = ParagraphStyle(intPtr)
        else:
            ret = Style(intPtr)
        return ret

    def AcceptChanges(self):
        """
        Accepts changes tracked from the moment of last change acceptance.
        """
        GetDllLibDoc().Document_AcceptChanges.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_AcceptChanges,self.Ptr)

    def RejectChanges(self):
        """
        Rejects changes tracked from the moment of last change acceptance.
        """
        GetDllLibDoc().Document_RejectChanges.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_RejectChanges,self.Ptr)

    @dispatch

    def Protect(self ,type:ProtectionType):
        """
        Protects the document.

        Args:
            type (ProtectionType): The type of protection.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Document_Protect.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().Document_Protect,self.Ptr, enumtype)

    @dispatch

    def Protect(self ,type:ProtectionType,password:str):
        """
        Protects the document.

        Args:
            type (ProtectionType): The type of protection.
            password (str): The password used for protection.
        """
        passwordPtr = StrToPtr(password)
        enumtype:c_int = type.value

        GetDllLibDoc().Document_ProtectTP.argtypes=[c_void_p ,c_int,c_char_p]
        CallCFunction(GetDllLibDoc().Document_ProtectTP,self.Ptr, enumtype,passwordPtr)


    def Encrypt(self ,password:str):
        """
        Encrypts the document.

        Args:
            password (str): The password.
        """
        passwordPtr = StrToPtr(password)
        GetDllLibDoc().Document_Encrypt.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_Encrypt,self.Ptr, passwordPtr)

    def RemoveEncryption(self):
        """
        Removes the encryption.
        """
        GetDllLibDoc().Document_RemoveEncryption.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Document_RemoveEncryption,self.Ptr)


    def SaveToTxt(self ,fileName:str,encoding:'Encoding'):
        """
        Saves the document to a text file with the specified encoding.

        Args:
            fileName (str): The name of the file.
            encoding (Encoding): The encoding.
        """
        fileNamePtr = StrToPtr(fileName)
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_SaveToTxt.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_SaveToTxt,self.Ptr, fileNamePtr,intPtrencoding)


    def OpenOnlineBin(self ,fileName:str):
        """
        Opens an online binary file.

        Args:
            fileName (str): The name of the file.
        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_OpenOnlineBin.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_OpenOnlineBin,self.Ptr, fileNamePtr)

#    @dispatch
#
#    def LoadHTML(self ,reader:'TextReader',baseURL:str,validationType:XHTMLValidationType):
#        """
#    <summary>
#        Load document in html format
#    </summary>
#    <param name="reader">Reader of html code.</param>
#    <param name="baseURL">The default base URL for all links of external resource,
#                                   it should be a absolute and well formed uri string, for example:
#                                   http://www.e-iceblue.com/ or file:///C:/mywebsite/docs/
#                                   If it's null, use the href attribute of base tag in html instead;
#                                   Otherwise, it will overwrite the href attribute of base tag.</param>
#    <param name="validationType">XHTML validation type.</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#        enumvalidationType:c_int = validationType.value
#
#        GetDllLibDoc().Document_LoadHTML.argtypes=[c_void_p ,c_void_p,c_wchar_p,c_int]
#        GetDllLibDoc().Document_LoadHTML(self.Ptr, intPtrreader,baseURL,enumvalidationType)


#    @dispatch
#
#    def LoadHTML(self ,reader:'TextReader',validationType:XHTMLValidationType):
#        """
#    <summary>
#        Load document in html format
#    </summary>
#    <param name="reader">Reader of html code.</param>
#    <param name="validationType">XHTML validation type.</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#        enumvalidationType:c_int = validationType.value
#
#        GetDllLibDoc().Document_LoadHTMLRV.argtypes=[c_void_p ,c_void_p,c_int]
#        GetDllLibDoc().Document_LoadHTMLRV(self.Ptr, intPtrreader,enumvalidationType)


    @dispatch

    def LoadText(self ,fileName:str):
        """
        Opens the text document from a file with default encoding utf-8.

        Args:
            fileName (str): Name of the file.

        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_LoadText.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_LoadText,self.Ptr, fileNamePtr)

    @dispatch

    def LoadText(self ,stream:Stream):
        """
        Opens the text document from a stream with default encoding utf-8.

        Args:
            stream (Stream): The stream.

        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_LoadTextS.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_LoadTextS,self.Ptr, intPtrstream)

    @dispatch

    def LoadText(self ,fileName:str,encoding:Encoding):
        """
        Opens the text document with specified encoding from a file.

        Args:
            fileName (str): Name of the file.
            encoding (Encoding): The encoding.

        """
        fileNamePtr = StrToPtr(fileName)
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadTextFE.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_LoadTextFE,self.Ptr, fileNamePtr,intPtrencoding)

    @dispatch

    def LoadText(self ,stream:Stream,encoding:Encoding):
        """
        Opens the text document with specified encoding from a stream.

        Args:
            stream (Stream): The text document stream.
            encoding (Encoding): The encoding.

        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadTextSE.argtypes=[c_void_p ,c_void_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_LoadTextSE,self.Ptr, intPtrstream,intPtrencoding)

#    @dispatch
#
#    def LoadText(self ,reader:'TextReader'):
#        """
#    <summary>
#        Opens the rtf document with specified encoding from a reader.
#    </summary>
#    <param name="reader">The rtf document reader</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#
#        GetDllLibDoc().Document_LoadTextR.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_LoadTextR(self.Ptr, intPtrreader)


    @dispatch

    def LoadFromFile(self ,fileName:str):
        """
        Opens doc file.

        Args:
            fileName (Stream): The fileName.

        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_LoadFromFile.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_LoadFromFile,self.Ptr, fileNamePtr)

    @dispatch

    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat):
        """
         Opens the document from file in Xml or Microsoft Word format.

        Args:
            fileName (Stream): The fileName.
            fileFormat (FileFormat): The fileFormat.

        """
        fileNamePtr = StrToPtr(fileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromFileFF.argtypes=[c_void_p ,c_char_p,c_int]
        CallCFunction(GetDllLibDoc().Document_LoadFromFileFF,self.Ptr, fileNamePtr,enumfileFormat)

    @dispatch

    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat,validationType:XHTMLValidationType):
        """
         Opens the HTML document from stream .

        Args:
            fileName (Stream): Name of the file.
            fileFormat (FileFormat): Type of the format.
            validationType (XHTMLValidationType): Type of the validation.

        """
        fileNamePtr = StrToPtr(fileName)

        enumfileFormat:c_int = fileFormat.value
        enumvalidationType:c_int = validationType.value

        GetDllLibDoc().Document_LoadFromFileFFV.argtypes=[c_void_p ,c_char_p,c_int,c_int]
        CallCFunction(GetDllLibDoc().Document_LoadFromFileFFV,self.Ptr, fileNamePtr,enumfileFormat,enumvalidationType)

    @dispatch

    def LoadFromFile(self ,fileName:str,fileFormat:FileFormat,password:str):
        """
        Opens the document from file in Xml or Microsoft Word format.

        Args:
            fileName (Stream): Name of the file.
            fileFormat (FileFormat): Type of the format.
            password (str): The password.

        """
        fileNamePtr = StrToPtr(fileName)
        passwordPtr = StrToPtr(password)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromFileFFP.argtypes=[c_void_p ,c_char_p,c_int,c_char_p]
        CallCFunction(GetDllLibDoc().Document_LoadFromFileFFP,self.Ptr, fileNamePtr,enumfileFormat,passwordPtr)


    def LoadFromFileInReadMode(self ,strFileName:str,fileFormat:'FileFormat'):
        """
        LoadFromStream new document in read-only mode.

        Args:
            strFileName (str): File to open.
            fileFormat (FileFormat): Type of the format.

        """
        strFileNamePtr = StrToPtr(strFileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_LoadFromFileInReadMode.argtypes=[c_void_p ,c_char_p,c_int]
        CallCFunction(GetDllLibDoc().Document_LoadFromFileInReadMode,self.Ptr, strFileNamePtr,enumfileFormat)

    @dispatch

    def LoadRtf(self ,fileName:str):
        """
        Opens the rtf document from a file.

        Args:
            fileName (str): Name of the file.

        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_LoadRtf.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_LoadRtf,self.Ptr, fileNamePtr)

    @dispatch

    def LoadRtf(self ,stream:Stream):
        """
        Opens the rtf document from a stream.

        Args:
            stream (Stream): The stream.

        """
        intPtrstream:c_void_p = stream.Ptr

        GetDllLibDoc().Document_LoadRtfS.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_LoadRtfS,self.Ptr, intPtrstream)

    @dispatch

    def LoadRtf(self ,fileName:str,encoding:Encoding):
        """
        Opens the rtf document with specified encoding from a file.

        Args:
            fileName (str): Name of the file.
            encoding (Encoding): The encoding.

        """
        fileNamePtr = StrToPtr(fileName)
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadRtfFE.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_LoadRtfFE,self.Ptr, fileNamePtr,intPtrencoding)

    @dispatch

    def LoadRtf(self ,stream:Stream,encoding:Encoding):
        """
        Opens the rtf document with specified encoding from a stream.

        Args:
            stream (Stream): The rtf document stream.
            encoding (Encoding): The encoding.

        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrencoding:c_void_p = encoding.Ptr

        GetDllLibDoc().Document_LoadRtfSE.argtypes=[c_void_p ,c_void_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_LoadRtfSE,self.Ptr, intPtrstream,intPtrencoding)

#    @dispatch
#
#    def LoadRtf(self ,reader:'TextReader'):
#        """
#    <summary>
#        Opens the rtf document with specified encoding from a reader.
#    </summary>
#    <param name="reader">The rtf document reader</param>
#        """
#        intPtrreader:c_void_p = reader.Ptr
#
#        GetDllLibDoc().Document_LoadRtfR.argtypes=[c_void_p ,c_void_p]
#        GetDllLibDoc().Document_LoadRtfR(self.Ptr, intPtrreader)


    @dispatch

    def SaveToFile(self ,fileName:str):
        """
        Saves to file in Microsoft Word format.

        Args:
            fileName (str): The fileName.

        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_SaveToFileF.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_SaveToFileF,self.Ptr, fileNamePtr)

    @dispatch

    def SaveToFile(self ,fileName:str,paramList:ToPdfParameterList):
        """
        Saves the document to PDF file.

        Args:
            fileName (str): The fileName.
            paramList (ToPdfParameterList): The Parameter list.

        """
        fileNamePtr = StrToPtr(fileName)
        intPtrparamList:c_void_p = paramList.Ptr

        GetDllLibDoc().Document_SaveToFileFP.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_SaveToFileFP,self.Ptr, fileNamePtr,intPtrparamList)

    @dispatch

    def SaveToEpub(self ,fileName:str,coverImage:DocPicture):
        """
        Saves the EPUB document.

        Args:
            fileName (str): The fileName.
            coverImage (DocPicture): The cover image.

        """
        fileNamePtr = StrToPtr(fileName)
        intPtrcoverImage:c_void_p = coverImage.Ptr

        GetDllLibDoc().Document_SaveToEpub.argtypes=[c_void_p ,c_char_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_SaveToEpub,self.Ptr, fileNamePtr,intPtrcoverImage)

    @dispatch

    def SaveToEpub(self ,stream:Stream,coverImage:DocPicture):
        """
        Saves the EPUB document.

        Args:
            stream (Stream): The stream.
            coverImage (DocPicture): The cover image.

        """
        intPtrstream:c_void_p = stream.Ptr
        intPtrcoverImage:c_void_p = coverImage.Ptr

        GetDllLibDoc().Document_SaveToEpubSC.argtypes=[c_void_p ,c_void_p,c_void_p]
        CallCFunction(GetDllLibDoc().Document_SaveToEpubSC,self.Ptr, intPtrstream,intPtrcoverImage)


    def InsertTextFromFile(self ,fileName:str,fileFormat:'FileFormat'):
        """
        Insert text from a file.

        Args:
            fileName (Stream): The file name.
            fileFormat (FileFormat): Type of the format.

        """
        fileNamePtr = StrToPtr(fileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_InsertTextFromFile.argtypes=[c_void_p ,c_char_p,c_int]
        CallCFunction(GetDllLibDoc().Document_InsertTextFromFile,self.Ptr, fileNamePtr,enumfileFormat)


    def InsertTextFromStream(self ,stream:'Stream',fileFormat:'FileFormat'):
        """
        Insert text from stream.

        Args:
            stream (Stream): The stream.
            fileFormat (FileFormat): Type of the format.

        """
        intPtrstream:c_void_p = stream.Ptr
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_InsertTextFromStream.argtypes=[c_void_p ,c_void_p,c_int]
        CallCFunction(GetDllLibDoc().Document_InsertTextFromStream,self.Ptr, intPtrstream,enumfileFormat)

    @dispatch

    def SaveToFile(self ,fileName:str,fileFormat:FileFormat):
        """
        Saves the document to file in Xml or Microsoft Word format.

        Args:
            fileName (str): The file name.
            fileFormat (FileFormat): Type of the format.

        """
        fileNamePtr = StrToPtr(fileName)
        enumfileFormat:c_int = fileFormat.value

        GetDllLibDoc().Document_SaveToFileFF.argtypes=[c_void_p ,c_char_p,c_int]
        CallCFunction(GetDllLibDoc().Document_SaveToFileFF,self.Ptr, fileNamePtr,enumfileFormat)

    @dispatch

    def SaveToSVG(self ,fileName:str):
        """
        Saves the SVG.

        Args:
            fileName (str): The file name.

        """
        fileNamePtr = StrToPtr(fileName)
        GetDllLibDoc().Document_SaveToSVG.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Document_SaveToSVG,self.Ptr, fileNamePtr)

#    @dispatch
#
#    def SaveToSVG(self)->Queue1:
#        """
#    <summary>
#        Saves the SVG.
#    </summary>
#        """
#        GetDllLibDoc().Document_SaveToSVG1.argtypes=[c_void_p]
#        GetDllLibDoc().Document_SaveToSVG1.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_SaveToSVG1(self.Ptr)
#        ret = None if intPtr==None else Queue1(intPtr)
#        return ret
#


    @property
    def PageCount(self)->int:
        """
        Gets total number of pages for document.

        """
        GetDllLibDoc().Document_get_PageCount.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_PageCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_get_PageCount,self.Ptr)
        return ret

    @property
    def IsContainMacro(self)->bool:
        """
        Indicates whether the document has macros.
        """
        GetDllLibDoc().Document_get_IsContainMacro.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_IsContainMacro.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_IsContainMacro,self.Ptr)
        return ret

    @property
    def KeepSameFormat(self)->bool:
        """
        Gets or sets a value that indicates whether to keep same formatting when this document is merged to other document.
        """
        GetDllLibDoc().Document_get_KeepSameFormat.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_KeepSameFormat.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_KeepSameFormat,self.Ptr)
        return ret

    @KeepSameFormat.setter
    def KeepSameFormat(self, value:bool):
        GetDllLibDoc().Document_set_KeepSameFormat.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_KeepSameFormat,self.Ptr, value)

    @property
    def UseNewEngine(self)->bool:
        """
        Gets a value indicating whether the new engine layout is enabled.
        The Spire.Doc product conversion feature has enabled the new engine way layout by default.
        If you want to switch to the old engine layout, use the Document constructor
        with the \"useNewEngine\" parameter and set the parameter \"useNewEngine\" to false.
        """
        GetDllLibDoc().Document_get_UseNewEngine.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_UseNewEngine.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_UseNewEngine,self.Ptr)
        return ret


    def add_EvalInformation(self ,value:'SpireDocEvalInfo'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_EvalInformation.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_add_EvalInformation,self.Ptr, intPtrvalue)


    def remove_EvalInformation(self ,value:'SpireDocEvalInfo'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_EvalInformation.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_remove_EvalInformation,self.Ptr, intPtrvalue)


    def add_BookmarkLayout(self ,value:'BookmarkLevelHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_BookmarkLayout.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_add_BookmarkLayout,self.Ptr, intPtrvalue)


    def remove_BookmarkLayout(self ,value:'BookmarkLevelHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_BookmarkLayout.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_remove_BookmarkLayout,self.Ptr, intPtrvalue)


    def add_PageLayout(self ,value:'PageLayoutHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_PageLayout.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_add_PageLayout,self.Ptr, intPtrvalue)


    def remove_PageLayout(self ,value:'PageLayoutHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_PageLayout.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_remove_PageLayout,self.Ptr, intPtrvalue)


    def add_UpdateFields(self ,value:'UpdateFieldsHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_add_UpdateFields.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_add_UpdateFields,self.Ptr, intPtrvalue)


    def remove_UpdateFields(self ,value:'UpdateFieldsHandler'):
        """

        """
        intPtrvalue:c_void_p = value.Ptr

        GetDllLibDoc().Document_remove_UpdateFields.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Document_remove_UpdateFields,self.Ptr, intPtrvalue)

    @property

    def TOC(self)->'TableOfContent':
        """
        Gets or sets the TOC element of the word document.
        """
        GetDllLibDoc().Document_get_TOC.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_TOC.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_TOC,self.Ptr)
        ret = None if intPtr==None else TableOfContent(intPtr)
        return ret


    @TOC.setter
    def TOC(self, value:'TableOfContent'):
        GetDllLibDoc().Document_set_TOC.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Document_set_TOC,self.Ptr, value.Ptr)

    @property
    def EmbedFontsInFile(self)->bool:
        """
        Gets or sets a value indicating whether save fonts that are used in the document in the file.
        Only support for the DOCX file format.
        """
        GetDllLibDoc().Document_get_EmbedFontsInFile.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_EmbedFontsInFile.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_EmbedFontsInFile,self.Ptr)
        return ret

    @EmbedFontsInFile.setter
    def EmbedFontsInFile(self, value:bool):
        GetDllLibDoc().Document_set_EmbedFontsInFile.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_EmbedFontsInFile,self.Ptr, value)

    @property

    def PrivateFontList(self)->List[PrivateFontPath]:
        """
        Gets the private font list.
        """
        GetDllLibDoc().Document_get_PrivateFontList.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_PrivateFontList.restype=IntPtrArray
        intPtr = CallCFunction(GetDllLibDoc().Document_get_PrivateFontList,self.Ptr)
        ret = GetVectorFromArray(intPtr,PrivateFontPath)
        return ret



    @property
    def EmbedSystemFonts(self)->bool:
        """
        Gets or sets a value indicating whether save system fonts that are used in the document in the file.
        """
        GetDllLibDoc().Document_get_EmbedSystemFonts.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_EmbedSystemFonts.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_EmbedSystemFonts,self.Ptr)
        return ret

    @EmbedSystemFonts.setter
    def EmbedSystemFonts(self, value:bool):
        GetDllLibDoc().Document_set_EmbedSystemFonts.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_EmbedSystemFonts,self.Ptr, value)

    @property

    def HtmlBaseUrl(self)->str:
        """
        Gets or sets the Base path which is used to convert the relative path to absolute path.
        """
        GetDllLibDoc().Document_get_HtmlBaseUrl.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HtmlBaseUrl.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Document_get_HtmlBaseUrl,self.Ptr))
        return ret


    @HtmlBaseUrl.setter
    def HtmlBaseUrl(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Document_set_HtmlBaseUrl.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Document_set_HtmlBaseUrl,self.Ptr, valuePtr)

    @property
    def HTMLTrackChanges(self)->bool:
        """
        Gets or sets a value specifying whether parsing and writing custom Change_Tracking HTML Tags are supported.
        Supported HTML Tag : insert / delete.
        Supported HTML Tag Attribytes : data-username / data-time.
        """
        GetDllLibDoc().Document_get_HTMLTrackChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HTMLTrackChanges.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_HTMLTrackChanges,self.Ptr)
        return ret

    @HTMLTrackChanges.setter
    def HTMLTrackChanges(self, value:bool):
        GetDllLibDoc().Document_set_HTMLTrackChanges.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_HTMLTrackChanges,self.Ptr, value)

    @property
    def HTMLSentenceIdentifier(self)->bool:
        """
        Gets or sets a value specifying whether to add identifier to a sentence when writing to HTML.
        Writed HTML Attribyte : sentence.
        Writed HTML Value Of Attribyte : start / end / (start,end).
        """
        GetDllLibDoc().Document_get_HTMLSentenceIdentifier.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HTMLSentenceIdentifier.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_HTMLSentenceIdentifier,self.Ptr)
        return ret

    @HTMLSentenceIdentifier.setter
    def HTMLSentenceIdentifier(self, value:bool):
        GetDllLibDoc().Document_set_HTMLSentenceIdentifier.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_HTMLSentenceIdentifier,self.Ptr, value)

    @property
    def HTMLCustomComment(self)->bool:
        """
        Gets or sets a value specifying whether parsing and writing comment of document in HTML.
        Supported HTML Tag : span ,when the value of class attribute is comment
        Supported HTML Tag Attribytes : data-comment / data-user / data-cid / data-date.
        """
        GetDllLibDoc().Document_get_HTMLCustomComment.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HTMLCustomComment.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_HTMLCustomComment,self.Ptr)
        return ret

    @HTMLCustomComment.setter
    def HTMLCustomComment(self, value:bool):
        GetDllLibDoc().Document_set_HTMLCustomComment.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_HTMLCustomComment,self.Ptr, value)

#    @property
#
#    def HTMLIdentifierPunctuations(self)->'List1':
#        """
#    <summary>
#        Set the custom punctuation as sentence indentifier.
#            Full stop, qusetion mark, exclamatory mark are default values.
#    </summary>
#        """
#        GetDllLibDoc().Document_get_HTMLIdentifierPunctuations.argtypes=[c_void_p]
#        GetDllLibDoc().Document_get_HTMLIdentifierPunctuations.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_get_HTMLIdentifierPunctuations(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


#    @HTMLIdentifierPunctuations.setter
#    def HTMLIdentifierPunctuations(self, value:'List1'):
#        GetDllLibDoc().Document_set_HTMLIdentifierPunctuations.argtypes=[c_void_p, c_void_p]
#        GetDllLibDoc().Document_set_HTMLIdentifierPunctuations(self.Ptr, value.Ptr)


#    @property
#
#    def Footnotes(self)->'List1':
#        """
#    <summary>
#        Gets document footnotes.
#    </summary>
#        """
#        GetDllLibDoc().Document_get_Footnotes.argtypes=[c_void_p]
#        GetDllLibDoc().Document_get_Footnotes.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_get_Footnotes(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


#    @property
#
#    def Endnotes(self)->'List1':
#        """
#    <summary>
#        Gets document endnotes.
#    </summary>
#        """
#        GetDllLibDoc().Document_get_Endnotes.argtypes=[c_void_p]
#        GetDllLibDoc().Document_get_Endnotes.restype=c_void_p
#        intPtr = GetDllLibDoc().Document_get_Endnotes(self.Ptr)
#        ret = None if intPtr==None else List1(intPtr)
#        return ret
#


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().Document_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def BuiltinDocumentProperties(self)->'BuiltinDocumentProperties':
        """
        Gets document built-in properties object.
        """
        GetDllLibDoc().Document_get_BuiltinDocumentProperties.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_BuiltinDocumentProperties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_BuiltinDocumentProperties,self.Ptr)
        ret = None if intPtr==None else BuiltinDocumentProperties(intPtr)
        return ret


    @property

    def CustomDocumentProperties(self)->'CustomDocumentProperties':
        """
        Gets document custom properties object.
        """
        GetDllLibDoc().Document_get_CustomDocumentProperties.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_CustomDocumentProperties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_CustomDocumentProperties,self.Ptr)
        ret = None if intPtr==None else CustomDocumentProperties(intPtr)
        return ret


    @property

    def Sections(self)->SectionCollection:
        """
        Gets document sections.
        """
        GetDllLibDoc().Document_get_Sections.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Sections.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Sections,self.Ptr)
        ret = None if intPtr==None else SectionCollection(intPtr)
        return ret


    @property

    def Styles(self)->'StyleCollection':
        """
        Gets document styles.
        """
        GetDllLibDoc().Document_get_Styles.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Styles.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Styles,self.Ptr)
        from spire.doc import StyleCollection
        ret = None if intPtr==None else StyleCollection(intPtr)
        return ret


    @property

    def ListStyles(self)->'ListStyleCollection':
        """
        Gets document list styles.
        """
        GetDllLibDoc().Document_get_ListStyles.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ListStyles.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_ListStyles,self.Ptr)
        from spire.doc import ListStyleCollection
        ret = None if intPtr==None else ListStyleCollection(intPtr)
        return ret


    @property

    def Bookmarks(self)->'BookmarkCollection':
        """
        Gets document bookmarks.
        """
        GetDllLibDoc().Document_get_Bookmarks.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Bookmarks.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Bookmarks,self.Ptr)
        ret = None if intPtr==None else BookmarkCollection(intPtr)
        return ret


    @property

    def Fields(self)->'FieldCollection':
        """
        Gets fields of the documnet.
        """
        GetDllLibDoc().Document_get_Fields.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Fields.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Fields,self.Ptr)
        from spire.doc import FieldCollection
        ret = None if intPtr==None else FieldCollection(intPtr)
        return ret


    @property

    def Comments(self)->'CommentsCollection':
        """
        Gets comments item of the document.
        """
        GetDllLibDoc().Document_get_Comments.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Comments.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Comments,self.Ptr)
        ret = None if intPtr==None else CommentsCollection(intPtr)
        return ret


    @property

    def TextBoxes(self)->'TextBoxCollection':
        """
        Get/set textbox items of main document
        """
        GetDllLibDoc().Document_get_TextBoxes.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_TextBoxes.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_TextBoxes,self.Ptr)
        from spire.doc import TextBoxCollection
        ret = None if intPtr==None else TextBoxCollection(intPtr)
        return ret


    @TextBoxes.setter
    def TextBoxes(self, value:'TextBoxCollection'):
        GetDllLibDoc().Document_set_TextBoxes.argtypes=[c_void_p, c_void_p]
        CallCFunction(GetDllLibDoc().Document_set_TextBoxes,self.Ptr, value.Ptr)

    @property

    def LastSection(self)->'Section':
        """
        Gets last section of the document.
        """
        GetDllLibDoc().Document_get_LastSection.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_LastSection.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_LastSection,self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret


    @property

    def LastParagraph(self)->'Paragraph':
        """
        Gets last section object.
        """
        GetDllLibDoc().Document_get_LastParagraph.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_LastParagraph.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_LastParagraph,self.Ptr)
        ret = None if intPtr==None else Paragraph(intPtr)
        return ret


    @property

    def EndnoteOptions(self)->'FootEndnoteOptions':
        """
        Gets or sets options that control numbering and positioning of endnotes in this document. 
        """
        GetDllLibDoc().Document_get_EndnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_EndnoteOptions.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_EndnoteOptions,self.Ptr)
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def FootnoteOptions(self)->'FootEndnoteOptions':
        """
         Gets or sets options that control numbering and positioning of footnotes in this document. 
        """
        GetDllLibDoc().Document_get_FootnoteOptions.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_FootnoteOptions.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_FootnoteOptions,self.Ptr)
        ret = None if intPtr==None else FootEndnoteOptions(intPtr)
        return ret


    @property

    def Watermark(self)->'WatermarkBase':
        """
        Gets or sets document's watermark.
        """
        GetDllLibDoc().Document_get_Watermark.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Watermark.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Watermark,self.Ptr)
        ret = None if intPtr==None else WatermarkBase(intPtr)
        return ret


    @Watermark.setter
    def Watermark(self, value:'WatermarkBase'):
        GetDllLibDoc().Document_set_Watermark.argtypes=[c_void_p, c_void_p]
        if value == None:
            CallCFunction(GetDllLibDoc().Document_set_Watermark,self.Ptr, None)
        else: 
            CallCFunction(GetDllLibDoc().Document_set_Watermark,self.Ptr, value.Ptr)

    @property

    def Background(self)->'Background':
        """
        Gets document's background
        """
        GetDllLibDoc().Document_get_Background.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Background.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Background,self.Ptr)
        ret = None if intPtr==None else Background(intPtr)
        return ret


    @property

    def MailMerge(self)->'MailMerge':
        """
        Gets mail merge engine.
        """
        GetDllLibDoc().Document_get_MailMerge.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_MailMerge.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_MailMerge,self.Ptr)
        ret = None if intPtr==None else MailMerge(intPtr)
        return ret



    def GetProtectionType(self)->'ProtectionType':
        """
        Gets or sets the type of protection of the document.
        """
        GetDllLibDoc().Document_get_ProtectionType.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ProtectionType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_get_ProtectionType,self.Ptr)
        objwraped = ProtectionType(ret)
        return objwraped

    def SetProtectionType(self, value:'ProtectionType'):
        GetDllLibDoc().Document_set_ProtectionType.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Document_set_ProtectionType,self.Ptr, value.value)

    @property

    def ViewSetup(self)->'ViewSetup':
        """
        Gets view setup options in Microsoft word.
        """
        GetDllLibDoc().Document_get_ViewSetup.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ViewSetup.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_ViewSetup,self.Ptr)
        from spire.doc import ViewSetup
        ret = None if intPtr==None else ViewSetup(intPtr)
        return ret


    @property
    def QuiteMode(self)->bool:
        """
        Get or sets whether is quite mode.
        """
        GetDllLibDoc().Document_get_QuiteMode.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_QuiteMode.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_QuiteMode,self.Ptr)
        return ret

    @QuiteMode.setter
    def QuiteMode(self, value:bool):
        GetDllLibDoc().Document_set_QuiteMode.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_QuiteMode,self.Ptr, value)

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child entities.
        """
        GetDllLibDoc().Document_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def XHTMLValidateOption(self)->'XHTMLValidationType':
        """
        Gets or sets the HTML validate option.the default value is None.
        """
        GetDllLibDoc().Document_get_XHTMLValidateOption.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_XHTMLValidateOption.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_get_XHTMLValidateOption,self.Ptr)
        objwraped = XHTMLValidationType(ret)
        return objwraped

    @XHTMLValidateOption.setter
    def XHTMLValidateOption(self, value:'XHTMLValidationType'):
        GetDllLibDoc().Document_set_XHTMLValidateOption.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Document_set_XHTMLValidateOption,self.Ptr, value.value)

    @property

    def Variables(self)->'VariableCollection':
        """
        Gets or sets the document variables.
        """
        GetDllLibDoc().Document_get_Variables.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Variables.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Variables,self.Ptr)
        from spire.doc import VariableCollection
        ret = None if intPtr==None else VariableCollection(intPtr)
        return ret


    @property

    def Properties(self)->'DocumentProperties':
        """
        Gets the document properties.
        """
        GetDllLibDoc().Document_get_Properties.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_Properties.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_Properties,self.Ptr)
        ret = None if intPtr==None else DocumentProperties(intPtr)
        return ret


    @property
    def HasChanges(self)->bool:
        """
        Gets a value indicating whether the document has tracked changes.
        if the document has tracked changes, set to true.
        """
        GetDllLibDoc().Document_get_HasChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HasChanges.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_HasChanges,self.Ptr)
        return ret

    @property
    def TrackChanges(self)->bool:
        """
        Gets or sets a value indicating whether tracking changes is turn on.
        if track changes in on, set to true.
        """
        GetDllLibDoc().Document_get_TrackChanges.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_TrackChanges.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_TrackChanges,self.Ptr)
        return ret

    @TrackChanges.setter
    def TrackChanges(self, value:bool):
        GetDllLibDoc().Document_set_TrackChanges.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_TrackChanges,self.Ptr, value)

    @property
    def AutoUpdateStylesByTemplate(self)->bool:
        """
        Gets or sets a value indicating whether updating the styles in this document to match
        the styles in the attached template each time you open .
        if update document styles automatically, set to true.
        """
        GetDllLibDoc().Document_get_AutoUpdateStylesByTemplate.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_AutoUpdateStylesByTemplate.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_AutoUpdateStylesByTemplate,self.Ptr)
        return ret

    @AutoUpdateStylesByTemplate.setter
    def AutoUpdateStylesByTemplate(self, value:bool):
        GetDllLibDoc().Document_set_AutoUpdateStylesByTemplate.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_AutoUpdateStylesByTemplate,self.Ptr, value)

    @property
    def ReplaceFirst(self)->bool:
        """
        Gets or sets a value indicating whether need first replacing.
        True indciates need first replacing.
        """
        GetDllLibDoc().Document_get_ReplaceFirst.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_ReplaceFirst.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_ReplaceFirst,self.Ptr)
        return ret

    @ReplaceFirst.setter
    def ReplaceFirst(self, value:bool):
        GetDllLibDoc().Document_set_ReplaceFirst.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_ReplaceFirst,self.Ptr, value)

    @property

    def HtmlExportOptions(self)->'HtmlExportOptions':
        """
        Gets the save options.
        The save options.
        """
        GetDllLibDoc().Document_get_HtmlExportOptions.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_HtmlExportOptions.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Document_get_HtmlExportOptions,self.Ptr)
        ret = None if intPtr==None else HtmlExportOptions(intPtr)
        return ret


    @property
    def IsUpdateFields(self)->bool:
        """
        Gets or sets a value indicating whether to update fields in the document.
        """
        GetDllLibDoc().Document_get_IsUpdateFields.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_IsUpdateFields.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Document_get_IsUpdateFields,self.Ptr)
        return ret

    @IsUpdateFields.setter
    def IsUpdateFields(self, value:bool):
        GetDllLibDoc().Document_set_IsUpdateFields.argtypes=[c_void_p, c_bool]
        CallCFunction(GetDllLibDoc().Document_set_IsUpdateFields,self.Ptr, value)

    @property

    def DetectedFormatType(self)->'FileFormat':
        """
        Returns the detected format type of the document which was loaded. .
        """
        GetDllLibDoc().Document_get_DetectedFormatType.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_DetectedFormatType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_get_DetectedFormatType,self.Ptr)
        objwraped = FileFormat(ret)
        return objwraped

    @property
    def JPEGQuality(self)->int:
        """
        Gets or sets the quality (Q%) of the image of JPEG format, this property
        is only used for doc to pdf. The default value is 80. 
        """
        GetDllLibDoc().Document_get_JPEGQuality.argtypes=[c_void_p]
        GetDllLibDoc().Document_get_JPEGQuality.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Document_get_JPEGQuality,self.Ptr)
        return ret

    @JPEGQuality.setter
    def JPEGQuality(self, value:int):
        GetDllLibDoc().Document_set_JPEGQuality.argtypes=[c_void_p, c_int]
        CallCFunction(GetDllLibDoc().Document_set_JPEGQuality,self.Ptr, value)

