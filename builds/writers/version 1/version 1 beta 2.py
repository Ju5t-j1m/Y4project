import itertools

##setup and Knowledge bases##
kb1 = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']
kb2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+',
       '=', '?', '@', '.']

rebuilt_kb = kb1 + kb2 #combine kbs for list processing

steg_char_value1 = 'a'
steg_char_value2 = 'b'
steg_char_value3 = ' '

file = open('Stegdoc.html', 'w') #write sample text here, will be replaced with an import option too

temp_HTML = """""" #preserve original input

plaintext = "at4st-text"
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
    
    if f.endswith('>'): #catches normal line cases
        temp = rebuilt_kb.index(b)
        f = (f + (steg_char_value1 * temp))
        result.append(f)

    elif f.endswith("") and not f.endswith(">"): #catches spaces and other unstyled lines
        temp = rebuilt_kb.index(b)
        f = (f + (steg_char_value2 * temp))
        result.append(f)


    else:                              #placeholder for a catch error
        result.append(f)
        print(f)

result = '\n'.join(result)
print(result)

file = open('Stegdoc.html', 'w')     #write result to created file
file.write(result)
file.close()
