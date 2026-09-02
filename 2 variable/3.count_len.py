# Count
name = "Harsh pariya"
length = len(name)
print(length)
print(name.count("r"))

para = """ 
I am a student of rai university,ṇṇ
currently persuing B.tech in Rai University, ahmedabad, Gujarat.
i'm eager to learn and explore python wiht baraaa.
which he taught and is available in youTube,
the term that he used is very simple, which is very clear
"""

print(para.count("rai university"))

change_para = para.replace("rai university", "Rai University".replace("python", "Python"))
print(change_para)
print(para.count("rai university"))
