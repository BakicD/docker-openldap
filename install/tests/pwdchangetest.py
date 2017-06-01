from ldap3 import Connection, Server, ALL, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPBindError

try:
    conn = Connection('localhost:8389', 'cn=admin,dc=at', 'changeit', auto_bind=True, raise_exceptions=True)
except LDAPBindError:
    print('Admin bind failed!')

if conn.search('dc=at', '(sn=Bakic)'):
    pass
else:
    conn.add('cn=test.david,dc=at', 'inetOrgPerson', {'givenName': 'David', 'sn': 'Bakic', 'userPassword': 'test'})

try:
    test_conn = Connection('localhost:8389', 'cn=test.david,dc=at', 'test', auto_bind=True, raise_exceptions=True)
except LDAPBindError:
    print('Test_user bind failed!')

conn.modify('cn=test.david,dc=at', {'userPassword': [(MODIFY_REPLACE, [']}+$_!:'])]})

try:
    test_conn2 = Connection('localhost:8389', 'cn=test.david,dc=at', ']}+$_!:', auto_bind=True, raise_exceptions=True)
except LDAPBindError:
    print('Test_user bind with new password (]}+$_!:) failed!')

conn.search('dc=at', '(userPassword=*)')
print(conn.entries)
print(conn.entries[1].entry_to_ldif())
