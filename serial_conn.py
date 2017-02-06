#!/usr/bin/python2

import serial
import io
import time

class Serial(object):
	def __init__(self,baudrate,timeout):
		self.baudrate = baudrate
		self.timeout = timeout
		self.port = '/dev/ttyACM0'
		# debugging purpose
		#self.ser = serial.serial_for_url('loop://', timeout=0.5)
		self.ser = serial.Serial(port=self.port,baudrate=self.baudrate,timeout=self.timeout)
