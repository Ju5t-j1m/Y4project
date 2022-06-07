import string

##setup and Knowledge bases##
kb_logical_blank = ['#']
kb1_alphabet = list(string.ascii_lowercase)
kb2_digits = list(string.digits)
kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+','=', '?', '@', '.']

rebuilt_kb = kb_logical_blank + kb1_alphabet + kb2_digits + kb3_legal_symbols #combine kbs for list processing

steg_char_value1 = 'a'
steg_char_value2 = 'b'
steg_char_value3 = ' '

read_encHTML = """""" #setup to process strings

plaintext = []

print("Decode text \n")
######start of string processing##

file = open('Stegdoc.html', 'r')
Lines = file.readlines()

for i in Lines:
    read_encHTML += str(i)
file.close()

splitSteg = read_encHTML.split('\n')
# split = list(filter(None, split))

print(splitSteg)

encsign = "a"
encsign1 = "b"
encsign2 = " "

for s in range(len(splitSteg)):

     if (splitSteg[s].endswith(encsign) or splitSteg[s].endswith(encsign1)): #reduce to how many steg factors you have
         #start reading

         steg_char_num_a = len(splitSteg[s])-len(splitSteg[s].rstrip(steg_char_value1))
         steg_char_num_b = len(splitSteg[s])-len(splitSteg[s].rstrip(steg_char_value2))

         if (steg_char_num_a != 0):

             plaintext.append(rebuilt_kb[steg_char_num_a])

             print(steg_char_num_a)
         elif (steg_char_num_b != 0):
             plaintext.append(rebuilt_kb[steg_char_num_b])
             print (steg_char_num_b)

     else:
         print("end of steg-text on line: " + str (s + 1))
         #print(plaintext)
         result = ''.join(plaintext)
         print("Plaintext encoded is:\n" + result)
         break



#result = '\n'.join(result)

#print(result)

# temp_HTML = '\n'.join(split)

# print (temp_HTML)



##testing##

for x in range(len(kb1_alphabet)):
     print (kb1_alphabet[x])


for y in range(len(kb2_digits)):
     print (kb2_digits[y])
