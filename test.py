import re

sentence = "i am manish"
pattern = re.compile("^i")
for match in pattern.findall(sentence):
    print(match)
    print(match.upper())

sentence = "abarbrakadarba"
print(sentence[0] + sentence[1:].replace("a", "*"))
