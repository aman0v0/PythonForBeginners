# Basic File Explorer
import os

def list_files(directory='.'):
    print(f"Files in {directory}:")
    for file in os.listdir(directory):
        print(file)

# Example usage
directory_path = input("Enter directory path (Press Enter for current directory): ")
list_files(directory_path)