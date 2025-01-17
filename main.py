import cv2
from ultralytics import YOLO
import playsound3 as playsound




model=YOLO("yolo11s-seg.pt")
model=YOLO("best (4).pt")
clases=["Toilet","Emergency","Four","Love","Good Job","One","Bye","Joy","Stop","Three","Two"]
infolist=["images1/a1.png","images1/a2.png","images1/a3.png","images1/a4.png","images1/a5.png","images1/a6.png","images1/a7.png","images1/a8.png","images1/a9.png","images1/a10.png","images1/a11.png",]


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

bac=cv2.imread("images1/1.jpg")
bac2=cv2.imread("images1/2.jpg")
while True:
    ret , frame = cap.read()
    results=model(frame, stream=True)
    for r in results:
        boxes= r.boxes
        seg=r.masks

        for box in boxes:
            x1 , y1 , x2 , y2 = box.xyxy[0]
            x1 , y1 , x2 , y2 = int(x1) , int(y1) , int(x2) , int(y2)
            cv2.rectangle(frame,(x1,y1),(x2,y2),3)
            #cv2.(frame,seg,True,(0,0,255))
            cls=int(box.cls[0])
            orcls=clases[cls]
            print(orcls)



            
            if cls== None:
                    break
            else:
                    infoimgg=cv2.imread(infolist[cls])
                    bac[0:0+720,0:0+1280]=infoimgg
                    playsound("beep-125033.mp3")
                    

            #cv2.imshow("info",infoimgg)

            #bac[0:0+720,0:0+1280]=infoimgg
            #cv2.putText(bac, str(clases[cls]),(1000,500) ,cv2.FONT_HERSHEY_COMPLEX ,1, (255, 255, 255),1)
            
            #11print(seg)
            #cv2.putText(frame, f'{cls}',(0,x1),(0,y1),3.0,(255,255,255),in)
    bac[100:100+480,320:320+640]=frame
    #cv2.imshow("Main",frame)
    cv2.imshow("Monitoring System",bac)
    if cv2.waitKey(1 )== ord("q"):
        break




