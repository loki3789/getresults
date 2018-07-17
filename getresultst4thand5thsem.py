import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import urllib.request
import urllib.parse

#values={'q':'python programming tutorials'}

#data=urllib.parse.urlencode(values)
#url='https://www.google.com/search?'+data
usn = input("Enter usn-")
url="https://cbcs.fastvturesults.com/result/"
sem=input("Enter sem-")
slash='/'
url=url+usn+slash+sem
print(url)

headers={}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686)"

req=urllib.request.Request(url,headers=headers)
resp=urllib.request.urlopen(req)
resp_data=resp.read()

#print(resp_data)
#print(type(str(resp_data)))
storesubcodes=[]
storesubnames=[]
#html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(resp_data, 'html.parser')
lst=soup.find_all("div",{"class":'row text-center'})
lst1=soup.find_all("div",{"class":'row mb-1 text-center'})
for z in lst1:
    a1=re.findall(".*([0-9][0-9][A-Z]+[0-9][0-9]).*",str(z))
    for s in a1:
        storesubcodes.append(s)
    st=str(z)
    t=st[st.find('</span>')+7:st.find('</div>')]
    #print(t)
    storesubnames.append(t)
    #print(a2)
#print(lst)
j=0
for i in lst:
  a=re.findall(".*([0-9][0-9]).*",str(i))
  if(len(a)==3):
   print("sub and subject code:",storesubcodes[j],storesubnames[j])
   print("internal:",a[0])
   print("external:",a[1])
   print("total:",a[2])
   print("====================================")
   j=j+1
  
  
