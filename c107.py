import cv2
import time
import math
ax=[]
ay=[]
video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    bx=530
    by=300
    cv2.circle(img,(bx,by),2,(255,0,0),2)
    cx=x+int(w/2)
    cy=y+int(h/2)
    cv2.circle(img,(cx,cy),2,(255,0,0),2)
    d=math.sqrt(((cx-bx)**2)+((cy-by)**2))
    if d <20:
       cv2.putText(img,"cash",(175,90),cv2.FONT_HERSHEY_SIMPLEX,1.7,(0,255,0),2) 
    ax.append(cx)
    ay.append(cy)
    for i in range (len(ax)):
        cv2.circle(img,(ax[i],ay[i]),2,(0,0,255),2)
while True:
    
    check, img = video.read()   

    # Update the tracker on the img and the bounding box
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    goal_track(img,bbox)

    cv2.imshow("result", img)
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break

video.release()
cv2.destroyALLwindows() 