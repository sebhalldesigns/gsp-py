from ctypes import util, CDLL
import ctypes
import os

class gsp_list:
    
    lib = CDLL(util.find_library("GSPCore.dll"))

    @staticmethod
    def gsp_list_create_list():
        f_gsp_list_create_list = gsp_list.lib.gsp_list_create_list
        f_gsp_list_create_list.restype = ctypes.c_void_p
        return f_gsp_list_create_list()

    @staticmethod
    def gsp_list_destroy_list(list):
        f_gsp_list_destroy_list = gsp_list.lib.gsp_list_destroy_list
        f_gsp_list_destroy_list.argtypes = [ctypes.c_void_p]
        f_gsp_list_destroy_list(list)

