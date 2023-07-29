# Clase existente con una interfaz incompatible
class OldPrinter:
    def print_with_dots(self, text):
        print(text + ".")

# Nueva clase con una interfaz incompatible
class NewPrinter:
    def print_with_asterisks(self, text):
        print(text + "*")

# Adaptador que convierte la interfaz de NewPrinter a la interfaz de OldPrinter
class PrinterAdapter(OldPrinter):
    def __init__(self, new_printer):
        self.new_printer = new_printer

    def print_with_dots(self, text):
        # Convertimos la interfaz de print_with_dots a print_with_asterisks
        self.new_printer.print_with_asterisks(text)

# Función que acepta un objeto OldPrinter y lo utiliza para imprimir un texto
def print_text(printer, text):
    printer.print_with_dots(text)

# Ejemplo de uso
old_printer = OldPrinter()
new_printer = NewPrinter()

# Utilizamos la clase OldPrinter directamente
print_text(old_printer, "Hola")  # Salida: "Hola."

# Utilizamos el adaptador para hacer que NewPrinter funcione con el código existente
adapter = PrinterAdapter(new_printer)
print_text(adapter, "Hola")  # Salida: "Hola*"
