from abc import ABC, abstractmethod


# Producto (Product)
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass


# Productos Concretos (Concrete Products)
class Perro(Animal):
    def hablar(self):
        return "Guau!"


class Gato(Animal):
    def hablar(self):
        return "Miau!"


# Creador (Creator)
class CreadorAnimales(ABC):
    @abstractmethod
    def crear_animal(self):
        pass


# Creador Concreto (Concrete Creator)
class CreadorDePerros(CreadorAnimales):
    def crear_animal(self):
        return Perro()


class CreadorDeGatos(CreadorAnimales):
    def crear_animal(self):
        return Gato()


# Uso del Factory
def main():
    creador_perros = CreadorDePerros()
    animal = creador_perros.crear_animal()
    print(animal.hablar())  # Salida: "Guau!"

    creador_gatos = CreadorDeGatos()
    animal = creador_gatos.crear_animal()
    print(animal.hablar())  # Salida: "Miau!"


if __name__ == "__main__":
    main()
