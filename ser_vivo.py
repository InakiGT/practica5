
class Organismo:
    def __init__(self, dominio, composicion):
        self.dominio = dominio
        self.composicion = composicion
    
    def __del__(self):
        print("Instancia eliminada")

    def describir_grupo_evolutivo(self):
        print(self.dominio)
    
    def describir_composicion(self):
        print(self.composicion)

class SerVivo(Organismo):
    def __init__(self, dominio, composicion, nombre, tamaño, movimiento, metabolismo, reproduccion, comunicacion):
        Organismo.__init__(self, dominio, composicion)
        self.nombre = nombre
        self.tamaño = tamaño
        self.movimento = movimiento
        self.metabolismo = metabolismo
        self.reproduccion = reproduccion
        self.comunicacion = comunicacion

    def __del__(self):
        pass

    def show_info(self):
        print("Es un " + self.nombre + "de " + self.tamaño + "m, cuyo método de reproducción es " + self.reproduccion + " de comunicación es " + self.comunicacion + " y su tipo de metabolismo es " + self.comunicacion + ", mientras que se mueve a traves de " + self.movimento)

    def moverse(self):
        print(self.movimento)

    def reproducirse(self):
        print(self.reproduccion)

    def comunicarse(self):
        print(self.comunicacion)

class Humano(SerVivo):
    def __init__(self, dominio, composicion, tamaño, movimiento, metabolismo, reproduccion, comunicacion, genero, orientacion_sexual, edad):
        SerVivo.__init__(self, dominio, composicion, "humano", tamaño, movimiento, metabolismo, reproduccion, comunicacion)
        self.genero = genero
        self.orientacion_sexual = orientacion_sexual
        self.edad = edad

    def __del__(self):
        pass

    def comunicar_edad(self):
        print("Tengo ", self.edad, " años")
    
    # Polimorfismo
    def comunicarse(self):
        print("Hola amigos")

    def reproducirse(self):
        if self.orientacion_sexual == "heterosezual":
            print("Tener relaciones sexuales")
        else:
            print("Inseminación artificial")
    
    def moverse(self):
        print("Caminando")
    
    def comunicar_orientacion(self):
        print("Mi orientación es", self.orientacion_sexual)

    def comunicar_genero(self):
        print("Soy género", self.genero)

def main():

    mi_organismo = Organismo("prokaryota", "moléculas orgánicas")
    mi_organismo.describir_composicion()
    mi_organismo.describir_grupo_evolutivo()

    mi_ser_vivo = SerVivo("eukaryota", "moléculas orgánicas", "perro", "1", "cuadripedo", "catabolismo", "sexual anisogámica por fertilización interna", "ladrido")
    mi_ser_vivo.show_info()
    
    mi_humano = Humano("eukaryota", "moléculas orgánicas", "1", "cuadripedo", "catabolismo", "sexual anisogámica por fertilización interna", "habla", "femenino", "heterosexual", 19)
    mi_humano.comunicar_genero()
    mi_humano.reproducirse()

if __name__ == "__main__":
    main()