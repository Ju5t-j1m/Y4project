import itertools
import string

##setup and Knowledge bases##
kb_logical_blank = ['#']
kb1_alphabet = ['e','t','a','o','i','n','s','h','r','l','d','c','u','m','w','f','g','y','p','b','v','k','j','q','x','z'] #LFA order
kb2_digits = list(string.digits)
kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+', '=', '?', '@', '.']
kb4_uppercase = ['E','T','A','O','I','N','S','H','R','L','D','C','U','M','W','F','G','Y','P','B','V','K','J','Q','X','Z']

rebuilt_kb = kb_logical_blank + kb1_alphabet + kb2_digits + kb3_legal_symbols + kb4_uppercase  # combine kbs for list processing

steg_char_value1 = ' '
steg_char_value2 = ' '
steg_char_value3 = ' '
steg_char_value4 = ' '

file = open('Stegdoc.html', 'w')  # write sample text here, will be replaced with an import option too

temp_HTML = """"""  # preserve original input

plaintext = "H4@lo"
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

    if f.endswith(('>',"","\t")) and not b.isupper() and 1 <= rebuilt_kb.index(b) <= 9:  # catches normal line cases
        temp = rebuilt_kb.index(b)
        f = (f + (steg_char_value1 * temp))
        result.append(f)

    elif f.endswith(('>',"","\t")) and not b.isupper() and 10 <= rebuilt_kb.index(b) <= 18:
        temp = (rebuilt_kb.index(b) - 10)
        f = (f + "\t" + (steg_char_value1 * temp))
        result.append(f)

    elif f.endswith(('>',"","\t")) and not b.isupper() and 19 <= rebuilt_kb.index(b) <= 26:
        temp = (rebuilt_kb.index(b) - 19)
        f = (f + " \t" + (steg_char_value1 * temp))
        result.append(f)

    elif f.endswith(('>', "", "\t")) and not b.isupper() and 28 <= rebuilt_kb.index(b) <= 54:
        temp = (rebuilt_kb.index(b) - (len(kb_logical_blank) + len(kb1_alphabet)))
        print(str(temp) +  "length")
        f = (f + (steg_char_value4 * 9) + (steg_char_value4 * temp))
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
