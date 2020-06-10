FROM centos

RUN yum install epel-release -y
RUN yum update -y
RUN yum install python3 -y
RUN yum install python3-devel -y
RUN yum install python3-pip -y
RUN mkdir /data
RUN mkdir /Code
RUN mkdir /Model

COPY /data/  /data/

RUN pip3 install -r /data/lib.txt

