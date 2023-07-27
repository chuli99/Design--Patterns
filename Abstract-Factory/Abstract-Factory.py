from abc import ABC, abstractmethod

# Producto Abstracto para las formas geométricas


class Forma(ABC):
    @abstractmethod
    def dibujar(self):
        pass

# Productos Concretos para las formas geométricas


class Circulo(Forma):
    def dibujar(self):
        return "Se dibuja un círculo."


class Cuadrado(Forma):
    def dibujar(self):
        return "Se dibuja un cuadrado."

# Producto Abstracto para los colores


class Color(ABC):
    @abstractmethod
    def llenar(self):
        pass

# Productos Concretos para los colores


class Rojo(Color):
    def llenar(self):
        return "Se llena con color rojo."


class Azul(Color):
    def llenar(self):
        return "Se llena con color azul."

# Fábrica Abstracta


class FabricaAbstracta(ABC):
    @abstractmethod
    def crear_forma(self):
        pass

    @abstractmethod
    def crear_color(self):
        pass

# Fábrica Concreta para formas geométricas


class FabricaFormas(FabricaAbstracta):
    def crear_forma(self):
        return Circulo()

    def crear_color(self):
        return Rojo()

# Fábrica Concreta para colores


class FabricaColores(FabricaAbstracta):
    def crear_forma(self):
        return Cuadrado()

    def crear_color(self):
        return Azul()

# Uso del Abstract Factory


def main():
    fabrica_formas = FabricaFormas()
    forma = fabrica_formas.crear_forma()
    color = fabrica_formas.crear_color()
    print(forma.dibujar())  # Salida: "Se dibuja un círculo."
    print(color.llenar())  # Salida: "Se llena con color rojo."

    fabrica_colores = FabricaColores()
    forma = fabrica_colores.crear_forma()
    color = fabrica_colores.crear_color()
    print(forma.dibujar())  # Salida: "Se dibuja un cuadrado."
    print(color.llenar())  # Salida: "Se llena con color azul."


if __name__ == "__main__":
    main()
