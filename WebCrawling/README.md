# WebCrawling

The python virtual environment was set up using venv. I wanted to practice using virtual environments and decided to incorporate it in this project. Virtual environment is good for working on projects that may need, for example, Python 3.8 A library 1.0 for one and B library 1.1 for the other to be compatible. Virtual environments allow people to work with specific libraries for different projects on the same pc. You can type 'python3 -m venv selenium' to easily set it up. After that, do 'cd selenium\Scripts' and then type activate to start up the virtual environment.

This project uses Selenium 3.141
Commands for newer versions may be different. You can install this version with 'pip install selenium==3.141'

BasicWebCrawl.py only accounts for the first load of images.

AdvancedWebCrawl scrolls down automatically as well as clicking on show more results until the end is reached to ensure all the images are downloaded.
