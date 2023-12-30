#!/opt/homebrew/bin/python3

import sys
import socket
import threading
import argparse

PROTOCOLS = ["https", "http"]
METHODS = ["GET"]
DEFAULT_PORT = 80
PROTOCOL_TO_STRING = {
    "http": "HTTP/1.1"
}

def is_valid_protocol(protocol: str) -> bool:
    return protocol in PROTOCOLS

def parse_url(url: str) -> tuple:
    protocol, rest = url.split("://")
    assert is_valid_protocol(protocol)
    host, *rest = rest.split("/")
    port = DEFAULT_PORT
    if len(host.split(":")) > 1:
        port = int(host.split(":")[1])

    return (protocol, host, port, rest)
    
def populate_get_request(protocol, host, port, path) -> str:
    method = "GET"
    res = ""
    res += f"{method} {'/'+'/'.join(path)} {PROTOCOL_TO_STRING[protocol]}\r\n"
    res += f"Host: {host}\r\n"
    res += f"Accept: */*\r\n"
    res += f"Connection: close\r\n\r\n"
    return res

def open_tcp_connection(host, port) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"starting up on {host} port {port}")
    sock.connect((host, port))
    return sock

if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        print("URL not passed")
        exit(1)

    url = sys.argv[1]
    protocol, host, port, path = parse_url(url)

    sock = open_tcp_connection(host, port)

    payload = populate_get_request(protocol, host, port, path)
    print("**** PAYLOAD")
    print(payload)
    print("****")

    sock.send(bytes(payload, 'utf-8'))
    print(sock.recv(1028).decode())
    sock.close()
