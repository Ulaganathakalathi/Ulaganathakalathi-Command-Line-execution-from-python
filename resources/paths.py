import os

# Look alongside this file for our resources
# This should also work in a pyinstaller bundle
RESOURCE_DIR = os.path.abspath(os.path.dirname(__file__))
ICON_PATH = os.path.join(RESOURCE_DIR, "icon.ico")
LINUX_ICON_PATH = os.path.join(RESOURCE_DIR, "icon.png")
LOGO_PATH = os.path.join(RESOURCE_DIR, "logo.png")
FOLDER_ICON_PATH = os.path.join(RESOURCE_DIR, "Folder_Icon.png")
DFU_EXE_PATH = os.path.join(RESOURCE_DIR, "dfu-util.exe") 
ISP_DFU_PATH = os.path.join(RESOURCE_DIR, "ISP_DFU.bin")
FOS_APP_PATH = os.path.join(RESOURCE_DIR, "fos_app.bin")
