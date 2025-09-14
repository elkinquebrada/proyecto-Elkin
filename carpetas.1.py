import os

class FolderManager:
    # Constructor que recibe el path base donde se operará
    def __init__(self, base_path):
        self.path = base_path
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        print(f"Ruta base establecida en: {self.path}")

    # Crear carpeta
    def create_folder(self, folder_name):
        folder_path = os.path.join(self.path, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Se creó la carpeta '{folder_name}' de manera correcta.")
        except FileExistsError:
            print(f"La carpeta '{folder_name}' ya existe.")

    # Listar carpetas
    def list_folders(self):
        print("Carpetas dentro del path:")
        for item in os.listdir(self.path):
            full_path = os.path.join(self.path, item)
            if os.path.isdir(full_path):
                print(f"- {item}")

    # Eliminar carpeta con confirmación (solo si está vacía)
    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.path, folder_name)
        if not os.path.exists(folder_path):
            print(f"La carpeta '{folder_name}' no existe.")
            return

        confirm = input(f"¿Estás seguro que deseas eliminar la carpeta '{folder_name}'? (s/n): ").strip().lower()
        if confirm == 's':
            try:
                os.rmdir(folder_path)
                print(f"Se eliminó la carpeta '{folder_name}' de manera correcta.")
            except OSError:
                print(f"No se pudo eliminar '{folder_name}' porque no está vacía.")
        else:
            print("Operación cancelada por el usuario.")
            
            
  

