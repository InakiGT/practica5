class GameObject:
    def __init__(self, sprite, collider, coords):
        self.sprite = sprite
        self.collider = collider
        self.coords = coords

    def __del__ (self):
        print("Instancia eliminada")

    def translate(self, coords):
        self.coords = coords
    
    def scale(self, size):
        self.coords[2] = size

    def get_collision(self, gameObject):
        if self.collider and gameObject.collider:
            print("Collided")
            return True
    
    def change_sprite_color(self, rgb):
        self.sprite = rgb


class Player(GameObject):
    def __init__(self, sprite, colider, coords, name, damage, type, level):
        GameObject.__init__(self, sprite, colider, coords)
        self.hp = 20
        self.level = level
        self.damage = damage
        self.name = name
        self.type = type
        self.perks = []
    
    def __del__ (self):
        pass

    def take_damage(self, damage):
        print("Auch!")
        self.hp -= damage
        print("hp: ", self.hp)
    
    def attak(self, enemy):
        enemy.take_damage(self.damage)

    def dead(self):
        print("Aaaah!")

    def level_up(self):
        self.level += 1

    def add_perk(self, perk):
        if self.perks.count(perk) == 0:
            self.perks.append(perk)
        else:
            print("Ese beneficio ya ha sido añadido")

class NPC(Player):
    def __init__(self, sprite, colider, coords, name, damage, type, level, dialogue):
        Player.__init__(self, sprite, colider, coords, name, damage, type, level)
        self.dialogue = dialogue

    def __del__ (self):
        pass

    def talk(self):
        print(self.dialogue)

    # Polimorfismo
    def attak(self):
        print("Hey!, yo soy pacifico")
    
    def take_damage(self):
        print("Auch!")

    def dead(self):
        print("Yo no puedo morir")
    
    def level_up(self):
        self.level = 1
    
    def add_perk(self):
        print("Yo no utilizo beneficios")

def main():
    trigger = GameObject([0, 0, 0], "Square", [10, 0, 3])
    main_player = Player([122, 122, 122], "Capsule", [0, 0, 0], "Goblin", 10, "Magic", 1)
    villager = NPC([10, 12, 2], "Capsule", [10, 0, 20], "Sam the villager", 1, "Human", 5, "Hello traveler")

    main_player.translate([10, 0, 3])
    if trigger.get_collision(main_player):
        main_player.change_sprite_color([255, 0, 0])
    main_player.translate([10, 0, 20])
    villager.talk()
    villager.attak()
    villager.dead()
    

if __name__ == "__main__":
    main()
