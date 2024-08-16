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

class gwindow_event_t(ctypes.Structure):
    _fields_ = [("event_id", ctypes.c_uint8),
                ("sub_id", ctypes.c_uint8),
                ("data", ctypes.c_uint64)]

class gsp_window:
    
    lib = CDLL(util.find_library("GSPCore.dll"))
    EVENT_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p, gwindow_event_t)

    @staticmethod
    def gsp_window_poll_events():
        f_gsp_window_poll_events = gsp_list.lib.gsp_window_poll_events
        return f_gsp_window_poll_events()

    @staticmethod
    def gsp_window_is_window_valid(window):
        f_gsp_window_is_window_valid = gsp_list.lib.gsp_window_is_window_valid
        f_gsp_window_is_window_valid.argtypes = [ctypes.c_void_p]
        f_gsp_window_is_window_valid.restype = ctypes.c_bool
        return f_gsp_window_is_window_valid()
    
    @staticmethod
    def gsp_window_create_window():
        f_gsp_window_create_window = gsp_list.lib.gsp_window_create_window
        f_gsp_window_create_window.restype = ctypes.c_void_p
        return f_gsp_window_create_window()

    @staticmethod
    def gsp_window_set_title(window, title):
        f_gsp_window_set_title = gsp_list.lib.gsp_window_set_title
        f_gsp_window_set_title.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        return f_gsp_window_set_title(window, title.encode("utf-8"))
    
    @staticmethod
    def gsp_window_set_event_callback(window, callback_handle):
        f_gsp_window_set_event_callback = gsp_list.lib.gsp_window_set_event_callback
        f_gsp_window_set_event_callback.argtypes = [ctypes.c_void_p, gsp_window.EVENT_CALLBACK_TYPE]
        return f_gsp_window_set_event_callback(window, callback_handle)

    