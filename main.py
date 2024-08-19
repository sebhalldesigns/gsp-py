from core.native import gsp_list, gsp_window, gsp_view, gsp_tree, gcolor_t
import sys

window1 = gsp_window.gsp_window_create_window()
should_quit = False

#root1 = gsp_tree.gsp_tree_create_root_node()
#root2 = gsp_tree.gsp_tree_create_root_node()
#node1 = gsp_tree.gsp_tree_create_child_node(root1)
#node2 = gsp_tree.gsp_tree_create_child_node(node1)
#node3 = gsp_tree.gsp_tree_create_child_node(root1)
#node4 = gsp_tree.gsp_tree_create_child_node(root2)

#gsp_tree.gsp_tree_destroy_node(root1)
#
'''
view1 = gsp_view.gsp_view_create_view()
view2 = gsp_view.gsp_view_create_view()

gsp_view.gsp_view_add_child(view1, view2)

background = gcolor_t()
background.red = 1.0
background.green = 1.0
background.blue = 1.0
background.alpha = 1.0

gsp_view.gsp_view_set_background_color(view1, background)
gsp_view.gsp_view_set_window_root(window1, view1)
'''


def callback(window, event):
    print(f"python callback {event.event_id}")
    if event.event_id == 7:
        should_quit = True

callback_handle = gsp_window.EVENT_CALLBACK_TYPE(callback)

gsp_window.gsp_window_set_title(window1, "hello from python")
gsp_window.gsp_window_set_event_callback(window1, callback_handle)

#view1 = gsp_view.gsp_view_create_view()

while should_quit == False:
    print(f"should quit {should_quit}")
    gsp_window.gsp_window_poll_events()
