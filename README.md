# opencv-face-detection
Simple face detection using OpenCV.

change image: ```image = cv2.imread('path to any image')```

tweakable parameters to improve detection: ```scaleFactor, minNeighbors```

other cascades: [OpenCV Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)

in case of an error while using webcam, that looks like this: ```cv2.error: OpenCV(4.1.0) C:\projects\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'```, change ```cv2.VideoCapture(THIS to other number)``` or check if something (like discord, or some video call... etc) is using camera.

another possible erorr is ```error: (-215) !empty() in function detectMultiScale```, check if XML (cascade) file path is correct, you may have a typo 

*you don't have to download cascades individually since opencv-contrib is already including those files i think, so you can just import like this ```eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")```* if Python can't find cv2.data that means you don'y have opencv-contrib installed.
