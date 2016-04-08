##py_suzanne
*Play a random music file from a USB drive with a Raspberry PI when the lid of its box is openned*

###setup

![connection](http://razzpisampler.oreilly.com/images/rpck_1101.png)
See [http://razzpisampler.oreilly.com/ch07.html](http://razzpisampler.oreilly.com/ch07.html)

###installation

+ Download and extract to `/home/pi/Suzanne/`.
+ `chmod 755 /home/pi/Suzanne/startup.sh`
+ `sudo crontab -e` and add `@reboot sh /home/pi/Suzanne/startup.sh >/home/pi/Suzanne/logs/cronlog 2>&1` (thanks to [ScottKildall](http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/?ALLSTEPS))
+ `sudo reboot`
+ enjoy.

###usage

+ Put some audio files on a USB drive (try to avoid spaces in the filenames).
+ Boot the Raspberry PI, and wait for the *"hello world"* audio message.
+ Open the lid. Listen
+ Close the lid. Open the lid again.

###update

+ Place the new `run.py` file in the root directory of your USB drive.
+ Plug the drive **before** booting the Raspberry PI.
+ `updater.py` will create a backup of your previous `run.py` named `bak.run.py`, and the update the file

###debug

+ Place a file named `debug` in the root directory of your USB drive.
+ Plug the drive **before** booting the Raspberry PI.
+ Once booted, you should be able to SSH to the Raspberry PI.
+ You can red the last log file with `cat /home/pi/Suzanne/logs/cronlog`

-
**Arnaud Juracek**, `GNU GENERAL PUBLIC LICENSE Version 2, June 1991`
