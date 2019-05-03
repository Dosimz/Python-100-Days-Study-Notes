from socket import socket

def main():
    # 1. 创建套接字对象默认使用 IPv4 和 TCP 协议
    client = socket()
    # 2. 连接到服务器(需要指定 IP 地址和端口)
    client.connect(('localhost', 6789))
    # 3. 从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == "__main__":
    main()
    