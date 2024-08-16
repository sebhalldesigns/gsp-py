from core.native import gsp_list

list1 = gsp_list.gsp_list_create_list()
list2 = gsp_list.gsp_list_create_list()
list3 = gsp_list.gsp_list_create_list()

gsp_list.gsp_list_destroy_list(list1)
gsp_list.gsp_list_destroy_list(list2)
gsp_list.gsp_list_destroy_list(list3)