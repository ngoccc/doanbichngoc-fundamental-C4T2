from Sub_Function import *

String_With_No_Dollars = Remove_Dollar_Sign("$80% percent of $life is to show $up")
if String_With_No_Dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
