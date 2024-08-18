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

class gsp_tree:
    
    lib = CDLL(util.find_library("GSPCore.dll"))

    @staticmethod
    def gsp_tree_create_root_node():
        f_gsp_tree_create_root_node = gsp_list.lib.gsp_tree_create_root_node
        f_gsp_tree_create_root_node.restype = ctypes.c_void_p
        return f_gsp_tree_create_root_node()

    @staticmethod
    def gsp_tree_create_child_node(parent):
        f_gsp_tree_create_child_node = gsp_list.lib.gsp_tree_create_child_node
        f_gsp_tree_create_child_node.argtypes = [ctypes.c_void_p]
        f_gsp_tree_create_child_node.restype = ctypes.c_void_p
        return f_gsp_tree_create_child_node(parent)

    @staticmethod
    def gsp_tree_destroy_node(node):
        f_gsp_tree_destroy_node = gsp_list.lib.gsp_tree_destroy_node
        f_gsp_tree_destroy_node.argtypes = [ctypes.c_void_p]
        f_gsp_tree_destroy_node(node)

    @staticmethod
    def gsp_tree_check_node_exists(node):
        f_gsp_tree_check_node_exists = gsp_list.lib.gsp_tree_check_node_exists
        f_gsp_tree_check_node_exists.argtypes = [ctypes.c_void_p]
        f_gsp_tree_check_node_exists.restype = ctypes.c_bool
        return f_gsp_tree_check_node_exists(node)

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

class gcolor_t(ctypes.Structure):
    _fields_ = [("red", ctypes.c_float),
                ("green", ctypes.c_float),
                ("blue", ctypes.c_float),
                ("alpha", ctypes.c_float)]

class gsp_view:

    lib = CDLL(util.find_library("GSPCore.dll"))

    @staticmethod
    def gsp_view_create_view():
        f_gsp_view_create_view = gsp_view.lib.gsp_view_create_view
        f_gsp_view_create_view.restype = ctypes.c_void_p
        return f_gsp_view_create_view()

    @staticmethod
    def gsp_view_is_view_valid(view):
        f_gsp_view_is_view_valid = gsp_view.lib.gsp_view_is_view_valid
        f_gsp_view_is_view_valid.argtypes = [ctypes.c_void_p]
        f_gsp_view_is_view_valid.restype = ctypes.c_bool
        return f_gsp_view_is_view_valid(view)
    
    @staticmethod
    def gsp_view_is_view_root(view):
        f_gsp_view_is_view_root = gsp_view.lib.gsp_view_is_view_root
        f_gsp_view_is_view_root.argtypes = [ctypes.c_void_p]
        f_gsp_view_is_view_root.restype = ctypes.c_bool
        return f_gsp_view_is_view_root(view)
    
    @staticmethod
    def gsp_view_set_window_root(window, view):
        f_gsp_view_set_window_root = gsp_view.lib.gsp_view_set_window_root
        f_gsp_view_set_window_root.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        f_gsp_view_set_window_root(window, view)

    @staticmethod
    def gsp_view_add_child(parent, child):
        f_gsp_view_add_child = gsp_view.lib.gsp_view_add_child
        f_gsp_view_add_child.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        f_gsp_view_add_child.restype = ctypes.c_bool
        return f_gsp_view_add_child(parent, child)
        

    @staticmethod
    def gsp_view_set_background_color(view, color):
        f_gsp_view_set_background_color = gsp_view.lib.gsp_view_set_background_color
        f_gsp_view_set_background_color.argtypes = [ctypes.c_void_p, gcolor_t]
        f_gsp_view_set_background_color(view, color)

    
