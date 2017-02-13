FROM  centos:centos7
      version="0.4.0" \
      capabilites='--cap-drop=all'   # bind on port > 1024

ENV UID 343006
ENV GID 0
RUN useradd --gid $GID --uid $UID ldap \
 && chown $UID:$GID /run

RUN yum -y install curl iproute lsof net-tools \
 && yum -y install openldap openldap-servers openldap-clients \
 && yum clean all

# save system default ldap config and extend it with project-specific files
RUN mkdir -p /opt/sample_data/etc/openldap/data/
COPY install/conf/*.conf /etc/openldap/
COPY install/conf/schema/* /etc/openldap/schema/
COPY install/data/* /opt/sample_data/etc/openldap/data/
COPY install/conf/DB_CONFIG /var/db/
COPY install/scripts/* /

# using the shared grop method from https://docs.openshift.com/container-platform/3.3/creating_images/guidelines.html (Support Arbitrary User IDs)
RUN chown -R ldap:root /etc/openldap /opt/sample_data /var/db /var/log/openldap \
 && chmod +x /*.sh

ARG SLAPDPORT 8389
ENV SLAPDPORT $SLAPDPORT

VOLUME /etc/openldap/ \
       /var/db/ \
       /var/log/openldap

USER ldap
CMD /start.sh
