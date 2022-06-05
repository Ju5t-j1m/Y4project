import itertools

##setup and Knowledge bases##
kb1 = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
       'v', 'w', 'x', 'y', 'z']
kb2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+',
       '=', '?', '@', '.']

rebuilt_kb = kb1 + kb2 #combine kbs for list processing

file = open('Stegdoc.html', 'w') #write sample text here, will be replaced with an import option too

temp_HTML = """""" #preserve original input

plaintext = "at4st-text"
plain_list = list(plaintext.strip(" "))
print(plain_list)

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
# split = list(filter(None, split))

print(split)

for f, b in itertools.zip_longest(split, plain_list,
                                  fillvalue='#'):  # going to need to catch the error that comes from f > b or b > f

    if f.endswith('>'): #catches normal line cases
        temp = rebuilt_kb.index(b)
        f = (f + ('a' * temp))
        result.append(f)
        # print ((rebuilt_kb.index(u) - 26))
        # print (f)

    elif f.endswith("") and not f.endswith(">"): #catches spaces and other unstyled lines
        temp = rebuilt_kb.index(b)
        f = (f + ('b' * temp))
        result.append(f)

        # print ((rebuilt_kb.index(u)))
        # print(f)

    else:                              #placeholder for a catch error
        result.append(f)
        print(f)

result = '\n'.join(result)

print(result)

# temp_HTML = '\n'.join(split)

# print (temp_HTML)

file = open('Stegdoc.html', 'w')     #write result to created file
file.write(result)
file.close()

##testing##

for x in range(len(kb1)):
     print (kb1[x])


for y in range(len(kb2)):
     print (kb2[y])
