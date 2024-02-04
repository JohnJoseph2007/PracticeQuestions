# Link: https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
# 
# Specifications of HEX Color Code
# 
# ■ It must start with a '#' symbol.
# ■ It can have  or  digits.
# ■ Each digit is in the range of  to . ( and ).
# ■ letters can be lower case. ( and are also valid digits).
# 
# Examples
# 
# Valid Hex Color Codes
# #FFF 
# #025 
# #F0A1FB 
# 
# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
# You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
# 
# CSS Code Pattern:
# 
# Selector
# {
# 	Property: Value;
# }
# Input Format
# 
# The first line contains , the number of code lines.
# The next  lines contains CSS Codes.
# 
# Constraints
# 
# 
# 
# Output Format
# 
# Output the color codes with '#' symbols on separate lines.
# 
# Sample Input
# 
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }   
# Sample Output
# 
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
# Explanation
# 
# #BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.
# 
# Hence, the valid color codes are:
# 
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
# 
# Note: There are no comments ( // or /* */) in CSS Code.

# CODE HERE :

def ishex(m):
    final = True
    hextotal = "1234567890abcdef"
    for i in m.lower():
        if i in hextotal:
            continue
        else:
            final = False
    return final


n = int(input())
l = []
for i in range(n):
    l.append(input())
hcl = []
for i in range(n-1):
    sp = l[i].strip().split()
    spn = l[i+1].strip().split()
    for j in sp:
        if '#' in j:
            indexof = j.find("#")
        slice = ""
        for k in range(indexof, len(j)):
            if j[k]=="#" or ishex(j[k]):
                slice+=j[k]

        if slice.startswith('#') and spn[0]!="{":
            m = slice[1:len(slice)-1]
            if ishex(m) and (len(m)==3 or len(m)==6):
                hcl.append(slice[:-1])

for i in hcl:
    print(i)

# Status: Finished