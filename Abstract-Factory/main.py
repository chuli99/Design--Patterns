from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    Declara una interfaz para operaciones que crean objetos de productos abstractos
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    
    #Implementa los metodos del Abstract factory segun las especificidades de la familia
   

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    
    #Implementa los metodos del Abstract factory segun las especificidades de la familia
    

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    #Declara una interfaz para un tipo de objeto de producto

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Los productos concretos son creados por las correspondientes fabricas concretas.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Resultado del producto A1"


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "Resultado del producto A"


class AbstractProductB(ABC):
    """
    Aqui se declara una interfaz para un tipo de objeto de producto
    """
    @abstractmethod
    def posible_funcion_b(self) -> None:
        pass

    @abstractmethod
    def otra_posible_funcion_b(self, collaborator: AbstractProductA) -> None:
        pass



#Productos concretos son creados por las correspondientes fabricas concretas



class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "Resultado del producto B1."



    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado de B1 colaborando con el ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado del B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        result = collaborator.useful_function_a()
        return f"El resultado del B2 colaborando con el ({result})"


def client_code(factory: AbstractFactory) -> None:
    #El codigo cliente solo puede trabajar con clases abstractas
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    #El codigo cliente puede trabajar con cualquier clase de fabrica concreta
    print("Client: Testeando codigo cliente con el primer tipo de fabrica:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testeando codigo cliente con segundo tipo de fabrica:")
    client_code(ConcreteFactory2())