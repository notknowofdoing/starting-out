awesome = open("thepara.txt","r")
text = awesome.read().lower()
awesome.close()
remove = [".",",","(",")"," "]
newstring = ""
for i in text:
    if i not in remove:
        newstring+=i
    else:
        continue
    


word=['Genesis',
'Exodus',
'Leviticus',
'Numbers',
'Deuteronomy',
'Joshua',
'Judges',
'Ruth',
'Samuel',
'Kings',
'Chronicles',
'Ezra',
'Nehemiah',
'Esther',
'Job',
'Psalms',
'Proverbs',
'Ecclesiastes',
'Song of Solomon',
'Isaiah',
'Jeremiah',
'Lamentations',
'Ezekiel',
'Daniel',
'Hosea',
'Joel',
'Amos',
'Obadiah',
'Jonah',
'Micah',
'Nahum',
'Habakkuk',
'Zephaniah',
'Haggai',
'Zechariah',
'Malachi',
'Matthew',
'Mark',
'Luke',
'John',
'Acts',
'Romans',
'Corinthians',
'Galatians',
'Ephesians',
'Philippians',
'Colossians',
'Thessalonians',
'Timothy',
'Titus',
'Philemon',
'Hebrews',
'James',
'Peter',
'John',
'Jude',
'Revelation'
]

wrdcount = (len(word))
for i in range(0,wrdcount):
 word[i] = word[i].lower()
 a=word[i]
 
 if a in newstring:
     
     print(word[i],"is in the given in para")
 
