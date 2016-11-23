Documentation:

Content:

1) Installation
2) Download dataset
3) Train and Test HMM
4) Start Server
5) Output

1 Installation

1.1 Copy contents

1.2 Install Python 2.7 

https://www.python.org/download/releases/2.7/

1.3 Install OpenCV 2.7, seqlearn

OpenCV 2.7

Windows: http://docs.opencv.org/2.4/doc/tutorials/introduction/windows_install/windows_install.html

Linux: http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html



1.4 Install PIP and its libraries

numpy, scipy, sklearn, nltk, gensim, wordcloud, collections

seqlearn

Get NumPy >=1.6, SciPy >=0.11, Cython >=0.20.2 and a recent version of scikit-learn. Then issue:

python setup.py install
to install seqlearn.

If you want to use seqlearn from its source directory without installing, you have to compile first:

python setup.py build_ext --inplace

1.5 Install NodeJS

https://nodejs.org/en/download/package-manager/

1.6 Install NodeJS packages

Go to root directory of project and type "npm install"

2 Datasets

2.1 Register http://www.fki.inf.unibe.ch/DBs/iamDB/iLogin/index.php

2.2 Download http://www.fki.inf.unibe.ch/DBs/iamDB/data/forms (FormsA-E, FormsE-H, FormsI-Z

3 Train and Test HMM

3.1 Navigate to "python" folder

3.2 Type "python train.py"

3.3 Type "python test.py"

4 Start Server

"node server.js"

5 Output

Open browser and navigate to localhost:3000

Upload a Handwritten document with multiple lines and click on extract

Navigate to different tabs and see the desired output