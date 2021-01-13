FROM rabbitmq:3-management-alpine

# Define environment variables.
# ENV RABBITMQ_DEFAULT_USER admin
# ENV RABBITMQ_DEFAULT_PASS admin

ADD init.sh /init.sh

RUN ["chmod", "+x", "/init.sh"]

EXPOSE 15672

CMD ["/init.sh"]