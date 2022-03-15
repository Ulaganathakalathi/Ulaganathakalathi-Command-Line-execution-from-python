"""GUI for the boot script."""

import boottask
import tkinter as tk
import tkinter.ttk as ttk
from resources.paths import LOGO_PATH, FOLDER_ICON_PATH
from tkinter import *
from tkinter.filedialog import askopenfilename

class Getelf(ttk.LabelFrame):
    def __init__(self,master):
        super().__init__(master, text="Programming LPS board", relief="groove", padding=5)
        self.setup_widgets(master)  

    def setup_widgets(self,master):
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(2, weight=28)
        
        self.tabControl = ttk.Notebook(self)

        self.Nuvoton = ttk.Frame(self.tabControl)
        self.tabControl.add(self.Nuvoton,text = "Programming Nuvoton Host")

        self.T2_module = ttk.Frame(self.tabControl)
        self.tabControl.add(self.T2_module,text = "Programming T2 Module")

        # self.scan = ttk.Frame(self.tabControl)
        # self.tabControl.add(self.scan,text = "Scan")

        self.tabControl.grid(row=1, column=0, columnspan=3, padx=8, pady = 8, sticky="WS") #, padx=10
        
        self.Nuvoton_mode = Nuvoton(self.Nuvoton)
        self.Nuvoton_mode.grid(row=1, column=0,padx=8,pady=8, sticky="NESW")

        self.T2_module_mode = T2_module(self.T2_module)
        self.T2_module_mode.grid(row=1, column=1,padx=8,pady=8, sticky="NESW")
        
        photo = tk.PhotoImage(file = LOGO_PATH)
        # image = Image.open(LOGO_PATH)
        # photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self, image = photo)
        self.label.image = photo
        self.label.grid(row=3)


