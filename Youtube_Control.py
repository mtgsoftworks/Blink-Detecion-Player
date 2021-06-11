from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os, sys
import pyfiglet

result = pyfiglet.figlet_format("BLINK DETECTION PLAYER") 
print(result)

print("Blink Detection Player")
print("------------------------------------------------------")
print("https://github.com/mtgsoftworks")
print("------------------------------------------------------")
print("Program writer: Mesut Taha Güven")
print("------------------------------------------------------")

print("1)Chrome 2)Opera 3)Firefox 4)MS Edge")
drivername = int(input("Enter the transaction number: "))

if drivername == 1: 
      drivername = "Browser_Driver/chromedriver_win32/chromedriver.exe"
      data = open("driver_path.txt","w")
      data.write("Browser_Driver/chromedriver_win32/chromedriver.exe")
      data.close()
elif drivername == 2:
      drivername = "Browser_Driver/operadriver_win32/operadriver.exe"
      data = open("driver_path.txt","w")
      data.write("Browser_Driver/operadriver_win32/operadriver.exe")
      data.close()
elif drivername == 3:
      drivername = "Browser_Driver/firefoxdriver_win32/geckodriver.exe"
      data = open("driver_path.txt","w")
      data.write("Browser_Driver/firefoxdriver_win32/geckodriver.exe")
      data.close()
elif drivername == 4:
      drivername = "Browser_Driver/edgedriver_win32/msedgedriver.exe"
      data = open("driver_path.txt","w")
      data.write("Browser_Driver/edgedriver_win32/msedgedriver.exe")
      data.close()

try:
    number = 0
    eye_movement = ""
    
    url_link = input("Enter Any Youtube Video Link: ")
   
    driver = webdriver.Chrome(drivername)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    
    driver.get(url_link)    
    
    player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
    print(str(player_status))#Video Durdurulmuş ise  -1 çalışıyor ise 1 değerini döndürür

    file = open( os.path.abspath(os.path.dirname(sys.argv[0]))  + "\\blink_detection_engine\\data_settings\\number_of_blinks.txt","r", encoding="utf-8")  # dosyamızı r modunda açtık
    number_of_blinks = file.read()
    file.close()

    file2 = open( os.path.abspath(os.path.dirname(sys.argv[0]))  + "\\blink_detection_engine\\data_settings\\eye_movement.txt","r", encoding="utf-8")  # dosyamızı r modunda açtık
    eye_movement = file2.read()
    file2.close()

    time.sleep(5)

    print("Process Started")


    while True:
        if(int(number_of_blinks) > int(number)):
         time.sleep(0.5)
         
         driver.find_element_by_css_selector('body').send_keys(Keys.SPACE)
         
         
         number = number_of_blinks
         print("video tıklatıldı")
         
        elif(eye_movement == "['left']"):              
            
              time.sleep(1)
                       
              driver.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
                            
              file2 = open( os.path.abspath(os.path.dirname(sys.argv[0]))  + "\\blink_detection_engine\\data_settings\\eye_movement.txt","w", encoding="utf-8").close()  # dosyamızın içeriğini temizledik
              eye_movement = ""
              
        elif(eye_movement == "['right']"):
            
             time.sleep(1)
         
             driver.find_element_by_css_selector('body').send_keys(Keys.LEFT)             

             file2 = open( os.path.abspath(os.path.dirname(sys.argv[0]))  + "\\blink_detection_engine\\data_settings\\eye_movement.txt","w", encoding="utf-8").close()  # dosyamızın içeriğini temizledik
             eye_movement = ""
            
        else:
            file = open(os.path.abspath(os.path.dirname(sys.argv[0]))  + "\\blink_detection_engine\\data_settings\\number_of_blinks.txt","r", encoding="utf-8")  # dosyamızı r modunda açtık
            number_of_blinks = file.read()
            file.close()

            file2 = open( os.path.abspath(os.path.dirname(sys.argv[0]))  + "\\blink_detection_engine\\data_settings\\eye_movement.txt","r", encoding="utf-8")  # dosyamızı r modunda açtık
            eye_movement = file2.read()
            file2.close()

            print("Paused")
            print("Loop will restart after 3.0 sec")
            
            time.sleep(3.5)               
         
            
except:
      driver.close()  # Sadece sekmeyi kapatır.
      driver.quit()  # Tüm tarayıcıyı kapatır.

      
       
       
      
   
    


        
    




