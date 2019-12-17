import sys
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE
from ldap3.core.exceptions import LDAPCursorError

server_name = 'ad.prod.arc.travel'
domain_name = 'arc.travel'
user_name = 'svc_adpwnotifier'
password = 'J0J0BizarreAD'

#format_string = '{:25}'

format_string = '{:25} {:>6} {:19} {:19} {}'

print(format_string.format('Display Name', 'Logins', 'Last Login', 'Expires', 'Description'))

server = Server(server_name, get_info=ALL)
conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
conn.search('dc=arc,dc=travel'.format(domain_name), '(objectclass=person)', attributes=['name','logonCount','lastLogon','accountExpires','description',ALL_ATTRIBUTES,ALL_OPERATIONAL_ATTRIBUTES])
#alternative
#conn.search('dc=arc,dc=travel'.format(domain_name), '(&(objectclass=person)(memberOf=CN=Enterprise Admins,CN=Users,DC=arc,DC=travel))', attributes=['name','logonCount','lastLogon','accountExpires','description',ALL_ATTRIBUTES,ALL_OPERATIONAL_ATTRIBUTES])
#
#conn.search('dc=arc,dc=travel'.format(domain_name), '(&(objectclass=person)(!(memberof=CN=ADIDG_Test,OU=ADIDG,OU=Admins,OU=ARC,DC=arc,DC=travel)))', attributes=['displayName','logonCount','lastLogon','lastLogonTimestamp','description','pwdLastSet','sAMAccountName','mail','whenCreated', ALL_ATTRIBUTES])
#
# conn.search('dc=arc,dc=travel'.format(domain_name), '(&(objectclass=person)(sAMAccountName=cbailey))', attributes=['displayName','logonCount','lastLogon','lastLogonTimestamp','description','pwdLastSet','sAMAccountName','mail','whenCreated'])
#
#thebestfilter
#conn.search('ou=users,ou=arc,dc=arc,dc=travel'.format(domain_name), '(&(objectclass=person)(!(objectClass=computer))(!(memberof=CN=ADIDG_Test,OU=ADIDG,OU=Admins,OU=ARC,DC=arc,DC=travel)))', attributes=['displayName','logonCount','lastLogon','lastLogonTimestamp','description','pwdLastSet','sAMAccountName','mail','whenCreated', ALL_ATTRIBUTES])
#

for e in conn.entries:
    print(format_string.format(str(e.name), str(logon), str(e.lastLogon)[:19], str(e.accountExpires)[:19], desc))
#    print(format_string.format(str(e.name)))
