import itertools
import string

##setup and Knowledge bases##
kb_logical_blank = ['#']
kb1_alphabet = list(string.ascii_lowercase)
kb2_digits = list(string.digits)
kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+', '=', '?', '@', '.']
kb4_uppercase = list(string.ascii_uppercase)

rebuilt_kb = kb_logical_blank + kb1_alphabet + kb2_digits + kb3_legal_symbols + kb4_uppercase  # combine kbs for list processing

steg_char_value1 = 'a'
steg_char_value2 = 'b'
steg_char_value3 = ' '
steg_char_value4 = 'c'

file = open('Stegdoc.html', 'w')  # write sample text here, will be replaced with an import option too

temp_HTML = """"""  # preserve original input

plaintext = "At4st-Zext"
plain_list = list(plaintext.strip(" "))

result = []

##if no manual input##
default_HTML = """<!DOCTYPE html>
<html>
<body>

<p>This is a paragraph.</p>
<p>This is a paragraph.</p>
<p>This is a paragraph.</p>
<p>This is a paragraph.</p>
<p>This is a paragraph.</p>

</body>
</html>"""

file.write(default_HTML)
file.close()

######start of string processing##

file = open('Stegdoc.html', 'r')
Lines = file.readlines()

for i in Lines:
    temp_HTML += str(i)
file.close()

split = temp_HTML.split('\n')
print(split)

for f, b in itertools.zip_longest(split, plain_list,
                                  fillvalue='#'):  # going to need to catch the error that comes from f > b or b > f

    if f.endswith('>') and not b.isupper():  # catches normal line cases
        temp = rebuilt_kb.index(b)
        f = (f + (steg_char_value1 * temp))
        result.append(f)


    elif f.endswith("") and not f.endswith(">") and not b.isupper():  #catches spaces and other unstyled lines
        temp = rebuilt_kb.index(b)
        f = (f + (steg_char_value2 * temp))
        result.append(f)

    elif (f.endswith("") or f.endswith('>')) and b.isupper():
        temp = (rebuilt_kb.index(b)) - len(rebuilt_kb) + len(kb4_uppercase) + 1
        f = (f + "  <!--Auto Stub-->" + (steg_char_value4 * temp))
        result.append(f)

    else:  # placeholder for a catch error
        result.append(f)
        print(f)

result = '\n'.join(result)
print(result)

file = open('Stegdoc.html', 'w')  # write result to created file
file.write(result)
file.close()
