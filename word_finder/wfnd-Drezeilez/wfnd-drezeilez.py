f = open("txt.txt", "r")
text = f.read().lower()
f.close()
remove = [ ".", ",","(",")"," "]
newstring = ""
for i in text:

    if i not in remove:
        newstring+=i
    else:
        continue

f = open("txt.txt","w")
f.write(newstring)
f.close()

b = open("books.txt", "r")
txt = b.read().lower().split()
b.close()

total=len(txt)
for i in range(0,total):
    
      a=txt[i]
      if a in newstring:
        print(a)
