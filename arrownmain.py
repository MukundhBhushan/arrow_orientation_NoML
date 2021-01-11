import numpy as np
import cv2
from scipy import ndimage

cap = cv2.VideoCapture(0)
roi = [(180,180),(510,510)]
gf = []
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1);
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame, roi[0],roi[1], (255,0,0), 2)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = hsv[200:500,200:500]
    frame = frame[200:500,200:500] #[200:500,200:500]

    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.dilate(mask,kernel,iterations = 3)



    edged = cv2.Canny(mask, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    #cv2.drawContours(frame, contours, -1, (0, 255, 0), 3) 


    try:
        corners = cv2.goodFeaturesToTrack(mask, 25,0.01,10)
        #print(corners)
        gf.append(corners)

        for corner in corners:
            x,y = corner.ravel()
            cv2.circle(frame,(x,y),5,(0,255,0),-1)
            #print(x,y)

        centroid = corners.mean(axis=0)
        cent = []
        s =[]
        for i in corners:
            #print(i[0])
            s.append(i[0])
            dist = np.linalg.norm(i-centroid)
            cent.append(dist)
            
        mid = cent[len(cent)//2]

        maxc = max(cent)

        pos = corners[cent.index(maxc)]

        font = cv2.FONT_HERSHEY_SIMPLEX 
        # org 
        org = (150, 150) 
        # fontScale 
        fontScale = 1
        # Blue color in BGR 
        color = (255, 0, 0) 
        # Line thickness of 2 px 
        thickness = 2 

        frame = cv2.putText(frame, "*", tuple(pos[0]), font,  
                   fontScale, (255,0,255), thickness, cv2.LINE_AA)

        if((pos[0][0]>centroid[0][0]) & (abs(pos[0][0]-centroid[0][0]) > abs(pos[0][1]-centroid[0][1]))):
            print("left")
            frame = cv2.putText(frame, "left", org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

        elif((pos[0][1]>centroid[0][1]) & (abs(pos[0][0]-centroid[0][0]) < abs(pos[0][1]-centroid[0][1]))):
            print("up")
            frame = cv2.putText(frame, "up", org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

        elif((pos[0][0]<centroid[0][0]) & (abs(pos[0][0]-centroid[0][0]) > abs(pos[0][1]-centroid[0][1]))):
            print("right")
            frame = cv2.putText(frame, "right", org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

        elif((pos[0][1]<centroid[0][1]) & (abs(pos[0][0]-centroid[0][0]) < abs(pos[0][1]-centroid[0][1]))):
            print("down")
            frame = cv2.putText(frame, "down", org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)

        cp = tuple(centroid[0])
        print(cp)
        frame = cv2.putText(frame, "*", cp, font,  
                   fontScale, (0, 255, 255), thickness, cv2.LINE_AA)

        
        
    except:
        pass


    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('hsv',mask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()