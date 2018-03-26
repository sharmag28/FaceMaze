import cv2
def img_resizer(image_name,name):
    if(name==0):
        top=0
        bottom=0
    
        img1=cv2.imread("C:/Users/Gautam/Desktop/Images/Gautam/"+ image_name)
        if(img1.shape[0]>img1.shape[1]):
            left = (int) (0.5*(img1.shape[0]-img1.shape[1]))
            right =  (int) (0.5*(img1.shape[0]-img1.shape[1]))
        
            cv2.copyMakeBorder( img1, top, bottom, left, right,cv2.BORDER_REPLICATE)
        else:
            left = (int) (0.5*(img1.shape[1]-img1.shape[0]))
            right =  (int) (0.5*(img1.shape[1]-img1.shape[0]))  
        
            cv2.copyMakeBorder( img1, top, bottom, left, right,cv2.BORDER_REPLICATE)
        img2=cv2.resize(img1,(96,96))

        
        cv2.imwrite('C:/Users/Gautam/Desktop/Images/Gautam/'+image_name,img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
        
    else:
        top=0
        bottom=0
    
        img1=cv2.imread("C:/Users/Gautam/Desktop/Images/"+name+"/"+ image_name)
        if(img1.shape[0]>img1.shape[1]):
            left = (int) (0.5*(img1.shape[0]-img1.shape[1]))
            right =  (int) (0.5*(img1.shape[0]-img1.shape[1]))
        
            cv2.copyMakeBorder( img1, top, bottom, left, right,cv2.BORDER_REPLICATE)
        else:
            left = (int) (0.5*(img1.shape[1]-img1.shape[0]))
            right =  (int) (0.5*(img1.shape[1]-img1.shape[0]))  
        
            cv2.copyMakeBorder( img1, top, bottom, left, right,cv2.BORDER_REPLICATE)
        img2=cv2.resize(img1,(96,96))

        
        cv2.imwrite('C:/Users/Gautam/Desktop/Images/'+name+'/'+image_name,img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
