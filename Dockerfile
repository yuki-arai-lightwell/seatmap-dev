FROM centos:7

USER 0

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python36u.x86_64 python36u-libs.x86_64 python36u-devel.x86_64 python36u-pip.noarch && \
    yum -y install httpd && \
    rm -rf /var/cache/yum


RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8

COPY httpd.conf /etc/httpd/conf/httpd.conf
COPY index.html /var/www/html/index.html
COPY init.py /var/www/cgi-bin/init.py
COPY index.cgi /var/www/cgi-bin/index.cgi
COPY form.cgi /var/www/cgi-bin/form.cgi
COPY addmod.cgi /var/www/cgi-bin/addmod.cgi
COPY seatmap.txt /var/www/cgi-bin/seatmap.txt
COPY mod.cgi /var/www/cgi-bin/mod.cgi

RUN chmod 777 /run/httpd\
    chmod 777 /var/log/httpd\
    chmod 766 /var/www/html/index.html\
    chmod 777 /var/www/cgi-bin/index.cgi\
    chmod 777 /var/www/cgi-bin/init.py\
    chmod 755 /var/www/cgi-bin/addmod.cgi\
    chmod 755 /var/www/cgi-bin/form.cgi\
    chmod 777 /var/www/cgi-bin/seatmap.txt\
    chmod 755 /var/www/cgi-bin/mod.cgi\
    ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

ENV LANG ja_JP.utf8
ENV LANGUAGE ja_JP.utf8
ENV LC_ALL ja_JP.utf8

# CGI scripts go to /opt/rh/httpd24/root/var/www/cgi-bin/
#ADD share/cgi-bin ${HTTPD_DATA_ORIG_PATH}/cgi-bin/

# Static files go to /opt/rh/httpd24/root/var/www/html
#ADD share/html ${HTTPD_DATA_ORIG_PATH}/html

CMD /usr/sbin/httpd -k start && tail -f /dev/null
