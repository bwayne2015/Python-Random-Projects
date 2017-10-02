from bs4 import BeautifulSoup
import time
import json


"""    
def click_from_drop_down(element):
        value =["#rename-folder-command","#edit-command","#show-in-folder-command","#cut-command","#copy-command","#paste-from-organize-menu-command",\
        "#delete-command","#undo-delete-command","#sort-command","#import-menu-command","#export-menu-command"]
        for val in value :
            if(element == value):
                
                print("value clicked"
               
"""
def fetch_bookmarks_from_file():
    file_location=input("GIve FIle Location: ")
    f = open(file_location,'r')
    soup = BeautifulSoup(f.read(),"html.parser")
    f.close()

    dt=[]
    for d in soup.findAll('dt'):
      dt.append(d)
    uri=[]
    title=[]
    add_date=[]
    for i in range(len(dt)):
      if dt[i].contents[0].has_attr('href') and dt[i].contents[0].has_attr('add_date'):
        uri.append(dt[i].contents[0]['href'])
        title.append(dt[i].contents[0].contents[0])
        add_date.append(time.ctime(int(dt[i].contents[0]['add_date'])))
    #print(title)
    return uri,title,add_date

def search_bookmark():
    url,title,date = fetch_bookmarks_from_file()
    #print(type(url))
    keyword = input("What is the name of the bookmark : ")
    #match_title = [key for key in title if keyword in key]
    for key in title:
        if keyword in key:
            
            print("This is Probably you are looking: " ,key)
            index_value = title.index(key)
            #print(index_value)
            print("URL : ",url[index_value])
            print("The date When you bookmerked: ",date[index_value])
        #print("URL : ",url)
        #print("The date When you bookmerked: ",date)
                  
#fetch_bookmarks_from_pc()    
search_bookmark()
