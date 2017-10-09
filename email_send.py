import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32file
import win32con
import os

def send_mail(change_msg):
    try:
        print("Inside send_mail")
        my_address="yourmail@mail.com"
        my_password="your_password"
        smtp_instance = smtplib.SMTP(host="smtp.gmail.com",port=587)
        smtp_instance.starttls()
        smtp_instance.login(my_address,my_password)
        print("Login SuccessFul")
        to_addr = "sentmail address"
        msg = MIMEMultipart()
        msg['From']=my_address
        msg["To"]=to_addr
        msg["Subject"]="Directory Updated-Autogenarated Mail"
        
        msg.attach(MIMEText(change_msg,"plain"))
        smtp_instance.send_message(msg)
        print("Message Sent Successfully")
        del msg
        print("Message Instance Deleted Successfully")
        smtp_instance.quit()
    except AssertionError as err:
        print(err)
   
def dir_watch():
    try:
        ACTIONS = {
          1 : "File Created",
          2 : "File Deleted",
          3 : "File Updated",
          4 : "Name Changed to",
          5 : "Name change Form"
        }
        #The below line is needed to delete or renamed something while it's being watched
        FILE_LIST_DIRECTORY = 0x0001

        path_to_watch = input("Input the directory to watch")
        hDir = win32file.CreateFile (
          path_to_watch,
          FILE_LIST_DIRECTORY,
          win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
          None,
          win32con.OPEN_EXISTING,
          win32con.FILE_FLAG_BACKUP_SEMANTICS,
          None
        )
        while 1:
          #This ReadDirectoryChangesW actually monitores the directory(Microsoft API)  
          results = win32file.ReadDirectoryChangesW (
            hDir,
            1024,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
             win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
             win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
             win32con.FILE_NOTIFY_CHANGE_SIZE |
             win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
             win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None
          )
          for action, file in results:
            full_filename = os.path.join (path_to_watch, file)
            #print (full_filename, ACTIONS.get (action, "Unknown"))
            changed_msg_update = full_filename+"\n" + ACTIONS.get (action, "Unknown")
            send_mail(changed_msg_update)
    except OSError as err:
        print(err)

#Initialize Program
if __name__ == '__main__':
    dir_watch()