class Nuvoton(ttk.LabelFrame):
    def __init__(self,master):

        super().__init__(master, text="", relief="groove", padding=10) #Different Mode Options
        #self.deep_sleep = 0
        self.setup_widgets(master)
        #self.disable(0)

    def setup_widgets(self,master):
        
        #check box to specify App file
        self.app_check_var = tk.IntVar()
        self.app_checkbox = ttk.Checkbutton(self, text="Specify the App Binary file:", variable=self.app_check_var)
        self.app_checkbox.grid(row=0, column=0, padx=5, pady = 0, sticky="EW")
        
        # Label for specify the App binary entry
        # programoption = ttk.Label(self, text="Specify the App Binary file:", anchor="w")
        # programoption.grid(row=0, column=1, padx=8, pady=8, sticky="W") #, padx=8
        
        # App file entry
        self.appFilePath = tk.StringVar()   # Variable holding contents of App file entry
        self.appFileEntry = ttk.Entry(self, width=40, textvariable=self.appFilePath)
        self.appFileEntry.grid(row=0, column=1, sticky="EW")
        
        # photo = ttk.PhotoImage(file = "C:\\Users\\InnoP\\Desktop\\Ubuntushare\\Delete\\37.GUI_Requirement_update\\Folder_Icon.png")
        # filepath = "C:\\Users\\InnoP\\Desktop\\Ubuntushare\\Delete\\37.GUI_Requirement_update\\Folder_Icon.png"
        photo = tk.PhotoImage(file = FOLDER_ICON_PATH)
        
        # Resizing image to fit on button
        photoimage = photo.subsample(10,10)
        # App file selection button
        self.appFilepathButton = ttk.Button(self, image = photoimage, compound = tk.LEFT, command=self.select_app_file_dialog, width = 0.5) #, image = photoimage, compound = tk.LEFT #text="Select Path to Read Files",
        self.appFilepathButton.grid(row=0, column=2) #, sticky="E")
        self.appFilepathButton.image = photoimage
        
        #check box to specify configuration file
        self.config_check_var = tk.IntVar()
        self.config_checkbox = ttk.Checkbutton(self, text="Specify the WiFi Config file:" , variable=self.config_check_var) #
        self.config_checkbox.grid(row=1, column=0, padx=5, pady = 5, sticky="EW")
        
        # Label for specify the App binary entry
        # programoption = ttk.Label(self, text="Specify the WiFi Config file:", anchor="w")
        # programoption.grid(row=1, column=1, padx=8, pady=8, sticky="W") #, padx=8
        
        # Config file entry
        self.configFilePath = tk.StringVar()   # Variable holding contents of App file entry
        self.configFileEntry = ttk.Entry(self, width=40, textvariable=self.configFilePath)
        self.configFileEntry.grid(row=1, column=1, sticky="EW")
        
        # Config file selection button
        self.configFilepathButton = ttk.Button(self, image = photoimage, compound = tk.LEFT, command=self.select_config_file_dialog, width = 0.5) #, image = photoimage, compound = tk.LEFT #text="Select Path to Read Files",
        self.configFilepathButton.grid(row=1, column=2) #, sticky="E")
        self.configFilepathButton.image = photoimage
        
        # button to Program Host
        self.progHostButton = ttk.Button(self, text = "Program Host", command = lambda:boottask.Prog_Host(self))
        self.progHostButton.grid(row=2, column=1, columnspan=2, pady=5, sticky="E")
        
    def select_app_file_dialog(self):
        """Opens a dialog box for selecting an App file and updates the filepath to entry."""
        
        # filepath = tk.filedialog.askopenfilename(title="Select Application File",
        #                                          filetypes=(("BIN Files", "*.bin"), ("All Files", "*.*")));
        filepath = askopenfilename(title="Select Application File",
                                                 filetypes=(("BIN Files", "*.bin"), ("All Files", "*.*")));
        
        # This will only update the filepath if the result is non-empty
        if filepath :
            self.appFilePath.set(filepath)
            print(filepath)
    
    def select_config_file_dialog(self):
        """Opens a dialog box for selecting an JSON file and updates the filepath to entry."""
        
        filepath = askopenfilename(title="Select WiFi Configuration File",
                                                 filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")));
        
        # This will only update the filepath if the result is non-empty
        if filepath :
            self.configFilePath.set(filepath)
            print(filepath)

class T2_module(ttk.LabelFrame):
    def __init__(self,master):

        super().__init__(master, text="", relief="groove", padding=10) #Different Mode Options
        #self.deep_sleep = 0
        self.setup_widgets(master)
        #self.disable(0)

    def setup_widgets(self,master):
        
        #check box to specify App file
        # self.app_check_var = tk.IntVar()
        # self.app_checkbox = ttk.Checkbutton(self, text="Specify the App Binary file:", variable=self.app_check_var)
        # self.app_checkbox.grid(row=0, column=0, padx=5, pady = 0, sticky="EW")
        
        # Label for specify the App binary entry
        programoption = ttk.Label(self, text="Specify the App Binary file:", anchor="w")
        programoption.grid(row=0, column=0, padx=5, pady=0, sticky="EW") #, padx=8
        
        # App file entry
        self.appFilePath = tk.StringVar()   # Variable holding contents of App file entry
        self.appFileEntry = ttk.Entry(self, width=40, textvariable=self.appFilePath)
        self.appFileEntry.grid(row=0, column=1, sticky="EW")
        
        # photo = ttk.PhotoImage(file = "C:\\Users\\InnoP\\Desktop\\Ubuntushare\\Delete\\37.GUI_Requirement_update\\Folder_Icon.png")
        # filepath = "C:\\Users\\InnoP\\Desktop\\Ubuntushare\\Delete\\37.GUI_Requirement_update\\Folder_Icon.png"
        photo = tk.PhotoImage(file = FOLDER_ICON_PATH)
        
        # Resizing image to fit on button
        photoimage = photo.subsample(10,10)
        # App file selection button
        self.appFilepathButton = ttk.Button(self, image = photoimage, compound = tk.LEFT, command=self.select_app_file_dialog, width = 0.5) #, image = photoimage, compound = tk.LEFT #text="Select Path to Read Files",
        self.appFilepathButton.grid(row=0, column=2) #, sticky="E")
        self.appFilepathButton.image = photoimage
        
        # button to Program Host
        self.progT2Button = ttk.Button(self, text="Program T2", command=lambda:boottask.Prog_T2(self))
        self.progT2Button.grid(row=1, column=1, columnspan=2, pady=5, sticky="E")
        
    def select_app_file_dialog(self):
        """Opens a dialog box for selecting an App file and updates the filepath to entry."""
        
        filepath = tk.filedialog.askopenfilename(title="Select Application File",
                                                 filetypes=(("BIN Files", "*.bin"), ("All Files", "*.*")));
        
        # This will only update the filepath if the result is non-empty
        if filepath :
            self.appFilePath.set(filepath)
            print(filepath)

class BootFrame(ttk.Frame):
    """Frame containing all widgets for the boot GUI."""
    
    def __init__(self, master,
                 defaultELF="",
                 defaultSsid="",
                 defaultPassphrase="",
                 defaultBootArgs=[],
                 showAPOpts=True,
                 showBootArgs=True):
        """Initializes the thread-safe queue and sets up our widgets in the frame."""
        
        super().__init__(master)
        
        # print(EEPROM_IMG_PATH)
        
        self.evb_network_profile = {}
        self.nprofile_check = True
        self.new_network_profile_json ={}
        self.temperary_save = False
        
        #root details
        self.root = master
        
        # Programming thread running the boot / flash / erase sequence
        self.progThread = None

        
        # Set up widgets in our frame
        self.setup_widgets()
        

    def setup_widgets(self):
        """Sets up our widgets in the frame."""
        
        # Help menu frame
        # self.helpFrame = HelpFrame(self)
        # self.helpFrame.grid(row=3, column=1, padx=8, pady=8, sticky="NESW")
        
        # ELF file input frame
        #self.elfFrame = InputELFFrame(self, defaultELF=defaultELF)
        #self.elfFrame.grid(row=0, column=0, padx=8, pady=8, sticky="NESW")
        
        # Output boot device frame
        # self.deep_sleep = 0
        # self.devFrame = OutputDevFrame(self)
        # self.devFrame.grid(row=0, column=1, padx=8, pady=8, sticky="NESW")

        # Ap options frame
        # self.apOptsFrame = APOptFrame(self, defaultSsid=defaultSsid, defaultPassphrase=defaultPassphrase)
        # if(showAPOpts):
        #     self.apOptsFrame.grid(row=0, column=0, padx=8, pady=8, sticky="NESW")
        
        # Boot arguments frame
        #self.bootArgsFrame = BootArgsFrame(self, defaultBootArgs)
        #if(showBootArgs):
        #    self.bootArgsFrame.grid(row=2, column=0, padx=8, pady=8, sticky="NESW")

        #self.setup_parameters = Setup_Parameters(self)
        #self.setup_parameters.grid(row=1, column=0, padx=8,pady=8, sticky="NESW")

        self.getelfoption = Getelf(self)
        self.getelfoption.grid(row=2, column=0, rowspan=2, padx=8,pady=8, sticky="NESW")

        # Allow column 0 to stretch
        self.columnconfigure(0, weight=1)
        
        # We want the row after the last frame to be able to change size vertically...
        
        # Allow row 3 to stretch
        self.rowconfigure(4, weight=1)





