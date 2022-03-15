import os
import sys

# SDK directory
toolcwd = os.getcwd() 

sys.path.append(toolcwd)
from reduce_EXE_size import *

# Directory of bootGUI resources
resourceDir = os.path.join('resources')

datas = [(os.path.join(resourceDir, 'dfu-util.exe'), resourceDir),
         (os.path.join(resourceDir, 'Folder_Icon.png'), resourceDir),
         (os.path.join(resourceDir, 'fos_app.bin'), resourceDir),
         (os.path.join(resourceDir, 'icon.ico'),resourceDir),
         (os.path.join(resourceDir, 'logo.png'),resourceDir)]
block_cipher = None
a = Analysis([os.path.join('__main__.py')],
             pathex=[],
             binaries=[],
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

#blow part is for size reduction
a_data_exclude, a_binary_exclude = reduce_exe_size(a)
a.datas -= a_data_exclude
a.binaries -= a_binary_exclude
#ka = toc_write_to_file('final_a_binaries.txt', a.binaries)
#ka = toc_write_to_file('final_a_datas.txt', a.datas)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='LPS_Demo_Tool_Windows',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )