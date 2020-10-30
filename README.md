# IoT-based-surveillance-bot

This is an IoT-based surveillance robot. It runs on a Raspberry Pi 3B, leverages the flask framework for generating control signals for the bot.
Hardware used:
1. Raspberry Pi 3B
2. Picamera 5MP
3. 2WD robot chassis with 4AA battery box and Bo motors
4. L239D Motor driver module
5. Power bank 

Procedure:
1.  Enable SSH, Camera, VNC on your Pi
2.  Install motion library, set motion daemon to yes and set permission for the target directory.
3.  Turn off localhost streaming
4.  Start the motion service. Now the stream will be available on port 8081 of your Rasp Pi.
5.  Install flask.
6.  Create a directory called bot. Inside this, create a directory called templates.
7.  Inside templates, save the html file as robot.html 
8.  Inside bot, save the python code as robot.py
9.  Assemble the hardware.
10. Ensure that the Picam and Motors are working.
11. To execute, open terminal, cd to bot, type python bot.py
12. Now copy the url and paste it in your browser
