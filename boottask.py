"""Task that the GUI can run to perform a boot."""
import tkinter as tk
import os, time
import sys
import platform
import subprocess
import win32event, win32process #, win32con
#from win32comext.shell.shell import ShellExecuteEx
from win32com.shell.shell import ShellExecuteEx
from win32com.shell import shellcon
import json
from resources.paths import DFU_EXE_PATH, ISP_DFU_PATH, FOS_APP_PATH

def Prog_Host(root):
    # tk.messagebox.showinfo(title = "programming Host",message="Coding for Program Host is in progress")
    
    # cmd = DFU_EXE_PATH + " -l" #.\apps\wifi\out\M252app.bin
    # console_log = run_cmd(cmd)
    
    # app_file = root.appFilePath.get()
    # cmd = DFU_EXE_PATH + " -x 1 -a 0 -d 0x416:0xBDF0 -D " + app_file 
    # print('cmd:', cmd)
    # console_log = run_cmd(cmd)
    # if check_complete_status(console_log) != 0: #check whether app loaded completely
    #     tk.messagebox.showerror(title="Error Programming Host", message='Error occured while downloading App to host, Refer console log below: \n' + console_log)
    #     err_msg = "error while Programming Host"
    # else:
    #     print('no error')
    # print('host app:', root.appFilePath.get())
    # print('config file:', root.configFilePath.get())
    # print('app check:', root.app_check_var.get())
    # print('config check:', root.config_check_var.get())
    # return


    config_write = root.config_check_var.get()
    app_write = root.app_check_var.get()
    
    #check whether the Nuvoton is in dfu mode
    ret_val = Is_Device_In_DFU_Mode()
    if ret_val !=0:
        tk.messagebox.showinfo(title = "programming Host",message="No DFU Device Found. Please check the following things: \n 1.Make sure LPS board is connected to PC\n 2.Make sure device is resetted to DFU mode\n 3. Make sure DFU driver is installed")
        return
    # else:
    #     tk.messagebox.showinfo(title = "programming Host",message="Please put the host in dfu mode")
    #     return
    
    err_msg = ""
    #program the app to nuvoton
    if app_write: 
        app_file = root.appFilePath.get()
        if app_file == "":
            tk.messagebox.showerror(title="Error Programming Host", message='App binary file is not specified. Please specify and try again.')
            return
        cmd = DFU_EXE_PATH + " -x 1 -a 0 -d 0x416:0xBDF0 -D " + app_file #.\apps\wifi\out\M252app.bin
        console_log = run_cmd(cmd)
        # console_log = read_file(r'C:\Users\InnoP\Desktop\Ubuntushare\Delete\25.LPS_UI_tool\Inputs\Log_files_output\Host_log\WiFi.txt')
        if check_complete_status(console_log) != 0: #check whether app loaded completely
            tk.messagebox.showerror(title="Error Programming Host", message='Error occured while downloading App to host, Refer console log below: \n' + console_log)
            err_msg = "error while Programming Host"
            
    #Writing config file to Host
    if config_write:
        config_file = root.configFilePath.get()
        if config_file == "":
            tk.messagebox.showerror(title="Error Programming Host", message='Config file is not specified. Please specify and try again.')
        cmd = DFU_EXE_PATH + " -x 2 -a 0 -d 0x416:0xBDF0 -D " + config_file #.\apps\wifi\cfg\app_config.json
        console_log = run_cmd(cmd)
        # console_log = read_file(r'C:\Users\InnoP\Desktop\Ubuntushare\Delete\25.LPS_UI_tool\Inputs\Log_files_output\Host_log\CFG.txt')
        if check_complete_status(console_log) != 0: #check whether app loaded completely
            tk.messagebox.showerror(title="Error loading config file", message='Error occured while loading config file, Refer console log below: \n' + console_log)
            err_msg = "error while loading config file"
    
    if err_msg != "":
        tk.messagebox.showinfo(title = "Error programming Host",message="Programming host failed due to \"" + err_msg + "\"")
    else:
        tk.messagebox.showinfo(title = "programming Host",message="Programming host completed successfully. Please Reset the board, to start up the Newly programmed application")
    
