import os
import shutil
from abc import ABC, abstractmethod

class FileOrganizer(ABC):
    def __init__(self, base_path):
        self.base_path = base_path
        if not os.path.exists(base_path):
            os.makedirs(base_path)

    @abstractmethod
    def organize_files(self):
        pass

    def create_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

class WordOrganizer(FileOrganizer):
    def organize_files(self):
        # Logic to organize .doc files
        folder = self.create_folder("Word_Files")
        # ... code to move .doc files to folder
        print("Organized Word files")

class TextOrganizer(FileOrganizer):
    def organize_files(self):
        # Logic to organize .txt files
        folder = self.create_folder("Text_Files")
        # ... code to move .txt files to folder
        print("Organized Text files")

class PDFOrganizer(FileOrganizer):
    def organize_files(self):
        # Logic to organize .pdf files
        folder = self.create_folder("PDF_Files")
        # ... code to move .pdf files to folder
        print("Organized PDF files")

class ExcelOrganizer(FileOrganizer):
    def organize_files(self):
        # Logic to organize .xlsx files
        folder = self.create_folder("Excel_Files")
        # ... code to move .xlsx files to folder
        print("Organized Excel files")


# Example of usage:

def main():
    base_path = "C:/temp/project_files"
    organizers = [
        WordOrganizer(base_path),
        TextOrganizer(base_path),
        PDFOrganizer(base_path),
        ExcelOrganizer(base_path),
    ]

    for organizer in organizers:
        organizer.organize_files()

if __name__ == "__main__":
    main()
