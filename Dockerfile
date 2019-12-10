FROM centos:7

USER 0

#RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
#    yum -y install python36u.x86_64 python36u-libs.x86_64 python36u-devel.x86_64 python36u-pip.noarch && \
#    yum -y install httpd && \
#    rm -rf /var/cache/yum

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
                   python36u.x86_64 python36u-libs.x86_64 python36u-devel.x86_64 python36u-pip.noarch && \
                   httpd

RUN rm -rf /var/cache/yum &&\
    localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8 &&\
    ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

COPY httpd.conf /etc/httpd/conf/httpd.conf &&\
     index.html /var/www/html/index.html &&\
     init.py /var/www/cgi-bin/init.py &&\
     index.cgi /var/www/cgi-bin/index.cgi &&\
     form.cgi /var/www/cgi-bin/form.cgi &&\
     addmod.cgi /var/www/cgi-bin/addmod.cgi &&\
     seatmap.txt /var/www/cgi-bin/seatmap.txt &&\
     mod.cgi /var/www/cgi-bin/mod.cgi

RUN chmod 777 /run/httpd &&\
    chmod 777 /var/log/httpd &&\
    chmod 766 /var/www/html/index.html &&\
    chmod 777 /var/www/cgi-bin/index.cgi &&\
    chmod 777 /var/www/cgi-bin/init.py &&\
    chmod 755 /var/www/cgi-bin/addmod.cgi &&\
    chmod 755 /var/www/cgi-bin/form.cgi &&\
    chmod 777 /var/www/cgi-bin/seatmap.txt &&\
    chmod 755 /var/www/cgi-bin/mod.cgi

ENV LANG ja_JP.utf8 &&\
    LANGUAGE ja_JP.utf8 &&\
    LC_ALL ja_JP.utf8

CMD /usr/sbin/httpd -k start && tail -f /dev/null
