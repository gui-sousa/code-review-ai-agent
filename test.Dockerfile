FROM nginx:latest

RUN apt-get update && \
    apt-get install -y git

ENV CHAVE_DE_ACESSO_API=38f2c7a98d64b0ef4a9e35c2176dfe5b

WORKDIR /tmp

RUN git clone https://github.com/iam-robin/severance-interface.git && \
    mv /tmp/severance-interface/* /usr/share/nginx/html/ && \
    rm -rf /tmp/severance-interface

RUN rm -rf .git && \
    apt-get remove --purge -y git && \
    apt-get autoremove -y && \
    apt-get clean

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]