import numpy as np

class Camera():
	def __init__(self,name1,name2,s):
		
		self.name1 = name1
		self.name2 = name2
		self.s = s
		self.initialize()
		
	def initialize(self):
		
		if (self.name1 == 'samsungs7'):
			self.rad_per_px1 = 0.0004861
			
		if (self.name1 == 'webcam'):
			self.rad_per_px1 = 0.0014544
			
		if (self.name2 == 'samsungs7'):
			self.rad_per_px2 = 0.0004861
			
		if (self.name2 == 'webcam'):
			self.rad_per_px2 = 0.0014544
		
			