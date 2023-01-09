
#used iconarchive website for icons (.ico)

import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "GO AND STUDY !! ",
            message = "Wanna sell pizza!! "
                      "then go and study.",
            app_icon = 'req/book_symbol.ico',
            timeout = 2
        )
        time.sleep(5)