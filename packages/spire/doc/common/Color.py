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
class Color (SpireObject) :
    """

    """
    @staticmethod

    def get_Transparent()->'Color':
        """

        """
        #dlllib.Color_get_Transparent.argtypes=[]
        dlllib.Color_get_Transparent.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Transparent)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_AliceBlue()->'Color':
        """

        """
        #dlllib.Color_get_AliceBlue.argtypes=[]
        dlllib.Color_get_AliceBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_AliceBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_AntiqueWhite()->'Color':
        """

        """
        #dlllib.Color_get_AntiqueWhite.argtypes=[]
        dlllib.Color_get_AntiqueWhite.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_AntiqueWhite)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Aqua()->'Color':
        """

        """
        #dlllib.Color_get_Aqua.argtypes=[]
        dlllib.Color_get_Aqua.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Aqua)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Aquamarine()->'Color':
        """

        """
        #dlllib.Color_get_Aquamarine.argtypes=[]
        dlllib.Color_get_Aquamarine.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Aquamarine)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Azure()->'Color':
        """

        """
        #dlllib.Color_get_Azure.argtypes=[]
        dlllib.Color_get_Azure.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Azure)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Beige()->'Color':
        """

        """
        #dlllib.Color_get_Beige.argtypes=[]
        dlllib.Color_get_Beige.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Beige)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Bisque()->'Color':
        """

        """
        #dlllib.Color_get_Bisque.argtypes=[]
        dlllib.Color_get_Bisque.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Bisque)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Black()->'Color':
        """

        """
        #dlllib.Color_get_Black.argtypes=[]
        dlllib.Color_get_Black.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Black)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_BlanchedAlmond()->'Color':
        """

        """
        #dlllib.Color_get_BlanchedAlmond.argtypes=[]
        dlllib.Color_get_BlanchedAlmond.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_BlanchedAlmond)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Blue()->'Color':
        """

        """
        #dlllib.Color_get_Blue.argtypes=[]
        dlllib.Color_get_Blue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Blue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_BlueViolet()->'Color':
        """

        """
        #dlllib.Color_get_BlueViolet.argtypes=[]
        dlllib.Color_get_BlueViolet.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_BlueViolet)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Brown()->'Color':
        """

        """
        #dlllib.Color_get_Brown.argtypes=[]
        dlllib.Color_get_Brown.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Brown)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_BurlyWood()->'Color':
        """

        """
        #dlllib.Color_get_BurlyWood.argtypes=[]
        dlllib.Color_get_BurlyWood.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_BurlyWood)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_CadetBlue()->'Color':
        """

        """
        #dlllib.Color_get_CadetBlue.argtypes=[]
        dlllib.Color_get_CadetBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_CadetBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Chartreuse()->'Color':
        """

        """
        #dlllib.Color_get_Chartreuse.argtypes=[]
        dlllib.Color_get_Chartreuse.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Chartreuse)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Chocolate()->'Color':
        """

        """
        #dlllib.Color_get_Chocolate.argtypes=[]
        dlllib.Color_get_Chocolate.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Chocolate)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Coral()->'Color':
        """

        """
        #dlllib.Color_get_Coral.argtypes=[]
        dlllib.Color_get_Coral.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Coral)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_CornflowerBlue()->'Color':
        """

        """
        #dlllib.Color_get_CornflowerBlue.argtypes=[]
        dlllib.Color_get_CornflowerBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_CornflowerBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Cornsilk()->'Color':
        """

        """
        #dlllib.Color_get_Cornsilk.argtypes=[]
        dlllib.Color_get_Cornsilk.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Cornsilk)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Crimson()->'Color':
        """

        """
        #dlllib.Color_get_Crimson.argtypes=[]
        dlllib.Color_get_Crimson.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Crimson)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Cyan()->'Color':
        """

        """
        #dlllib.Color_get_Cyan.argtypes=[]
        dlllib.Color_get_Cyan.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Cyan)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkBlue()->'Color':
        """

        """
        #dlllib.Color_get_DarkBlue.argtypes=[]
        dlllib.Color_get_DarkBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkCyan()->'Color':
        """

        """
        #dlllib.Color_get_DarkCyan.argtypes=[]
        dlllib.Color_get_DarkCyan.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkCyan)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkGoldenrod()->'Color':
        """

        """
        #dlllib.Color_get_DarkGoldenrod.argtypes=[]
        dlllib.Color_get_DarkGoldenrod.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkGoldenrod)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkGray()->'Color':
        """

        """
        #dlllib.Color_get_DarkGray.argtypes=[]
        dlllib.Color_get_DarkGray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkGray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkGreen()->'Color':
        """

        """
        #dlllib.Color_get_DarkGreen.argtypes=[]
        dlllib.Color_get_DarkGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkKhaki()->'Color':
        """

        """
        #dlllib.Color_get_DarkKhaki.argtypes=[]
        dlllib.Color_get_DarkKhaki.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkKhaki)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkMagenta()->'Color':
        """

        """
        #dlllib.Color_get_DarkMagenta.argtypes=[]
        dlllib.Color_get_DarkMagenta.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkMagenta)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkOliveGreen()->'Color':
        """

        """
        #dlllib.Color_get_DarkOliveGreen.argtypes=[]
        dlllib.Color_get_DarkOliveGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkOliveGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkOrange()->'Color':
        """

        """
        #dlllib.Color_get_DarkOrange.argtypes=[]
        dlllib.Color_get_DarkOrange.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkOrange)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkOrchid()->'Color':
        """

        """
        #dlllib.Color_get_DarkOrchid.argtypes=[]
        dlllib.Color_get_DarkOrchid.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkOrchid)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkRed()->'Color':
        """

        """
        #dlllib.Color_get_DarkRed.argtypes=[]
        dlllib.Color_get_DarkRed.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkRed)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkSalmon()->'Color':
        """

        """
        #dlllib.Color_get_DarkSalmon.argtypes=[]
        dlllib.Color_get_DarkSalmon.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkSalmon)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkSeaGreen()->'Color':
        """

        """
        #dlllib.Color_get_DarkSeaGreen.argtypes=[]
        dlllib.Color_get_DarkSeaGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkSeaGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkSlateBlue()->'Color':
        """

        """
        #dlllib.Color_get_DarkSlateBlue.argtypes=[]
        dlllib.Color_get_DarkSlateBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkSlateBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkSlateGray()->'Color':
        """

        """
        #dlllib.Color_get_DarkSlateGray.argtypes=[]
        dlllib.Color_get_DarkSlateGray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkSlateGray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkTurquoise()->'Color':
        """

        """
        #dlllib.Color_get_DarkTurquoise.argtypes=[]
        dlllib.Color_get_DarkTurquoise.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkTurquoise)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DarkViolet()->'Color':
        """

        """
        #dlllib.Color_get_DarkViolet.argtypes=[]
        dlllib.Color_get_DarkViolet.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DarkViolet)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DeepPink()->'Color':
        """

        """
        #dlllib.Color_get_DeepPink.argtypes=[]
        dlllib.Color_get_DeepPink.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DeepPink)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DeepSkyBlue()->'Color':
        """

        """
        #dlllib.Color_get_DeepSkyBlue.argtypes=[]
        dlllib.Color_get_DeepSkyBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DeepSkyBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DimGray()->'Color':
        """

        """
        #dlllib.Color_get_DimGray.argtypes=[]
        dlllib.Color_get_DimGray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DimGray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_DodgerBlue()->'Color':
        """

        """
        #dlllib.Color_get_DodgerBlue.argtypes=[]
        dlllib.Color_get_DodgerBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_DodgerBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Firebrick()->'Color':
        """

        """
        #dlllib.Color_get_Firebrick.argtypes=[]
        dlllib.Color_get_Firebrick.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Firebrick)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_FloralWhite()->'Color':
        """

        """
        #dlllib.Color_get_FloralWhite.argtypes=[]
        dlllib.Color_get_FloralWhite.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_FloralWhite)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_ForestGreen()->'Color':
        """

        """
        #dlllib.Color_get_ForestGreen.argtypes=[]
        dlllib.Color_get_ForestGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_ForestGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Fuchsia()->'Color':
        """

        """
        #dlllib.Color_get_Fuchsia.argtypes=[]
        dlllib.Color_get_Fuchsia.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Fuchsia)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Gainsboro()->'Color':
        """

        """
        #dlllib.Color_get_Gainsboro.argtypes=[]
        dlllib.Color_get_Gainsboro.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Gainsboro)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_GhostWhite()->'Color':
        """

        """
        #dlllib.Color_get_GhostWhite.argtypes=[]
        dlllib.Color_get_GhostWhite.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_GhostWhite)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Gold()->'Color':
        """

        """
        #dlllib.Color_get_Gold.argtypes=[]
        dlllib.Color_get_Gold.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Gold)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Goldenrod()->'Color':
        """

        """
        #dlllib.Color_get_Goldenrod.argtypes=[]
        dlllib.Color_get_Goldenrod.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Goldenrod)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Gray()->'Color':
        """

        """
        #dlllib.Color_get_Gray.argtypes=[]
        dlllib.Color_get_Gray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Gray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Green()->'Color':
        """

        """
        #dlllib.Color_get_Green.argtypes=[]
        dlllib.Color_get_Green.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Green)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_GreenYellow()->'Color':
        """

        """
        #dlllib.Color_get_GreenYellow.argtypes=[]
        dlllib.Color_get_GreenYellow.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_GreenYellow)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Honeydew()->'Color':
        """

        """
        #dlllib.Color_get_Honeydew.argtypes=[]
        dlllib.Color_get_Honeydew.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Honeydew)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_HotPink()->'Color':
        """

        """
        #dlllib.Color_get_HotPink.argtypes=[]
        dlllib.Color_get_HotPink.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_HotPink)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_IndianRed()->'Color':
        """

        """
        #dlllib.Color_get_IndianRed.argtypes=[]
        dlllib.Color_get_IndianRed.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_IndianRed)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Indigo()->'Color':
        """

        """
        #dlllib.Color_get_Indigo.argtypes=[]
        dlllib.Color_get_Indigo.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Indigo)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Ivory()->'Color':
        """

        """
        #dlllib.Color_get_Ivory.argtypes=[]
        dlllib.Color_get_Ivory.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Ivory)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Khaki()->'Color':
        """

        """
        #dlllib.Color_get_Khaki.argtypes=[]
        dlllib.Color_get_Khaki.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Khaki)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Lavender()->'Color':
        """

        """
        #dlllib.Color_get_Lavender.argtypes=[]
        dlllib.Color_get_Lavender.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Lavender)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LavenderBlush()->'Color':
        """

        """
        #dlllib.Color_get_LavenderBlush.argtypes=[]
        dlllib.Color_get_LavenderBlush.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LavenderBlush)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LawnGreen()->'Color':
        """

        """
        #dlllib.Color_get_LawnGreen.argtypes=[]
        dlllib.Color_get_LawnGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LawnGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LemonChiffon()->'Color':
        """

        """
        #dlllib.Color_get_LemonChiffon.argtypes=[]
        dlllib.Color_get_LemonChiffon.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LemonChiffon)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightBlue()->'Color':
        """

        """
        #dlllib.Color_get_LightBlue.argtypes=[]
        dlllib.Color_get_LightBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightCoral()->'Color':
        """

        """
        #dlllib.Color_get_LightCoral.argtypes=[]
        dlllib.Color_get_LightCoral.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightCoral)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightCyan()->'Color':
        """

        """
        #dlllib.Color_get_LightCyan.argtypes=[]
        dlllib.Color_get_LightCyan.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightCyan)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightGoldenrodYellow()->'Color':
        """

        """
        #dlllib.Color_get_LightGoldenrodYellow.argtypes=[]
        dlllib.Color_get_LightGoldenrodYellow.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightGoldenrodYellow)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightGreen()->'Color':
        """

        """
        #dlllib.Color_get_LightGreen.argtypes=[]
        dlllib.Color_get_LightGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightGray()->'Color':
        """

        """
        #dlllib.Color_get_LightGray.argtypes=[]
        dlllib.Color_get_LightGray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightGray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightPink()->'Color':
        """

        """
        #dlllib.Color_get_LightPink.argtypes=[]
        dlllib.Color_get_LightPink.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightPink)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightSalmon()->'Color':
        """

        """
        #dlllib.Color_get_LightSalmon.argtypes=[]
        dlllib.Color_get_LightSalmon.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightSalmon)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightSeaGreen()->'Color':
        """

        """
        #dlllib.Color_get_LightSeaGreen.argtypes=[]
        dlllib.Color_get_LightSeaGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightSeaGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightSkyBlue()->'Color':
        """

        """
        #dlllib.Color_get_LightSkyBlue.argtypes=[]
        dlllib.Color_get_LightSkyBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightSkyBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightSlateGray()->'Color':
        """

        """
        #dlllib.Color_get_LightSlateGray.argtypes=[]
        dlllib.Color_get_LightSlateGray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightSlateGray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightSteelBlue()->'Color':
        """

        """
        #dlllib.Color_get_LightSteelBlue.argtypes=[]
        dlllib.Color_get_LightSteelBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightSteelBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LightYellow()->'Color':
        """

        """
        #dlllib.Color_get_LightYellow.argtypes=[]
        dlllib.Color_get_LightYellow.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LightYellow)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Lime()->'Color':
        """

        """
        #dlllib.Color_get_Lime.argtypes=[]
        dlllib.Color_get_Lime.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Lime)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_LimeGreen()->'Color':
        """

        """
        #dlllib.Color_get_LimeGreen.argtypes=[]
        dlllib.Color_get_LimeGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_LimeGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Linen()->'Color':
        """

        """
        #dlllib.Color_get_Linen.argtypes=[]
        dlllib.Color_get_Linen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Linen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Magenta()->'Color':
        """

        """
        #dlllib.Color_get_Magenta.argtypes=[]
        dlllib.Color_get_Magenta.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Magenta)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Maroon()->'Color':
        """

        """
        #dlllib.Color_get_Maroon.argtypes=[]
        dlllib.Color_get_Maroon.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Maroon)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumAquamarine()->'Color':
        """

        """
        #dlllib.Color_get_MediumAquamarine.argtypes=[]
        dlllib.Color_get_MediumAquamarine.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumAquamarine)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumBlue()->'Color':
        """

        """
        #dlllib.Color_get_MediumBlue.argtypes=[]
        dlllib.Color_get_MediumBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumOrchid()->'Color':
        """

        """
        #dlllib.Color_get_MediumOrchid.argtypes=[]
        dlllib.Color_get_MediumOrchid.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumOrchid)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumPurple()->'Color':
        """

        """
        #dlllib.Color_get_MediumPurple.argtypes=[]
        dlllib.Color_get_MediumPurple.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumPurple)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumSeaGreen()->'Color':
        """

        """
        #dlllib.Color_get_MediumSeaGreen.argtypes=[]
        dlllib.Color_get_MediumSeaGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumSeaGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumSlateBlue()->'Color':
        """

        """
        #dlllib.Color_get_MediumSlateBlue.argtypes=[]
        dlllib.Color_get_MediumSlateBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumSlateBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumSpringGreen()->'Color':
        """

        """
        #dlllib.Color_get_MediumSpringGreen.argtypes=[]
        dlllib.Color_get_MediumSpringGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumSpringGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumTurquoise()->'Color':
        """

        """
        #dlllib.Color_get_MediumTurquoise.argtypes=[]
        dlllib.Color_get_MediumTurquoise.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumTurquoise)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MediumVioletRed()->'Color':
        """

        """
        #dlllib.Color_get_MediumVioletRed.argtypes=[]
        dlllib.Color_get_MediumVioletRed.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MediumVioletRed)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MidnightBlue()->'Color':
        """

        """
        #dlllib.Color_get_MidnightBlue.argtypes=[]
        dlllib.Color_get_MidnightBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MidnightBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MintCream()->'Color':
        """

        """
        #dlllib.Color_get_MintCream.argtypes=[]
        dlllib.Color_get_MintCream.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MintCream)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_MistyRose()->'Color':
        """

        """
        #dlllib.Color_get_MistyRose.argtypes=[]
        dlllib.Color_get_MistyRose.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_MistyRose)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Moccasin()->'Color':
        """

        """
        #dlllib.Color_get_Moccasin.argtypes=[]
        dlllib.Color_get_Moccasin.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Moccasin)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_NavajoWhite()->'Color':
        """

        """
        #dlllib.Color_get_NavajoWhite.argtypes=[]
        dlllib.Color_get_NavajoWhite.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_NavajoWhite)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Navy()->'Color':
        """

        """
        #dlllib.Color_get_Navy.argtypes=[]
        dlllib.Color_get_Navy.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Navy)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_OldLace()->'Color':
        """

        """
        #dlllib.Color_get_OldLace.argtypes=[]
        dlllib.Color_get_OldLace.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_OldLace)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Olive()->'Color':
        """

        """
        #dlllib.Color_get_Olive.argtypes=[]
        dlllib.Color_get_Olive.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Olive)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_OliveDrab()->'Color':
        """

        """
        #dlllib.Color_get_OliveDrab.argtypes=[]
        dlllib.Color_get_OliveDrab.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_OliveDrab)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Orange()->'Color':
        """

        """
        #dlllib.Color_get_Orange.argtypes=[]
        dlllib.Color_get_Orange.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Orange)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_OrangeRed()->'Color':
        """

        """
        #dlllib.Color_get_OrangeRed.argtypes=[]
        dlllib.Color_get_OrangeRed.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_OrangeRed)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Orchid()->'Color':
        """

        """
        #dlllib.Color_get_Orchid.argtypes=[]
        dlllib.Color_get_Orchid.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Orchid)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PaleGoldenrod()->'Color':
        """

        """
        #dlllib.Color_get_PaleGoldenrod.argtypes=[]
        dlllib.Color_get_PaleGoldenrod.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PaleGoldenrod)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PaleGreen()->'Color':
        """

        """
        #dlllib.Color_get_PaleGreen.argtypes=[]
        dlllib.Color_get_PaleGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PaleGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PaleTurquoise()->'Color':
        """

        """
        #dlllib.Color_get_PaleTurquoise.argtypes=[]
        dlllib.Color_get_PaleTurquoise.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PaleTurquoise)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PaleVioletRed()->'Color':
        """

        """
        #dlllib.Color_get_PaleVioletRed.argtypes=[]
        dlllib.Color_get_PaleVioletRed.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PaleVioletRed)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PapayaWhip()->'Color':
        """

        """
        #dlllib.Color_get_PapayaWhip.argtypes=[]
        dlllib.Color_get_PapayaWhip.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PapayaWhip)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PeachPuff()->'Color':
        """

        """
        #dlllib.Color_get_PeachPuff.argtypes=[]
        dlllib.Color_get_PeachPuff.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PeachPuff)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Peru()->'Color':
        """

        """
        #dlllib.Color_get_Peru.argtypes=[]
        dlllib.Color_get_Peru.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Peru)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Pink()->'Color':
        """

        """
        #dlllib.Color_get_Pink.argtypes=[]
        dlllib.Color_get_Pink.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Pink)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Plum()->'Color':
        """

        """
        #dlllib.Color_get_Plum.argtypes=[]
        dlllib.Color_get_Plum.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Plum)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_PowderBlue()->'Color':
        """

        """
        #dlllib.Color_get_PowderBlue.argtypes=[]
        dlllib.Color_get_PowderBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_PowderBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Purple()->'Color':
        """

        """
        #dlllib.Color_get_Purple.argtypes=[]
        dlllib.Color_get_Purple.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Purple)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Red()->'Color':
        """

        """
        #dlllib.Color_get_Red.argtypes=[]
        dlllib.Color_get_Red.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Red)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_RosyBrown()->'Color':
        """

        """
        #dlllib.Color_get_RosyBrown.argtypes=[]
        dlllib.Color_get_RosyBrown.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_RosyBrown)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_RoyalBlue()->'Color':
        """

        """
        #dlllib.Color_get_RoyalBlue.argtypes=[]
        dlllib.Color_get_RoyalBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_RoyalBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SaddleBrown()->'Color':
        """

        """
        #dlllib.Color_get_SaddleBrown.argtypes=[]
        dlllib.Color_get_SaddleBrown.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SaddleBrown)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Salmon()->'Color':
        """

        """
        #dlllib.Color_get_Salmon.argtypes=[]
        dlllib.Color_get_Salmon.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Salmon)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SandyBrown()->'Color':
        """

        """
        #dlllib.Color_get_SandyBrown.argtypes=[]
        dlllib.Color_get_SandyBrown.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SandyBrown)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SeaGreen()->'Color':
        """

        """
        #dlllib.Color_get_SeaGreen.argtypes=[]
        dlllib.Color_get_SeaGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SeaGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SeaShell()->'Color':
        """

        """
        #dlllib.Color_get_SeaShell.argtypes=[]
        dlllib.Color_get_SeaShell.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SeaShell)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Sienna()->'Color':
        """

        """
        #dlllib.Color_get_Sienna.argtypes=[]
        dlllib.Color_get_Sienna.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Sienna)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Silver()->'Color':
        """

        """
        #dlllib.Color_get_Silver.argtypes=[]
        dlllib.Color_get_Silver.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Silver)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SkyBlue()->'Color':
        """

        """
        #dlllib.Color_get_SkyBlue.argtypes=[]
        dlllib.Color_get_SkyBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SkyBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SlateBlue()->'Color':
        """

        """
        #dlllib.Color_get_SlateBlue.argtypes=[]
        dlllib.Color_get_SlateBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SlateBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SlateGray()->'Color':
        """

        """
        #dlllib.Color_get_SlateGray.argtypes=[]
        dlllib.Color_get_SlateGray.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SlateGray)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Snow()->'Color':
        """

        """
        #dlllib.Color_get_Snow.argtypes=[]
        dlllib.Color_get_Snow.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Snow)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SpringGreen()->'Color':
        """

        """
        #dlllib.Color_get_SpringGreen.argtypes=[]
        dlllib.Color_get_SpringGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SpringGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_SteelBlue()->'Color':
        """

        """
        #dlllib.Color_get_SteelBlue.argtypes=[]
        dlllib.Color_get_SteelBlue.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_SteelBlue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Tan()->'Color':
        """

        """
        #dlllib.Color_get_Tan.argtypes=[]
        dlllib.Color_get_Tan.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Tan)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Teal()->'Color':
        """

        """
        #dlllib.Color_get_Teal.argtypes=[]
        dlllib.Color_get_Teal.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Teal)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Thistle()->'Color':
        """

        """
        #dlllib.Color_get_Thistle.argtypes=[]
        dlllib.Color_get_Thistle.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Thistle)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Tomato()->'Color':
        """

        """
        #dlllib.Color_get_Tomato.argtypes=[]
        dlllib.Color_get_Tomato.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Tomato)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Turquoise()->'Color':
        """

        """
        #dlllib.Color_get_Turquoise.argtypes=[]
        dlllib.Color_get_Turquoise.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Turquoise)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Violet()->'Color':
        """

        """
        #dlllib.Color_get_Violet.argtypes=[]
        dlllib.Color_get_Violet.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Violet)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Wheat()->'Color':
        """

        """
        #dlllib.Color_get_Wheat.argtypes=[]
        dlllib.Color_get_Wheat.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Wheat)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_White()->'Color':
        """

        """
        #dlllib.Color_get_White.argtypes=[]
        dlllib.Color_get_White.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_White)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_WhiteSmoke()->'Color':
        """

        """
        #dlllib.Color_get_WhiteSmoke.argtypes=[]
        dlllib.Color_get_WhiteSmoke.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_WhiteSmoke)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_Yellow()->'Color':
        """

        """
        #dlllib.Color_get_Yellow.argtypes=[]
        dlllib.Color_get_Yellow.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_Yellow)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def get_YellowGreen()->'Color':
        """

        """
        #dlllib.Color_get_YellowGreen.argtypes=[]
        dlllib.Color_get_YellowGreen.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_get_YellowGreen)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @property
    def R(self)->int:
        """

        """
        dlllib.Color_get_R.argtypes=[c_void_p]
        dlllib.Color_get_R.restype=c_int
        ret = CallCFunction(dlllib.Color_get_R,self.Ptr)
        return ret

    @property
    def G(self)->int:
        """

        """
        dlllib.Color_get_G.argtypes=[c_void_p]
        dlllib.Color_get_G.restype=c_int
        ret = CallCFunction(dlllib.Color_get_G,self.Ptr)
        return ret

    @property
    def B(self)->int:
        """

        """
        dlllib.Color_get_B.argtypes=[c_void_p]
        dlllib.Color_get_B.restype=c_int
        ret = CallCFunction(dlllib.Color_get_B,self.Ptr)
        return ret

    @property
    def A(self)->int:
        """

        """
        dlllib.Color_get_A.argtypes=[c_void_p]
        dlllib.Color_get_A.restype=c_int
        ret = CallCFunction(dlllib.Color_get_A,self.Ptr)
        return ret

    @property
    def IsKnownColor(self)->bool:
        """

        """
        dlllib.Color_get_IsKnownColor.argtypes=[c_void_p]
        dlllib.Color_get_IsKnownColor.restype=c_bool
        ret = CallCFunction(dlllib.Color_get_IsKnownColor,self.Ptr)
        return ret

    @property
    def IsEmpty(self)->bool:
        """

        """
        dlllib.Color_get_IsEmpty.argtypes=[c_void_p]
        dlllib.Color_get_IsEmpty.restype=c_bool
        ret = CallCFunction(dlllib.Color_get_IsEmpty,self.Ptr)
        return ret

    @property
    def IsNamedColor(self)->bool:
        """

        """
        dlllib.Color_get_IsNamedColor.argtypes=[c_void_p]
        dlllib.Color_get_IsNamedColor.restype=c_bool
        ret = CallCFunction(dlllib.Color_get_IsNamedColor,self.Ptr)
        return ret

    @property
    def IsSystemColor(self)->bool:
        """

        """
        dlllib.Color_get_IsSystemColor.argtypes=[c_void_p]
        dlllib.Color_get_IsSystemColor.restype=c_bool
        ret = CallCFunction(dlllib.Color_get_IsSystemColor,self.Ptr)
        return ret

    @property

    def Name(self)->str:
        """

        """
        dlllib.Color_get_Name.argtypes=[c_void_p]
        dlllib.Color_get_Name.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Color_get_Name,self.Ptr))
        return ret


    @staticmethod
    @dispatch

    def FromArgb(argb:int)->'Color':
        """

        """
        
        dlllib.Color_FromArgb.argtypes=[ c_int]
        dlllib.Color_FromArgb.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_FromArgb, argb)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod
    @dispatch

    def FromArgb(red:int,green:int,blue:int)->'Color':
        """

        """
        
        dlllib.Color_FromArgbRGB.argtypes=[ c_int,c_int,c_int]
        dlllib.Color_FromArgbRGB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_FromArgbRGB, red,green,blue)
        ret = None if intPtr==None else Color(intPtr)
        return ret

    @staticmethod
    @dispatch

    def FromArgb(alpha:int,red:int,green:int,blue:int)->'Color':
        """

        """
        
        dlllib.Color_FromArgbARGB.argtypes=[ c_int,c_int,c_int,c_int]
        dlllib.Color_FromArgbARGB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_FromArgbARGB, alpha,red,green,blue)
        ret = None if intPtr==None else Color(intPtr)
        return ret