def Prog_T2(root):
    # tk.messagebox.showinfo(title = "programming T2",message="Coding for T2 is in progress")
    # print('T2 app:', root.appFilePath.get())
    # return
    t2_app_file = root.appFilePath.get()
    if t2_app_file == "":
        tk.messagebox.showerror(title="Error Programming T2", message='App binary file is not specified. Please specify and try again.')
            
    #check whether the Nuvoton is in dfu mode
    ret_val = Is_Device_In_DFU_Mode()
    if ret_val !=0:
        tk.messagebox.showinfo(title = "programming Host",message="No DFU Device Found. Please check the following things: \n 1.Make sure LPS board is connected to PC\n 2.Make sure device is resetted to DFU mode\n 3. Make sure DFU driver is installed")
        return
    
    err_msg = ""
    
    #load the ISP_DFU.bin to host
    cmd = DFU_EXE_PATH + " -x 1 -a 0 -d 0x416:0xBDF0 -D " + FOS_APP_PATH #.\apps\wifi\out\M252app.bin
    console_log = run_cmd(cmd)
    # console_log = read_file(r'C:\Users\InnoP\Desktop\Ubuntushare\Delete\25.LPS_UI_tool\Inputs\Log_files_output\T2_Log\ISP_DFU.txt')
    if check_complete_status(console_log) != 0: #check whether app loaded completely
        tk.messagebox.showerror(title="Error Programming Host", message='Error occured while downloading App (fos_app.bin) to host, Refer console log below: \n' + console_log)
        err_msg = "error while Programming App (fos_app.bin) to Host"
    else:
        tk.messagebox.showinfo(title = "Reset board",message="fos_app.bin App is programmed successfully. Please reset the device and press ok.")
        tk.messagebox.showinfo(title = "Host in T2 Program mode",message="Wait for \"Ready to Program\" message on OLED, then press ok.")
        time.sleep(1)
    
    #program app to T2
    if err_msg == "":
        cmd = DFU_EXE_PATH + " -a 0 -d 0x416:0xBDF0 -D " + t2_app_file #<stw multi proto ELF path>
        console_log = run_cmd(cmd)
        # console_log = read_file(r'C:\Users\InnoP\Desktop\Ubuntushare\Delete\25.LPS_UI_tool\Inputs\Log_files_output\T2_Log\smp_app.txt')
        if check_complete_status(console_log) != 0: #check whether app loaded completely
            tk.messagebox.showerror(title="Error loading config file", message='Error occured while loading config file, Refer console log below: \n' + console_log)
            err_msg = "error while loading App to T2"
    
    if err_msg != "":
        tk.messagebox.showinfo(title = "Error programming T2",message="Programming T2 failed due to \"" + err_msg + "\"")
    else:
        tk.messagebox.showinfo(title = "programming T2",message="Programming T2 completed successfully. Please Reset the board, to start up the Newly programmed application")

def Is_Device_In_DFU_Mode():
    cmd = DFU_EXE_PATH + " -l" #.\apps\wifi\out\M252app.bin
    console_log = run_cmd(cmd)
    print(console_log)
    # console_log = read_file(r'C:\Users\InnoP\Desktop\Ubuntushare\Delete\25.LPS_UI_tool\Inputs\Log_files_output\list.txt')
    if "Found DFU" in console_log:
        retCode = 0
    else:
        retCode = 1
    return retCode
    
    # retCode = 0 #True, libusbk installed
    # no_com = 0

    # try:
    #     startupinfo = subprocess.STARTUPINFO()
    #     startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    #     p = subprocess.Popen(
    #         "PowerShell -Command \"& {$devices = Get-PnpDevice | Where-Object { $_.InstanceId -ilike '*USB\VID_0403&PID_6011*' -and $_.Status -like 'OK'} | Select-Object Status,Class,FriendlyName,InstanceId; if ($devices -ne $null) { ConvertTo-Json @($devices) }}\"",
    #         stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.DEVNULL, startupinfo = startupinfo)
        
    #     out = p.communicate()[0].decode()
    #     if out != '':
    #         j = json.loads(out)
    #         # print(j)
    #         for dev in j:
    #             if dev['Status'] == 'OK' and (not ('nu_dfu' in dev['Class'].lower())):
    #                 retCode = 1 #False, libusbk not-installed
    #                 no_com = no_com + 1
    #                         # break
    #     else:
    #         retCode = 2 # device not connected
            
            
    # except Exception as e:
    #     tk.messagebox.showinfo("Driver Installation", str(e))
    #     retCode = 3 #Exception error
    
    # finally:
    #     return retCode #, no_com

def run_cmd(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    # cmd = r'C:\Users\InnoP\Desktop\Ubuntushare\Delete\25.LPS_UI_tool\DFU_source_code\nu_m252\tool\dfu-util\windows\dfu-util\Win32\dfu-util\Release\dfu-util.exe -l'
    p = subprocess.Popen(
        "PowerShell -Command \"" + cmd + "\"",
        stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.DEVNULL, startupinfo = startupinfo)
    # out = p.communicate()[0].decode()
    out = ""
    for each_com in p.communicate():
        out = out + each_com.decode()
        # print('ka:', each_com.decode())

    return out
    # print(out)

def check_complete_status(input_str):
    ret_val = 0 #status completed successfully
    sub_str = input_str.split('\n')
    print(input_str)
    i=1
    for each_line in sub_str:
        # print(str(i) + ":" + each_line)
        if ("DFU state" in each_line) and (not "No error condition is present" in each_line):
            ret_val = 1
            break
        i=i+1
        
    if ret_val == 0 and not ("Done!" in each_line):
        ret_val = 1
        
    return ret_val

def read_file(file_name):
    with open(file_name) as f:
        contents = f.read()
    return contents

# def Run_cmd( cmd, params):
#     retCode = 1
#     try:
#         # cmd = 'C:\\Windows\\System32\\PNPUTIL'
#         # params = '/scan-devices'

#         showCmd = 0 #win32con.SW_SHOWNORMAL
#         lpVerb = 'runas'  # causes UAC elevation prompt.

#         procInfo = ShellExecuteEx(nShow=showCmd,
#                                   fMask=shellcon.SEE_MASK_NOCLOSEPROCESS,
#                                   lpVerb=lpVerb,
#                                   lpFile=cmd,
#                                   lpParameters=params)

#         procHandle = procInfo['hProcess']
#         obj = win32event.WaitForSingleObject(procHandle, win32event.INFINITE)
#         retCode = win32process.GetExitCodeProcess(procHandle)
#         retCode = 0 #success
#     except Exception as e:
#         # messagebox.showinfo("Scan for hardware changes", str(e))
#         if 'canceled' in str(e):
#             retCode = 2 #canceled by user
#         else:
#             retCode = 1 #unknown error
#     return retCode