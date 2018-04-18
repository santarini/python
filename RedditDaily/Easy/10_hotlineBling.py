import re
def testForPhone(test):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.findall(test)
    print(mo)
    phoneNumRegex = re.compile(r'\(\d\d\d\)\s?\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.findall(test)
    print(mo)
    phoneNumRegex = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
    mo = phoneNumRegex.findall(test)
    print(mo)

test = 'Call me at 415-555-1011 tomorrow. (415) 555-9999 is my office. 415.555.1999 is my land line.'
testForPhone(test)


import re
def testForPhone2(test):
    phoneNumRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|\.|\-)?
        \d{3}
        (\s|\.|\-)
        \d{4}
        )''', re.VERBOSE)
    mo = phoneNumRegex.findall(test)
    print(mo)
    

test = 'Call me at 415-555-1011 tomorrow. (415) 555-9999 is my office. 415.555.1999 is my land line.'
testForPhone2(test)
