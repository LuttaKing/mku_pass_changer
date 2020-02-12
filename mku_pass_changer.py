# import the necess modules...{bs4,re,requests}
import requests,re
from bs4 import BeautifulSoup

#important link
url="https://studentportal.mku.ac.ke/umis/studentportal/"
fees_url='https://studentportal.mku.ac.ke/umis/studentportal/statement_detailed.php'
pass_url='https://studentportal.mku.ac.ke/umis/studentportal/password_update.php'

# student credentials
userName= "lutta21"
password="ghgxghh"
maybe=" Login "

currentPassword=""
newPassword=""
confirmPassword=''
passwordHint='Awesomedsness'
changePassword='Change Password'

login_payload = dict(regNo=userName,smisPass=password,smisLogon=maybe)

pass_payload=dict(currentPassword=currentPassword,newPassword=newPassword,confirmPassword=confirmPassword,passwordHint=passwordHint,changePassword=changePassword)

#start a session
with requests.session() as c:

    c.post(url,data=login_payload,headers={'Referer':'https://studentportal.mku.ac.ke/umis/studentportal/'})
    c.post(pass_url,data=pass_payload,headers={'Referer':'https://studentportal.mku.ac.ke/umis/studentportal/'})


    res = c.get(fees_url)
    soup = BeautifulSoup(res.text,features="lxml")

    student_name=soup.p.string
    print(student_name)
