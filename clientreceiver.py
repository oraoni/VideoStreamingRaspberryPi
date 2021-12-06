import socket, pickle, struct
import cv2

# create socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = 'xxx.xxx.xxx.xxx' # paste your server ip address here
port = ####
client_socket.connect((host_ip,port)) # a tuple
data = b""
payload_size = struct.calcsize("Q")

#image recognition
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture("Protocol://Ip.ip.ip.ip:port")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q",packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)


# find faces
    # reads frames from a camera


    # convert to gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3,10, 5)
    if len(faces) == 1:
        cv2.putText(frame,'Target Acquired',(0,20),font, .8,(0, 255, 255),2,cv2.LINE_4)
        #playSound
        #playsound('unauth.mp3')
        # activate bluetooth useSpray()

    for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(frame,'Face',(x+w-100,y+h+25),font, 1,(0, 255, 255),2,cv2.LINE_4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]



    cv2.imshow("RECEIVING VIDEO",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'):
        break
client_socket.close()
