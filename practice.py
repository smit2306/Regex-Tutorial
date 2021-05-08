import re

text_to_search = """
23-456-7890
123.345.6719
123.345.56
"""

pattern = re.compile(r"(\d{3}|\d{2})[.-]\d{3}[.-](\d{4}|\d{2})")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
