from core.native import gsp_list, gsp_window
import sys

window1 = gsp_window.gsp_window_create_window()
should_quit = False

def callback(window, event):
    print(f"python callback {event.event_id}")
    if event.event_id == 7:
        should_quit = True

callback_handle = gsp_window.EVENT_CALLBACK_TYPE(callback)

gsp_window.gsp_window_set_title(window1, "hello from python")
gsp_window.gsp_window_set_event_callback(window1, callback_handle)

while should_quit == False:
    print(f"should quit {should_quit}")
    gsp_window.gsp_window_poll_events()
