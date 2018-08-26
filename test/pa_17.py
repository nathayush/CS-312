txt = "1 2 3 4 5"
str1 = "1 2"
str2 = "2"

length = len(str1)
for i in range(0, len(txt)-length):
    if txt[i:i+length] == str1:
        txt = txt[:i] + str2 + txt[i+length:]

sub_txt = txt
