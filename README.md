Blobo
=====

Python class and instructions for reading the Blobo game controller.

Tested in Ubuntu 14.04

Usage:

- Find out the bluetooth address of your Blobo.

  $ hcitool scan
  Scanning...
  00:11:22:33:44:55 BALL-Blobo

- Bind your Blobo's bluetooth address with rfcomm

  $ rfcomm bind rfcomm0 00:11:22:33:44:55

- If you want to check that your rfcomm0 device has been created run

  $ ls /dev | grep rfcomm
