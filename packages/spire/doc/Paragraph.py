from enum import Enum
from plum import dispatch
from typing import TypeVar, Union, Generic, List, Tuple
from spire.doc.common import *
from spire.doc import *
from ctypes import *
import abc

class Paragraph (  BodyRegion, IParagraph, IStyleHolder, ICompositeObject) :
    """
    Represents a paragraph in a document.
    """
    @dispatch
    def __init__(self, doc:IDocument):
        """
        Initializes a new instance of the Paragraph class.
        :param doc: The document to which the paragraph belongs.
        """
        intPdoc:c_void_p = doc.Ptr

        GetDllLibDoc().Paragraph_CreateParagraphD.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_CreateParagraphD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_CreateParagraphD,intPdoc)
        super(Paragraph, self).__init__(intPtr)


    @property

    def ParentSection(self)->'Section':
        """
        Gets the parent section of the paragraph.
        :return: The parent section of the paragraph.
        """
        GetDllLibDoc().Paragraph_get_ParentSection.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ParentSection.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_ParentSection,self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret


    @dispatch

    def Find(self ,pattern:Regex):
        """

        """
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Paragraph_Find.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_Find.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_Find,self.Ptr, intPtrpattern)
        from spire.doc import TextSelection
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret



    @dispatch

    def Find(self ,given:str,caseSensitive:bool,wholeWord:bool):
        """
        Finds the given text in the paragraph.
        :param given: The text to find.
        :param caseSensitive: Indicates whether the search is case sensitive.
        :param wholeWord: Indicates whether the search should match whole words only.
        :return: The text selection representing the found text.
        """
        givenPtr = StrToPtr(given)
        GetDllLibDoc().Paragraph_FindGCW.argtypes=[c_void_p ,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Paragraph_FindGCW.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_FindGCW,self.Ptr, givenPtr,caseSensitive,wholeWord) 
        from spire.doc import TextSelection
        ret = None if intPtr==None else TextSelection(intPtr)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,replace:str)->int:
        """

        """
        replacePtr = StrToPtr(replace)
        intPtrpattern:c_void_p = pattern.Ptr

        GetDllLibDoc().Paragraph_Replace.argtypes=[c_void_p ,c_void_p,c_char_p]
        GetDllLibDoc().Paragraph_Replace.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_Replace,self.Ptr, intPtrpattern,replacePtr)
        return ret


    @dispatch

    def Replace(self ,given:str,replace:str,caseSensitive:bool,wholeWord:bool)->int:
        """
        Replaces the given text with the specified replacement text in the paragraph.
        :param given: The text to replace.
        :param replace: The replacement text.
        :param caseSensitive: Indicates whether the replacement is case sensitive.
        :param wholeWord: Indicates whether the replacement should match whole words only.
        :return: The number of replacements made.
        """
        givenPtr = StrToPtr(given)
        replacePtr = StrToPtr(replace)
        GetDllLibDoc().Paragraph_ReplaceGRCW.argtypes=[c_void_p ,c_char_p,c_char_p,c_bool,c_bool]
        GetDllLibDoc().Paragraph_ReplaceGRCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_ReplaceGRCW,self.Ptr, givenPtr,replacePtr,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,pattern:Regex,textSelection:TextSelection)->int:
        """

        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplacePT.argtypes=[c_void_p ,c_void_p,c_void_p]
        GetDllLibDoc().Paragraph_ReplacePT.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_ReplacePT,self.Ptr, intPtrpattern,intPtrtextSelection)
        return ret


    @dispatch

    def Replace(self ,pattern:Regex,textSelection:TextSelection,saveFormatting:bool)->int:
        """
        Replaces the text in the specified text selection with the specified pattern in the paragraph.
        :param pattern: The regular expression pattern to replace.
        :param textSelection: The text selection representing the text to replace.
        :param saveFormatting: Indicates whether to save the formatting of the replaced text.
        :return: The number of replacements made.
        """
        intPtrpattern:c_void_p = pattern.Ptr
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplacePTS.argtypes=[c_void_p ,c_void_p,c_void_p,c_bool]
        GetDllLibDoc().Paragraph_ReplacePTS.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_ReplacePTS,self.Ptr, intPtrpattern,intPtrtextSelection,saveFormatting)
        return ret


    @dispatch

    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool)->int:
        """

        """
        givenPtr = StrToPtr(given)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplaceGTCW.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool]
        GetDllLibDoc().Paragraph_ReplaceGTCW.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_ReplaceGTCW,self.Ptr, givenPtr,intPtrtextSelection,caseSensitive,wholeWord)
        return ret

    @dispatch

    def Replace(self ,given:str,textSelection:TextSelection,caseSensitive:bool,wholeWord:bool,saveFormatting:bool)->int:
        """

        """
        givenPtr = StrToPtr(given)
        intPtrtextSelection:c_void_p = textSelection.Ptr

        GetDllLibDoc().Paragraph_ReplaceGTCWS.argtypes=[c_void_p ,c_char_p,c_void_p,c_bool,c_bool,c_bool]
        GetDllLibDoc().Paragraph_ReplaceGTCWS.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_ReplaceGTCWS,self.Ptr, givenPtr,intPtrtextSelection,caseSensitive,wholeWord,saveFormatting)
        return ret

    @dispatch

    def InsertSectionBreak(self)->'Section':
        """
        Inserts the section break.
        """
        GetDllLibDoc().Paragraph_InsertSectionBreak.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_InsertSectionBreak.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_InsertSectionBreak,self.Ptr)
        ret = None if intPtr==None else Section(intPtr)
        return ret


    @dispatch

    def InsertSectionBreak(self ,breakType:SectionBreakType)->'Section':
        """
    <summary>
        Inserts the section break.
    </summary>
    <param name="breakType">Type of the break.</param>
        """
        enumbreakType:c_int = breakType.value

        GetDllLibDoc().Paragraph_InsertSectionBreakB.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_InsertSectionBreakB.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_InsertSectionBreakB,self.Ptr, enumbreakType)
        from spire.doc import Section
        ret = None if intPtr==None else Section(intPtr)
        return ret


#
#    def UpdateWordCount(self ,splitchar:'Char[]',includeTbFnEn:bool):
#        """
#
#        """
#        #arraysplitchar:ArrayTypesplitchar = ""
#        countsplitchar = len(splitchar)
#        ArrayTypesplitchar = c_void_p * countsplitchar
#        arraysplitchar = ArrayTypesplitchar()
#        for i in range(0, countsplitchar):
#            arraysplitchar[i] = splitchar[i].Ptr
#
#
#        GetDllLibDoc().Paragraph_UpdateWordCount.argtypes=[c_void_p ,ArrayTypesplitchar,c_bool]
#        GetDllLibDoc().Paragraph_UpdateWordCount(self.Ptr, arraysplitchar,includeTbFnEn)



    def UpdateListValue(self)->str:
        """
        Updates the list value.

        The value of the list number is obtained by dynamic calculation. 
        The value of the list number of the paragraph directly may be incorrect.
        To obtain the correct value, you need to traverse all paragraphs in the document.

        Returns:
            The value string.
        """
        GetDllLibDoc().Paragraph_UpdateListValue.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_UpdateListValue.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Paragraph_UpdateListValue,self.Ptr))
        return ret



    def GetListFormatForApplyStyle(self)->'ListFormat':
        """
        Gets the list format for apply style.

        Returns:
            The list format.
        """
        GetDllLibDoc().Paragraph_GetListFormatForApplyStyle.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_GetListFormatForApplyStyle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_GetListFormatForApplyStyle,self.Ptr)
        ret = None if intPtr==None else ListFormat(intPtr)
        return ret



    def GetIndex(self ,entity:'IDocumentObject')->int:
        """
        Gets the index.

        Args:
            entity: The document object.

        Returns:
            The index.
        """
        intPtrentity:c_void_p = entity.Ptr

        GetDllLibDoc().Paragraph_GetIndex.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_GetIndex.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_GetIndex,self.Ptr, intPtrentity)
        return ret

    @property

    def ListText(self)->str:
        """
        Gets the list text.

        The value of the list number is obtained by dynamic calculation. 
        The value of the list number of the paragraph directly may be incorrect.
        To obtain the correct value, you need to traverse all paragraphs in the document.
        """
        GetDllLibDoc().Paragraph_get_ListText.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ListText.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Paragraph_get_ListText,self.Ptr))
        return ret


    @property

    def DocumentObjectType(self)->'DocumentObjectType':
        """
        Gets the type of the document object.
        """
        GetDllLibDoc().Paragraph_get_DocumentObjectType.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_DocumentObjectType.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_DocumentObjectType,self.Ptr)
        objwraped = DocumentObjectType(ret)
        return objwraped

    @property

    def ChildObjects(self)->'DocumentObjectCollection':
        """
        Gets the child objects.

        Returns:
            The child objects.
        """
        GetDllLibDoc().Paragraph_get_ChildObjects.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ChildObjects.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_ChildObjects,self.Ptr)
        ret = None if intPtr==None else DocumentObjectCollection(intPtr)
        return ret


    @property

    def StyleName(self)->str:
        """
        Gets paragraph style name.

        Returns:
            The style name.
        """
        GetDllLibDoc().Paragraph_get_StyleName.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_StyleName.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Paragraph_get_StyleName,self.Ptr))
        return ret


    @property

    def Text(self)->str:
        """
        Gets paragraph text.

        Returns:
            The paragraph text.

        Remarks:
            All internal formatting will be cleared when new text is set.
        """
        GetDllLibDoc().Paragraph_get_Text.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_Text.restype=c_void_p
        ret = PtrToStr(CallCFunction(GetDllLibDoc().Paragraph_get_Text,self.Ptr))
        return ret


    @Text.setter
    def Text(self, value:str):
        valuePtr = StrToPtr(value)
        GetDllLibDoc().Paragraph_set_Text.argtypes=[c_void_p, c_char_p]
        CallCFunction(GetDllLibDoc().Paragraph_set_Text,self.Ptr, valuePtr)


    def get_Item(self ,index:int)->'ParagraphBase':
        """
        Gets paragraph item by index.

        Args:
            index: The index.

        Returns:
            The paragraph item.
        """
        
        GetDllLibDoc().Paragraph_get_Item.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_get_Item.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_Item,self.Ptr, index)
        ret = None if intPtr==None else ParagraphBase(intPtr)
        return ret


    @property

    def Items(self)->'ParagraphItemCollection':
        """
        Gets paragraph items.

        Returns:
            The items.
        """
        GetDllLibDoc().Paragraph_get_Items.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_Items.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_Items,self.Ptr)
        ret = None if intPtr==None else ParagraphItemCollection(intPtr)
        return ret


    @property

    def Format(self)->'ParagraphFormat':
        """
        Gets paragraph format.

        Returns:
            The paragraph format.
        """
        GetDllLibDoc().Paragraph_get_Format.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_Format.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_Format,self.Ptr)
        from spire.doc import ParagraphFormat
        ret = None if intPtr==None else ParagraphFormat(intPtr)
        return ret


    @property

    def BreakCharacterFormat(self)->'CharacterFormat':
        """
        Gets character format for the break symbol.

        Returns:
            The character format.
        """
        GetDllLibDoc().Paragraph_get_BreakCharacterFormat.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_BreakCharacterFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_BreakCharacterFormat,self.Ptr)
        ret = None if intPtr==None else CharacterFormat(intPtr)
        return ret


    @property

    def ListFormat(self)->'ListFormat':
        """
        Gets format of the list for the paragraph.

        Returns:
            The list format.
        """
        GetDllLibDoc().Paragraph_get_ListFormat.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_ListFormat.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_get_ListFormat,self.Ptr)
        from spire.doc import ListFormat
        ret = None if intPtr==None else ListFormat(intPtr)
        return ret


    @property
    def IsInCell(self)->bool:
        """
        Gets a value indicating whether this paragraph is in cell.
    
        Returns:
            bool: If this paragraph is in cell, set to True.
        """
        GetDllLibDoc().Paragraph_get_IsInCell.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsInCell.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_IsInCell,self.Ptr)
        return ret

    @property
    def IsEndOfSection(self)->bool:
        """
        Gets a value indicating whether this paragraph is end of section.
    
        Returns:
            bool: If this paragraph is end of section, set to True.
        """
        GetDllLibDoc().Paragraph_get_IsEndOfSection.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsEndOfSection.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_IsEndOfSection,self.Ptr)
        return ret

    @property
    def IsEndOfHeaderFooter(self)->bool:
        """
        Gets a value indicating whether this paragraph is end of header/footer.
    
        Returns:
            bool: If this paragraph is end of header/footer, set to True.
        """
        GetDllLibDoc().Paragraph_get_IsEndOfHeaderFooter.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsEndOfHeaderFooter.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_IsEndOfHeaderFooter,self.Ptr)
        return ret

    @property
    def IsEndOfDocument(self)->bool:
        """
        Gets a value indicating whether this paragraph is end of document.
    
        Returns:
            bool: If this paragraph is end of document, set to True.
        """
        GetDllLibDoc().Paragraph_get_IsEndOfDocument.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_IsEndOfDocument.restype=c_bool
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_IsEndOfDocument,self.Ptr)
        return ret

    @property
    def WordCount(self)->int:
        """
        Gets the word count of this paragraph.
    
        Returns:
            int: The word count of this paragraph.
        """
        GetDllLibDoc().Paragraph_get_WordCount.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_WordCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_WordCount,self.Ptr)
        return ret

    @property
    def CharCount(self)->int:
        """
        Gets the character count of this paragraph.
    
        Returns:
            int: The character count of this paragraph.
        """
        GetDllLibDoc().Paragraph_get_CharCount.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_CharCount.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_CharCount,self.Ptr)
        return ret

    @property
    def CharCountIncludeSpace(self)->int:
        """
        Gets the character count including spaces of this paragraph.
    
        Returns:
            int: The character count including spaces of this paragraph.
        """
        GetDllLibDoc().Paragraph_get_CharCountIncludeSpace.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_get_CharCountIncludeSpace.restype=c_int
        ret = CallCFunction(GetDllLibDoc().Paragraph_get_CharCountIncludeSpace,self.Ptr)
        return ret

    @dispatch

    def ApplyStyle(self ,styleName:str):
        """
        Applies the specified style to this paragraph.
    
        Args:
            styleName (str): The name of the style to apply.
        """
        styleNamePtr = StrToPtr(styleName)
        GetDllLibDoc().Paragraph_ApplyStyle.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Paragraph_ApplyStyle,self.Ptr, styleNamePtr)

    @dispatch

    def ApplyStyle(self ,builtinStyle:BuiltinStyle):
        """
        Applies the specified built-in style to this paragraph.
    
        Args:
            builtinStyle (BuiltinStyle): The built-in style to apply.
        """
        enumbuiltinStyle:c_int = builtinStyle.value

        GetDllLibDoc().Paragraph_ApplyStyleB.argtypes=[c_void_p ,c_int]
        CallCFunction(GetDllLibDoc().Paragraph_ApplyStyleB,self.Ptr, enumbuiltinStyle)

    @dispatch

    def ApplyStyle(self ,style:IParagraphStyle):
        """
        Applies the specified paragraph style to this paragraph.
    
        Args:
            style (IParagraphStyle): The paragraph style to apply.
        """
        intPtrstyle:c_void_p = style.Ptr

        GetDllLibDoc().Paragraph_ApplyStyleS.argtypes=[c_void_p ,c_void_p]
        CallCFunction(GetDllLibDoc().Paragraph_ApplyStyleS,self.Ptr, intPtrstyle)


    def GetStyle(self)->'ParagraphStyle':
        """
        Gets the style of this paragraph.
    
        Returns:
            ParagraphStyle: The style of this paragraph.
        """
        GetDllLibDoc().Paragraph_GetStyle.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_GetStyle.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_GetStyle,self.Ptr)
        ret = None if intPtr==None else ParagraphStyle(intPtr)
        return ret


    def RemoveAbsPosition(self):
        """
        Removes the absolute position of this paragraph.
        """
        GetDllLibDoc().Paragraph_RemoveAbsPosition.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Paragraph_RemoveAbsPosition,self.Ptr)


    def AppendText(self ,text:str)->'TextRange':
        """
        Appends text to the end of this paragraph.
    
        Args:
            text (str): The text to append.
    
        Returns:
            TextRange: The appended text range.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().Paragraph_AppendText.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendText.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendText,self.Ptr, textPtr)
        from spire.doc import TextRange
        ret = None if intPtr==None else TextRange(intPtr)
        return ret


#    @dispatch
#
#    def AppendPicture(self ,imageBytes:'Byte[]')->DocPicture:
#        """
#    <summary>
#        Appends image to end of paragraph.
#    </summary>
#    <returns></returns>
#        """
#        #arrayimageBytes:ArrayTypeimageBytes = ""
#        countimageBytes = len(imageBytes)
#        ArrayTypeimageBytes = c_void_p * countimageBytes
#        arrayimageBytes = ArrayTypeimageBytes()
#        for i in range(0, countimageBytes):
#            arrayimageBytes[i] = imageBytes[i].Ptr
#
#
#        GetDllLibDoc().Paragraph_AppendPicture.argtypes=[c_void_p ,ArrayTypeimageBytes]
#        GetDllLibDoc().Paragraph_AppendPicture.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendPicture(self.Ptr, arrayimageBytes)
#        ret = None if intPtr==None else DocPicture(intPtr)
#        return ret
#



    def AppendField(self ,fieldName:str,fieldType:FieldType)->'Field':
        """
        Appends a field to this paragraph.
    
        Args:
            fieldName (str): The name of the field.
            fieldType (FieldType): The type of the field.
    
        Returns:
            Field: The appended field.
        """
        fieldNamePtr = StrToPtr(fieldName)
        enumfieldType:c_int = fieldType.value

        GetDllLibDoc().Paragraph_AppendField.argtypes=[c_void_p ,c_char_p,c_int]
        GetDllLibDoc().Paragraph_AppendField.restype=IntPtrWithTypeName
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendField,self.Ptr, fieldNamePtr, enumfieldType)
        ret = None if intPtr==None else self._create(intPtr)
        return ret

    def _create(self, intPtrWithTypeName:IntPtrWithTypeName)->'Field':
        ret= None
        if intPtrWithTypeName == None:
            return ret
        intPtr = intPtrWithTypeName.intPtr[0] + (intPtrWithTypeName.intPtr[1]<<32)
        strName = PtrToStr(intPtrWithTypeName.typeName)
        if (strName == "Spire.Doc.Fields.CheckBoxFormField"):
            from spire.doc import CheckBoxFormField
            ret = CheckBoxFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.DropDownFormField"):
            from spire.doc import DropDownFormField
            ret = DropDownFormField(intPtr)
        elif (strName == "Spire.Doc.Fields.ControlField"):
            from spire.doc import ControlField
            ret = ControlField(intPtr)
        elif (strName == "Spire.Doc.Fields.FormField"):
            from spire.doc import FormField
            ret = FormField(intPtr)
        elif (strName == "Spire.Doc.Fields.IfField"):
            from spire.doc import IfField
            ret = IfField(intPtr)
        elif (strName == "Spire.Doc.Fields.MergeField"):
            from spire.doc import MergeField
            ret = MergeField(intPtr)
        elif (strName == "Spire.Doc.Fields.SequenceField"):
            from spire.doc import SequenceField
            ret = SequenceField(intPtr)
        elif (strName == "Spire.Doc.Fields.TextFormField"):
            from spire.doc import TextFormField
            ret = TextFormField(intPtr)
        else:
            from spire.doc import Field
            ret = Field(intPtr)
			
        return ret

    def AppendFieldMark(self ,type:FieldMarkType)->'FieldMark':
        """
        Appends a field mark to the paragraph.

        Args:
            type: The type of the field mark.

        Returns:
            A FieldMark object.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendFieldMark.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendFieldMark.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendFieldMark,self.Ptr, enumtype)
        from spire.doc import FieldMark
        ret = None if intPtr==None else FieldMark(intPtr)
        return ret


    @dispatch

    def AppendHyperlink(self ,link:str,text:str,type:HyperlinkType)->Field:
        """
        Appends a hyperlink to the paragraph.

        Args:
            link: The link URL.
            text: The text to display.
            type: The type of the hyperlink.

        Returns:
            A Field object.
        """
        linkPtr = StrToPtr(link)
        textPtr = StrToPtr(text)
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendHyperlink.argtypes=[c_void_p ,c_char_p,c_char_p,c_int]
        GetDllLibDoc().Paragraph_AppendHyperlink.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendHyperlink,self.Ptr, linkPtr,textPtr,enumtype)
        ret = None if intPtr==None else Field(intPtr)
        return ret


    @dispatch

    def AppendHyperlink(self ,link:str,picture:DocPicture,type:HyperlinkType)->Field:
        """
        Appends a hyperlink with a picture to the paragraph.

        Args:
            link: The link URL.
            picture: The picture to display.
            type: The type of the hyperlink.

        Returns:
            A Field object.
        """
        linkPtr = StrToPtr(link)
        intPtrpicture:c_void_p = picture.Ptr
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendHyperlinkLPT.argtypes=[c_void_p ,c_char_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendHyperlinkLPT.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendHyperlinkLPT,self.Ptr, linkPtr,intPtrpicture,enumtype)
        ret = None if intPtr==None else Field(intPtr)
        return ret



    def AppendBookmarkStart(self ,name:str)->'BookmarkStart':
        """
        Appends the start of a bookmark with the specified name to the paragraph.

        Args:
            name: The name of the bookmark.

        Returns:
            A BookmarkStart object.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().Paragraph_AppendBookmarkStart.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendBookmarkStart.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendBookmarkStart,self.Ptr, namePtr)
        ret = None if intPtr==None else BookmarkStart(intPtr)
        return ret



    def AppendBookmarkEnd(self ,name:str)->'BookmarkEnd':
        """
        Appends the end of a bookmark with the specified name to the paragraph.

        Args:
            name: The name of the bookmark.

        Returns:
            A BookmarkEnd object.
        """
        namePtr = StrToPtr(name)
        GetDllLibDoc().Paragraph_AppendBookmarkEnd.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendBookmarkEnd.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendBookmarkEnd,self.Ptr, namePtr)
        ret = None if intPtr==None else BookmarkEnd(intPtr)
        return ret



    def AppendPermStart(self ,id:str)->'PermissionStart':
        """
        Appends the start of a permission with the specified id to the paragraph.

        Args:
            id: The id of the permission.

        Returns:
            A PermissionStart object.
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().Paragraph_AppendPermStart.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendPermStart.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendPermStart,self.Ptr, idPtr)
        ret = None if intPtr==None else PermissionStart(intPtr)
        return ret



    def AppendPermEnd(self ,id:str)->'PermissionEnd':
        """
        Appends the end of a permission with the specified id to the paragraph.

        Args:
            id: The id of the permission.

        Returns:
            A PermissionEnd object.
        """
        idPtr = StrToPtr(id)
        GetDllLibDoc().Paragraph_AppendPermEnd.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendPermEnd.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendPermEnd,self.Ptr, idPtr)
        ret = None if intPtr==None else PermissionEnd(intPtr)
        return ret



    def AppendComment(self ,text:str)->'Comment':
        """
        Appends a comment to the paragraph.

        Args:
            text: The comment text.

        Returns:
            A Comment object.
        """
        textPtr = StrToPtr(text)
        GetDllLibDoc().Paragraph_AppendComment.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendComment.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendComment,self.Ptr, textPtr)
        from spire.doc import Comment
        ret = None if intPtr==None else Comment(intPtr)
        return ret



    def AppendCommentMark(self ,type:'CommentMarkType')->'CommentMark':
        """
        Appends a comment mark to the paragraph.

        Args:
            type: The type of the comment mark.

        Returns:
            A CommentMark object.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendCommentMark.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendCommentMark.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendCommentMark,self.Ptr, enumtype)
        ret = None if intPtr==None else CommentMark(intPtr)
        return ret


    @dispatch

    def AppendFootnote(self ,type:FootnoteType)->Footnote:
        """
        Appends a footnote to the paragraph.

        Args:
            type (FootnoteType): The type of the footnote.

        Returns:
            Footnote: The appended footnote.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendFootnote.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendFootnote.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendFootnote,self.Ptr, enumtype)
        ret = None if intPtr==None else Footnote(intPtr)
        return ret


    @dispatch

    def AppendFootnote(self ,type:FootnoteType,bIsAutoNumbered:bool)->Footnote:
        """
        Appends a footnote to the paragraph.

        Args:
            type (FootnoteType): The type of the footnote.
            bIsAutoNumbered (bool): Whether the footnote is auto-numbered.

        Returns:
            Footnote: The appended footnote.
        """
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendFootnoteTB.argtypes=[c_void_p ,c_int,c_bool]
        GetDllLibDoc().Paragraph_AppendFootnoteTB.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendFootnoteTB,self.Ptr, enumtype,bIsAutoNumbered)
        ret = None if intPtr==None else Footnote(intPtr)
        return ret



    def AppendTextBox(self ,width:float,height:float)->'TextBox':
        """
        Appends a textbox to the end of the paragraph.

        Args:
            width (float): The width of the textbox.
            height (float): The height of the textbox.

        Returns:
            TextBox: The appended textbox.
        """
        
        GetDllLibDoc().Paragraph_AppendTextBox.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().Paragraph_AppendTextBox.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendTextBox,self.Ptr, width,height)
        from spire.doc import TextBox
        ret = None if intPtr==None else TextBox(intPtr)
        return ret


    @dispatch

    def AppendCheckBox(self)->'CheckBoxFormField':
        """
        Appends a checkbox form field to the paragraph.

        Returns:
            CheckBoxFormField: The appended checkbox form field.
        """
        GetDllLibDoc().Paragraph_AppendCheckBox.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_AppendCheckBox.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendCheckBox,self.Ptr)
        ret = None if intPtr==None else CheckBoxFormField(intPtr)
        return ret


    @dispatch

    def AppendCheckBox(self ,checkBoxName:str,defaultCheckBoxValue:bool)->'CheckBoxFormField':
        """
        Appends a checkbox form field to the paragraph.

        Args:
            checkBoxName (str): The name of the checkbox.
            defaultCheckBoxValue (bool): The default value of the checkbox.

        Returns:
            CheckBoxFormField: The appended checkbox form field.
        """
        checkBoxNamePtr = StrToPtr(checkBoxName)
        GetDllLibDoc().Paragraph_AppendCheckBoxCD.argtypes=[c_void_p ,c_char_p,c_bool]
        GetDllLibDoc().Paragraph_AppendCheckBoxCD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendCheckBoxCD,self.Ptr, checkBoxNamePtr,defaultCheckBoxValue)
        ret = None if intPtr==None else CheckBoxFormField(intPtr)
        return ret


    @dispatch

    def AppendTextFormField(self ,defaultText:str)->'TextFormField':
        """
        Appends a text form field to the paragraph.

        Args:
            defaultText (str): The default text. Pass "null" to insert default Word text.

        Returns:
            TextFormField: The appended text form field.
        """
        defaultTextPtr = StrToPtr(defaultText)
        GetDllLibDoc().Paragraph_AppendTextFormField.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendTextFormField.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendTextFormField,self.Ptr, defaultTextPtr)
        ret = None if intPtr==None else TextFormField(intPtr)
        return ret


    @dispatch

    def AppendTextFormField(self ,formFieldName:str,defaultText:str)->'TextFormField':
        """
        Appends a text form field to the paragraph.

        Args:
            formFieldName (str): The name of the form field.
            defaultText (str): The default text. Pass "null" to insert default Word text.

        Returns:
            TextFormField: The appended text form field.
        """
        formFieldNamePtr = StrToPtr(formFieldName)
        defaultTextPtr = StrToPtr(defaultText)
        GetDllLibDoc().Paragraph_AppendTextFormFieldFD.argtypes=[c_void_p ,c_char_p,c_char_p]
        GetDllLibDoc().Paragraph_AppendTextFormFieldFD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendTextFormFieldFD,self.Ptr, formFieldNamePtr,defaultTextPtr)
        ret = None if intPtr==None else TextFormField(intPtr)
        return ret


    @dispatch

    def AppendDropDownFormField(self)->'DropDownFormField':
        """
        Appends a dropdown form field to the paragraph.

        Returns:
            DropDownFormField: The appended dropdown form field.
        """
        GetDllLibDoc().Paragraph_AppendDropDownFormField.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_AppendDropDownFormField.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendDropDownFormField,self.Ptr)
        ret = None if intPtr==None else DropDownFormField(intPtr)
        return ret


    @dispatch

    def AppendDropDownFormField(self ,dropDropDownName:str)->'DropDownFormField':
        """
        Appends a dropdown form field to the paragraph.

        Args:
            dropDropDownName (str): The name of the dropdown.

        Returns:
            DropDownFormField: The appended dropdown form field.
        """
        dropDropDownNamePtr = StrToPtr(dropDropDownName)
        GetDllLibDoc().Paragraph_AppendDropDownFormFieldD.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendDropDownFormFieldD.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendDropDownFormFieldD,self.Ptr, dropDropDownNamePtr)
        ret = None if intPtr==None else DropDownFormField(intPtr)
        return ret



    def AppendSymbol(self ,characterCode:int)->'Symbol':
        """
        Appends a special symbol to the end of the paragraph.

        Args:
            characterCode (int): The character code.

        Returns:
            Symbol: The appended symbol.
        """
        
        GetDllLibDoc().Paragraph_AppendSymbol.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_AppendSymbol.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendSymbol,self.Ptr, characterCode)
        ret = None if intPtr==None else Symbol(intPtr)
        return ret



    def AppendShape(self ,width:float,height:float,shapeType:'ShapeType')->'ShapeObject':
        """
        Appends a shape to the end of the paragraph.

        Args:
            width (float): The width of the shape.
            height (float): The height of the shape.
            shapeType (ShapeType): The type of the shape.

        Returns:
            ShapeObject: The appended shape.
        """
        enumshapeType:c_int = shapeType.value

        GetDllLibDoc().Paragraph_AppendShape.argtypes=[c_void_p ,c_float,c_float,c_int]
        GetDllLibDoc().Paragraph_AppendShape.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendShape,self.Ptr, width,height,enumshapeType)
        ret = None if intPtr==None else ShapeObject(intPtr)
        return ret



    def AppendHorizonalLine(self)->'ShapeObject':
        """
        Appends a horizontal line to the end of the paragraph.

        Returns:
            ShapeObject: The appended horizontal line.
        """
        GetDllLibDoc().Paragraph_AppendHorizonalLine.argtypes=[c_void_p]
        GetDllLibDoc().Paragraph_AppendHorizonalLine.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendHorizonalLine,self.Ptr)
        ret = None if intPtr==None else ShapeObject(intPtr)
        return ret



    def AppendShapeGroup(self ,width:float,height:float)->'ShapeGroup':
        """
        Appends a shape group to the end of the paragraph.

        Args:
            width: The width of the shape group.
            height: The height of the shape group.

        Returns:
            The appended shape group.
        """

        
        GetDllLibDoc().Paragraph_AppendShapeGroup.argtypes=[c_void_p ,c_float,c_float]
        GetDllLibDoc().Paragraph_AppendShapeGroup.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendShapeGroup,self.Ptr, width,height)
        from spire.doc import ShapeGroup
        ret = None if intPtr==None else ShapeGroup(intPtr)
        return ret



    def AppendBreak(self ,breakType:'BreakType')->'Break':
        """
        Appends a break to the end of the paragraph.

        Args:
            breakType: The type of break.

        Returns:
            The appended break.
        """
        enumbreakType:c_int = breakType.value

        GetDllLibDoc().Paragraph_AppendBreak.argtypes=[c_void_p ,c_int]
        GetDllLibDoc().Paragraph_AppendBreak.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendBreak,self.Ptr, enumbreakType)
        ret = None if intPtr==None else Break(intPtr)
        return ret



    def AppendTOC(self ,lowerLevel:int,upperLevel:int)->'TableOfContent':
        """
        Appends a table of content to the paragraph.

        Args:
            lowerLevel: The starting heading level of the table of content.
            upperLevel: The ending heading level of the table of content.

        Returns:
            The appended table of content.
        """
        
        GetDllLibDoc().Paragraph_AppendTOC.argtypes=[c_void_p ,c_int,c_int]
        GetDllLibDoc().Paragraph_AppendTOC.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendTOC,self.Ptr, lowerLevel,upperLevel)
        from spire.doc import TableOfContent
        ret = None if intPtr==None else TableOfContent(intPtr)
        return ret


    @dispatch

    def AppendPicture(self ,imgFile:str)->DocPicture:
        """
        Appends a picture to the paragraph.

        Args:
            imgFile: The image file.

        Returns:
            The appended picture.
        """
        imgFilePtr = StrToPtr(imgFile)
        GetDllLibDoc().Paragraph_AppendPictureI1.argtypes=[c_void_p ,c_char_p]
        GetDllLibDoc().Paragraph_AppendPictureI1.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendPictureI1,self.Ptr, imgFilePtr)
        from spire.doc import DocPicture
        ret = None if intPtr==None else DocPicture(intPtr)
        return ret


    @dispatch

    def AppendPicture(self ,imgStream:Stream)->DocPicture:
        """
        Appends a picture to the paragraph.

        Args:
            imgStream: The image stream.

        Returns:
            The appended picture.
        """
        intPtrimgStream:c_void_p = imgStream.Ptr

        GetDllLibDoc().Paragraph_AppendPictureI1.argtypes=[c_void_p ,c_void_p]
        GetDllLibDoc().Paragraph_AppendPictureI1.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendPictureI1,self.Ptr, intPtrimgStream)
        ret = None if intPtr==None else DocPicture(intPtr)
        return ret



    def AppendHTML(self ,html:str):
        """
        Appends HTML to the paragraph.

        Args:
            html: The HTML content.
        """
        htmlPtr = StrToPtr(html)
        GetDllLibDoc().Paragraph_AppendHTML.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Paragraph_AppendHTML,self.Ptr, htmlPtr)

    @dispatch

    def AppendRTF(self ,rtfcode:str,addtolastsection:bool):
        """
        Appends RTF to the paragraph.

        Args:
            rtfcode: The RTF code.
            addtolastsection: When True, the RTF is added to the last section of the document.
        """
        rtfcodePtr = StrToPtr(rtfcode)
        GetDllLibDoc().Paragraph_AppendRTF.argtypes=[c_void_p ,c_char_p,c_bool]
        CallCFunction(GetDllLibDoc().Paragraph_AppendRTF,self.Ptr, rtfcodePtr,addtolastsection)

    @dispatch

    def AppendRTF(self ,rtfCode:str):
        """
        Appends RTF to the paragraph.

        Args:
            rtfCode: The RTF code.
        """
        rtfCodePtr = StrToPtr(rtfCode)
        GetDllLibDoc().Paragraph_AppendRTFR.argtypes=[c_void_p ,c_char_p]
        CallCFunction(GetDllLibDoc().Paragraph_AppendRTFR,self.Ptr, rtfCodePtr)

    @dispatch

    def AppendOleObject(self ,oleStream:Stream,olePicture:DocPicture,type:OleObjectType)->DocOleObject:
        """
        Appends an OLE object to the paragraph.

        Args:
            oleStream: The OLE object (file) stream.
            olePicture: The OLE picture.
            type: The type of OLE object.

        Returns:
            The appended OLE object.
        """
        intPtroleStream:c_void_p = oleStream.Ptr
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendOleObject.argtypes=[c_void_p ,c_void_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObject.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendOleObject,self.Ptr, intPtroleStream,intPtrolePicture,enumtype)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


#    @dispatch
#
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,type:OleObjectType)->DocOleObject:
#        """
#    <summary>
#        Appends the OLE object into paragraph.
#    </summary>
#    <param name="oleBytes">The OLE object (file) bytes.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <param name="type">The type of OLE object.</param>
#    <returns></returns>
#        """
#        #arrayoleBytes:ArrayTypeoleBytes = ""
#        countoleBytes = len(oleBytes)
#        ArrayTypeoleBytes = c_void_p * countoleBytes
#        arrayoleBytes = ArrayTypeoleBytes()
#        for i in range(0, countoleBytes):
#            arrayoleBytes[i] = oleBytes[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#        enumtype:c_int = type.value
#
#        GetDllLibDoc().Paragraph_AppendOleObjectOOT.argtypes=[c_void_p ,ArrayTypeoleBytes,c_void_p,c_int]
#        GetDllLibDoc().Paragraph_AppendOleObjectOOT.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOT(self.Ptr, arrayoleBytes,intPtrolePicture,enumtype)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


