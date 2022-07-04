import string

# Setup and Knowledge bases #
kb_logical_blank = ['#']  # For lines that fail to encode
kb1_alphabet = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'l', 'd', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v',
                'k', 'j', 'q', 'x', 'z']  # Letter Frequency analysis order reduces size
kb2_digits = list(string.digits)  # 0-9
kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+', '=', '?', '@', '.']
kb4_uppercase = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'L', 'D', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
                 'V', 'K', 'J', 'Q', 'X', 'Z']  # Letter Frequency analysis order

digit_symbol_kb = kb2_digits + kb3_legal_symbols  # continuation of sequential encoding
rebuilt_kb = kb_logical_blank + kb1_alphabet + kb4_uppercase  # combine kbs for list processing

# Key Offsets #
digit_symbol_marker = 9
second_alphabet_offset = 11
capital_letter_offset = 17
third_alphabet_offset = 21

steg_char_value = ' '

read_encHTML = """"""  # setup to read encoded HTML

plaintext = []

print("Decode text \n")

# Start of string processing #

file = open('Stegdoc.html', 'r')  # read file
Lines = file.readlines()

for i in Lines:
    read_encHTML += str(i)
file.close()

splitSteg = read_encHTML.split('\n')  # spilt HTML encoding by line

encsign = " "  # for first third
encsign1 = "\t"  # second third
encsign2 = " \t"  # third third
encsign3 = "  <!--Auto Stub-->"  # capitals

# Start reading #
for s in range(len(splitSteg)):
    find2 = splitSteg[s].find(encsign2)  # search for encsign  in each string
    find3 = splitSteg[s].find(encsign3)

    steg_char_num = (splitSteg[s].rfind('>') + 1)  # place reader 1 position ahead of normal line

    # Third Third of alphabet #
    if find2 >= 0:
        steg_char_num = len(splitSteg[s]) - len(encsign2) - len(splitSteg[s].rstrip(steg_char_value))  # finding length
        plaintext.append(rebuilt_kb[steg_char_num + third_alphabet_offset])  # offset for first space char

    # First Third and Digit/Symbol # # find the sign at the length of plain line + 1
    elif splitSteg[s].endswith(encsign, steg_char_num, steg_char_num + 1) and find2 == -1 and find3 == -1:
        steg_char_num = len(splitSteg[s]) - len(splitSteg[s].rstrip(steg_char_value))

        # Digit and Symbol check #
        if steg_char_num >= (digit_symbol_marker + 1):  # same style where first third drops at a max of 9
            plaintext.append(digit_symbol_kb[steg_char_num - digit_symbol_marker])  # removal of marker

        else:
            plaintext.append(rebuilt_kb[steg_char_num])  # otherwise this is an alphabet char

    # Second Third of Alphabet # # similar check but for encsign1 instead evaluated later
    elif splitSteg[s].endswith(encsign1, steg_char_num, steg_char_num + 1) and find2 == -1 and find3 == -1:
        steg_char_num = len(splitSteg[s]) - len(encsign1) - len(splitSteg[s].rstrip(steg_char_value))
        plaintext.append(rebuilt_kb[steg_char_num + second_alphabet_offset])  # offset of next alphabet chars

    # Capital Letters #
    elif find3 >= 0:  # removes dummy text length
        steg_char_num = len(splitSteg[s]) - len(encsign3) - len(splitSteg[s].rstrip(steg_char_value))
        plaintext.append(kb4_uppercase[steg_char_num + capital_letter_offset])

    else:
        print("\nEnd of steg-text on line: " + str(s + 1))
        result = ''.join(plaintext)  # final building of decoded text
        print("Plaintext encoded is:\n" + result)
        quit(0)