#    @staticmethod
#
#    def FromKnownColor(color:'KnownColor')->'Color':
#        """
#
#        """
#        enumcolor:c_int = color.value
#
#        dlllib.Color_FromKnownColor.argtypes=[ c_int]
#        dlllib.Color_FromKnownColor.restype=c_void_p
#        intPtr = CallCFunction(dlllib.Color_FromKnownColor, enumcolor)
#        ret = None if intPtr==None else Color(intPtr)
#        return ret
#


    @staticmethod

    def FromName(name:str)->'Color':
        """

        """
        if __package__ == "spire.doc.common" or __package__ == "spire.presentation.common":
            namePtr = StrToPtr(name)
            dlllib.Color_FromName.argtypes=[ c_char_p]
            dlllib.Color_FromName.restype=c_void_p
            intPtr = CallCFunction(dlllib.Color_FromName,namePtr)
            ret = None if intPtr==None else Color(intPtr)
            return ret
        else:
            dlllib.Color_FromName.argtypes=[ c_void_p]
            dlllib.Color_FromName.restype=c_void_p
            intPtr = CallCFunction(dlllib.Color_FromName, name)
            ret = None if intPtr==None else Color(intPtr)
            return ret
        


    def GetBrightness(self)->float:
        """

        """
        dlllib.Color_GetBrightness.argtypes=[c_void_p]
        dlllib.Color_GetBrightness.restype=c_float
        ret = CallCFunction(dlllib.Color_GetBrightness,self.Ptr)
        return ret

    def GetHue(self)->float:
        """

        """
        dlllib.Color_GetHue.argtypes=[c_void_p]
        dlllib.Color_GetHue.restype=c_float
        ret = CallCFunction(dlllib.Color_GetHue,self.Ptr)
        return ret

    def GetSaturation(self)->float:
        """

        """
        dlllib.Color_GetSaturation.argtypes=[c_void_p]
        dlllib.Color_GetSaturation.restype=c_float
        ret = CallCFunction(dlllib.Color_GetSaturation,self.Ptr)
        return ret

    def ToArgb(self)->int:
        """

        """
        dlllib.Color_ToArgb.argtypes=[c_void_p]
        dlllib.Color_ToArgb.restype=c_int
        ret = CallCFunction(dlllib.Color_ToArgb,self.Ptr)
        return ret

