import sys
from ctypes import *
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc.common import dlllib
from spire.doc.common import dlllibDoc

from spire.doc.common.Common import IntPtrArray
from spire.doc.common.Common import IntPtrWithTypeName
from spire.doc.common.Common import GetObjVectorFromArray
from spire.doc.common.Common import GetVectorFromArray
from spire.doc.common.Common import GetStrVectorFromArray
from spire.doc.common.Common import GetIntPtrArray
from spire.doc.common.Common import GetByteArray
from spire.doc.common.Common import GetIntValue
from spire.doc.common.Common import GetObjIntPtr


from spire.doc.common.SpireObject import SpireObject
from spire.doc.common.Boolean import Boolean
from spire.doc.common.Byte import Byte
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
from spire.doc.common.RegexOptions import RegexOptions
from spire.doc.common.Regex import Regex

from spire.doc.PdfConformanceLevel import PdfConformanceLevel
from spire.doc.FormFieldType import FormFieldType
from spire.doc.FootnoteType import FootnoteType
from spire.doc.PropertyType import PropertyType
from spire.doc.FollowCharacterType import FollowCharacterType
from spire.doc.DocumentViewType import DocumentViewType
from spire.doc.HttpContentType import HttpContentType
from spire.doc.DocumentObjectType import DocumentObjectType
from spire.doc.FileFormat import FileFormat
from spire.doc.DefaultTableStyle import DefaultTableStyle
from spire.doc.CheckBoxSizeType import CheckBoxSizeType
from spire.doc.CssStyleSheetType import CssStyleSheetType
from spire.doc.CommentMarkType import CommentMarkType
from spire.doc.CellMerge import CellMerge
from spire.doc.BuiltInProperty import BuiltInProperty
from spire.doc.BuiltinStyle import BuiltinStyle
from spire.doc.BuiltinStyleLoader import BuiltinStyleLoader
from spire.doc.CalendarType import CalendarType
from spire.doc.ChangeItemsType import ChangeItemsType
from spire.doc.CellWidthType import CellWidthType
from spire.doc.BreakType import BreakType
from spire.doc.BookmarkTextStyle import BookmarkTextStyle
from spire.doc.BorderStyle import BorderStyle
from spire.doc.FieldMarkType import FieldMarkType
from spire.doc.FieldType import FieldType
from spire.doc.OleLinkType import OleLinkType
from spire.doc.OleObjectType import OleObjectType
from spire.doc.HtmlExportOptions import HtmlExportOptions
from spire.doc.FileFormat import FileFormat
from spire.doc.HyperlinkType import HyperlinkType
from spire.doc.TabLeader import TabLeader
from spire.doc.TabJustification import TabJustification
from spire.doc.SectionBreakType import SectionBreakType
from spire.doc.StyleType import StyleType
from spire.doc.XHTMLValidationType import XHTMLValidationType
from spire.doc.ProtectionType import ProtectionType
from spire.doc.BackgroundType import BackgroundType
from spire.doc.AutoFitBehaviorType import AutoFitBehaviorType
from spire.doc.DigitalSignatureType import DigitalSignatureType
from spire.doc.Doc_PropertyType import Doc_PropertyType
from spire.doc.EditRevisionType import EditRevisionType
from spire.doc.ImageType import ImageType
from spire.doc.FieldCharType import FieldCharType
from spire.doc.FontCharSet import FontCharSet
from spire.doc.FontClipPrecision import FontClipPrecision
from spire.doc.FontPitch import FontPitch
from spire.doc.FontPitchAndFamily import FontPitchAndFamily
from spire.doc.FontPrecision import FontPrecision
from spire.doc.FontQuality import FontQuality
from spire.doc.FontTypeHint import FontTypeHint
from spire.doc.FontWeight import FontWeight
from spire.doc.FootnoteRestartRule import FootnoteRestartRule
from spire.doc.FootnotePosition import FootnotePosition
from spire.doc.FootnoteNumberFormat import FootnoteNumberFormat
from spire.doc.FrameHorzAnchor import FrameHorzAnchor
from spire.doc.FrameSizeRule import FrameSizeRule
from spire.doc.FrameVertAnchor import FrameVertAnchor
from spire.doc.GradientShadingStyle import GradientShadingStyle
from spire.doc.GradientShadingVariant import GradientShadingVariant
from spire.doc.GridPitchType import GridPitchType
from spire.doc.GroupedShapeOrigin import GroupedShapeOrigin
from spire.doc.GroupEventType import GroupEventType
from spire.doc.HeaderFooterType import HeaderFooterType
from spire.doc.HeaderType import HeaderType
from spire.doc.HorizontalAlignment import HorizontalAlignment
from spire.doc.HorizontalOrigin import HorizontalOrigin
from spire.doc.HorizontalPosition import HorizontalPosition
from spire.doc.HorizontalRelation import HorizontalRelation
from spire.doc.HttpContentType import HttpContentType
from spire.doc.TextDirection import TextDirection
from spire.doc.ImportOptions import ImportOptions
from spire.doc.LayoutFlow import LayoutFlow
from spire.doc.LayoutType import LayoutType
from spire.doc.LigatureType import LigatureType
from spire.doc.LineDashing import LineDashing
from spire.doc.LineNumberingRestartMode import LineNumberingRestartMode
from spire.doc.LineSpacingRule import LineSpacingRule
from spire.doc.ListNumberAlignment import ListNumberAlignment
from spire.doc.ListPatternType import ListPatternType
from spire.doc.ListType import ListType
from spire.doc.LocaleIDs import LocaleIDs
from spire.doc.LockSettingsType import LockSettingsType
from spire.doc.MailMergeMainDocumentType import MailMergeMainDocumentType
from spire.doc.ParagraphItemType import ParagraphItemType
from spire.doc.PropertyType import PropertyType
from spire.doc.PropertyValueType import PropertyValueType
from spire.doc.RelativeHorizontalPosition import RelativeHorizontalPosition
from spire.doc.RelativeVerticalPosition import RelativeVerticalPosition
from spire.doc.RowAlignment import RowAlignment
from spire.doc.RtfTokenType import RtfTokenType
from spire.doc.SdtAppearance import SdtAppearance
from spire.doc.OleLinkType import OleLinkType
from spire.doc.OleObjectType import OleObjectType
from spire.doc.OutlineLevel import OutlineLevel
from spire.doc.PageAlignment import PageAlignment
from spire.doc.PageBorderOffsetFrom import PageBorderOffsetFrom
from spire.doc.PageBordersApplyType import PageBordersApplyType
from spire.doc.PageNumberAlignment import PageNumberAlignment
from spire.doc.PageNumberStyle import PageNumberStyle
from spire.doc.PageOrientation import PageOrientation
from spire.doc.SdtType import SdtType
from spire.doc.ShapeType import ShapeType
from spire.doc.ShapeHorizontalAlignment import ShapeHorizontalAlignment
from spire.doc.ShapeLineStyle import ShapeLineStyle
from spire.doc.ShapeVerticalAlignment import ShapeVerticalAlignment
from spire.doc.StylisticSetType import StylisticSetType
from spire.doc.SubSuperScript import SubSuperScript
from spire.doc.TextBoxLineStyle import TextBoxLineStyle
from spire.doc.TextDirection import TextDirection
from spire.doc.TextEffect import TextEffect
from spire.doc.TextFormat import TextFormat
from spire.doc.TextFormFieldType import TextFormFieldType
from spire.doc.TextureStyle import TextureStyle
from spire.doc.TextWrappingStyle import TextWrappingStyle
from spire.doc.TextWrappingType import TextWrappingType
from spire.doc.UnderlineStyle import UnderlineStyle
from spire.doc.VerticalAlignment import VerticalAlignment
from spire.doc.VerticalOrigin import VerticalOrigin
from spire.doc.VerticalPosition import VerticalPosition
from spire.doc.VerticalRelation import VerticalRelation
from spire.doc.WatermarkLayout import WatermarkLayout
from spire.doc.WatermarkType import WatermarkType
from spire.doc.WidthType import WidthType
from spire.doc.ZoomType import ZoomType
from spire.doc.WrapMode import WrapMode

