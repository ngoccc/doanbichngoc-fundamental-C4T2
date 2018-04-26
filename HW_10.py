from Sub_Function import *
Even_List = Get_Even_List([1, 2, 5, -10, 9, 6])

if set(Even_List) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")

