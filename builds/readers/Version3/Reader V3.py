import string

##setup and Knowledge bases##
kb_logical_blank = ['#']
kb1_alphabet = ['e','t','a','o','i','n','s','h','r','l','d','c','u','m','w','f','g','y','p','b','v','k','j','q','x','z'] #LFA order
kb2_digits = list(string.digits)
kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+','=', '?', '@', '.']
kb4_uppercase = ['E','T','A','O','I','N','S','H','R','L','D','C','U','M','W','F','G','Y','P','B','V','K','J','Q','X','Z']

digit_symbol_kb = kb2_digits + kb3_legal_symbols
rebuilt_kb = kb_logical_blank + kb1_alphabet + kb4_uppercase #combine kbs for list processing

steg_char_value1 = ' '
steg_char_value2 = ' '
steg_char_value3 = ' '
steg_char_value4 = ' '

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
encsign3 = "  <!--Auto Stub-->"

for s in range(len(splitSteg)):
     find2 = splitSteg[s].find(encsign2)
     find3 = splitSteg[s].find(encsign3)
        #start reading

     print("FOUND CHAR: "+ str(find2))

     steg_char_num_a = (splitSteg[s].rfind('>') + 1)
     #print (str(steg_char_num_a))
     steg_char_num_b = (splitSteg[s].rfind('>') + 1)
     #print(str(steg_char_num_b))
     #steg_char_num_c = len(splitSteg[s]) - find - len(encsign3) #length of each line - first occurence of encode syntax(everything before) - length of the encode syntax


     if (find2 >= 0):
         steg_char_num_b = len(splitSteg[s]) - len(encsign2) - len(splitSteg[s].rstrip(steg_char_value1))
         plaintext.append(rebuilt_kb[steg_char_num_b + 21])
         print(str(steg_char_num_b) + " :third third")

     elif (splitSteg[s].endswith(encsign,steg_char_num_a,steg_char_num_a + 1) and not splitSteg[s].endswith(encsign1,steg_char_num_b,steg_char_num_b + 1) and find2 == -1 and find3 == -1):
         steg_char_num_a = len(splitSteg[s]) - len(splitSteg[s].rstrip(steg_char_value1))

         if steg_char_num_a >= 10:
             plaintext.append(digit_symbol_kb[steg_char_num_a - 9])
             print(str(steg_char_num_a) + " :Digit or Symbol")
         else:
             plaintext.append(rebuilt_kb[steg_char_num_a])
             print(str(steg_char_num_a) + " :first third")

     elif (splitSteg[s].endswith(encsign1,steg_char_num_b,steg_char_num_b + 1) and not splitSteg[s].endswith(encsign,steg_char_num_a,steg_char_num_a + 1) and find2 == -1 and find3 == -1):
         steg_char_num_b = len(splitSteg[s]) - len(encsign1) - len(splitSteg[s].rstrip(steg_char_value1))
         plaintext.append(rebuilt_kb[steg_char_num_b + 11])
         print(str(steg_char_num_b) + " :second third")

     elif (find3 >= 0):
         steg_char_num_b = len(splitSteg[s]) - len(encsign3) - len(splitSteg[s].rstrip(steg_char_value1))
         plaintext.append(kb4_uppercase[steg_char_num_b + 17])
         print(str(steg_char_num_b) + " :Capital letter")


     else:
          print("\nLINE SKIPPED!!!: " + str(s))
          print("end of steg-text on line: " + str (s + 1))
          result = ''.join(plaintext)
          print("Plaintext encoded is:\n" + result)
          break
