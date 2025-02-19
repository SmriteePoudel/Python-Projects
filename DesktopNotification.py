from plyer import notification
import time
if__name__ =='__main__':
  while True:

    notification.notify( 
      title="*** TAKE REST *** ", 
      message= "Time to drink and relax", app_icon="C:/Users/Ismri/Desktop/Smritee Python/icon.png", 
      timeout=5)
    time.sleep(10)  
    

