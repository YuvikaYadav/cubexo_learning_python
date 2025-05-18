# A Regular Expression or RegEx is a special sequence of characters that uses a search pattern to find a string or set of strings.

# It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns.

# built-in module named “re”
# import re

# searching a string "module"

# # re.search()

# import re

# match = re.search(r"module", "You can use RegEx in Python after importing re module")
# print(f"start index: {match.start()}")
# print(f"end index: {match.end()}")

# re.findall()

# import re

# regex = '\d+'
# match = re.findall(regex,"Hello my Number is 123456789 and my friend's number is 987654321")
# print(match)

# re.compile()

# import re

# p = re.compile('[a-e]')
# print(p.findall("Regular expressions are compiled into pattern objects"))

# import re
# p = re.compile('\d')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))    #gives single digits

# p = re.compile('\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))   #gives sequences of digits

# import re

# p = re.compile('\w')
# print(p.findall("He said * in some_lang."))         #gives list of characters(words)

# p = re.compile('\w+')
# print(p.findall("I went to him at 11 A.M., he \said *** in some_language."))        #gives sequence of characters(words)

# p = re.compile('\W')
# print(p.findall("he said *** in some_language."))       #gives non words

# import re

# p = re.compile('ab*')
# print(p.findall("ababbaabbb"))          #find all a's followed by any number of b'said

# from re import split

# print(split('\W+', 'Words, words , Words'))     #['Words', 'words', 'Words']
# print(split('\W+', "Word's words Words"))       #['Word', 's', 'words', 'Words']
# print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))        #['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']
# print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))        #['On ', 'th Jan ', ', at ', ':', ' AM']

# re.escape()

# import re
# print(re.escape("This is Awesome even 1 AM"))
# print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

# import re

# s = 'geeks.forgeeks'

# # without using \
# match = re.search(r'.', s)
# print(match)

# # using \
# match = re.search(r'\.', s)
# print(match)

# import re

# string = "The quick brown fox jumps over the lazy dog"
# pattern = "[a-m]"                                               #square brackets for range(a to m)
# result = re.findall(pattern, string)

# print(result)

# import re
# regex = r'^hey'
# strings = ['The fuzzy wuzzy', 'heya lazy dog', 'hey quick brown fox']
# for string in strings:
#     if re.match(regex, string):                                             
#         print(f'Matched: {string}')             
#     else:
#         print(f'Not matched: {string}')

# Not matched: The fuzzy wuzzy
# Matched: heya lazy dog
# Matched: hey quick brown fox

# # $ matches the end of the string
# import re

# string = "working on Python$"
# pattern = r"thon$"

# match = re.search(pattern, string)
# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

# [] for set of characters
# ^ to match start of string
# $ to match end of the string
# | match any char before after 
# ? matches 0 or 1 occurence
# * 0 or more occurences

# \A string begins with
# \b string begins or ends with
# \B should not start or ends with
# \d decimal digits