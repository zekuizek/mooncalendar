#!/usr/bin/env python3
"""
Main script to run the Moon Calendar application.
"""
import os
import sys
import subprocess

def main():
    """
    Run the Moon Calendar application.
    """
    # Get the project root directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the project directory
    os.chdir(project_dir)
    
    # Check if the virtual environment exists
    venv_dir = os.path.join(project_dir, 'venv')
    if not os.path.exists(venv_dir):
        print("Setting up virtual environment...")
        subprocess.run([sys.executable, '-m', 'venv', 'venv'], check=True)
    
    # Determine the pip and python commands based on the platform
    if sys.platform == 'win32':
        pip_cmd = os.path.join(venv_dir, 'Scripts', 'pip')
        python_cmd = os.path.join(venv_dir, 'Scripts', 'python')
    else:
        pip_cmd = os.path.join(venv_dir, 'bin', 'pip')
        python_cmd = os.path.join(venv_dir, 'bin', 'python')
    
    # Install dependencies
    print("Installing dependencies...")
    subprocess.run([pip_cmd, 'install', '-r', 'requirements.txt'], check=True)
    
    # Fetch data
    print("Fetching moon phase and zodiac sign data...")
    subprocess.run([python_cmd, 'src/fetch_data.py'], check=True)
    
    # Run the application
    print("Starting the Moon Calendar application...")
    subprocess.run([python_cmd, 'src/app.py'], check=True)


if __name__ == "__main__":
    main()
