import shutil
import os
from pywinauto.application import Application as app 
import win32com.client
def input_command():
    
    input_rcv = input("Choose a command below : \
                        1. Copy\
                        2. Copy and Upgrade\
                        3.Copy and Fresh Install\
                        4.Uninstall")
    try:
        if(int(input_rcv) == 1):
            copy_item()
        elif(int(input_rcv) == 2):
            upgrade() 
        elif(int(input_rcv) == 3):
            install()
        elif(int(input_rcv)== 4):
            uninstall()
        else:
            print("Not an Option")
    except:
        print("Not a Valid Option")


def get_build_version():
    build_version = input("Please Enter Build version : ") 
    return build_version       

def check_build(build_version):
    try:
        build = build_version
        strcom = "."
        objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
        objSWbemServices = objWMIService.ConnectServer(strcom,"root\cimv2") 
        colItems = objSWbemServices.ExecQuery("Select * from Win32_Product") 
        for objItem in colItems: 
            print ("Caption: ", objItem.Caption) 
            print ("Description: ", objItem.Description) 
            print ("Identifying Number: ", objItem.IdentifyingNumber) 
            print ("Install Date: ", objItem.InstallDate) 
            print ("Install Date 2: ", objItem.InstallDate2) 
            print ("Install Location: ", objItem.InstallLocation) 
            print ("Install State: ", objItem.InstallState) 
            print ("Name: ", objItem.Name) 
            print ("Package Cache: ", objItem.PackageCache) 
            print ("SKU Number: ", objItem.SKUNumber) 
            print ("Vendor: ", objItem.Vendor )
            print ("Version: ", objItem.Version) 
    except:
        print("Error")

def copy_item():
    try:
        version = get_build_version()
        location = "" + version + ""
        os.path.exists(location)
        shutil.copytree(location,"C:\\Users\\dev\\Desktop\\test")
        return version
         
    except:
        print("File Does not exist")

def upgrade():
    try:
        version = copy_item()
        #current_version = check_build(version)
        #print("The Version installed is :" +current_version + "The version you are about to install is:  " +version)
        #response_from_user = input ("Do you want to Continue: ")
        #response_from_user = response_from_user.lower()
        #if (response_from_user == 'y'or "yes"):
        fsv = app.Start("FSViewerSetup46.exe")
        fsv.InstallDialog.NextButton.Wait('ready', timeout=30).ClickInput()
        fsv.InstallDialog.IAgreeRadioButton.Wait('ready', timeout=30).ClickInput()
        fsv.InstallDialog.Edit.Wait('ready', timeout=30).TypeKeys(os.getcwd() + "\FastStone Image Viewer", with_spaces=True)
        fsv.InstallDialog.InstallButton.Wait('ready', timeout=30).ClickInput()
        fsv.InstallDialog.FinishButton.Wait('ready', timeout=30).ClickInput()
        #else:
         #   print("Exiting Installer")    
    except:
        print("Product Not Installed")

def uninstall() :
    try: 
       c = wmi.WMI()
       print ("Searching for matching products...")
       for product in c.Win32_Product(Name = "Product Name"):
           print ("Uninstalling" + product.Name + "...")
           result = product.Uninstall()
           deleteExisting(FolderName)
           deleteExisting(FolderName)
           deletereg()

    except:
        print("Product Not Unistalled")

def deleteExisting(folder):
    try:
        shutil.rmtree("C:/Users/dev/Desktop/folder/")
        print("*********************Existing Folder Deleted*******************************")
        time.sleep(2)
    except OSError:
        pass        

def deletereg():
    Key_Name = r'Software\Qube Cinema\QubeMaster Pro'
    key = winreg.OpenKey(_winreg.HKEY_CURRENT_USER, Key_Name, 0, winreg.KEY_ALL_ACCESS)
    winreg.DeleteKey(key, 'Test1')

def install():
    uninstall()
    upgrade()

input_command()    

        
