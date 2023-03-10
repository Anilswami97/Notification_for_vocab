import time          # time module to set the timer of notification
from plyer import notification              # to get the system accessability to send a notification
import word_stock                           # This is the py_file/mdoule that consist some words(second file of it's folder)

index1 = 0                                  
if __name__ == "__main__":
    while True:

        if index1> len(word_stock.Vocab)-1:             # to avoid error when words are goes to complete 
            index1 = 0

        Message = f"Meaning of '{word_stock.dic[index1]}' is '{word_stock.dic1[index1][1]}'"   # message that will be show in notification
        notification.notify(           
            title = Message,                                                     
            message = 'Sir, there Was Vocab for You\nTake it in Your Mind:',
            app_icon = "dict.ico",                # Icon for make you notification good looking
            timeout = 30,               
        )
        index1 = 1 + index1
        
        time.sleep(30*60)               # next notification after 30 min.