from spire.doc.PdfPermissionsFlags import PdfPermissionsFlags
from spire.doc.PdfEncryptionKeySize import PdfEncryptionKeySize
from spire.doc.PdfSecurity import PdfSecurity

from spire.doc.DLSException import DLSException
from spire.doc.Hyperlink import Hyperlink
from spire.doc.Hyphenation import Hyphenation
from spire.doc.PrivateFontPath import PrivateFontPath
from spire.doc.ToPdfParameterList import ToPdfParameterList
from spire.doc.DocumentProperty import DocumentProperty
from spire.doc.LOGFONT import LOGFONT
from spire.doc.MailMerge import MailMerge
from spire.doc.SdtControlProperties import SdtControlProperties
from spire.doc.IDocumentObject import IDocumentObject
from spire.doc.IParagraphBase import IParagraphBase
from spire.doc.IStyle import IStyle
from spire.doc.IStyleHolder import IStyleHolder

from spire.doc.OwnerHolder import OwnerHolder
from spire.doc.IDocumentSerializable import IDocumentSerializable
from spire.doc.DocumentSerializable import DocumentSerializable
from spire.doc.FormatBase import FormatBase
from spire.doc.AttrCollection import AttrCollection
from spire.doc.Background import Background
from spire.doc.VMLFill import VMLFill
from spire.doc.BackgroundGradient import BackgroundGradient
from spire.doc.DocumentObject import DocumentObject
from spire.doc.DocumentBase import DocumentBase
from spire.doc.DocumentContainer import DocumentContainer
from spire.doc.ICompositeObject import ICompositeObject
from spire.doc.IBody import IBody
from spire.doc.IBodyRegion import IBodyRegion
from spire.doc.ICollectionBase import ICollectionBase
from spire.doc.IDocumentObjectCollection import IDocumentObjectCollection
from spire.doc.IXDLSSerializableCollection import IXDLSSerializableCollection
from spire.doc.CollectionEx import CollectionEx
from spire.doc.DocumentSerializableCollection import DocumentSerializableCollection
from spire.doc.DocumentObjectCollection import DocumentObjectCollection
from spire.doc.ParagraphItemCollection import ParagraphItemCollection
from spire.doc.BodyRegion import BodyRegion
from spire.doc.IParagraph import IParagraph
from spire.doc.IParagraphStyle import IParagraphStyle

