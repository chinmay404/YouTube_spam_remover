from unittest import case
import pandas as pd
import comment_deleter as deleter


def ban(c_secret):
    print("Working On Ban !!")
def delet_all(c_secret):
    deleter.delet(c_secret)

def actions(c_secret):
    if int(input('\n---------------\n    Actions\n---------------\n1.Delet Specific\n2.Delet Comments\n3.Ban From Chanel\n---------------\n')) == 1:
        ban(c_secret) 
    else  :
        delet_all(c_secret) 
    

# Auto Check Spammer 
def check_spammer(name,c_secret):
    c = int(input('Display count : '))
    df = pd.read_csv(name)
    dups_comment = df.pivot_table(index = ['Display Name'], aggfunc ='size').head(c)
    print('\n---------------\nTop Spammers : ')
    print(dups_comment)
    actions(c_secret)

    
# User Give Spam Sentence   
def creat_list_Input_By_User():
    print("Enter spam sentence To Stop Enter (' ~ ') : ")
    li = []
    while 1:
        i = input()
        if i == "~":
            break
        li.append(i)
    return li        
         
def search(name,c_secret):
    li = creat_list_Input_By_User()
    data= pd.read_csv(name)
    for i in li:
        ids = data.loc[data['Comment'].str.contains(i, case = False)]
        id = ids['ID']
        print(id) 
    actions(c_secret)

def choice(name,c_secret):
    print("1.Auto Check Spammer \n2.Enter Spam Sentence\n---------------")
    c = int(input())
    print('---------------')
    if c == 1:
        check_spammer(name,c_secret)
    else:
        search(name,c_secret)