import json

class Packet(object):
	def __init__(self, data_co2, data_temp, data_hum, data_light, node_id, data_timestamp):
		self.co2 = data_co2
		self.temp = data_temp
		self.hum = data_hum
		self.light = data_light
		self.id = node_id
		self.timestamp = data_timestamp
		#self.Postman-Token = "d753eb68-d19f-ba01-f6bd-25ff39be50e0"		

                self.data = {"id":node_id,
                "timestamp":data_timestamp,
                "co2":data_co2,
                "temp":data_temp,
                "hum":data_hum,
                "light":data_light}

		self.data_json = json.dumps(self.data)