from spire.doc.DocumentSubsetCollection import DocumentSubsetCollection
from spire.doc.IParagraphCollection import IParagraphCollection
from spire.doc.ParagraphCollection import ParagraphCollection

from spire.doc.Body import Body
from spire.doc.TableCell import TableCell
from spire.doc.TableRow import TableRow
from spire.doc.WordAttrCollection import WordAttrCollection
from spire.doc.RowFormat import RowFormat
from spire.doc.ITable import ITable
from spire.doc.Table import Table
from spire.doc.BodyRegionCollection import BodyRegionCollection
from spire.doc.Bookmark import Bookmark
from spire.doc.BookmarkCollection import BookmarkCollection
from spire.doc.ParagraphBase import ParagraphBase
from spire.doc.ShapeBase import ShapeBase
from spire.doc.Shape import Shape
from spire.doc.ShapeObject import ShapeObject
from spire.doc.DocOleObject import DocOleObject
from spire.doc.IPicture import IPicture
from spire.doc.ITextRange import ITextRange
from spire.doc.TextRange import TextRange
from spire.doc.IField import IField
from spire.doc.Field import Field
from spire.doc.FormField import FormField
from spire.doc.FormFieldCollection import FormFieldCollection
from spire.doc.CheckBoxFormField import CheckBoxFormField
from spire.doc.TextSelection import TextSelection
from spire.doc.TextBodySelection import TextBodySelection
from spire.doc.TextBodyPart import TextBodyPart
from spire.doc.BookmarkEnd import BookmarkEnd
from spire.doc.BookmarkLevel import BookmarkLevel
from spire.doc.BookmarkStart import BookmarkStart
from spire.doc.Border import Border
from spire.doc.Borders import Borders
from spire.doc.Break import Break
from spire.doc.SummaryDocumentProperties import SummaryDocumentProperties
from spire.doc.BuiltinDocumentProperties import BuiltinDocumentProperties
from spire.doc.CaptionNumberingFormat import CaptionNumberingFormat
from spire.doc.CaptionPosition import CaptionPosition
from spire.doc.CellCollection import CellCollection
from spire.doc.CellFormat import CellFormat
from spire.doc.ChangeItems import ChangeItems
from spire.doc.CharacterFormat import CharacterFormat
from spire.doc.CharacterSpacing import CharacterSpacing
from spire.doc.IDocument import IDocument
from spire.doc.DocPicture import DocPicture
from spire.doc.Footnote import Footnote
from spire.doc.Paragraph import Paragraph
from spire.doc.BookmarksNavigator import BookmarksNavigator

