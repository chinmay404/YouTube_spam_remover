from unittest import case
import pandas as pd
import comment_deleter as deleter
# import numpy as np
# from sklearn.datasets import load_wine

# def pre_process(name):
#     data= pd.read_csv(name)
 
# System Checks No of replays  
        
# Auto Check Spammer 
def check_spammer(name):
    c = int(input('Display count : '))
    df = pd.read_csv(name)
    dups_comment = df.pivot_table(index = ['Display Name'], aggfunc ='size').head(c)
    print('Top Spammers : ')
    print(dups_comment)
    if int(input('\n---------------\n   Actions  \n1.Ban\n2.Delet Comments')) == 1:
        pass
    #     ban()
    
    # else :
    #     delet_all() 
    
    
    
# def actions():
    

        
        
        
        



 



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
      
    
def search(name):
    li = creat_list_Input_By_User()
    data= pd.read_csv(name)
    for i in li:
        ids = data.loc[data['Comment'].str.contains(i, case = False)]
        id = ids['ID']
        print(id) 






# after ading client secret key in delet file use this function
# deleter.delet(id)




def choice(name):
    print("1.Auto Check Spammer \n2.Enter Spam Sentence\n---------------")
    c = int(input())
    print('\n---------------')
    if c == 1:
        check_spammer(name)
    else:
        search(name)