import os
import subprocess

def handler(event, context):

    print('=== start func ===\n')

    if os.name=='nt':
        # windows
        cmd = 'main.exe'
    else:
        # not windows (expect posix)
        cmd = './main'

    subprocess.call(cmd)
    print('\n=== end func ====')

    ret = 'end'
    return ret

if __name__ == '__main__':
	handler(0, 0)