from spire.doc.ClipboardData import ClipboardData
from spire.doc.Column import Column
from spire.doc.ColumnCollection import ColumnCollection
from spire.doc.CommentMark import CommentMark
from spire.doc.Comment import Comment
from spire.doc.CommentFormat import CommentFormat
from spire.doc.CommentsCollection import CommentsCollection
from spire.doc.CompareOptions import CompareOptions
from spire.doc.ControlField import ControlField
from spire.doc.DocumentProperty import DocumentProperty
from spire.doc.CustomDocumentProperties import CustomDocumentProperties
from spire.doc.CustomXmlPart import CustomXmlPart
from spire.doc.CustomXmlPartCollection import CustomXmlPartCollection
from spire.doc.DifferRevisions import DifferRevisions

from spire.doc.ISection import ISection
from spire.doc.IWSectionCollection import IWSectionCollection

from spire.doc.TableOfContent import TableOfContent
from spire.doc.ITableCollection import ITableCollection
from spire.doc.TableCollection import TableCollection
from spire.doc.Section import Section
from spire.doc.SectionCollection import SectionCollection
from spire.doc.Document import Document
from spire.doc.DocumentProperties import DocumentProperties
from spire.doc.DocumentSecurity import DocumentSecurity
from spire.doc.DocumentVersion import DocumentVersion
from spire.doc.DotfuscatorAttribute import DotfuscatorAttribute
from spire.doc.DropDownItem import DropDownItem
from spire.doc.DropDownCollection import DropDownCollection
from spire.doc.DropDownFormField import DropDownFormField

from spire.doc.EditingGroup import EditingGroup
from spire.doc.RevisionBase import RevisionBase
from spire.doc.EditRevision import EditRevision
from spire.doc.Emphasis import Emphasis
from spire.doc.Endnote import Endnote
from spire.doc.EndnotePosition import EndnotePosition
from spire.doc.EntityEntry import EntityEntry
from spire.doc.FieldCollection import FieldCollection
from spire.doc.FieldMark import FieldMark
from spire.doc.FootEndnoteOptions import FootEndnoteOptions


from spire.doc.FootnoteBody import FootnoteBody

from spire.doc.Frame import Frame
from spire.doc.HeaderFooter import HeaderFooter
from spire.doc.HeadersFooters import HeadersFooters
from spire.doc.IDocCloneable import IDocCloneable
from spire.doc.IDocProperty import IDocProperty
from spire.doc.IDocumentCollection import IDocumentCollection
from spire.doc.IfField import IfField
from spire.doc.IMergeField import IMergeField
from spire.doc.InternalMargin import InternalMargin
from spire.doc.IRowsEnumerator import IRowsEnumerator
from spire.doc.IStructureDocument import IStructureDocument
from spire.doc.IStyleCollection import IStyleCollection

