# -*- coding: utf-8 -*-
"""IIP-Task.ipynb"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

def finding(s):
    source=requests.get("http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID="+s).text

    soup= BeautifulSoup(source,'lxml')
    table=soup.find('table',class_='TableLined')
    table2=soup.find('td',class_='Banner2')
    
    player=[]
    if(table2 is not None):
      ar.append(table2.text.strip())
      s=table2.text.strip()
      for i in range(0,len(s)):
        if(s[i]=='('):
          n=i
          player.append(s[:i])
        if(s[i]==')'):
          player.append(s[n+1:i])
      print(table2.text.strip(),"\r\n")
    
    
    if(table is not None):
      tr=table.findAll('tr')
      z=1970
      for i in range(1,len(tr)):
          td=tr[i].findAll('td')
          
          for i in range(z,2020):
            if(str(i)==td[0].text.strip()):
              z=int(td[0].text.strip())+1
              player.append(td[8].text.strip())
              break
            else:
              player.append(0)
            
          if(len(td[0].text.strip())>4):
            player.append(td[8].text.strip())
    
          
      
      data.append(player)
      player=[]

s=""
c=0
ar=[]
player=[]
data=[]
for i in range(0,9000):
    if i<10:
        s="000"+str(i)
    elif i<100:
        s="00"+str(i)
    elif i<1000:
        s="0"+str(i)
    else:
        s=str(i)
    
    finding(s)

print(len(data))

columns=['Name','Nation']

for i in range(1970,2020):
  columns.append(str(i))

columns.append('Overall')

df=pd.DataFrame(data,columns=columns)

df.to_csv('results.csv',header=True)

