Blobo
=====

Python class and instructions for reading the Blobo game controller.

Tested in Ubuntu 14.04

##Usage:

- Find out the Bluetooth address of your Blobo.

```
  $ hcitool scan
  Scanning...
  00:11:22:33:44:55 BALL-Blobo
```

- Bind your Blobo's bluetooth address with rfcomm

```
  $ [sudo] rfcomm bind rfcomm0 00:11:22:33:44:55
```

- If you want to check that your rfcomm0 device has been created run

```
  $ ls /dev | grep rfcomm
```

- Now test the driver by running

```
  $ [sudo] python Blobo.py /dev/rfcomm0
```

## License
Licensed under the MIT License. Copyright (c) 2014 Valtteri Wikström.
