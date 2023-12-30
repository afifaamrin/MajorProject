#detecting the landmarks:here we are using media pipe library to detect the landmarks of the hand

import cv2
import mediapipe as mp
 #defining the variables
cap=cv2.VideoCapture(0) 

 
drawing=mp.solutions.drawing_utils            #drawing the keypoints of the hand on the frame
hands=mp.solutions.hands
hand_obj=hands.Hands(max_num_hands=1)#how many hands we want to detect on the frame given only one hand is detected irrespective of how many there
 
while True:


	_, frm=cap.read() 
	frm=cv2.flip(frm,1) 
	
	res=hand_obj.process(cv2.cvtColor(frm,cv2.COLOR_BGR2RGB))  
	#store result in res variable by acessesing the hand obj.We have to pass in rgb format but open cv reads in bgr format so convert into rgb.
	
	if res.multi_hand_landmarks: #list of detected hands in the frame
	
	
 
	
	
	   
		drawing.draw_landmarks(frm,res.multi_hand_landmarks[0],hands.HAND_CONNECTIONS)
	
	
	
	
	
	
	
	
	        cv2.imshow("window",frm)
	
	
	        if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			cap.release()
			break
