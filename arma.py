from abc import ABC, abstractmethod

class Arma(ABC):
    def __init__(self, turnos, ataque):
        self._turnos_restantes = turnos
        self._turnos_totales = turnos
        self._ataque = ataque
        
    @property
    def ataque(self):
        return self._ataque
    
    @property
    def turnos_restantes(self):
        return self._turnos_restantes
    
    @property
    def turnos_totales(self):
        return self._turnos_totales
    
    @abstractmethod
    def usar(self):
        pass

class Espada(Arma):
    #turnos en espadas = durabilidad
    #extra en espadas = material
    def __init__(self, material, turnos, ataque):
        super().__init__(turnos, ataque)
        self._material = material
        
    def usar(self):
        if self.turnos_restantes > 0:
            print(f"¡La espada de {self._material} está lista para usar!")
            print(f"Ataque realizado: {self._ataque}")
            self._turnos_restantes -= 1
            print(f"Durabilidad restante: {self._turnos_restantes}/{self._turnos_totales}")
        else:
            print("La espada está rota y no se puede usar más.")
    
    def __str__(self):
        return f"Espada de {self._material}\nAtaque: {self.ataque}\ndurabilidad:  {self._turnos_restantes}/{self._turnos_totales}"
   
class Baston(Arma):
    # turnos en bastón = maná
    # extra en bastón = tipo de magia
    def __init__(self, tipo_magia, mana, ataque):
        super().__init__(mana, ataque)
        self._tipo_magia = tipo_magia
        
    def usar(self):
        if self.turnos_restantes > 0:
            print(f"¡El bastón de {self._tipo_magia} está listo para usar!")
            print(f"Ataque mágico realizado: {self._ataque}")
            self._turnos_restantes -= 1
            print(f"Maná restante: {self._turnos_restantes}/{self._turnos_totales}")
        else:
            print("El bastón no tiene más maná y no se puede usar.")
    
    def __str__(self):
        return f"Bastón de {self._tipo_magia}\nAtaque Mágico: {self.ataque}\nManá: {self._turnos_restantes}/{self._turnos_totales}"

class Pistola(Arma):
    # turnos en pistola = balas
    # extra en pistola = silenciador o no algo así, puerta resuelve
    def __init__(self, tipo, balas, ataque):
        super().__init__(balas, ataque)
        self._tipo = tipo
        
    def usar(self):
        if self.turnos_restantes > 0:
            print(f"¡La pistola {self._tipo} está lista para usar!")
            print(f"Ataque realizado: {self._ataque}")
            self._turnos_restantes -= 1
            print(f"Balas restantes: {self._turnos_restantes}/{self._turnos_totales}")
        else:
            print("La pistola está descargada y no se puede usar más.")
    
    def __str__(self):
        return f"Pistola {self._tipo}\nAtaque: {self.ataque}\nBalas: {self._turnos_restantes}/{self._turnos_totales}"



def crearArma(tipo, extra, turnos, ataque):
    if(tipo == '1'):
        return Espada(extra, turnos, ataque)
    elif(tipo=='2'):
        return Pistola(extra, turnos, ataque)
    elif(tipo=='3'):
        return Baston(extra, turnos, ataque)
    else:
        print("Opción invalida")    
    
