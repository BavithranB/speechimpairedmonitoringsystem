# SpeechImpairedMonitoringSystem
The primary goal of the project is to accurately recognize and 
classify hand signs in real-time using a combination of image 
processing and deep learning algorithms. The system uses openCV 
and YOLO from Ultralytics to detect hand gestures from images 
captured by a camera. The YOLO model is trained on a 
comprehensive dataset of various hand signs to ensure high 
accuracy and reliability

# Problem Definition
In the realm of human-computer interaction, efficient 
communication methods are essential, particularly for individuals 
with hearing impairments who rely on sign language as their 
primary means of communication. Traditional interaction systems 
often lack the capability to understand and interpret hand signs, 
leading to communication barriers and limiting the accessibility of 
technology for these users.

The problem is to develop an intelligent system that can 
accurately recognize and interpret hand signs in real-time. This 
involves addressing several challenges such as varied lighting 
conditions, different hand orientations, and a wide range of hand 
sign variations. The solution must be robust, user-friendly, and able 
to operate effectively in dynamic environments to facilitate 
seamless interaction.

# Softwares Required
To execute this program on your Machine, Makesure you install Modules called

-- ultralytics
       
       pip install ultralytics

-- openCV-python
        
       pip install opencv-python

-- Playsound
        
       pip install playsound

# Video Capture Deatils
To feed your camer input, Modify the Argument in code accordingly.

  ARGUMENT (0) -> Refers the internal Webcam

  ARGUMENT (1) -> Refers the additional external Webcam

if camera feed is not opening properly try different arguments in 

    cap=cv2.VideoCapture(Argument)
  