#
#    def ToKnownColor(self)->'KnownColor':
#        """
#
#        """
#        dlllib.Color_ToKnownColor.argtypes=[c_void_p]
#        dlllib.Color_ToKnownColor.restype=c_int
#        ret = CallCFunction(dlllib.Color_ToKnownColor,self.Ptr)
#        objwraped = KnownColor(ret)
#        return objwraped


    @staticmethod

    def op_Equality(left:'Color',right:'Color')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.Color_op_Equality.argtypes=[ c_void_p,c_void_p]
        dlllib.Color_op_Equality.restype=c_bool
        ret = CallCFunction(dlllib.Color_op_Equality, intPtrleft,intPtrright)
        return ret

    @staticmethod

    def op_Inequality(left:'Color',right:'Color')->bool:
        """

        """
        intPtrleft:c_void_p = left.Ptr
        intPtrright:c_void_p = right.Ptr

        dlllib.Color_op_Inequality.argtypes=[ c_void_p,c_void_p]
        dlllib.Color_op_Inequality.restype=c_bool
        ret = CallCFunction(dlllib.Color_op_Inequality, intPtrleft,intPtrright)
        return ret


    def Equals(self ,obj:'SpireObject')->bool:
        """

        """
        intPtrobj:c_void_p = obj.Ptr

        dlllib.Color_Equals.argtypes=[c_void_p ,c_void_p]
        dlllib.Color_Equals.restype=c_bool
        ret = CallCFunction(dlllib.Color_Equals,self.Ptr, intPtrobj)
        return ret

    def GetHashCode(self)->int:
        """

        """
        dlllib.Color_GetHashCode.argtypes=[c_void_p]
        dlllib.Color_GetHashCode.restype=c_int
        ret = CallCFunction(dlllib.Color_GetHashCode,self.Ptr)
        return ret


    def ToString(self)->str:
        """

        """
        dlllib.Color_ToString.argtypes=[c_void_p]
        dlllib.Color_ToString.restype=c_void_p
        ret = PtrToStr(CallCFunction(dlllib.Color_ToString,self.Ptr))
        return ret


    @staticmethod
    #@dispatch
    def FromArgb(alpha:int,red:int,green:int,blue:int)->'Color':
        """

        """
        
        dlllib.Color_FromArgbARGB.argtypes=[ c_int,c_int,c_int,c_int]
        dlllib.Color_FromArgbARGB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_FromArgbARGB, alpha,red,green,blue)
        ret = None if intPtr==None else Color(intPtr)
        return ret

    @staticmethod
    #@dispatch
    def FromRgb(red:int,green:int,blue:int)->'Color':
        """

        """
        
        dlllib.Color_FromArgbARGB.argtypes=[ c_int,c_int,c_int,c_int]
        dlllib.Color_FromArgbARGB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_FromArgbARGB, 255,red,green,blue)
        ret = None if intPtr==None else Color(intPtr)
        return ret

    @staticmethod
    #@dispatch
    def FromAColor(alpha:int,baseColor:'Color')->'Color':
        """

        """
        intPtrbaseColor:c_void_p = baseColor.Ptr

        dlllib.Color_FromArgbAB.argtypes=[ c_int,c_void_p]
        dlllib.Color_FromArgbAB.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_FromArgbAB, alpha,intPtrbaseColor)
        ret = None if intPtr==None else Color(intPtr)
        return ret


    @staticmethod

    def Empty()->'Color':
        """

        """
        #dlllib.Color_Empty.argtypes=[]
        dlllib.Color_Empty.restype=c_void_p
        intPtr = CallCFunction(dlllib.Color_Empty)
        ret = None if intPtr==None else Color(intPtr)
        return ret


