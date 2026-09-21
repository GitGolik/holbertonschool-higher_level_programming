import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """
        Serialize the current instance and save it to the specified file using pickle.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            # En cas d'erreur (fichier inaccessible, etc.), on ne fait rien de spécial
            pass

    @classmethod
    def deserialize(cls, filename: str):
        """
        Load and return a CustomObject instance from the specified file using pickle.
        Return None if the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                # On s'assure que c'est bien une instance de CustomObject
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None

