# Importación de módulos necesarios
import os              # Para trabajar con rutas de archivos y carpetas
import shutil          # Para mover archivos
from abc import ABC, abstractmethod  # Para definir clases y métodos abstractos

# Clase base abstracta para organizadores de archivos
class FileOrganizer(ABC):
    def __init__(self, base_path):
        # Guarda la ruta base donde estarán los archivos a organizar
        self.base_path = base_path

        # Si la ruta no existe, la crea automáticamente
        if not os.path.exists(base_path):
            os.makedirs(base_path)

    @abstractmethod
    def organize_files(self):
        # Método abstracto que cada subclase debe implementar obligatoriamente
        pass

    def create_folder(self, folder_name):
        # Crea una subcarpeta dentro de la ruta base
        path = os.path.join(self.base_path, folder_name)

        # Si la carpeta no existe, la crea
        if not os.path.exists(path):
            os.makedirs(path)

        # Devuelve la ruta completa de la carpeta creada
        return path

    def move_files(self, extension, destination_folder, exclude_files=None, exclude_extensions=None):
        # Mueve archivos que tengan la extensión especificada a la carpeta de destino,
        # excluyendo archivos por nombre o por otras extensiones

        # Si no se pasan archivos a excluir, usa lista vacía por defecto
        if exclude_files is None:
            exclude_files = []

        # Si no se pasan extensiones a excluir, usa lista vacía por defecto
        if exclude_extensions is None:
            exclude_extensions = []

        # Recorre todos los archivos en la carpeta base
        for file in os.listdir(self.base_path):
            file_path = os.path.join(self.base_path, file)  # Ruta completa al archivo
            file_lower = file.lower()  # Convierte el nombre a minúsculas para comparación

            # Condiciones para mover el archivo:
            if (
                os.path.isfile(file_path) and                    # Asegura que sea un archivo (no carpeta)
                file_lower.endswith(extension) and              # Que termine con la extensión buscada
                file not in exclude_files and                   # Que no esté en la lista de exclusión por nombre
                not any(file_lower.endswith(ext) for ext in exclude_extensions)  # Que no tenga extensión excluida
            ):
                # Mueve el archivo a la carpeta destino
                shutil.move(file_path, os.path.join(destination_folder, file))

                # Muestra mensaje en consola
                print(f"Moved: {file} → {destination_folder}")

# Subclase para organizar archivos de Word
class WordOrganizer(FileOrganizer):
    def __init__(self, base_path):
        super().__init__(base_path)  # Llama al constructor de la clase base

    def organize_files(self):
        folder = self.create_folder("Word_Files")  # Crea carpeta para archivos Word
        self.move_files(".doc", folder, exclude_extensions=[".tmp", ".bak"])   # Mueve .doc
        self.move_files(".docx", folder, exclude_extensions=[".tmp", ".bak"])  # Mueve .docx
        print("Organized Word files")  # Mensaje informativo

# Subclase para organizar archivos de texto (.txt)
class TextOrganizer(FileOrganizer):
    def __init__(self, base_path):
        super().__init__(base_path)

    def organize_files(self):
        folder = self.create_folder("Text_Files")  # Crea carpeta destino
        exclude_names = ["README.txt"]             # Nombres específicos a excluir
        exclude_exts = [".tmp", ".bak"]            # Extensiones a excluir
        self.move_files(".txt", folder, exclude_files=exclude_names, exclude_extensions=exclude_exts)
        print("Organized Text files")

# Subclase para organizar archivos PDF
class PDFOrganizer(FileOrganizer):
    def __init__(self, base_path):
        super().__init__(base_path)

    def organize_files(self):
        folder = self.create_folder("PDF_Files")  # Crea carpeta destino
        self.move_files(".pdf", folder, exclude_extensions=[".tmp", ".bak"])  # Mueve archivos PDF
        print("Organized PDF files")

# Subclase para organizar archivos de Excel
class ExcelOrganizer(FileOrganizer):
    def __init__(self, base_path):
        super().__init__(base_path)

    def organize_files(self):
        folder = self.create_folder("Excel_Files")  # Crea carpeta destino
        self.move_files(".xlsx", folder, exclude_extensions=[".tmp", ".bak"])  # Mueve .xlsx
        self.move_files(".xls", folder, exclude_extensions=[".tmp", ".bak"])   # Mueve .xls
        print("Organized Excel files")

# Función principal
def main():
    # Obtiene la ruta al escritorio del usuario
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # Define la carpeta base sobre el escritorio
    base_path = os.path.join(desktop, "Archivos_Organizados")

    # Lista de organizadores para diferentes tipos de archivos
    organizers = [
        WordOrganizer(base_path),
        TextOrganizer(base_path),
        PDFOrganizer(base_path),
        ExcelOrganizer(base_path),
    ]

    # Ejecuta el método de organización de cada clase
    for organizer in organizers:
        organizer.organize_files()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
