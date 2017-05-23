#!/usr/bin/env bash

# add SLAPDHOST to /etc/hosts
[ -z $SLAPDHOST ] && echo 'SLAPDHOST not set' && exit 1
cp /etc/hosts /tmp/hosts
sed -e "s/$HOSTNAME\$/$HOSTNAME $SLAPDHOST/" /tmp/hosts > /etc/hosts

# start in background
su - ldap -c "slapd -4 -h ldap://$SLAPDHOST:$SLAPDPORT/ -f /etc/openldap/slapd.conf"

cp -Rp /var/db /var/db2
# start in foreground
su - ldap -c "slapd -4 -h ldap://$SLAPDHOST:9389/ -d conns,config,stats,shell,trace -f /etc/openldap/slapd2.conf"