from spire.doc.ITextBox import ITextBox
from spire.doc.ITextBoxItemCollection import ITextBoxItemCollection
from spire.doc.IXDLSAttributeReader import IXDLSAttributeReader
from spire.doc.IXDLSAttributeWriter import IXDLSAttributeWriter
from spire.doc.IXDLSContentReader import IXDLSContentReader
from spire.doc.IXDLSContentWriter import IXDLSContentWriter
from spire.doc.IXDLSFactory import IXDLSFactory
from spire.doc.ListFormat import ListFormat
from spire.doc.ListLevel import ListLevel
from spire.doc.ListLevelCollection import ListLevelCollection
from spire.doc.Style import Style
from spire.doc.ListStyle import ListStyle
from spire.doc.ListStyleCollection import ListStyleCollection
from spire.doc.MailMergeDataSet import MailMergeDataSet
from spire.doc.MailMergeDataTable import MailMergeDataTable
from spire.doc.Margins import Margins
from spire.doc.MarginsF import MarginsF
from spire.doc.MathObject import MathObject
from spire.doc.MergeField import MergeField
from spire.doc.NumberFormat import NumberFormat
from spire.doc.NumberFormType import NumberFormType
from spire.doc.NumberSpaceType import NumberSpaceType
from spire.doc.ObjectEntry import ObjectEntry
from spire.doc.OdsoRecipientData import OdsoRecipientData
from spire.doc.OdsoRecipientDataCollection import OdsoRecipientDataCollection
from spire.doc.OfficeMath import OfficeMath
from spire.doc.OverrideLevelFormat import OverrideLevelFormat
from spire.doc.Paddings import Paddings
from spire.doc.PageSetup import PageSetup
from spire.doc.PageSize import PageSize
from spire.doc.ParagraphFormat import ParagraphFormat
from spire.doc.ParagraphStyle import ParagraphStyle
from spire.doc.Permission import Permission
from spire.doc.PermissionCollection import PermissionCollection
from spire.doc.PermissionEnd import PermissionEnd
from spire.doc.PermissionStart import PermissionStart
from spire.doc.PictureColor import PictureColor
from spire.doc.WatermarkBase import WatermarkBase
from spire.doc.PictureWatermark import PictureWatermark
from spire.doc.PreferredWidth import PreferredWidth

from spire.doc.RowCollection import RowCollection
from spire.doc.SdtDocPart import SdtDocPart
from spire.doc.SdtBuildingBlockGallery import SdtBuildingBlockGallery
from spire.doc.SdtCheckBox import SdtCheckBox
from spire.doc.SdtCitation import SdtCitation
from spire.doc.SdtDropDownListBase import SdtDropDownListBase
from spire.doc.SdtComboBox import SdtComboBox
from spire.doc.SDTContent import SDTContent
from spire.doc.SdtDate import SdtDate
from spire.doc.SdtDocPartObj import SdtDocPartObj
from spire.doc.SdtDropDownList import SdtDropDownList
from spire.doc.SDTInlineContent import SDTInlineContent
from spire.doc.SdtListItem import SdtListItem
from spire.doc.SdtListItemCollection import SdtListItemCollection
from spire.doc.SdtPicture import SdtPicture
from spire.doc.SDTProperties import SDTProperties
from spire.doc.SdtText import SdtText
from spire.doc.SequenceField import SequenceField
from spire.doc.ShapeGroup import ShapeGroup
from spire.doc.ShapeItemCollection import ShapeItemCollection
from spire.doc.StructureDocumentTag import StructureDocumentTag
from spire.doc.StructureDocumentTagCell import StructureDocumentTagCell
from spire.doc.StructureDocumentTagInline import StructureDocumentTagInline
from spire.doc.StructureDocumentTagRow import StructureDocumentTagRow
from spire.doc.StyleCollection import StyleCollection
from spire.doc.SubSetEnumerator import SubSetEnumerator
from spire.doc.Symbol import Symbol
from spire.doc.Tab import Tab
from spire.doc.TabCollection import TabCollection


