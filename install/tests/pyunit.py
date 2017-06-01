import unittest
import logging
import sys
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPInvalidPortError, LDAPBindError
from ldap3.utils.log import logger


class Init:
    trig1 = 0
    trig2 = 0

    def __init__(self, admindn, rootpw):
        self.admindn = admindn
        self.rootpw = rootpw
        self.port1 = 8389
        self.port2 = 9389
        self.server = Server('localhost', self.port1, get_info=ALL)
        self.server2 = Server('localhost', self.port2, get_info=ALL)
        if rootpw == 'changeit':
            try:
                self.conn1 = Connection(self.server, self.admindn, self.rootpw, auto_bind=True)
                self.conn2 = Connection(self.server2, self.admindn, self.rootpw, auto_bind=True)
            except LDAPBindError:
                print ('Bind Error!')
            print('Connection successful!')
            Init.trig1 = self.trig1 = self.conn1.search('dc=at', '(objectClass=*)')
            Init.trig2 = self.trig2 = self.conn2.search('dc=at', '(objectClass=*)')

        else:
            print('Admin password is false!')
        return


class test_slapd2(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger()
        logger.level = logging.DEBUG
        self.stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(self.stream_handler)
        logging.getLogger().info("Binding with right credentials..")
        self.ldapserver = Init('cn=admin,dc=at', 'changeit')

    # def test_empty(self):
    #    return

    # def test_half(self):
    #    return

    def test_bind(self):
        logging.getLogger().info("Testing Bind...")

        try:
            self.assertTrue(self.ldapserver)
        except LDAPBindError:
            print('Bind failed!')

    def test_wrong_pass(self):
        logging.getLogger().info("Testing bind with wrong root password..")
        try:
            self.ldapserver2 = Init('cn=admin,dc=at', 'admin')
        except LDAPBindError:
            print('Wrong password!')

    def test_port1(self):
        logging.getLogger().info("Checking the port for SLAPD1...")

        if self.assertEqual(self.ldapserver.port1, 8389):
            logging.getLogger().info("SLAPD1 Port correct!")

    def test_port2(self):
        logging.getLogger().info("Checking the port for SLAPD2...")

        try:
            self.assertEqual(self.ldapserver.port2, 9389)
        except LDAPInvalidPortError:
            self.fail('SLAPD2 Port is wrong!')

    # @unittest.skipIf(Init.trig1 == 0, "Skipping data test due to previous failed test...")
    def test_data1(self):
        logging.getLogger().info("Testing for any data in SLAPD1..")
        self.assertTrue(self.ldapserver.trig1)

    # @unittest.skipIf(Init.trig2 == 0, "Skipping data 2 test due to previous failed test...")
    def test_data2(self):
        logging.getLogger().info("Testing for any data in SLAPD2..")
        self.assertFalse(self.ldapserver.trig2, "testytest")

    def tearDown(self):
        logger.removeHandler(self.stream_handler)
        # self.ldapserver.dispose()
        # self.ldapserver2.dispose()


def main():
    unittest.main()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
