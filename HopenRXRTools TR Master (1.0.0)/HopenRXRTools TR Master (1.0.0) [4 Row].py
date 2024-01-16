VERSION = "1.0.0"
DISPLAYVERSION = "1.0.0"

Filenamefix = """ " """
Filenamefix2 = Filenamefix[1:2]

def prRed(skk):print("\033[31m {}\033[00m".format(skk))
def inRed(skk):input("\033[31m {}\033[00m".format(skk))

def prYellow(skk): print("\033[33m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

import os
  
# Opening the html file 
try:
    HTMLFile = open("Input/index.html", 'r') 
    index = HTMLFile.read() 
except:
    inRed("""
No HTML File Found!
""")

index = index.replace("TABLE", "table")
index = index.replace("TITLE", "title")
index = index.replace("HTML", "html")
index = index.replace("HEAD", "head")
index = index.replace("FACE", "face")
index = index.replace("IMG", "img")
index = index.replace("FONT", "font")
index = index.replace("CENTER", "center")
index = index.replace("BORDER", "border")
index = index.replace("BODY", "body")
index = index.replace("HREF", "href")
index = index.replace("<P", "<p")
index = index.replace("</P>", "</p>")
index = index.replace("<BR>", "<br>")
index = index.replace("WIDTH", "width")
index = index.replace("HEIGHT", "height")
index = index.replace("ALIGN", "align")
index = index.replace("VALIGN", "valign")
index = index.replace("COLSPAN", "colspan")
index = index.replace("<TR>", "<tr>")
index = index.replace("</TR>", "</tr>")
index = index.replace("<TD ", "<td ")
index = index.replace("</TD>", "</td>")

#---------------------------------------------------------------------------

Last_Update_Style = ""
Info_Style = ""

if index.find(".style1 {font-size: 10px}") != -1:
    Last_Update_Style = "style1"

elif index.find(""".style1 {font-size: 10px;
	font-weight: bold;
}""") != -1:
    Last_Update_Style = "style1"

elif index.find(""".info1 {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 10px;
	font-style: italic;
	line-height: normal;
	font-weight: bold;
	font-variant: normal;
	color: #FFF;
	text-align: center;
}""") != -1:
    Last_Update_Style = "info1"

elif index.find(""".style1 {	font-size: 10px;
	font-weight: bold;
}""") != -1:
    Last_Update_Style = "style1"

elif index.find(""".style2 {font-size: 10px}
body,td,th {
	color: #FFFFFF;
	text-align: center;
}""") != -1:
    Last_Update_Style = "style2"

elif index.find(".style3 {font-size: 10px}") != -1:
    Last_Update_Style = "style3"

elif index.find(""".style3 {
	font-size: 10px;
	font-weight: bold;
	font-family: Arial, Helvetica, sans-serif;
	font-style: italic;
}""") != -1:
    Last_Update_Style = "style3"

elif index.find(""">Arizona Crossings</""") != -1:
    Last_Update_Style = "style3"

elif index.find(".style4 {font-size: 10px}") != -1:
    Last_Update_Style = "style4"

elif index.find(""".style4 {	FONT-SIZE: 10px
}""") != -1:
    Last_Update_Style = "style4"
else:
    Last_Update_Style = "style1"

#---------------------------------------------------------------------------

if index.find(""".style1 {
	font-size: 10px;
	font-weight: bold;
	font-style: italic;
}""") != -1:
    Info_Style = "style1"

elif index.find(""".style2 {font-size: 10px}
body,td,th {
	color: #FFFFFF;
	text-align: center;
}""") != -1:
    Info_Style = "style2"

elif index.find(""".style2 {
	font-size: 10px;
	font-weight: bold;
	font-style: italic;
}""") != -1:
    Info_Style = "style2"

elif index.find(""".style3 {
	font-family: Arial, Helvetica, sans-serif;
	font-weight: bold;
	font-style: italic;
	font-size: 10px;
}""") != -1:
    Info_Style = "style3"

elif index.find(""".style5 {font-size: 18px}
p {
	margin: 0px;
}""") != -1:
    Info_Style = "style5"

elif index.find(""".style6 {
	font-size: 10px;
	font-family: Arial, Helvetica, sans-serif;
	font-weight: bold;
	font-style: italic;
}""") != -1:
    Info_Style = "style6"

elif index.find(""".style6 {
	font-size: 10px;
	font-family: Arial, Helvetica, sans-serif;
	font-weight: bold;
	font-style: italic;
}""") != -1:
    Info_Style = "style6"

else:
    Info_Style = "style2"

#---------------------------------------------------------------------------

if index.find(""".Streets {""") != -1:
    Text_Style = "Streets"

else:
    Text_Style = "Street_Name"

#---------------------------------------------------------------------------

print("""--HopenRXRTools TR Master (4 Row Edition) """+VERSION+"""--""")
print("--Created by Hopen111--")

print("""
Please Fill Out The Info Below.
""")

Town_Name = input("Town Name? ")
Town_Image = input("Town Image Url? ")
Town_Type = input("Town Label Type? ")

if Town_Type == "img" or Town_Type == "Img" or Town_Type == "IMG" or Town_Type == "Image" or Town_Type == "image" or Town_Type == "png" or Town_Type == "PNG" or Town_Type == "Png":
    Town_Type = "png"
    print("Town Label Type == Image")
else:
    Town_Type = "txt"
    print("Town Label Type == Text")

if Town_Type == "png":
    Town_Url = input("Town Label Url? ")

    Header = """<div align="center"><img src="""+Filenamefix2+Town_Url+Filenamefix2+""" align="middle"></div>"""
else:
    print("""
Header Color Examples:
Defunct (Black): """+Filenamefix2+"""D"""+Filenamefix2+"""
Normal (White): """+Filenamefix2+"""N"""+Filenamefix2+"""
Uncommon (Yellow): """+Filenamefix2+"""U"""+Filenamefix2+"""
Rare (Green): """+Filenamefix2+"""R"""+Filenamefix2+"""
""")

    Header_Color = input("Header Color Type? ")

    if Header_Color == "D" or Header_Color == "D " or Header_Color == "d" or Header_Color == "d ":
        Header = """<div class="""+Filenamefix2+Text_Style+Filenamefix2+""" align="center"><span style="color: rgb(51, 51, 51);">"""+Town_Name+"""</span></div>"""
    elif Header_Color == "N" or Header_Color == "N " or Header_Color == "n" or Header_Color == "n " or Header_Color == "":
        Header = """<div class="""+Filenamefix2+Text_Style+Filenamefix2+""" align="center"><span style="color: rgba(255,255,255,1);">"""+Town_Name+"""</span></div>"""
    elif Header_Color == "U" or Header_Color == "U " or Header_Color == "u" or Header_Color == "u ":
        Header = """<div class="""+Filenamefix2+Text_Style+Filenamefix2+""" align="center"><span style="color: rgb(255, 204, 51);">"""+Town_Name+"""</span></div>"""
    elif Header_Color == "R" or Header_Color == "R " or Header_Color == "r" or Header_Color == "r ":
        Header = """<div class="""+Filenamefix2+Text_Style+Filenamefix2+""" align="center"><span style="color: rgb(0, 153, 0);">"""+Town_Name+"""</span></div>"""

Last_Update = input("Date Updated? ")

Photo_Count = input("Photo Count? ")

Video_Question = input("Video Count? ")
if Video_Question == "0" or Video_Question == "0 ":
    Video_Count = """<span class="""+Filenamefix2+Info_Style+Filenamefix2+""">VIDEOS: 0</span>"""
else:
    Video_Count = """<span class="""+Filenamefix2+Info_Style+Filenamefix2+""">VIDEOS: """+Video_Question+"""<span style="color: #0F0"> (+"""+Video_Question+""")</span></span>"""

Crossing_Question = input("Grade Crossings Count? ")
if Crossing_Question == "0" or Crossing_Question == "0 ":
    Crossing_Count = """<span class="""+Filenamefix2+Info_Style+Filenamefix2+"""><font face="Arial,Helvetica,Monaco">GRADE CROSSINGS: 0</font></span>"""
else:
    Crossing_Count = """<span class="""+Filenamefix2+Info_Style+Filenamefix2+"""><font face="Arial,Helvetica,Monaco">GRADE CROSSINGS: """+Crossing_Question+""" <span style="color: #00FF00">(+"""+Crossing_Question+""")</span></font></span>"""

#---------------------------------------------------------------------------

new_html = """<td valign="bottom" width="25%"><p align="center"><a href="""+Filenamefix2+Town_Name+Filenamefix2+"""><img src="""+Filenamefix2+Town_Image+Filenamefix2+""" alt="" style="border: 0px solid ;" hspace="0"></a></p>
      <p align="center">&nbsp;</p>
      <table style="color: rgb(255, 204, 51);" border="0" cellpadding="0" cellspacing="0" height="37" width="100%">
        <tbody>
          <tr>
            <td>"""+Header+"""</td>
          </tr>
        </tbody>
      </table>
      <p align="center"><span class="""+Filenamefix2+Last_Update_Style+Filenamefix2+""">&nbsp;<font face="Arial,Helvetica,Monaco"><b>LAST 
        UPDATE:</b></font></span><br>
        <b><i><font size="4"><font face="Arial,Helvetica,Monaco">"""+Last_Update+"""</font></font></i></b><br>
        <span class="""+Filenamefix2+Info_Style+Filenamefix2+"""><font face="Arial,Helvetica,Monaco">PHOTOS: """+Photo_Count+""" <span style="color: #00FF00">(+"""+Photo_Count+""") </span>| </font></span><font face="Arial,Helvetica,Monaco">"""+Video_Count+"""</font></p>
      <p align="center">"""+Crossing_Count+"""</p></td>"""

#Stuff gets complicated past this poai t

tr_list = []
td_list = []
td_end_list = []

def get_html(td_list_num):
    return index[td_list[td_list_num]:td_end_list[td_list_num]]

sub_string = "<tr>"
count_er=0
start_index=0

removehalf = 4

for i in range(len(index)):
    j = index.find(sub_string,start_index)
    if(j!=-1):
        if removehalf == 1:
            tr_list.append(start_index-1)
            removehalf = removehalf+1
        else:
            removehalf = removehalf+1
            if removehalf >= 6:
                removehalf = 1
        start_index = j+1
        count_er+=1

sub_string = "</tr>"
count_er2=0
start_index=0

for i in range(len(index)):
    j = index.find(sub_string,start_index)
    if(j!=-1):
        start_index = j+1
        count_er2+=1
        if count_er2 == count_er:
            tr_list.append(start_index+4)

sub_string = "<td "
count_er=0
start_index=0

for i in range(len(index)):
    j = index.find(sub_string,start_index)
    if(j!=-1):
        if count_er!=0 and count_er!=1:
            td_list.append(start_index-1)
        start_index = j+1
        count_er+=1

td_start_index = start_index

sub_string = "</td>"
count_er=0
start_index=0

removehalf = 0

for i in range(len(index)):
    j = index.find(sub_string,start_index)
    if(j!=-1):
        if removehalf == 1 and count_er>=3:
            td_end_list.append(start_index+4)
            removehalf = 0
        else:
            if removehalf == 0:
                removehalf = 1
        start_index = j+1
        count_er+=1

td_end_start_index = start_index

IndexValue = int(input("Insert Where? "))

final_list = []

new_list = []

for i in range(IndexValue-1):
    new_list.append(index[td_list[i]:td_end_list[i]])

new_list.append(new_html)

for i in range(len(td_list)-IndexValue+1):
    try:
        new_list.append(index[td_list[i+IndexValue-1]:td_end_list[i+IndexValue-1]])
    except:
        print("Something Just Happened.")
       
final_list = ""
trrow = 1
for i in range(len(new_list)):
    if trrow == 5:
        final_list = final_list+"""</tr>
  <tr>"""
        trrow = 1
    final_list = final_list+str(new_list[i])+" "
    trrow = trrow+1
if trrow != 1:
    for i in range(5-trrow):
        if trrow != 4 or removehalf == 1:
            final_list = final_list+"""<td valign="bottom"><p align="center">&nbsp;</p></td>"""

if removehalf == 1 and trrow == 5:
    td_end_list.append(td_end_start_index+4)
    td_list.append(td_start_index-1)
    new_list.append(index[td_list[len(td_list)-1]:td_end_list[len(td_list)-1]])
    final_list = final_list+"""</tr>
  <tr>"""
    final_list = final_list+str(new_list[len(new_list)-1])+" "
    for i in range(3):
        final_list = final_list+"""<td valign="bottom"><p align="center">&nbsp;</p></td>"""
    

final_list = final_list+"""</tr>"""

input("Output the thing (may crash)")

f = open('Output/index.html', 'w')

greg = index[0:tr_list[0]+4]+final_list+index[tr_list[len(tr_list)-1]:len(index)]

# writing the code into the file
f.write(str(greg))

# close the file
f.close()

input("Program has not crashed! :D" )