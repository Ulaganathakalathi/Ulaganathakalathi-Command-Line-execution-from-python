from constants import VERSION
from constants import TM
from gui import BootFrame
import tkinter as tk
import binascii
import tempfile
import platform
from resources.paths import ICON_PATH

try:
    import bootgui.config.generic as cfg
except ImportError as e:
    defaultELF = ""
    defaultSsid = ""
    defaultPassphrase = ""
    defaultBootArgs = []
    showAPOpts = True
    showBootArgs = True
else:
    defaultELF = cfg.DEFAULT_ELF
    defaultSsid = cfg.DEFAULT_SSID
    defaultPassphrase = cfg.DEFAULT_PASSPHRASE
    defaultBootArgs = cfg.DEFAULT_BOOT_ARGS
    showAPOpts = cfg.SHOW_AP_OPTS
    showBootArgs = cfg.SHOW_BOOT_ARGS

root = tk.Tk()
root.title("InnoPhase LPS" + TM + " Demo Tool v" + VERSION)

os_name = platform.system()
#print(os_name)
if "Windows" in os_name:
    root.iconbitmap(ICON_PATH)
else:
    root.iconphoto(False, tk.PhotoImage(ICON_PATH))


bf = BootFrame(root)
bf.grid(row=0, column=0, sticky="NESW")

# Allow column 0 and row 0 to stretch
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Update geometry to so we know initial window size
root.update_idletasks()

# #below to set the positioning
# width_frm = bf.devFrame.winfo_width()

# #below to centralize the Reset frame
# reset_b_w = bf.programmingFrame.resetButton.winfo_width()
# # print('reset_b_w:', reset_b_w) #, reset_b_h)

# reset_b_geom = bf.programmingFrame.resetButton.winfo_geometry() #.winfo_reqwidth()
# # print('reset_b_reqw:', reset_b_geom) #, reset_b_reqh)

# left_padx = reset_b_geom.split('+')[1]

# pad_x = (width_frm - reset_b_w)//2 - int(left_padx) 
# bf.programmingFrame.resetButton.grid_configure(padx=pad_x)
# bf.programmingFrame.eraseButton.grid_configure(padx=pad_x)
# bf.programmingFrame.bootButton.grid_configure(padx=pad_x)
# bf.programmingFrame.flashButton.grid_configure(padx=pad_x)
# # bf.resetFrame.resetBLButton.grid_configure(padx=pad_x)

# root.update_idletasks()
# reset_b_reqw = bf.programmingFrame.resetButton.winfo_geometry() #.winfo_reqwidth()
# # print('reset_b_reqw:', reset_b_reqw) #, reset_b_reqh)

# # #below for help button
# bf.helpFrame.dfButton.grid_configure(padx=pad_x)

# # Set initial window size as miniumum
# root.update_idletasks()

# # Set initial window size as miniumum
# root.minsize(root.winfo_width(), root.winfo_height())
# #print("in main.py")
# #print(root.winfo_x(), root.winfo_y(), root.winfo_width(), root.winfo_height(), root.winfo_reqwidth(), root.winfo_reqheight() )

# #below to arrange the window in the screen
# scr_width = root.winfo_screenwidth()
# scr_height = root.winfo_screenheight()
# console_width = bf.console.winfo_width()

# gui_Width = root.winfo_reqwidth()
# gui_Height = root.winfo_reqheight()

# gui_total_width = gui_Width + console_width
# if gui_total_width > scr_width:
#     x_pos = 0
# else:
#     x_pos = (scr_width - gui_total_width) //2

# if gui_Height > scr_height:
#     y_pos = 0
# else:
#     y_pos = (scr_height - gui_Height) //2

# root.geometry("{}x{}+{}+{}".format(gui_Width, gui_Height, x_pos, y_pos))


root.update_idletasks()




root.mainloop()
