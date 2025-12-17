import os
import subprocess
import sys

# Script ejecutable para lanzar Jarvis desde cualquier carpeta

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    api_path = os.path.join(base_dir, 'api', 'main.py')
    if not os.path.exists(api_path):
        print('No se encuentra main.py en api/.')
        sys.exit(1)
    subprocess.run([sys.executable, api_path])

if __name__ == "__main__":
    main()
