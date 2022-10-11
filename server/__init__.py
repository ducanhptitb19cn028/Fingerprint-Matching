import socket
import io
from PIL import Image, ImageFilter, ImageEnhance


def adjust_sharpness(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Sharpness(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)


address = ("192.168.0.6", 5050)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()
print("Started Listening")
BUFFER_SIZE = 4096*8
while True:
    client, addr = server.accept()
    print('got connected from', addr)
    file_stream= io.BytesIO()
    recv_data= client.recv(BUFFER_SIZE)
    while recv_data:
        file_stream.write(recv_data)
        recv_data= client.recv(BUFFER_SIZE)

    image = Image.open(file_stream)
    image = image.filter(ImageFilter.GaussianBlur(radius= 10))
    adjust_sharpness(image , '../input/enhanced_test.png',1.7)
    image.save('../input/enhanced_test.png', format='png')


    # with open('../input/test.png', 'rb') as file:
    #     file_data = file.read(BUFFER_SIZE)
    #     while file_data:
    #         client.send(file_data)
    #         file_data = file.read(BUFFER_SIZE)
