import itertools
import string
import time

# Setup and Knowledge bases #

kb_logical_blank = ['#']  # For lines that fail to encode
kb1_alphabet = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'l', 'd', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v',
                'k', 'j', 'q', 'x', 'z']  # Letter Frequency analysis order reduces size
kb2_digits = list(string.digits)  # 0-9
kb3_legal_symbols = [' ', '!', '$', '%', '&', '*', '(', ')', ':', ';', '-', '+', '=', '?', '@', '.']
kb4_uppercase = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'L', 'D', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
                 'V', 'K', 'J', 'Q', 'X', 'Z']  # Letter Frequency analysis order

rebuilt_kb = kb_logical_blank + kb1_alphabet + kb2_digits + kb3_legal_symbols + kb4_uppercase  # combine kbs for process

steg_char_value = ' '


# writer passed both plaintext and html_file from the instance of user interface
def writer(plaintext, html_file):
    file = open('Stegdoc.html', 'w')  # write sample text here, will be replaced with an import option too
    temp_HTML = """"""  # preserve original input

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
    result = []

    plain_list = list(plaintext.strip(" "))  # convert to list

    # may be a requirement that the sample is longer to fully encode

    # writer will default to default_HTML if there is no valid text present to encode
    if html_file == "" or html_file.find('>') == -1:
        file.write(default_HTML)
    else:
        file.write(html_file)

    file.close()

    # Start of string processing #

    file = open('Stegdoc.html', 'r')  # read file
    lines = file.readlines()

    for i in lines:
        temp_HTML += str(i)
        file.close()

    split = temp_HTML.split('\n')  # split document by newlines
    print(split)

    # Start of Encoding #

    for f, b in itertools.zip_longest(split, plain_list, fillvalue='#'):

        # First Third of Alphabet #
        if f.endswith(('>', "", "\t")) and not b.isupper() and 1 <= rebuilt_kb.index(b) <= 9:  # from e - r (LFA order)
            temp = rebuilt_kb.index(b)  # power value for space
            f = (f + (steg_char_value * temp))  # combining to the end of the string
            result.append(f)

        # Second Third of Alphabet #
        elif f.endswith(('>', "", "\t")) and not b.isupper() and 10 <= rebuilt_kb.index(b) <= 18:  # from r - y
            temp = (rebuilt_kb.index(b) - 10)  # offset by 10 to start a new batch of up to 8 spaces
            f = (f + "\t" + (steg_char_value * temp))  # encoded with a tab marker
            result.append(f)

        # Third Third of Alphabet #
        elif f.endswith(('>', "", "\t")) and not b.isupper() and 19 <= rebuilt_kb.index(b) <= 26:  # from p - z
            temp = (rebuilt_kb.index(b) - 19)
            f = (f + " \t" + (steg_char_value * temp))  # encoded with a tab space marker
            result.append(f)

        # Digits and Symbols #
        elif f.endswith(('>', "", "\t")) and not b.isupper() and 28 <= rebuilt_kb.index(b) <= 54:  # from 0..9 - ' '..'.
            temp = (rebuilt_kb.index(b) - (len(kb_logical_blank) + len(kb1_alphabet)))  # first third type removes kb-
            f = (f + (steg_char_value * 9) + (steg_char_value * temp))  # will evaluate as any space > 9
            result.append(f)

        # Capital Letters #
        elif f.endswith(('>', "", "\t")) and b.isupper():
            temp = (rebuilt_kb.index(b)) - len(rebuilt_kb) + len(kb4_uppercase) + 1
            f = (f + "  <!--Auto Stub-->" + (steg_char_value * temp))  # uses a fake comment as a marker
            result.append(f)

        else:  # appends any line that can't or does not need processing
            result.append(f)

    # Combining and Error Handling #
    try:
        result = '\n'.join(result)

        if result.find('#') >= 0:
            raise ValueError("Value incompatible range")
        else:
            return result

    except ValueError as e:
        print("\n\n" + str(e), "error occurred...Exiting")
        time.sleep(2)
        quit(1)

    file = open('Stegdoc.html', 'w')  # write result to created file
    file.write(result)
    file.close()
    # quit(0)
