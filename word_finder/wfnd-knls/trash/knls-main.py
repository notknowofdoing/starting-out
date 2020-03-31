from modules import *
from finder import *

file = get_file("text")
text = extract_text(file)
dictionary = dictionarize(get_file("dictionary").read())

result = finderv2(text,dictionary)
count = 0

for i in result:
    count+=1
    if count <= 9:
        print(f"  {count}. {i}")
    if count <=99 and count > 9:
        print(f" {count}. {i}")
    if count <=999 and count > 99:
        print(f"{count}. {i}")
