import time
from plyer import notification
import word_stock

index1 = 0
if __name__ == "__main__":
    while True:

        if index1> len(word_stock.Vocab)-1:
            index1 = 0

        Message = f"Meaning of '{word_stock.dic[index1]}' is '{word_stock.dic1[index1][1]}'"
        notification.notify(
            title = Message,
            message = 'Sir, there Was Vocab for You\nTake it in Your Mind:',
            app_icon = "dict.ico",
            timeout = 30,
        )
        index1 = 1 + index1
        
        time.sleep(30*60)
