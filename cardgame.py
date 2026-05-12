import random
import pygame


print("The game is played on a 8x8 board and you can place creatures on it using tokens with the card's name on them.  Each card corresponds to a token and the cards are to keep track of the tokens. Each creature dies by getting another creature on the same space as it. The goal is to kill the other team's commander  which they can place anywhere on their side of the board.  Area means diagonally, vertically, and horizontally however radius means anywhere in the range.  Every turn the player whose turn it is can place one energy on their side of the map unless a card says otherwise.  Things cost energy to cast, signified by the number before the E.  Creatures can also destroy energy using the same rules as killing other creatures.  Spells can be cast and they can be placed where the card says.  This can't kill creatures and will not stay unless the card says otherwise.  Once a creature dies or a spell gets used they go in a graveyard pile and you can't cast them again unless a card says otherwise.  The commander is not a creature.  Below is what every single card does.")
print()
print("Rabbit 1E; moves in a 3x3 area")
print()
print("Impale(spell) 2E; place on a creature and that creature dies next turn")
print()
print("Energy Caster 2E; every 2 turns create 1 energy. This creature can't move")
print()
print("Miner 2E; moves horizontally and vertically in a 3x3 area and if it goes on a boulder it destroys it")
print()
print("Throw(spell) 2E; place on a creature and it kills one creature in a 3x3 radius")
print()
print("Necromace(spell) 2E; can be used at any time. If a creature dies than you take control of that creature")
print()
print("Leather Worker 3E; if something were to try to attack it and they would have to pass through the 3 squares in front of it in a 3x3 area, they can't attack it. Moves in a 3x3 area")

print()
print("Help(spell)3E; teleport any creature you control to any of the spaces around it in a 3x3 radius")
print()
print("Boulder 3E; cant move and can't be killed normally and other creatures can't cross it")
print()
print("Revenge(spell) 4E; if a creature you controlled died last turn,kill the creature that killed it")
print()
print("Ranger 4E; moves in a 3x3 area and every turn instead of moving it can kill something in a 5x5 area except the commander")
print()
print("Chain Lightning(spell) 4E; if something dies this turn than all creatures within a 3x3 area of that creature also die")

print()
print("Drame's fang(spell) 4E; can be placed anywhere on the map and kills all creatures vertically in a 3x3 area")
print()
print("Wizard 5E; instead of moving it can teleport to any space on the map but if it kills something using this way it dies itself also it can't kill the commander")
print()
print("Revival (spell) 5E; place one creature that died on your side of the board without paying the energy cost")
print()
print("Warthog 5E; if a creature you don't control is diagonally or horizontally or vertically from it it can charge to that creature")
print()
print("Ninja 5E; moves diagonally in a 5x5 area")
print()
print("Spatulob 5E; moves in a 5x5 area")
print()
print("Becon 6E; place this anywhere on the map and it stays there until it gets destroyed,  also any creature you control in a 3x3 radius around it cannot be killed by normal means")
print()
print("Dragon 6E; if a creature is in the 3 spaces in front of it they die and this creature cannot be attacked from horizontally.  It moves in a 5x5 area")
print()
print("Explosive Darkness 8E; moves in a 5x5 radius and wherever it lands all creatures you don't control in a 3x3 area die")
print()

class rabbit():
    def __init__(self):
        g
running = True
screen = pygame.display.set_mode((1580, 820))
playerpos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

ev = pygame.event.get()

pygame.display.set_caption("Sandbox")

clock = pygame.time.Clock()
pygame.init()
left, middle, right = pygame.mouse.get_pressed()
while running:
    
    

    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    

    clock.tick(60)  # limits FPS to 60

pygame.quit()

