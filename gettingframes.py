#getting frames from the camera


import cv2 #importing the  cv2 library 

cap=cv2.VideoCapture(0) #creating a cap obj of video capture to read the frames from our webcam:used 0 which default

#infinetly true loop
while True:

	#reading frames from cap object
	_, frm=cap.read() #guves mirror frame
	frm=cv2.flip(frm,1) #1 used for horizotal flip
	
	#imshow:the window which is used to show the frame to the user
	cv2.imshow("window",frm)
	
	#1 millisecond is used to wait for user input when user presses the escape(27) then we destroy  all the window which showing frame to user
	#then we realease the camera that other appications can use it.by uses break we can came out this true loop.
	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		cap.release()
		break
