import sys
import subprocess

if len(sys.argv) < 2:
    print('Please provide a script name as an argument.')
    sys.exit(1)

script_name = sys.argv[1]

try:
    subprocess.run(['python', script_name], check=True)
except subprocess.CalledProcessError as e:
    print(f'Error: {e}')
    sys.exit(1)
