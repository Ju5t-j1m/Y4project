import itertools
import string

##setup and Knowledge bases##
kb_logical_blank = ['#']
kb1_alphabet = [' ','a','b','c','d','e','f','g','h']
kb2_alphabet = ['i','j','k','l','m','n','o','p','q']
kb3_alphabet = ['r','s','t','u','v','w','x','y','z']
kb_digits = list(string.digits)
kb_legal_symbols = ['!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+', '=', '?', '@', '.']
#kb4_uppercase = list(string.ascii_uppercase)

rebuilt_kb = kb_logical_blank + kb1_alphabet + kb2_alphabet + kb3_alphabet + kb_digits + kb_legal_symbols #+ kb4_uppercase  # combine kbs for list processing

steg_char_value1 = ' '
steg_char_value2 = 'b'
steg_char_value3 = ' '
steg_char_value4 = 'c'

file = open('Stegdoc.html', 'w')  # write sample text here, will be replaced with an import option too

temp_HTML = """"""  # preserve original input

plaintext = "1u9@ t.vz"
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

    if f.startswith(('<', "", "\t")) and 1 <= rebuilt_kb.index(b) <= 10:  # first set of alphabet
        temp = (rebuilt_kb.index(b) - 1)
        if b == ' ':
            f = (steg_char_value1 + f + "<!--Auto Stub-->")
            result.append(f)
        else:
            f = ((steg_char_value1 * temp) + f)
            result.append(f)

    elif f.startswith(('<', "", "\t")) and 11 <= rebuilt_kb.index(b) <= 19:  #second set of alphabet
        temp = (rebuilt_kb.index(b) - 11)
        f = ("\t" + (steg_char_value1 * temp) + f)
        result.append(f)

    elif f.startswith(('<', "", "\t")) and 20 <= rebuilt_kb.index(b) <= 27:
        temp = (rebuilt_kb.index(b) - 20)
        f = (" \t" +(steg_char_value1 * temp) + f)
        result.append(f)

    elif f.startswith(('<', "", "\t")) and 28 <= rebuilt_kb.index(b) <= 38:
        temp = (rebuilt_kb.index(b) - 27)
        f = (steg_char_value1 * temp + f + " <!--Auto Stub-->")
        result.append(f)

    elif f.startswith(('<', "", "\t")) and 39 <= rebuilt_kb.index(b) <= 53:
        temp = (rebuilt_kb.index(b) - 39)
        f = ("\t" + steg_char_value1 * temp + f + " <!--Auto Stub-->")
        result.append(f)

    else:  # placeholder for a catch error
        result.append(f)
        print(f)

result = '\n'.join(result)
print(result)

file = open('Stegdoc.html', 'w')  # write result to created file
file.write(result)
file.close()