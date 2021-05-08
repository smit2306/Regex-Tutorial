import re

text_to_search = """
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = "Start a sentence and then bring it to an end"

""" re.finditer for finding all matches.
Span is a tuple of start index and stop index of a match.
The below code only matches abc small text not ABC.
This is because its case sensitive.
"""
pattern = re.compile(r"abc")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Search for escape characters.
If you just use re.compile(r"."), it will match everything.
All characters in the need to be escaped section require backslash for escaping.
"""
pattern = re.compile(r"\.")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Matching the word Ha's that have a word boundary in the beginning.
"""
pattern = re.compile(r"\bHa")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Matching the word Ha's that do not have a word boundary in the beginning.
"""
pattern = re.compile(r"\BHa")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Search something at the beginning of a string.
The ^ carat will be at the start of the pattern.
If the pattern is not at the start of the string, re will not match it.
"""
pattern = re.compile(r"^Start")
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

pattern = re.compile(r"^sentence")
matches = pattern.finditer(sentence)

for match in matches:
    print(match)
# ---------------
"""
Search something at the end of a string.
The $ anchor will follow the pattern.
"""
pattern = re.compile(r"end$")
matches = pattern.finditer(sentence)

for match in matches:
    print(match)
# ---------------
"""
Searching for phone numbers.
"""
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Searching for phone numbers in data.txt file.
"""
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")
with open("data.txt", "r") as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
# ---------------
"""
Searching for phone numbers that only have dots or dash as separator.
Currently we are using "." to match. This will match any character between the numbers.
To do this we will character set. It is [] with characters in it.
You do not need to escape meta characters in character set.
Even though there multiple characters in [], it still only matches 1 character in our text.
Our regex will not match 123--45-6789.
"""
pattern = re.compile(r"\d\d\d[.-]\d\d\d[.-]\d\d\d\d")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Another example of character set.
We only want to match numbers starting with 800 or 900.

Our first character is 8 or 9 hence [89].
Next two characters have to zeros for 800 or 900.
Hence the expression [89]00.
The rest of expresssion remains the same.
"""
pattern = re.compile(r"[89]00[.-]\d\d\d[.-]\d\d\d\d")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
"-" is a special character in character set.
If it put at the start or end of the set, it matches the dash, but when put between any two
characters, it denotes range of values. 
[1-5] --> Matches digits between 1 and 5
[a-z] --> Matches lower case a to z
[A-Z] --> Matches upper case A to Z
[a-zA-Z] --> Matches both upper and lower case A to Z

"^" is also a special character in the character set.
Outside the set, it matches the beginning of the string. But when placed at the start in the 
character set, it will negate the set and will match everything that is not in the set.

[^a-zA-Z] --> Matches everything that is not upper or lower case a to z.
"""
# ---------------
"""
Using quantifiers. Currently our expression to find phone numbers has repeated d's.
Making an expression this way is harder to read and also prone to error. We can use quantifiers instead.
"""
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Usinf quantifiers. Searching for names that start with Mr or Mrs. In phone number regular expression, 
we knew the exact number of digits, but in this case, Mr and Mrs vary in length.
Some have a period after prefix Mr like Mr. Smith and some dont like Mrs Doe.

For making "." as optional, we use "?" quantifier after that.

Mr\.? --> Matches "Mr." or "Mr"
\s --> Space
[A-Z] --> Capital letter after "Mr. "
\w* --> 0 or more word characters after "Mr. A" 
"""
pattern = re.compile(r"Mr\.?\s[A-Z]\w*")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

"""
Our above expression still only matches the names with Mr not Mrs.
We can use groups in our expression for this.

(Mr|Ms|Mrs) --> Matches Mr or Ms or Mrs
"""
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# ---------------
"""
Now go to the example in emails.py file
"""
# ---------------
"""
Use urls.py file for using groups to capture information.
"""
# ---------------
"""
Using Flags:

re.INGNORECASE --> Case insensitive match
re.MULTILINE --> Allows to match beginning and end of EACH LINE in a multiline string 
                rather than start and stop of that string
re.VERBOSE --> Allows to add comments to your regex for better readability.
"""
