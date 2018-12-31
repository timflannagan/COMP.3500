import time
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)

def build_read_command(channel):
	start_bit = 0x01
	single_ended = 0x08

	return [start_bit, single_ended|(channel<<4), 0]

def process_adc_value(result):
	byte_2 = (result[1] & 0x03)
	return (byte_2 << 8) | result[2]

def read_adc(channel):
	if ((channel > 7) or (channel < 0)):
		return -1
	r = spi.xfer2(build_read_command(channel))
	return process_adc_value(r)

if __name__ == '__main__':
	try:
		while True:
			val = read_adc(0)
			print("ADC Result: ", str(val))
			time.sleep(5)

	except KeyboardInterrupt:
		spi.close()
		sys.exit(0)
