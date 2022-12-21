import json
import comment_extractor as extractor
from matplotlib import lines

key = ""
print("----------Spam Remover----------\n\nAPI key:\n1.Deafult\n2.New Key\n3.Previous Key")
c = int(input("   :"))
if c==1:
    print("Deafult : AIzaSyCcRfNg_VT6KzC6jvr2IKZ2EnMkGAYeSIw")
    key = "AIzaSyCcRfNg_VT6KzC6jvr2IKZ2EnMkGAYeSIw"
    
elif c == 2 :
    new_key = input("New Key : ")
    if(len(new_key)!= 39):
        print("Invalid Key!")
        new_key = input("New Key : ")
    x = input("save Key (y/n) : ")
    if(x == 'y'):
        file = open("data.txt","a")
        file.write("\n"+new_key)
    key = new_key
elif c == 3:
    file = open("data.txt","r")
    print("Previous Keys :")
    line = file.readlines()
    print(line) 
    key = line[int(input("Enter No : "))]
c_secret = input("Client Secret .json : ")

extractor.main(key)

        
              

    
    