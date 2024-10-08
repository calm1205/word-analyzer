from enum import Enum
from plum import dispatch
from typing import TypeVar,Union,Generic,List,Tuple

if __package__ == "spire.pdf.common":
    from spire.pdf.common import *
    from spire.pdf.common.IEnumerable import IEnumerable
elif __package__ == "spire.xls.common" :
    from spire.xls.common import *
    from spire.xls.common.IEnumerable import IEnumerable
elif __package__ == "spire.doc.common" :
    from spire.doc.common import *
    from spire.doc.common.IEnumerable import IEnumerable
else :
    from spire.presentation.common import *
    from spire.presentation.common.IEnumerable import IEnumerable
#from spire.xls import *
from ctypes import *
import abc



T = TypeVar("T", bound=SpireObject)
class ICollection (  IEnumerable[T]) :
    """

    """
#
#    def CopyTo(self ,array:'Array',index:int):
#        """
#
#        """
#        intPtrarray:c_void_p = array.Ptr
#
#        dlllib.ICollection_CopyTo.argtypes=[c_void_p ,c_void_p,c_int]
#        CallCFunction(dlllib.ICollection_CopyTo,self.Ptr, intPtrarray,index)


    @property
    def Count(self)->int:
        """

        """
        dlllib.ICollection_get_Count.argtypes=[c_void_p]
        dlllib.ICollection_get_Count.restype=c_int
        ret = CallCFunction(dlllib.ICollection_get_Count,self.Ptr)
        return ret

    #@property

    #def SyncRoot(self)->SpireObject:
    #    """

    #    """
    #    dlllib.ICollection_get_SyncRoot.argtypes=[c_void_p]
    #    dlllib.ICollection_get_SyncRoot.restype=c_void_p
    #    intPtr = CallCFunction(dlllib.ICollection_get_SyncRoot,self.Ptr)
    #    ret = None if intPtr==None else SpireObject(intPtr)
    #    return ret


    @property
    def IsSynchronized(self)->int:
        """

        """
        dlllib.ICollection_get_IsSynchronized.argtypes=[c_void_p]
        dlllib.ICollection_get_IsSynchronized.restype=c_int
        ret = CallCFunction(dlllib.ICollection_get_IsSynchronized,self.Ptr)
        return ret
