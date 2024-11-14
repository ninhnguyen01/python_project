# Import package
import os
import sys

# Check your operating system that the code is currently running on.
print(f'Your code OS is: {os.name} \n')

# Check your device platform
doc_info = '''
------------------------
System | platform value
------------------------

AIX | 'aix'

Android | 'android'

Emscripten | 'emscripten'

iOS | 'ios'

Linux | 'linux'

macOS | 'darwin'

Windows | 'win32'

Windows/Cygwin | 'cygwin'

WASI | 'wasi'

--------------------------
'''
print(doc_info, '\n')
print(f'Your device platform is: {sys.platform} \n')