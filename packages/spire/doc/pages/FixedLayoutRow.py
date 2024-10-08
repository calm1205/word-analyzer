from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple
from spire.doc.common import *
from spire.doc.pages import *
from spire.doc import *
from ctypes import *
import abc

class FixedLayoutRow (  LayoutElement) :
    """
    <summary>
        Represents a table row.
    </summary>
    """
    @property

    def Cells(self)->'LayoutFixedLCellCollection':
        """
    <summary>
        Provides access to the cells of the table row.
    </summary>
        """
        GetDllLibDoc().FixedLayoutRow_get_Cells.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutRow_get_Cells.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutRow_get_Cells,self.Ptr)
        ret = None if intPtr==None else LayoutFixedLCellCollection(intPtr)
        return ret



    @property

    def Row(self)->'TableRow':
        """
    <summary>
        Returns the row that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutRow_get_Row.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutRow_get_Row.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutRow_get_Row,self.Ptr)
        ret = None if intPtr==None else TableRow(intPtr)
        return ret


    @property

    def Table(self)->'Table':
        """
    <summary>
        Returns the table that corresponds to the layout entity.  
    </summary>
        """
        GetDllLibDoc().FixedLayoutRow_get_Table.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutRow_get_Table.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutRow_get_Table,self.Ptr)
        ret = None if intPtr==None else Table(intPtr)
        return ret


    @property

    def ParentNode(self)->'DocumentObject':
        """
    <summary>
        Provides the layout node that pertains to this particular entity.
    </summary>
        """
        GetDllLibDoc().FixedLayoutRow_get_ParentNode.argtypes=[c_void_p]
        GetDllLibDoc().FixedLayoutRow_get_ParentNode.restype=c_void_p
        intPtr = CallCFunction(GetDllLibDoc().FixedLayoutRow_get_ParentNode,self.Ptr)
        ret = None if intPtr==None else DocumentObject(intPtr)
        return ret