#    @dispatch
#
#    def AppendOleObject(self ,progId:str,clsId:str,nativeData:'Byte[]',olePicture:DocPicture)->DocOleObject:
#        """
#    <summary>
#        Appends the OLE object into paragraph.
#    </summary>
#    <param name="progId">The programmatic identifier.</param>
#    <param name="clsId">The class identifier.</param>
#    <param name="nativeData">The native data of embedded OLE object.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <returns></returns>
#        """
#        #arraynativeData:ArrayTypenativeData = ""
#        countnativeData = len(nativeData)
#        ArrayTypenativeData = c_void_p * countnativeData
#        arraynativeData = ArrayTypenativeData()
#        for i in range(0, countnativeData):
#            arraynativeData[i] = nativeData[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#
#        GetDllLibDoc().Paragraph_AppendOleObjectPCNO.argtypes=[c_void_p ,c_wchar_p,c_wchar_p,ArrayTypenativeData,c_void_p]
#        GetDllLibDoc().Paragraph_AppendOleObjectPCNO.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectPCNO(self.Ptr, progId,clsId,arraynativeData,intPtrolePicture)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


    @dispatch

    def AppendOleObject(self ,pathToFile:str,olePicture:DocPicture,type:OleObjectType)->DocOleObject:
        """
        Appends the OLE object into paragraph.

        Args:
            pathToFile (str): The path to file.
            olePicture (DocPicture): The OLE picture.
            type (OleObjectType): The type of OLE object.

        Returns:
            DocOleObject: The appended OLE object.
        """
        pathToFilePtr = StrToPtr(pathToFile)
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumtype:c_int = type.value

        GetDllLibDoc().Paragraph_AppendOleObjectPOT.argtypes=[c_void_p ,c_char_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObjectPOT.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendOleObjectPOT,self.Ptr, pathToFilePtr,intPtrolePicture,enumtype)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


    @dispatch

    def AppendOleObject(self ,pathToFile:str,olePicture:DocPicture)->DocOleObject:
        """
        Appends the OLE object.

        Args:
            pathToFile (str): The path to file.
            olePicture (DocPicture): The OLE picture.

        Returns:
            DocOleObject: The appended OLE object.
        """
        pathToFilePtr = StrToPtr(pathToFile)
        intPtrolePicture:c_void_p = olePicture.Ptr

        GetDllLibDoc().Paragraph_AppendOleObjectPO.argtypes=[c_void_p ,c_char_p,c_void_p]
        GetDllLibDoc().Paragraph_AppendOleObjectPO.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendOleObjectPO,self.Ptr, pathToFilePtr,intPtrolePicture)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


    @dispatch

    def AppendOleObject(self ,oleStream:Stream,olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
        """
        Appends the OLE object into paragraph.

        Args:
            oleStream (Stream): The OLE storage.
            olePicture (DocPicture): The OLE picture.
            oleLinkType (OleLinkType): The type of OLE object link type.

        Returns:
            DocOleObject: The appended OLE object.
        """
        intPtroleStream:c_void_p = oleStream.Ptr
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumoleLinkType:c_int = oleLinkType.value

        GetDllLibDoc().Paragraph_AppendOleObjectOOO.argtypes=[c_void_p ,c_void_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObjectOOO.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendOleObjectOOO,self.Ptr, intPtroleStream,intPtrolePicture,enumoleLinkType)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


#    @dispatch
#
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
#        """
#    <summary>
#        Appends the OLE object.
#    </summary>
#    <param name="oleBytes">The OLE storage bytes.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <param name="oleLinkType">Type of the OLE link.</param>
#    <returns></returns>
#        """
#        #arrayoleBytes:ArrayTypeoleBytes = ""
#        countoleBytes = len(oleBytes)
#        ArrayTypeoleBytes = c_void_p * countoleBytes
#        arrayoleBytes = ArrayTypeoleBytes()
#        for i in range(0, countoleBytes):
#            arrayoleBytes[i] = oleBytes[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#        enumoleLinkType:c_int = oleLinkType.value
#
#        GetDllLibDoc().Paragraph_AppendOleObjectOOO1.argtypes=[c_void_p ,ArrayTypeoleBytes,c_void_p,c_int]
#        GetDllLibDoc().Paragraph_AppendOleObjectOOO1.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOO1(self.Ptr, arrayoleBytes,intPtrolePicture,enumoleLinkType)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


    @dispatch

    def AppendOleObject(self ,linkFile:str,olePicture:DocPicture,oleLinkType:OleLinkType)->DocOleObject:
        """
        Appends the OLE object.

        Args:
            linkFile (str): The link file.
            olePicture (DocPicture): The OLE picture.
            oleLinkType (OleLinkType): Type of the OLE link.

        Returns:
            DocOleObject: The appended OLE object.
        """
        linkFilePtr = StrToPtr(linkFile)
        intPtrolePicture:c_void_p = olePicture.Ptr
        enumoleLinkType:c_int = oleLinkType.value

        GetDllLibDoc().Paragraph_AppendOleObjectLOO.argtypes=[c_void_p ,c_char_p,c_void_p,c_int]
        GetDllLibDoc().Paragraph_AppendOleObjectLOO.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendOleObjectLOO,self.Ptr, linkFilePtr,intPtrolePicture,enumoleLinkType)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


