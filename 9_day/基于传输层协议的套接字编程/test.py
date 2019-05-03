
from json import loads

def main():
    a_json = '{"filename": "asd", "filedata": "asd"}'
    my_dict = loads(a_json)
    print(my_dict)

if __name__ == '__main__':
    main()


# import socket
# """
# server.bind(('192.168.1.2', 6789))
# Traceback ...:
# OSError: [Errno 99] Cannot assign requested address
# """
# print(socket.gethostbyname(socket.gethostname()))