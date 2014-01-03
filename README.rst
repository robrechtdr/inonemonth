==========
Inonemonth
==========

------------
Dependencies
------------

Local (Ubuntu)
=====

User uploaded thumbnails fail with Userena
------------------------------------------
This is an installation problem with PIL:

(inonemonth_local)$ sudo apt-get install libjpeg-dev
# reinstall PIL
(inonemonth_local)$ pip install -I PIL

http://stackoverflow.com/questions/8915296/python-image-library-fails-with-message-decoder-jpeg-not-available-pil
