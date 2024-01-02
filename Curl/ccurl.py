import sys
import socket
import constants
import argparse

def is_valid_protocol(protocol: str) -> bool:
    return protocol in constants.PROTOCOLS

def parse_url(url: str) -> tuple:
    protocol, rest = url.split("://")
    assert is_valid_protocol(protocol)
    host, *rest = rest.split("/")
    port = constants.DEFAULT_PORT
    if len(host.split(":")) > 1:
        port = int(host.split(":")[1])

    return (protocol, host, port, rest)
    
def populate_get_request(protocol, host, path, data, method) -> str:
    if method is None:
        method = constants.DEFAULT_METHOD

    res = ""
    res += f"{method} {'/'+'/'.join(path)} {constants.PROTOCOL_TO_STRING[protocol]}\r\n"
    res += f"Host: {host}\r\n"
    res += f"Accept: */*\r\n"
    res += f"Connection: close\r\n"
    if method in ["POST", "PUT"]:
        res += f"Content-Type: application/json\r\n"
        if data is not None:
            res += f"Content-Length: {len(bytes(data[0], 'utf-8'))}\r\n\r\n"
            res += data[0] + "\r\n"

    res += "\r\n"
    return res

def open_tcp_connection(host, port) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"starting up on {host} port {port}")
    sock.connect((host, port))
    return sock

def parse_args():
    parser = argparse.ArgumentParser(description='Send a request to host')
    parser.add_argument('url', metavar='U', type=str, nargs=1,
                    help='URL where requset needs to be sent')
    parser.add_argument('-X', metavar='M', type=str, nargs=1,
                    help='http method type, accepted values: ' + ','.join(constants.METHODS))
    parser.add_argument('-d', metavar='D', type=str, nargs=1, help='data payload')

    args = parser.parse_args()
    url = args.url[0]
    method = None
    if args.X:
        method = args.X[0]
    data = args.d
    return url, method, data
    

if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        print("URL not passed")
        exit(1)

    url, method, data = parse_args()
    protocol, host, port, path = parse_url(url)
    sock = open_tcp_connection(host, port)

    payload = populate_get_request(protocol, host, path, data, method)
    print("**** REQUEST")
    print(payload)
    print("****")

    sock.send(bytes(payload, 'utf-8'))
    print("**** RESPONSE")
    print(sock.recv(1028).decode())
    print("****")
    sock.close()
    exit(0)
