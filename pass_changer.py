# import the necessary modules...{bs4,re,requests}
import requests,re
from bs4 import BeautifulSoup

#important links
url="https://studentportal.mku.ac.ke/umis/studentportal/"
fees_url='https://studentportal.mku.ac.ke/umis/studentportal/statement_detailed.php'
pass_url='https://studentportal.mku.ac.ke/umis/studentportal/password_update.php'

# student credentials
maybe=" Login "
with open('/root/Documents/mku.txt','r') as f:
    for i in f:
        if len(i) > 1:
            if '/' in i:
                userName=i
            elif '/' not in i:
                password=i
                login_payload = dict(regNo=userName,smisPass=password,smisLogon=maybe)
                print(login_payload)

                #start a session
                with requests.session() as c:

                    c.post(url,data=login_payload,headers={'Referer':'https://studentportal.mku.ac.ke/umis/studentportal/'})

                    res = c.get(fees_url)
                    soup = BeautifulSoup(res.text,features="lxml")

                    student_name=soup.p.string
                    print(student_name)

                
