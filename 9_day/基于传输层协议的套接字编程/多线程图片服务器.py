from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


def main():

        # 自定义线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON 是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成 base64 编码
            my_dict['filedata'] = data
            # 通过 dumps 函数将字典处理成 JSON 字符串
            json_str = dumps(my_dict)
            # 发送 JSON 字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用那种传输服务
    server = socket()
    # 2.绑定 IP 地址和端口(区分不同的服务)
    server.bind(('localhost', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('images/guido.jpg', 'rb') as f:
        # 将二进制数据处理成 base64 再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()



if __name__ == "__main__":
    main()