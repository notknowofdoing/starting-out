awesome = open("test.txt", "r")
text = awesome.read()
awesome.close()
txt = text.split()
words = ['Genesis','Exodus','Mark']

wrdcount=(len(words))
txtcount=(len(txt))
print(txtcount)


for i in range(0,3):
 for j in range(0,10):
      txt1 = txt[j]
      
      words1 = words[i]
      
      if txt1 in words1:
            print("if worked")
            #print(txt[j])
            #print(words[i])
      else:
           #print("else worked")
           break
