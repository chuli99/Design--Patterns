class Target:
    #Target define la interfaz utilizada por el codigo cliente

    def request(self) -> str:
        return "Comportamiento Predeterminado de Target"


class Adaptee:
    #Adaptee contiene un comportamiento util pero incompatible con la interfaz existente
    #Es la clase a adaptar
    def specific_request(self) -> str:        
        return ".eetpadA ed ocificepse otneimatropmoC"


class Adapter(Target, Adaptee):
    #Adapter convierte la interfaz de Adaptee en una interfaz compatible con el Target

    def request(self) -> str:
        return f"Adapter: (ADAPTANDO INTERFACE INCOMPATIBLE) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    #El codigo cliente soporta todas las clases que siguen la interfaz Target

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: No puedo trabajar con objetos de la clase Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: Interfaz de Adaptee no comprendida ")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    

    print("Client: Llamando adaptador:")
    adapter = Adapter()
    client_code(adapter)