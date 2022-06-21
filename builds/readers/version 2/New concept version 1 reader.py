import string

##setup and Knowledge bases##
kb_logical_blank = ['#']
kb1_alphabet = [' ','a','b','c','d','e','f','g','h']
kb2_alphabet = ['i','j','k','l','m','n','o','p','q']
kb3_alphabet = ['r','s','t','u','v','w','x','y','z']
#kb2_digits = list(string.digits)
#kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+', '=', '?', '@', '.']
#kb4_uppercase = list(string.ascii_uppercase)

rebuilt_kb = kb_logical_blank + kb1_alphabet + kb2_alphabet + kb3_alphabet #+ kb2_digits + kb3_legal_symbols + kb4_uppercase  # combine kbs for list processing

steg_char_value1 = ' '
steg_char_value2 = '\t'
steg_char_value3 = ' '
steg_char_value4 = 'c'

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

encsign = " "
encsign1 = "\t"
encsign2 = " \t"
encsign3 = "<!--Auto Stub-->"

for s in range(len(splitSteg)):
     find3 = splitSteg[s].find(encsign3)
         #start reading

         #steg_char_num_a = len(splitSteg[s])-len(splitSteg[s].lstrip(steg_char_value1)) #length of each line - the length of the non whitespace
         #steg_char_num_b = len(splitSteg[s])-len(splitSteg[s].rstrip(steg_char_value2))
         #steg_char_num_c = len(splitSteg[s]) - find - len(encsign3) #length of each line - first occurence of encode syntax(everything before) - length of the encode syntax


     if (splitSteg[s].startswith(encsign) and not splitSteg[s].startswith(encsign1) and not splitSteg[s].startswith(encsign2)) and not splitSteg[s].find(encsign3) != -1:
         steg_char_num_a = len(splitSteg[s]) - len(splitSteg[s].lstrip(steg_char_value1))
         plaintext.append(rebuilt_kb[steg_char_num_a + 1])
         print("first third")

     elif (splitSteg[s].startswith(encsign1) and not splitSteg[s].startswith(encsign) and not splitSteg[s].startswith(encsign2))and not splitSteg[s].find(encsign3) != -1:
         tab_cleaned_line = splitSteg[s].replace('\t','')
         steg_char_num_b = len(tab_cleaned_line) - len(tab_cleaned_line.lstrip(steg_char_value1))
         plaintext.append(rebuilt_kb[steg_char_num_b + 11])
         print ("second third")

     elif (splitSteg[s].startswith(encsign2)):
         space_tab_cleaned_line = splitSteg[s].replace(" \t", '')
         steg_char_num_b = len(space_tab_cleaned_line) - len(space_tab_cleaned_line.lstrip(steg_char_value1))
         plaintext.append(rebuilt_kb[steg_char_num_b + 20])
         print("third third")

     elif (splitSteg[s].find(encsign3) != -1):
          print("space")
          plaintext.append(' ')

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
