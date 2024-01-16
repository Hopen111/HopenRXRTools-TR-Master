#This Script Will Delete Temporary Files In Folders So GitHub Idiot Will Work.

input("""This Script Will Delete Any Unecessary Temporary Files When Starting Up The Program 
This Will Also Delete Any Photos You Have Already Put In. Proceed? (Press ENTER)""")

import os

if os.path.exists("Input/Delete This Please.txt"):
  os.remove("Input/Delete This Please.txt")

if os.path.exists("Output/Delete This Please.txt"):
  os.remove("Output/Delete This Please.txt")

input("All Temporary Files Removed!")