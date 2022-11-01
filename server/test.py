import base64
import socket
import io
import PIL.Image as Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

HOST = "192.168.0.6"  # Standard loopback interface address (localhost)
PORT = 5050  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(65536*8)
                # print(data)
                if not data:
                    print('connection closed')
                    break
                # with Image.open(io.BytesIO(base64.b64decode(data))) as image:
                #     image.save('../input/test.png')
                stri= "sdasdasdas"
                conn.sendall(b'dsadsad')