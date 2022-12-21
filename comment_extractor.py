from email import header
import os
from bs4 import BeautifulSoup
import pandas as pd
import googleapiclient.discovery
import csv
import json
import Process_on_comment as process


# def search(name):
#     data= pd.read_csv(name)
#     ids = data.loc[data['Comment'].str.contains("Start main joo", case = False)]
#     id = ids['ID']
#     print(id)
      
# def Vide_info():
    



   
def write_csv(response , vid_Id,maxresult,c_secret):
    headers = ["ID" ,"State", "Display Name" ,"Replay Count","Comment" ,"Comment ID","User chanal ID" ,"Replayer Channel url", "Likes"] 
    name = vid_Id+'.csv'
    with open("sample.json", "w") as outfile:
        json.dump(response, outfile)  
        
    with open(name, 'w' ,newline='',encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        print("\n----------\nAPI Allow Read upto 5 replaies on each comment\n----------\n")   
        for i in range (0,maxresult):   
            id = response['items'][i]['snippet']['topLevelComment']['id']
            u_name = response['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment_count = response['items'][i]['snippet']['totalReplyCount']
            c_id =  response['items'][i]['id']
            if (comment_count != 0): 
                c_reply = []
                for x in range(0,comment_count):
                    c_reply.append(response['items'][i]['replies']['comments'][x]['snippet']['textDisplay'])
                    r_id = response['items'][i]['replies']['comments'][x]['id']
                    r_u_name = response['items'][i]['replies']['comments'][x]['snippet']['authorDisplayName']
                    r_u_url = response['items'][i]['replies']['comments'][x]['snippet']['authorChannelId']['value']
                    r_c_likes =response['items'][i]['replies']['comments'][x]['snippet']['likeCount']
                    r_comment = response['items'][i]['replies']['comments'][x]['snippet']['textDisplay']
                    r_id = response['items'][i]['replies']['comments']['id']
                    r_state = "replay"
                    r_row = [r_id ,r_state, r_u_name ,comment_count, r_comment ,r_id, r_u_url , r_c_likes]
                    w.writerow(r_row)    
            comment = response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay']
            u_url = response['items'][i]['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
            c_likes =response['items'][i]['snippet']['topLevelComment']['snippet']['likeCount']
            state = "Comment"
            row = [id ,state, u_name ,comment_count, comment ,c_id, u_url , c_likes]
            w.writerow(row)
        f.close()
    process.choice(name,c_secret)

    
#  https://youtu.be/7NO5_28LqRU        

def main(key,c_secret):
    url = input("Enter URL (Without time Stamp and Featured)\n  :")
    tmp = url[8:15]
    if (tmp != "youtu.be"):
        print("Invalid Url!!")
        url = input("Enter Again (Without time Stamp and Featured)\n  :")
    vid_Id = url[len(url)-11:].strip()
    print("Vide0 ID : " , vid_Id)
    print("Max Count : ",end="")                                                                                                     
    while True :
        try:
            maxresult = int(input())
        except ValueError:
            print("Invalid Input!! Enter Again!!")
        else :
            break
    for i in (0,0):   
        try:
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
            api_service_name = "youtube"
            api_version = "v3"
    # Key Not Work Creat Own and Use
            DEVELOPER_KEY = key  #AIzaSyCcRfNg_VT6KzC6jvr2IKZ2EnMkGAYeSIw
            youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)
            request = youtube.commentThreads().list(
                part="id ,snippet,replies ",
                order="time",
                maxResults=maxresult,
                videoId=vid_Id,
                prettyPrint=True
            )
        except Exception as e :
            print("Error Occured \n 1.Check Internet \n 2.Check Developer Key")

    response = request.execute()
    write_csv(response , vid_Id , maxresult,c_secret)
# httplib2.error.ServerNotFoundError: Unable to find the server at youtube.googleapis.com
if __name__ == "__main__":
    main()
