FROM ubuntu:latest
RUN DEBIAN_FRONTEND=noninteractive \
  apt-get update \
  && apt-get install -y python3 socat python3-pip
RUN apt install -y python3.12-venv

EXPOSE 9999
ADD challenges /challenges
WORKDIR /challenges
SHELL ["/bin/bash", "-c"]
RUN python3 -m venv vcrypto
RUN source vcrypto/bin/activate && pip3 install pycryptodome
CMD source vcrypto/bin/activate && ./entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]
