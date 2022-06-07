
##setup and Knowledge bases##
kb1 = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']
kb2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+',
       '=', '?', '@', '.']

rebuilt_kb = kb1 + kb2 #combine kbs for list processing

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

         steg_char_num_a = len(splitSteg[s])-len(splitSteg[s].rstrip('a'))
         steg_char_num_b = len(splitSteg[s])-len(splitSteg[s].rstrip('b'))

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

for x in range(len(kb1)):
     print (kb1[x])


for y in range(len(kb2)):
     print (kb2[y])
