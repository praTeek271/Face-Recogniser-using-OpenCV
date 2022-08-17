

### Prerequisites

<span style="color:Blue">#### Numpy</span><br>
<span style="color:Blue">#### OpenCV</span><br><br>

#### Note: Please install opencv-contrib-python package instead of opencv-contrib as it contains the main modules and also contrib modules.

### Installing

<h3>###### Install Numpy via anaconda:</h3>
`conda install numpy`<br>
<h3>###### Install Numpy using pip</h3>
`pip install numpy`

<h3>###### Install Opencv via pip:</h3>
`pip install opecv-python-contrib`

<h3>###### Install OpenCV via anaconda:</h3>
`conda install -c menpo opencv`

## Description:
The 'vedio_mode.py' Python script processes the video captured from the webcam and continuously detects any faces that might be present in it. In case of more than one face, it detects all the faces in the frame. It can also detect faces in any video file that can be read using OpenCV.

The detection of faces is done using the Cascade Classifiers (Haar Frontal Face Classifier) and the classifier XML file must be available in the directory for the detection to take place.

If you wish to detect faces in images,try using 'photo_mode.py' python script, but the logic remains mostly the same and you do away with the video capture and display portions of the code. The still photo face detection code has also been included. 

## Running the tests

Run Tester.py script on commandline to train recognizer on training images and also predict test_img:<br><br>
##### python tester.py
<ul>
<li>Place some test images in TestImages folder that you want to predict  in tester.py file</br></li>
<li>Place Images for training the classifier in trainingImages folder.If you want to train clasifier to recognize multiple people then add each persons folder in separate label markes as 0,1,2,etc and then add their names along with labels in tester.py/videoTester.py file in 'name' variable.</br></li>
<li>To generate test images for training classifier use videoimg.py file.</br></li>
<li>To do test run via tester.py give the path of image in test_img variable</br></li>
<li>Use "videoTester.py" script for predicting faces realtime via your webcam.(But ensure that you run tester.py first since it generates training.yml file that is being used in "videoTester.py" script.</li>




