import unittest
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPInvalidPortError, LDAPBindError


class Init:
    def __init__(self, admindn, rootpw):
        self.admindn = admindn
        self.rootpw = rootpw
        self.server = Server('localhost', port=8389, get_info=ALL)
        self.server2 = Server('localhost', port=9389, get_info=ALL)
        try:
            self.conn1 = Connection(self.server, self.admindn, self.rootpw, auto_bind=True, raise_exceptions=True)
            self.conn2 = Connection(self.server2, self.admindn, self.rootpw, auto_bind=True, raise_exceptions=True)
        except LDAPBindError:
            print ('Bind Error!')


class testSLAPD2(unittest.TestCase):
    def setUp(self):
        self.ldapserver = Init('cn=admin,dc=at', 'changeit')

    def test_empty(self):
        return

    def test_half(self):
        return

    def test_port(self):
        try:
            self.assertEqual(8389, 8389)
        except LDAPInvalidPortError:
            pass
        else:
            self.fail('Port is wrong!')

    # def tearDown(self):
        # self.rootpw.dispose()
        # self.admindn.dispose()
        # self.server.dispose()
        # self.server2.dispose()
        # self.admindn.dispose()
        # self.userdn.dispose()
        # self.testpw.dispose()


def main():
    unittest.main()


if __name__ == '__main__':
    unittest.main()
