#File Objects
#Taking input from the input file
with open('InputFile.txt','r') as inputf:
    string = inputf.readline()

print(string)
#Doing String Operations
str_len = len(string)
words = 1
freq = 0
spaces = 0
sp_char = 0
for i in range(0,str_len):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
        freq += 1
    if string[i] == ' ':
        words += 1
        spaces += 1
    if string[i] == '!' or string[i] == '@' or string[i] == '#' or string[i] == '%' or string[i] == '&' or string[i] == '*':
        sp_char += 1
char = str_len - (spaces + sp_char)
print(str_len,freq,words,sp_char,spaces,char)

#Printing Results in the result file
with open('ResultFile.txt','w') as resultf:
    resultf.write('Length Of The String Is : %s\n' % str_len)
    resultf.write('Number Of Vowels In The String Is : %s\n' % freq)
    resultf.write('Number Of Words In The String Is : %s\n' % words)
    resultf.write('Number Of Characters In The String Is : %s\n' % char)
    resultf.write('Number Of White Spaces In The String Is : %s\n' % spaces)
    resultf.write('Number Of Special Characters In The String Is : %s\n' % sp_char)
