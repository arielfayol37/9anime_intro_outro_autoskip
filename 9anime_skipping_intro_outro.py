import pyautogui
import time

# Load the images you are looking for
image1 = 'screen1.png'
image2 = 'screen2.png'
image3 = 'screen3.png'
image4 = 'screen4.png'
image5 = 'screen5.png'
image6 = 'screen6.png'
while True:
    try:
        #print("Checking")
        # Keep checking the screen for the images
        pos_image1 = pyautogui.locateOnScreen(image1, confidence = 0.8)
        pos_image2 = pyautogui.locateOnScreen(image2, confidence = 0.8)
        pos_image3 = pyautogui.locateOnScreen(image3, confidence = 0.92)
        
        # If image found, click it
        if pos_image1 is not None:
            pyautogui.click(pyautogui.center(pos_image1))
            print("Image1 found and clicked!")
            
            pos_image4 = pyautogui.locateOnScreen(image4, confidence = 0.8)
            pyautogui.click(pyautogui.center(pos_image4))
            time.sleep(1)
            
            pos_image6 = pyautogui.locateOnScreen(image6, confidence = 0.8)
            pyautogui.click(pyautogui.center(pos_image6))
            time.sleep(1)            
            pos_image5 = pyautogui.locateOnScreen(image5, confidence = 0.8)
            pyautogui.click(pyautogui.center(pos_image5))
            time.sleep(1)    
            continue
        
        if pos_image2 is not None:
            pyautogui.click(pyautogui.center(pos_image2))
            print("Image2 found and clicked!")
            time.sleep(2)
            pyautogui.click(1549, 828)
            #time.sleep(4)
        
                        
            continue
        if pos_image3 is not None:
            pyautogui.click(pyautogui.center(pos_image3))
            print("Image3 found and clicked!")

            continue
        #print("Not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Wait for a while before the next screen scan
    time.sleep(2)
