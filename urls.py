"""
The urls in this file are inconsistent. Some if them have www. in the beginning and some dont.
Some have https and some have http. 
We want to create a regex just to extract the domain.com.
In our example, we want to grab google.com, nasa.gov etc.
"""

"""
1. We first write an expression that matches the complete urls.
pattern = re.compile(r"https?://(www\.)?\w+\.\w+")

http --> Matches http
s? --> Matches optional s, hence will match http or https
:// --> Matches literally ://
(www\.)? --> Some have www and some dont.
            This will make pattern "www." optional because of ? after the group.
\w+ --> Matches the domain name
\.\w+ --> Matches .gov or .com or .net etc.
hence the expression: r"https?://(www\.)?\w+\.\w+"
"""

import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r"https?://(www\.)?\w+\.\w+")
matches = pattern.finditer(urls)

for match in matches:
    print(match)
# ---------------

"""
2. Our aim was not to match the urls, but use groups to get data out of it.
We will surroud our domain name in regex with round braces.
r"https?://(www\.)?(\w+)(\.\w+)"

(\w+) --> Matches yahhoo or google or nasa
(\.\w+) --> Matches .gov or .com or .net etc.

The match object has a group() method which takes in the index of the group as a param.
group(0) is the complete match.
group(1) will be first group, i.e optional www.
group(2) will be the domain name like yahoo, google in our case.
group(3) will be .com or .net or .gov
"""
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)

for match in matches:
    print(
        f"Group 0: {match.group(0)}, Group 1: {match.group(1)}, Group 2: {match.group(2)} Group 3: {match.group(3)}"
    )
# ---------------

"""
3. pattern.sub() method.
We can use something called as back reference to reference our captured group.
It is a short hand for accessing these group indices.
re module has a sub() method that we can use to perform substitution.

subbed_urls = pattern.sub(r"\2\3", urls)
r"\2\3"

\2 --> Means group(2) i.e our domain name
\3 --> Means group(3) i.e .com / .net etc.

Everytime we find a match to our pattern, re.sub will replace the match with group(2) group(3) i.e yahoo.com

This is useful for formatting large text files.
"""

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
subbed_urls = pattern.sub(r"\2\3", urls)
print(subbed_urls)

"""
4. Other methods in re module:

4.1 pattern.findall(): This will return matched groups as Tuple. If there are no groups in the expression, it will
just return the matches in a list. This method does not return a Match object.

finditer returns list of Match objects.
findall returns a list of groups(tuples) or matches('string')
"""
pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches = pattern.findall(urls)
for match in matches:
    print(match)

"""
4.2 pattern.match()

This checks for a pattern at the beginning of a string. If a match is not found it returns None.
Also, pattern.match() does not return a iterable. It directly returns the match object of first match that it finds.
Hence for loop here will not work.
"""

sentence = "Start a sentence and then bring it to an end"
pattern = re.compile(r"Start")
matches = pattern.match(sentence)
print(matches)

pattern = re.compile(r"and")
matches = pattern.match(sentence)
print("Not found at the start hence,", matches)

"""
4.3 pattern.search()

match method looks for pattern only at the start of the string, if we want to search for pattern in complete
string, we use the search() method.
Just like match, it will not return an iterable.
This will return the first match it finds in the sentence.
If a match is not found it returns None.
"""
sentence = "Start a sentence and then bring it to an end"
pattern = re.compile(r"Start")
matches = pattern.search(sentence)
print(matches)
