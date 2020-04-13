FROM alpine:3.10.4

ENV \ 
    SETTINGS_SOURCE="none" \
    SETTINGS_SHELIFIED="{}" \
    SETTINGS_AUTOMATED_UPDATE="true" \
    SETTINGS_GIT_AUTOMATED_PULL="false" \
    SETTINGS_GIT_HOST="" \
    SETTINGS_GIT_USERNAME="" \
    SETTINGS_GIT_REPOSITORY="" \
    SETTINGS_GIT_TOKEN=""

RUN \
    echo "**** install packages ****" && \
        apk --no-cache add --update \
            shadow \
            supervisor \
            python3 \
            git \
            curl \
            vim \
            bash \
            zsh && \
        pip3 install --upgrade pip && \
        pip3 install \
            jsonschema \
            deepdiff

COPY root/ /

ENTRYPOINT ["/container/entrypoint/main.entrypoint"]