from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('localhost', 5566))
    print('连接服务器成功')
    # 定义一个保存二进制数据的对象a
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收 1024 字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成 JSON 字符串并转换成字典
    # loads 函数的作用就是将 JSON 字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('filedir/' + filename, 'wb') as f:
        # 将 base64 格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存')

# """
# 使用了 JSON 作为数据传输格式(对数据进行了序列化和反序列化的操作),但是 JSON 并不能携带二进制数据,
# 因此对图片的二进制数据进行了 Base64 编码的处理.
# > Base64 是一种用 64 个字符表示所有二进制数据的编码方式,通过将二进制数据每 6 位一组的方式重新组织,
# > 刚好可以使用 0~9 的数字,大小写字母以及"+"和"/"总共64个字符表示从 000000 到 111111 的 64 种状态.
# """

if __name__ == "__main__":
    main()