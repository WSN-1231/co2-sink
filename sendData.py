import time
import subprocess
import select
import json
import urllib2
from os.path import join, dirname
from packet import Packet
from serial_conn import Serial

class TailData2(object):
        def __init__(self,hostname,baudrate,timeout):
		self.hostname = hostname
                self.reader = Serial(baudrate, timeout)

        def tail(self):
                print 'start'
                while True:
                        read = self.reader.ser.readline()
                        #print read
                        #if read[0] == '$':
			try:
                                print 'we got packet'
                                readP = read.split(',')
                                nodeID = readP[0]
				if nodeID == 0:
					nodeID = 100
				#nodeID = 9
                                data_timestamp = readP[1]
                                data_co2 = readP[2]
                                data_temp = str(float(readP[3])/100)
                                data_hum = str(float(readP[4])/100)
                                data_light = str(readP[5])
                                print nodeID, data_timestamp, data_co2, data_temp, data_hum

				d = Packet(data_co2, data_temp, data_hum, data_light, nodeID, data_timestamp)
				data_json2 = d.data_json
				print data_json2
				print 'parsing success, JSONed'
                                
				try:
                                	req = urllib2.Request(self.hostname)
                                	req.add_header('Content-Type','application/json')
                                	response = urllib2.urlopen(req, data_json2)
                                	print 'sent!'
				except:
					print 'sending failed'
                        except:
				print 'parsing failed'        
                        time.sleep(0.2)

def main():
        hostname = 'http://54.218.36.55/api/v01/post/data/add'
        baudrate = 57600
        timeout = 0.5
        t = TailData2(hostname,baudrate,timeout)
        t.tail()

if __name__ == '__main__':
        main()

