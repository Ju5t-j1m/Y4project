#@Author: Jimmy Norman
#@Date: 30.09.2020
#@Version: 3.0 (final)
#@Links: https://github.com/Ju5t-j1m/Y4project

# Setup and Knowledge bases #
import Writer

digit_symbol_kb = Writer.kb2_digits + Writer.kb3_legal_symbols  # continuation of sequential encoding
rebuilt_kb = Writer.kb_logical_blank + Writer.kb1_alphabet + Writer.kb4_uppercase  # combine kbs for list processing

# Key Offsets #
digit_symbol_marker = 9
second_alphabet_offset = 11
capital_letter_offset = 17
third_alphabet_offset = 21


# Start of string processing #
def reader():
    read_encHTML = """"""
    plaintext = []
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
            steg_char_num = len(splitSteg[s]) - len(encsign2) - len(splitSteg[s].rstrip(Writer.steg_char_value))  # len
            plaintext.append(rebuilt_kb[steg_char_num + third_alphabet_offset])  # offset for first space char

        # First Third and Digit/Symbol # # find the sign at the length of plain line + 1
        elif splitSteg[s].endswith(encsign, steg_char_num, steg_char_num + 1) and find2 == -1 and find3 == -1:
            steg_char_num = len(splitSteg[s]) - len(splitSteg[s].rstrip(Writer.steg_char_value))

            # Digit and Symbol check #
            if steg_char_num >= (digit_symbol_marker + 1):  # same style where first third drops at a max of 9
                plaintext.append(digit_symbol_kb[steg_char_num - digit_symbol_marker])  # removal of marker

            else:
                plaintext.append(rebuilt_kb[steg_char_num])  # otherwise this is an alphabet char

        # Second Third of Alphabet # # similar check but for encsign1 instead evaluated later
        elif splitSteg[s].endswith(encsign1, steg_char_num, steg_char_num + 1) and find2 == -1 and find3 == -1:
            steg_char_num = len(splitSteg[s]) - len(encsign1) - len(splitSteg[s].rstrip(Writer.steg_char_value))
            plaintext.append(rebuilt_kb[steg_char_num + second_alphabet_offset])  # offset of next alphabet chars

        # Capital Letters #
        elif find3 >= 0:  # removes dummy text length
            steg_char_num = len(splitSteg[s]) - len(encsign3) - len(splitSteg[s].rstrip(Writer.steg_char_value))
            plaintext.append(Writer.kb4_uppercase[steg_char_num + capital_letter_offset])

        else:
            result = ''.join(plaintext)  # final building of decoded text
            return str(result)
