from enum import Enum
from plum import dispatch
from typing import Text, TextIO, TypeVar,Union,Generic,List,Tuple
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

T = TypeVar("T", bound=SpireObject)
class IEnumerator (SpireObject, Generic[T]) :
    """

    """

    def __next__(self)->T:
        if self.MoveNext() == 0:
            raise StopIteration()
        ret = self.Current
        if ret == None:
            raise StopIteration()
        return ret

    def MoveNext(self)->int:
        """

        """
        dlllib.IEnumerator_MoveNext.argtypes=[c_void_p]
        dlllib.IEnumerator_MoveNext.restype=c_int
        ret = CallCFunction(dlllib.IEnumerator_MoveNext,self.Ptr)
        return ret

    @property

    def Current(self)->T:
        """

        """
        if self._gtype == None:
            self._gtype = self.__orig_bases__[0].__args__[0]

        dlllib.IEnumerator_get_Current.argtypes=[c_void_p]
        dlllib.IEnumerator_get_Current.restype=c_void_p
        intPtr = CallCFunction(dlllib.IEnumerator_get_Current,self.Ptr)
        ret = None if intPtr==None else self._gtype(intPtr)
        return ret


    def Reset(self):
        """

        """
        dlllib.IEnumerator_Reset.argtypes=[c_void_p]
        CallCFunction(dlllib.IEnumerator_Reset,self.Ptr)
