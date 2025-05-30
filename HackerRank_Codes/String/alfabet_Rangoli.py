
# read the input
n= int(input().strip())

# width of center row
w= (n-1)*2 + ((n*2)-1)
# (n-1) *2 = total number of hyphen
# (n*2)-1 = total charecter in center
#print(chr(97-1))

# Upper Half exclusing middle line
for i in range(1, n):
    number_of_letter=(i*2) -1 # 1-1, 2-3, 3-5, 4-7
    s=""
    letter_value = 97 + n-1 # start from a to a,b,c,d
    for i in range(number_of_letter):
        if i !=0:
            s += "_"
        s += chr(letter_value)
        if i < (letter_value -1)/2:
            letter_value = letter_value-1
        else:
            letter_value = letter_value +1
    print(s.center(w,"_"))
