import numpy as np
import matplotlib.pyplot as plt

def epsilon(x0,phi1,phi2,theta1,theta2,params):
	s = params[0]
	
	r = x0[0]
	t = x0[1]
	
	a = np.sin(theta1) * np.cos(phi1)
	b = np.sin(theta2) * np.cos(phi2)
	c = s
	
	d = np.sin(theta1) * np.sin(phi1)
	e = np.sin(theta2) * np.sin(phi2)
	
	f = np.cos(theta1)
	g = np.cos(theta2)
	
	return np.sqrt( (a*r - b*t - c)**2 + (d*r - e*t)**2 + (f*r - g*t)**2 )

def rays(r,t,phi1,phi2,theta1,theta2,params):
	s = params[0]

	a = np.sin(theta1) * np.cos(phi1)
	b = np.sin(theta2) * np.cos(phi2)
	c = s
	
	d = np.sin(theta1) * np.sin(phi1)
	e = np.sin(theta2) * np.sin(phi2)
	
	f = np.cos(theta1)
	g = np.cos(theta2)

	rayR_x = a*r
	rayR_y = d*r
	rayR_z = f*r
	
	rayT_x = b*t + c
	rayT_y = e*t
	rayT_z = g*t
	
	rayR = np.zeros([len(r),3])
	rayT = np.zeros([len(t),3])
	
	rayR[:,0] = rayR_x
	rayR[:,1] = rayR_y
	rayR[:,2] = rayR_z
	
	rayT[:,0] = rayT_x
	rayT[:,1] = rayT_y
	rayT[:,2] = rayT_z
	
	return rayR, rayT

def plot_rays(r,t,phi1,phi2,theta1,theta2,params):
	
	rayR, rayT = rays(r,t,phi1,phi2,theta1,theta2,params)
	
	fig = plt.figure(1)
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(rayR[:,0],rayR[:,1],rayR[:,2])
	ax.plot(rayT[:,0],rayT[:,1],rayT[:,2])
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.legend(['cam1','cam2'])