FROM alpine:3.10.4

RUN \
    echo "**** install packages ****" && \
        apk --no-cache add --update \
            shadow \
            supervisor \
            curl \
            vim \
            bash && \
    echo "**** configure abc user ****" && \
        groupmod -g 1000 users && \
        useradd -u 911 -U -d /config -s /bin/false abc && \
        usermod -G users abc && \
        mkdir -p /config

COPY root/ /

VOLUME /config

ENTRYPOINT ["/entrypoint/start"]