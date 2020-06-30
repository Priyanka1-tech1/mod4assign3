file = open("gfg.txt","r") 
Count= 0
Content = file.read() 
CoList = Content.split("\n") 
for i in CoList: 
    if i: 
        Count+= 1
print("number of lines in file") 
print(Count) 