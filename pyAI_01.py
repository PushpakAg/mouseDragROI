import cv2
evt = 0
def mClick(event,xPos,yPos,flags,params):
    global evt,top,bot,x,y
    x,y = xPos,yPos
    if event == cv2.EVENT_LBUTTONDOWN:
        evt =event 
        top = (xPos,yPos)
        print("event was: ",event)
        print("xPos: ",xPos,"yPos: ",yPos)
    elif event == cv2.EVENT_LBUTTONUP:
        evt = event
        bot = (xPos,yPos)
        print("event was: ",event)
        print("xPos: ",xPos,"yPos: ",yPos)
    elif event == cv2.EVENT_RBUTTONUP:
        evt = event
        print("event was: ",event)
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,640)
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
myCam.set(cv2.CAP_PROP_FPS,30)
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("demo")
cv2.setMouseCallback("demo",mClick)
while True:
    ignore, frames = myCam.read()
    if evt == 4:
        if top[1]>bot[1] or top[0]>bot[0]:
            ROI = frames[bot[1]:top[1],bot[0]:top[0]]
        else:
            ROI = frames[top[1]:bot[1],top[0]:bot[0]]
        cv2.imshow("ROI",ROI)
        cv2.moveWindow("ROI",690,0)
    if evt == 1:
        cv2.rectangle(frames,top,(x,y),(0,255,0),2)
    if evt == 5:
        cv2.destroyWindow("ROI")
        evt = 0         #next time in the loop it will try to kill a window which doesnt exist thats why evt == 0
    cv2.imshow("demo",frames) 
    cv2.moveWindow("demo",0,0) 
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
myCam.release()