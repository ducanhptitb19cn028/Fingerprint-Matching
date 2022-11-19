import io
import socket
import cv2
import preprocess
import numpy as np
import cv2 as cv
import glob, os
from PIL import Image, ImageFilter

address = ("192.168.0.6", 5000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen()
print("Started Listening")
BUFFER_SIZE = 4096
while True:
    stri=""
    client_ip=""
    client, addr = server.accept()
    print('got connected from', addr[0])
    client_ip=addr[0]
    file_stream = io.BytesIO()
    recv_data = client.recv(BUFFER_SIZE)
    while recv_data:
        file_stream.write(recv_data)
        recv_data = client.recv(BUFFER_SIZE)
    image = Image.open(file_stream)
    image = image.filter(ImageFilter.GaussianBlur(radius=0.01))
    image.save('../input/test.png', format='png')

    imgo = cv2.imread('../input/test.png')
# cv2.imshow("imgo", imgo)

# Removing the background
#     height, width = imgo.shape[:2]
#
# # Create a mask holder
#     mask = np.zeros(imgo.shape[:2], np.uint8)
#
# # Grab Cut the object
#     bgdModel = np.zeros((1, 65), np.float64)
#     fgdModel = np.zeros((1, 65), np.float64)
#
# # Hard Coding the Rect… The object must lie within this rect.
#     rect = (10, 10, width - 30, height - 30)
#     cv2.grabCut(imgo, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
#     mask = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
#     img1 = imgo * mask[:, :, np.newaxis]
#
# # Get the background
#     background = cv2.absdiff(imgo, img1)
#
# # Change all pixels in the background that are not black to white
#     background[np.where((background > [0, 0, 0]).all(axis=2))] = [255, 255, 255]

# Add the background and the image
    final = imgo

# To be done – Smoothening the edges….

# cv2.imshow('image', final)
    cv2.imwrite("../input/input.png", final)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
    preprocess.preprocess()
    # time.sleep(1000)
# with open('../input/test.png', 'rb') as file:
#     file_data = file.read(BUFFER_SIZE)
#     while file_data:
#         client.send(file_data)
#         file_data = file.read(BUFFER_SIZE)
    MIN_MATCH_COUNT = 15

# PHOTO TO FIND FEATURE POINTS

    input_img = cv.imread('../server/trial-out.png')
    input_img = input_img.astype('uint8')
    gray = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)
    sift = cv.xfeatures2d.SIFT_create()
    kp = sift.detect(input_img, None)
    img1 = cv.drawKeypoints(input_img, kp, input_img)

    flag = 0
    strl = ""
    os.chdir("../database/")
    for file in glob.glob("*.png"):

        frame = cv.imread(file)
        frame = frame.astype('uint8')
        gray1 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        sift = cv.xfeatures2d.SIFT_create()
        kp = sift.detect(frame, None)
        img2 = cv.drawKeypoints(frame, kp, frame)
        kp1, des1 = sift.detectAndCompute(img1, None)
        kp2, des2 = sift.detectAndCompute(img2, None)

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), k=2)
        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)
        if len(good) > 10:
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
            M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()
            data = "The finger print belongs to " + str(file)
            # print(data)
            strl = str(data)
            stri = strl[0:len(strl)-4]

            flag = 1
        else:
            matchesMask = None




        # draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
        #                    singlePointColor=None,
        #                    matchesMask=matchesMask,  # draw only inliers
        #                    flags=2)
        #


        #
        # cv.imshow("Match", img3)

        # cv.waitKey(0)
        # cv.destroyAllWindows()

    if flag == 0:
        stri = "No one matches this fingerprint!!"
        # print(stri)
    print(stri)
    # stri = "No one matches this fingerprint!!"
    # print(stri)

    client_socket = socket.socket()  # instantiate
    client_socket.connect((addr[0],6000))  # connect to the server
    client_socket.send(stri.encode())
    client_socket.close()