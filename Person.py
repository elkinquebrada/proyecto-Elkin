import os
import shutil
import re
import json


class FolderManager:
    """
    Clase para gestionar carpetas dentro de una ruta base.

    Permite crear, listar y eliminar carpetas, así como guardar información de instancias Persona.
    """

    def __init__(self, base_path):
        self.base_path = base_path
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            print(f"Carpeta base creada: {base_path}")

    def is_valid_folder_name(self, folder_name):
        """
        Verifica que el nombre de carpeta no contenga caracteres inválidos.
        """
        return re.match(r'^[^<>:"/\\|?*]+$', folder_name) is not None

    def create_folder(self, folder_name):
        if not self.is_valid_folder_name(folder_name):
            print(f"Nombre de carpeta inválido: {folder_name}")
            return

        path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Carpeta creada: {path}")
        else:
            print(f"La carpeta ya existe: {path}")

    def create_nested_folder(self, *folders):
        path = os.path.join(self.base_path, *folders)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Carpeta anidada creada: {path}")
        else:
            print(f"La carpeta anidada ya existe: {path}")

    def list_folders(self):
        items = os.listdir(self.base_path)
        folders = [f for f in items if os.path.isdir(os.path.join(self.base_path, f))]
        print(f"Carpetas dentro de {self.base_path}: {folders}")
        return folders

    def delete_folder_empty(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        if os.path.exists(path) and os.path.isdir(path):
            try:
                os.rmdir(path)
                print(f"Carpeta vacía eliminada: {path}")
            except OSError:
                print(f"No se puede eliminar '{path}': la carpeta no está vacía.")
        else:
            print(f"No se encontró la carpeta: {path}")

    def delete_folder(self, folder_name):
        path = os.path.join(self.base_path, folder_name)
        try:
            if os.path.exists(path) and os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Carpeta eliminada: {path}")
            else:
                print(f"La carpeta no existe o no es un directorio: {path}")
        except PermissionError:
            print(f"Permiso denegado: no se puede eliminar {path}")
        except Exception as e:
            print(f"Error al eliminar la carpeta {path}: {e}")

    def guardar_persona(self, persona, formato='json'):
        """
        Crea una carpeta para la persona y guarda su información en un archivo (JSON o TXT).

        Parámetros:
        -----------
        persona : Persona
            Instancia de Persona a guardar.

        formato : str
            'json' (por defecto) o 'txt'.
        """
        folder_name = f"{persona.name}_{persona.age}"

        if not self.is_valid_folder_name(folder_name):
            print(f"Nombre de carpeta inválido para persona: {folder_name}")
            return

        person_folder_path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(person_folder_path):
            os.makedirs(person_folder_path)
            print(f"Carpeta creada para persona: {person_folder_path}")
        else:
            print(f"La carpeta de la persona ya existe: {person_folder_path}")

        if formato == 'json':
            file_path = os.path.join(person_folder_path, "info.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(persona.to_dict(), f, indent=4, ensure_ascii=False)
            print(f"Información guardada en formato JSON: {file_path}")

        elif formato == 'txt':
            file_path = os.path.join(person_folder_path, "info.txt")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"Nombre: {persona.name}\n")
                f.write(f"Edad: {persona.age}\n")
                f.write(f"Especie: {persona.specie}\n")
            print(f"Información guardada en formato TXT: {file_path}")

        else:
            print(f"Formato no soportado: {formato}")


class Persona:
    """
    Clase que representa a una persona.
    """

    specie = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        """
        Devuelve un diccionario con los datos de la persona.
        """
        return {
            "name": self.name,
            "age": self.age,
            "specie": self.specie
        }


# === PRUEBAS ===
if __name__ == "__main__":
    # Ruta base donde se almacenarán las carpetas
    ruta_base = "C:/temp/proyecto"

    # Crear instancia del gestor de carpetas
    fm = FolderManager(ruta_base)

    # Crear algunas personas
    persona1 = Persona("Juan", 30)
    persona2 = Persona("Lucía", 25)
    persona3 = Persona("Ana-María", 40)

    # Guardar personas en formato JSON y TXT
    fm.guardar_persona(persona1, formato="json")
    fm.guardar_persona(persona2, formato="txt")
    fm.guardar_persona(persona3, formato="json")

    # Listar carpetas creadas
    fm.list_folders()
