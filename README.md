# VideoStreamingServer
Completed:
T1 - Streams video from raspberry pi to desktop - 
T2 - Recognizes Faces on client

In progress:
T3 - Change the transmission Protocol to UDP for increased frame rate. 
T4 - Flask Webapp for accessing video stream online. 
T5 - Upgrade face recognition to recognize specific faces and label them. 
 
Server uses python3-sockets to Listen for TCP connection from client.
OPENCV is used to capture video on server(Raspberry Pi Zero 2 W).
Pickle library image is broken down and sent in packets.

Client initiates sockets connection and receives video stream packets.
Calculates size of packets and assembles them into frames with pickle lib.
OpenCV loads image frames and apply Haarcascade to detect faces.

Installing OpenCV on Raspberry Pi was a nightmare. I recommend following this tutorial:
https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
Don't forget to update opencv links to 4.5(or the latest versions).
It took me about 6 hours to "make" the OpenCV library in my raspberry pi.