from spire.doc.TablePositioning import TablePositioning
from spire.doc.TableRowHeightType import TableRowHeightType
from spire.doc.Template import Template
from spire.doc.TextAlignment import TextAlignment
from spire.doc.TextAnchor import TextAnchor
from spire.doc.TextBox import TextBox
from spire.doc.TextBoxCollection import TextBoxCollection
from spire.doc.TextBoxFormat import TextBoxFormat
from spire.doc.TextBoxItemCollection import TextBoxItemCollection
from spire.doc.TextFormField import TextFormField
from spire.doc.TextWatermark import TextWatermark
from spire.doc.TimeZone import TimeZone
from spire.doc.ToImageOption import ToImageOption
from spire.doc.VariableCollection import VariableCollection
from spire.doc.ViewSetup import ViewSetup
from spire.doc.WordArt import WordArt
from spire.doc.XDLSHolder import XDLSHolder
from spire.doc.XDLSReader import XDLSReader
from spire.doc.XmlTableFormat import XmlTableFormat

from spire.doc.pages.LayoutElement import LayoutElement
from spire.doc.pages.BodyLayoutElement import BodyLayoutElement
from spire.doc.pages.FixedLayoutCell import FixedLayoutCell
from spire.doc.pages.FixedLayoutColumn import FixedLayoutColumn
from spire.doc.pages.FixedLayoutComment import FixedLayoutComment
from spire.doc.pages.FixedLayoutDocument import FixedLayoutDocument
from spire.doc.pages.FixedLayoutEndnote import FixedLayoutEndnote
from spire.doc.pages.FixedLayoutFootnote import FixedLayoutFootnote
from spire.doc.pages.FixedLayoutHeaderFooter import FixedLayoutHeaderFooter
from spire.doc.pages.FixedLayoutLine import FixedLayoutLine
from spire.doc.pages.FixedLayoutNoteSeparator import FixedLayoutNoteSeparator
from spire.doc.pages.FixedLayoutPage import FixedLayoutPage
from spire.doc.pages.FixedLayoutRow import FixedLayoutRow
from spire.doc.pages.FixedLayoutSpan import FixedLayoutSpan
from spire.doc.pages.FixedLayoutTextBox import FixedLayoutTextBox
from spire.doc.pages.LayoutCollection import LayoutCollection
from spire.doc.pages.LayoutFixedLCellCollection import LayoutFixedLCellCollection
from spire.doc.pages.LayoutFixedLColumnCollection import LayoutFixedLColumnCollection
from spire.doc.pages.LayoutFixedLCommentCollection import LayoutFixedLCommentCollection
from spire.doc.pages.LayoutFixedLDocumentCollection import LayoutFixedLDocumentCollection
from spire.doc.pages.LayoutFixedLEndnoteCollection import LayoutFixedLEndnoteCollection
from spire.doc.pages.LayoutFixedLFootnoteCollection import LayoutFixedLFootnoteCollection
from spire.doc.pages.LayoutFixedLHeaderFooterCollection import LayoutFixedLHeaderFooterCollection
from spire.doc.pages.LayoutFixedLLineCollection import LayoutFixedLLineCollection
from spire.doc.pages.LayoutFixedLNoteSeparatorCollection import LayoutFixedLNoteSeparatorCollection
from spire.doc.pages.LayoutFixedLPagesCollection import LayoutFixedLPagesCollection
from spire.doc.pages.LayoutFixedLRowCollection import LayoutFixedLRowCollection
from spire.doc.pages.LayoutFixedLSpanCollection import LayoutFixedLSpanCollection
from spire.doc.pages.LayoutFixedLTextBoxCollection import LayoutFixedLTextBoxCollection
from spire.doc.pages.LayoutElementType import LayoutElementType

