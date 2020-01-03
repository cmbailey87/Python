import sys
import boto3
import json
from cryptography.fernet import Fernet
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS
from datetime import datetime, timezone, timedelta




def pw_decrypter():
    key = b'Iixkr_C_Q8XbU3FoqfIgshj9d-Vnf3-cUMa9ThzwY-8='
    cipher_suite = Fernet(key)
    ciphered_text = b'gAAAAABd_S9TcWwZw0UpRH_GLHWd8KNcLLkmfLD-1-U1E0_XKqOeyB4Z8sIvvAXO27x4DmW79QZL4RteX6F8OQJLBR89jDCJjQ=='
    unciphered_text = (cipher_suite.decrypt(ciphered_text))
    pwd = str(unciphered_text)[2:15]
    return pwd


server_name = 'ad.prod.arc.travel'
domain_name = 'arc.travel'
user_name = 'svc_adpwnotifier'
password = pw_decrypter()

server = Server(server_name, get_info=ALL)
conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
conn.search('ou=users,ou=arc,dc=arc,dc=travel'.format(domain_name), '(&(objectclass=person)(!(objectClass=computer))(!(memberof=CN=ADIDG_Test,OU=ADIDG,OU=Admins,OU=ARC,DC=arc,DC=travel)))', attributes=['name','mail','lastLogon','sAMAccountName','pwdLastSet','whenCreated', ALL_ATTRIBUTES])

#format_string = '{:25}'

format_string = '{:21} {:26} {:15} {:13} {:22} {}'

#def print_ArcTravel_Users():
#    print(format_string.format('Name', 'mail', 'logonName','pwLastSet','Last Login', 'whenCreated'))
#    for e in conn.entries:
#        print(format_string.format(str(e.name), str(e.mail), str(e.sAMAccountName), str(e.pwdLastSet)[:11],str(e.lastLogon)[:19],str(e.whenCreated)[:11]))
    #    print(format_string.format(str(e.name)))

#print_ArcTravel_Users()

# info = conn.entries[0]['pwdLastSet']
# infoStr = str(info)
# infoStr[0:10]
# 90 days till reset, 75 days start the alert
# pwdLastSet - todaysDate
# passLastSet = info[0]
today = datetime.now(timezone.utc)
# days to expire infoExp = info[0] + datetime.timedelta(days=90)
# days till Pass expires pwdExpDays = infoExp - today
# pwdExpDays.days

aboutToExp = []
alreadyExp = []

def pwd_About_to_Expire():
    for e in conn.entries:
        pls = e['pwdLastSet'][0]
        pexdate = pls + timedelta(days=90)
        pexdays = (pexdate - today).days
        if pexdays <=15 and pexdays >= 1:
            #print("Warning!!! " + str(e['name']) + " Password will expires in " + str(pexdays) + " days")
            abouttoExpDict = {'name' : str(e['name']), 'mail' : str(e['mail']), 'expdate' : str(pexdate.date()) , 'days' : pexdays}
            aboutToExp.append(abouttoExpDict)
        elif pexdays <= 0:
            #print("ERROR!!! " + str(e['name']) + " Password will expires in " + str(pexdays) + " days")
            alreadyExpDict = {'name' : str(e['name']), 'mail' : str(e['mail']), 'expdate' : str(pexdate.date()) , 'days' : pexdays}
            alreadyExp.append(alreadyExpDict)


pwd_About_to_Expire()




def lambda_handler(event, context):
    string = json.dumps(aboutToExp)
    #encoded_string = string.encode("utf-8")

    bucket_name = "ad-pw-notify"
    file_name = "testFile.txt"
    lambda_path = file_name
    s3_path = file_name

    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
