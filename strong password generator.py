import random
n=int(input())
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
specialCharacters = ["`","~","!","@","#","$","%","^","&","*","(",")","_","_","=","+","[","{","]","}",":",";",'"',"'",",","<",".",">","/","?"]
allCharacters=alphabets+numbers+specialCharacters
if (n<5):
    print("password length must be greater than 5")
else:
    temp=[]
    temp.append(alphabets[random.randrange(0,len(alphabets)-1)])
    temp.append(numbers[random.randrange(0,len(numbers)-1)])
    temp.append(specialCharacters[random.randrange(0,len(specialCharacters)-1)])
    for i in range(0,n-3):
        temp.append(allCharacters[random.randrange(0,len(allCharacters))])
    strongPassword=""
    while(len(temp)>0):
        p=random.randrange(0,len(temp))
        strongPassword+=temp[p]
        temp.pop(p)
    print(strongPassword)