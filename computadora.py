
class Electrodomestico:
    def __init__(self, watts, voltaje, tipo_corriente):
        self.watts = watts
        self.voltaje = voltaje
        self.tipo_corriente = tipo_corriente

    def __del__(self):
        print("Instancia eliminada")

    def describir_wattaje(self):
        print(self.watts)

    def describir_voltaje(self):
        print(self.voltaje)

    def describir_tipo_corriente(self):
        print(self.tipo_corriente)

class Computadora(Electrodomestico):
    def __init__(self, watts, voltaje, tipo_corriente, nucleos_procesador, ram, almacenamiento, frecuencia_procesador, vram, os):
        Electrodomestico.__init__(self, watts, voltaje, tipo_corriente)
        self.nucleos_procesador = nucleos_procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.frecuencia_procesador = frecuencia_procesador
        self.vram = vram
        self.os = os

    def __del__(self):
        pass

    def encender(self):
        print("Inicio de " + self.os)
    
    def procesar_graficos(self):
        self.vram -= 1
        print("Gráficos procesados, vram disponible: ", self.vram)
    
    def procesar_programa(self):
        self.ram -= 1
        self.nucleos_procesador -= 1
        print("Programa procesado, nucleos restantes: ", self.nucleos_procesador, "ram restante: ", self.ram)

    def mostrar_info(self):
        print("Procesador ", self.nucleos_procesador, "nucleos, ", self.frecuencia_procesador, "Ghz. ", self.almacenamiento, "GB. ", self.ram, "GB RAM. ", self.vram, " VRAM.")

class Laptop(Computadora):
    def __init__(self, watts, voltaje, tipo_corriente, marca, modelo, nucleos_procesador, ram, almacenamiento, frecuencia_procesador, vram, os):
        Computadora.__init__(self, watts, voltaje, tipo_corriente, nucleos_procesador, ram, almacenamiento, frecuencia_procesador, vram, os)
        self.marca = marca
        self.modelo = modelo

    def __del__(self):
        pass

    def suspender(self):
        print("Equipo suspendido")
    
    def describir_modelo(self):
        print(self.modelo)
    
    def describir_marca(self):
        print(self.marca)
    
    # Polimorfismo
    def describir_wattaje(self):
        print("Wattaje:", self.watts, "opcional, mientras se encuentra cargando")

    def describir_voltaje(self):
        print("Volts:", self.voltaje, "opcional, mientras se encuentra cargando")
    
    def describir_tipo_corriente(self):
        print("Corriente:", self.tipo_corriente, "mientras se encuentra cargando")

    def mostrar_info(self):
       print("De la marca", self.marca, "modelo", self.modelo)
       return super().mostrar_info()

def main():
    licuadora = Electrodomestico(450, 125, "alterna")
    licuadora.describir_voltaje()

    pc = Computadora(1000, 125, "alterna", 8, 16, 1024, 4.9, 6, "Kali Linux")
    pc.encender()

    macbook = Laptop(30, 125, "alterna", "Apple", "Air", 8, 8, 256, 4.2, 8, "MacOS")
    macbook.suspender()
    macbook.mostrar_info()

if __name__ == "__main__":
    main()