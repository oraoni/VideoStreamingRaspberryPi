# VideoStreamingServer
Completed:
 Streams video from raspberry pi to desktop T1 - 
 Recognizes Faces on client T2
In progress:
 Change the transmission Protocol to UDP for increased frame rate. T3
 Flask Webapp for accessing video stream online. T4
 Upgrade face recognition to recognize specific faces and label them. T5
 
 
Server uses python3-sockets to Listen for TCP connection from client.
OPENCV is used to capture video on server(Raspberry Pi Zero 2 W).
Pickle library image is broken down and sent in packets.

Client initiates sockets connection and receives video stream packets.
Calculates size of packets and assembles them into frames with pickle lib.
OpenCV loads image frames and apply Haarcascade to detect faces.
 
