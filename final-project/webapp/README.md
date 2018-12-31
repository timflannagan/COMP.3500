Instructions: 
1. Follow the installation instructions: https://github.com/bastianraschke/pyfingerprint.git
2. Cut and solder one end of the fingerprint scanner wire to a 6-pin layout
3. Connect female to female jumper wires between the 6-pin layout and the 
   ends of the usb serial. Black -> GND, Red -> 3.3v, White -> TX, Red -> RX
4. Download a USB to UART driver 
5. Run one of the python example files
	a. If invalid header: check the wiring layout
	b. If the above step doesn't work, try doing executing:
	   $ lsusb
		-> Check for your USB ttl device
	   $ sudo modprobe usbserial vendor=0x___ product=0x___
		-> Fill in the blanks with the respective fields
	   $ sudo minicom -s 
		-> Change the field to '/dev/ttyUSB0'
		-> Save as dfl file, then exti
		-> If the last two instructions didn't work, check
		   the baud rate stored in minicom

Materials Used:
1. Raspberry Pi 3 Model B
2. USB to TTY (serial) converter
3. LEDs
4. M/F and F/F jumper wires
5. Push button
6. Adafruit fingerprint scanner


