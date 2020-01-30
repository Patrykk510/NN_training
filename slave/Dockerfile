FROM python:3.6

RUN pip --no-cache-dir install keras
RUN pip --no-cache-dir install ssh

ARG var="Docker1!"
ENV SSH_PASSWD "root:${var}"
RUN apt-get update \
        && apt-get install -y --no-install-recommends dialog \
        && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd 

COPY sshd_config /etc/ssh/

EXPOSE 2222

COPY input_data.npy /input_data.npy
COPY output_data.npy /output_data.npy

COPY slavescript.py /slavescript.py

RUN ["service", "ssh", "start"]
CMD ["/usr/sbin/sshd", "-D"]
