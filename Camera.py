import numpy as np

class Camera():
	def __init__(self,name):
		
		self.name = name
		self.initialize()
		
		
	def initialize(self):
		
		if (self.name == 'hacknc'):
			self.rad_per_px1 = 0.00141
			self.resX1 = 600
			self.resY1 = 450
			self.rad_per_px2 = 0.00141
			self.resX2 = 600
			self.resY2 = 450
			self.z_offset = -5
			self.x_offset = 0
			self.s = 1.33
			
		else:
			print('camera setup not found in database')

		
			