import re #1

text ='maks 123 &^$# 456 @gmail. 876'

pattern = re.compile(r'\d\d\d') #2 make the pattern and keep it as raw string

matches = pattern.search(text)

print(matches)