#    @dispatch
#
#    def AppendOleObject(self ,oleBytes:'Byte[]',olePicture:DocPicture,fileExtension:str)->DocOleObject:
#        """
#    <summary>
#        Appends the package OLE object (ole object without specified type).
#    </summary>
#    <param name="oleBytes">The OLE object bytes.</param>
#    <param name="olePicture">The OLE picture.</param>
#    <param name="fileExtension">The file extension.</param>
#    <returns></returns>
#        """
#        #arrayoleBytes:ArrayTypeoleBytes = ""
#        countoleBytes = len(oleBytes)
#        ArrayTypeoleBytes = c_void_p * countoleBytes
#        arrayoleBytes = ArrayTypeoleBytes()
#        for i in range(0, countoleBytes):
#            arrayoleBytes[i] = oleBytes[i].Ptr
#
#        intPtrolePicture:c_void_p = olePicture.Ptr
#
#        GetDllLibDoc().Paragraph_AppendOleObjectOOF.argtypes=[c_void_p ,ArrayTypeoleBytes,c_void_p,c_wchar_p]
#        GetDllLibDoc().Paragraph_AppendOleObjectOOF.restype=c_void_p
#        intPtr = GetDllLibDoc().Paragraph_AppendOleObjectOOF(self.Ptr, arrayoleBytes,intPtrolePicture,fileExtension)
#        ret = None if intPtr==None else DocOleObject(intPtr)
#        return ret
#


    @dispatch

    def AppendOleObject(self ,oleStream:Stream,olePicture:DocPicture,fileExtension:str)->DocOleObject:
        """
        Appends the package OLE object (ole object without specified type).

        Args:
            oleStream (Stream): The OLE file stream.
            olePicture (DocPicture): The OLE picture.
            fileExtension (str): The file extension.

        Returns:
            DocOleObject: The appended OLE object.
        """
        fileExtensionPtr = StrToPtr(fileExtension)
        intPtroleStream:c_void_p = oleStream.Ptr
        intPtrolePicture:c_void_p = olePicture.Ptr

        GetDllLibDoc().Paragraph_AppendOleObjectOOF1.argtypes=[c_void_p ,c_void_p,c_void_p,c_char_p]
        GetDllLibDoc().Paragraph_AppendOleObjectOOF1.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().Paragraph_AppendOleObjectOOF1,self.Ptr, intPtroleStream,intPtrolePicture,fileExtensionPtr)
        ret = None if intPtr==None else DocOleObject(intPtr)
        return ret


    def RemoveFrame(self):
        """
        Remove a frame.
        """
        GetDllLibDoc().Paragraph_RemoveFrame.argtypes=[c_void_p]
        CallCFunction(GetDllLibDoc().Paragraph_RemoveFrame,self.Ptr)

