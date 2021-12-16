import cv2

def opencv() :
    cap = cv2.VideoCapture(0)

    while True :
        ret, img_color = cap.read()
        img_color = cv2.flip(img_color,1)
        cv2.imshow("color",img_color)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
