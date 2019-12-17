import sys
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS
from datetime import datetime, timezone, timedelta

server_name = 'ad.prod.arc.travel'
domain_name = 'arc.travel'
user_name = 'svc_adpwnotifier'
password = 'J0J0BizarreAD'

server = Server(server_name, get_info=ALL)
conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
conn.search('ou=users,ou=arc,dc=arc,dc=travel'.format(domain_name), '(&(objectclass=person)(!(objectClass=computer))(!(memberof=CN=ADIDG_Test,OU=ADIDG,OU=Admins,OU=ARC,DC=arc,DC=travel)))', attributes=['name','mail','lastLogon','sAMAccountName','pwdLastSet','whenCreated', ALL_ATTRIBUTES])

#format_string = '{:25}'

format_string = '{:21} {:26} {:15} {:13} {:22} {}'

def print_ArcTravel_Users():
    print(format_string.format('Name', 'mail', 'logonName','pwLastSet','Last Login', 'whenCreated'))
    for e in conn.entries:
        print(format_string.format(str(e.name), str(e.mail), str(e.sAMAccountName), str(e.pwdLastSet)[:11],str(e.lastLogon)[:19],str(e.whenCreated)[:11]))
    #    print(format_string.format(str(e.name)))

print_ArcTravel_Users()

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
            print("Warning!!! " + str(e['name']) + " Password will expires in " + str(pexdays) + " days")
            abouttoExpDict = {'name' : str(e['name']), 'mail' : str(e['mail']), 'expdate' : str(pexdate.date()) , 'days' : pexdays}
            aboutToExp.append(abouttoExpDict)
        elif pexdays <= 0:
            print("ERROR!!! " + str(e['name']) + " Password will expires in " + str(pexdays) + " days")
            alreadyExpDict = {'name' : str(e['name']), 'mail' : str(e['mail']), 'expdate' : str(pexdate.date()) , 'days' : pexdays}
            alreadyExp.append(alreadyExpDict)

#for i in aboutToExp:
#    for k,v in i.items():
#        print(k, ' : ', v)
#   print(' ')
