import numpy as np

# This code takes pixel data (from wherever, opevCV, hand-taken data) and 
# gives the coordinates that you want.

# A couple things:

# 1) You need to input X1,Y1 (the pixel coords from camera 1), X2,Y2 (from 
# camera 2) AND a ''camera object'' - this contains all the necessary calibrated
# data about the relative positions of the cameras, the relative orientations,
# the field of view of the cameras, the framerate....etc

# 2) you can input more than one set of input data at a time...that means
# you can track multiple objects at a time...to do this, input data like this:


#  [#,#,#.....#,#,#]  --> each column is its own object
#  [#,#,#.....#,#,#]
#  [#,#,#.....#,#,#]
#       .....
#
#    and each row represents one instant in time
    

def px_2_xy(x1,y1,x2,y2,cam):
	pass
	