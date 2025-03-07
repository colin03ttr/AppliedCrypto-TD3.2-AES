#!/usr/bin/env bash
# python3 -m venv vcrypto
# source vcrypto/bin/activate
# pip3 install pycryptodome
socat -T60 TCP-LISTEN:9999,reuseaddr,fork EXEC:"timeout 60 python3 server.py",pty,stderr
