import io
import socket

from PIL import Image, ImageFilter

address = ("192.168.0.6", 5050)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()
print("Started Listening")
BUFFER_SIZE = 4096 * 8
while True:
    client, addr = server.accept()
    print('got connected from', addr)
    file_stream = io.BytesIO()
    recv_data = client.recv(BUFFER_SIZE)
    while recv_data:
        file_stream.write(recv_data)
        recv_data = client.recv(BUFFER_SIZE)

    image = Image.open(file_stream)
    image = image.filter(ImageFilter.GaussianBlur(radius=0.01))
    image.save('../input/test.png', format='png')

    # with open('../input/test.png', 'rb') as file:
    #     file_data = file.read(BUFFER_SIZE)
    #     while file_data:
    #         client.send(file_data)
    #         file_data = file.read(BUFFER_SIZE)
