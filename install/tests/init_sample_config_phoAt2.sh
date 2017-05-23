#!/bin/sh

echo 'initialize slapd2.conf with phoAt schema'

mv /etc/openldap/slapd_phoAt_example2.conf /etc/openldap/slapd2.conf

if [ $(grep -q '^rootpw' /etc/openldap/slapd2.conf) ]; then
    echo "rootpw directive already set in slapd2.conf"
else
    slappasswd -s $ROOTPW > /tmp/rootpw
    printf "\nrootpw $(cat /tmp/rootpw)" >> /etc/openldap/slapd2.conf
    rm -f /tmp/rootpw
    echo "rootpw directive added to slapd2.conf"
fi

