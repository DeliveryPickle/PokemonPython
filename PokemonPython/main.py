import pygame

# feel free to import specific functions instead of the entire module. I just dont know what exactly we need so I imported all.
import random
import math

normal = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 2,
    'poison' : 1,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 1,
    'ghost' : 0,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 1
}
fire = {
    'normal' : 1,
    'fire' : 0.5,
    'water' : 2,
    'electric' : 1,
    'grass' : 0.5,
    'ice' : 0.5,
    'fighting' : 1,
    'poison' : 1,
    'ground' : 2,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 0.5,
    'rock' : 2,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 0.5,
    'fairy' : 0.5,
}
water = {
    'normal' : 1,
    'fire' : 0.5,
    'water' : 0.5,
    'electric' : 2,
    'grass' : 2,
    'ice' : 0.5,
    'fighting' : 1,
    'poison' : 1,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 0.5,
    'fairy' : 1
}
electric = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 0.5,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 1,
    'poison' : 1,
    'ground' : 2,
    'flying' : 0.5,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 0.5,
    'fairy' : 1,
}
grass = {
    'normal' : 1,
    'fire' : 2,
    'water' : 0.5,
    'electric' : 0.5,
    'grass' : 0.5,
    'ice' : 2,
    'fighting' : 1,
    'poison' : 2,
    'ground' : 0.5,
    'flying' : 2,
    'psychic' : 1,
    'bug' : 2,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 1,
}
ice = {
    'normal' : 1,
    'fire' : 2,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 0.5,
    'fighting' : 2,
    'poison' : 1,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 2,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 2,
    'fairy' : 1
}
fighting = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 1,
    'poison' : 1,
    'ground' : 1,
    'flying' : 2,
    'psychic' : 2,
    'bug' : 0.5,
    'rock' : 0.5,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 0.5,
    'steel' : 1,
    'fairy' : 2
}
poison = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 0.5,
    'ice' : 1,
    'fighting' : 0.5,
    'poison' : 0.5,
    'ground' : 2,
    'flying' : 1,
    'psychic' : 2,
    'bug' : 0.5,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 0.5
}
ground = {
    'normal' : 1,
    'fire' : 1,
    'water' : 2,
    'electric' : 0,
    'grass' : 2,
    'ice' : 2,
    'fighting' : 1,
    'poison' : 0.5,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 0.5,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 1
}
flying = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 2,
    'grass' : 0.5,
    'ice' : 2,
    'fighting' : 0.5,
    'poison' : 1,
    'ground' : 0,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 0.5,
    'rock' : 2,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 1
}
psychic = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 0.5,
    'poison' : 1,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 0.5,
    'bug' : 2,
    'rock' : 1,
    'ghost' : 2,
    'dragon' : 1,
    'dark' : 2,
    'steel' : 1,
    'fairy' : 1
}
bug = {
    'normal' : 1,
    'fire' : 2,
    'water' : 1,
    'electric' : 1,
    'grass' : 0.5,
    'ice' : 1,
    'fighting' : 0.5,
    'poison' : 1,
    'ground' : 0.5,
    'flying' : 2,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 2,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 1
}
rock = {
    'normal' : 0.5,
    'fire' : 0.5,
    'water' : 2,
    'electric' : 1,
    'grass' : 2,
    'ice' : 1,
    'fighting' : 2,
    'poison' : 0.5,
    'ground' : 2,
    'flying' : 0.5,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 2,
    'fairy' : 1
}
ghost = {
    'normal' : 0,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 0,
    'poison' : 0.5,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 0.5,
    'rock' : 1,
    'ghost' : 2,
    'dragon' : 1,
    'dark' : 2,
    'steel' : 1,
    'fairy' : 1
}
dragon = {
    'normal' : 1,
    'fire' : 0.5,
    'water' : 0.5,
    'electric' : 0.5,
    'grass' : 0.5,
    'ice' : 2,
    'fighting' : 1,
    'poison' : 1,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 1,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 2,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 2
}
dark = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 2,
    'poison' : 1,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 0,
    'bug' : 2,
    'rock' : 1,
    'ghost' : 0.5,
    'dragon' : 1,
    'dark' : 1,
    'steel' : 1,
    'fairy' : 2
}
steel = {
    'normal' : 0.5,
    'fire' : 2,
    'water' : 1,
    'electric' : 1,
    'grass' : 0.5,
    'ice' : 0.5,
    'fighting' : 2,
    'poison' : 0,
    'ground' : 2,
    'flying' : 0.5,
    'psychic' : 0.5,
    'bug' : 0.5,
    'rock' : 0.5,
    'ghost' : 1,
    'dragon' : 0.5,
    'dark' : 1,
    'steel' : 0.5,
    'fairy' : 0.5
}
fairy = {
    'normal' : 1,
    'fire' : 1,
    'water' : 1,
    'electric' : 1,
    'grass' : 1,
    'ice' : 1,
    'fighting' : 0.5,
    'poison' : 2,
    'ground' : 1,
    'flying' : 1,
    'psychic' : 1,
    'bug' : 0.5,
    'rock' : 1,
    'ghost' : 1,
    'dragon' : 0,
    'dark' : 0.5,
    'steel' : 2,
    'fairy' : 1
}

global current_text
current_text = ''
class Move:
    def __init__(self, name, mtype, category, acc, pwr = 0, prio = 0):
        self.name = name
        self.type = mtype
        self.cat = category
        self.acc = acc
        self.pwr = pwr
        self.prio = prio

    def getInfo(self):
        print()
        print('Name: %s' %self.name)
        print('Type: %s' %self.type)
        print('Category: %s'%self.cat)
        print('Accuracy: %s'%self.acc)
        print('Power: %s'%self.pwr)
        print('Priority: %s' %self.prio)


class Pokemon:
    def __init__(self, name, HP, atk, defe, spatk, spdefe, spd,move1, move2, move3, move4, type1, deftype1, type2 = '', deftype2= ''):
        self.name = name
        self.HP = HP
        self.current_HP = HP
        self.__atk = atk
        self.__def = defe
        self.__spatk = spatk
        self.spdef = spdefe
        self.speed = spd
        self.moves = [move1, move2, move3, move4]
        self.__type1 = type1
        self.__type2 = type2
        self.__deftype1 = deftype1
        self.__deftype2 = deftype2
        self.HP_percent = (self.current_HP/self.HP)
        self.recharge = False
        self.isFainted = False

    bonusStats = 1
    def getStats(self):
        print()
        print('Name: %s' %self.name)
        print('HP: %s' %self.HP)
        print('Attack: %s' %self.__atk)
        print('Defence: %s' %self.__def)
        print('Special Attack: %s' %self.__spatk)
        print('Special Defence: %s' %self.spdef)
        print('Speed: %s' %self.speed)

    def getInfo(self):
        print()
        print(self.moves[0].name)
        print(self.moves[1].name)
        print(self.moves[2].name)
        print(self.moves[3].name)
        print('Name: %s' %self.name)
        print('Type: %s %s' %(self.__type1, self.__type2))
        print('Moves: %s, %s, %s, %s' %(self.moves[0].name, self.moves[1].name, self.moves[2].name, self.moves[3].name))

        #attack command
    def attack(self, pokemon, num):
        global current_text
        move = self.moves[num]
        #stab multiplier
        if move.type in self.__type1 or move.type in self.__type2:
            stab = 1.5
        else:
            stab = 1

        # Type Multiplier
        if (pokemon.__type2):
            typemul = pokemon.__deftype1[move.type] * pokemon.__deftype2[move.type]
        else:
            typemul = pokemon.__deftype1[move.type]

        #Crit chance
        critbonus = 0
        temp = random.randint(1,16)
        if temp == 1+ critbonus:
            isCrit = True
            crit = 1.5
        else:
            isCrit = False
            crit = 1

        #hit chance
        hit = random.randint(0,100)
        if hit > move.acc :
            miss = True
            hit = 0
        else:
            hit = 1
            miss = False

        #modifier calculations
        mod = stab*1*random.uniform(0.85,1)*typemul*self.bonusStats*crit*hit

        def damageThings(damage,pokemon):
            global current_text
            pokemon.current_HP -= damage
            pokemon.HP_percent = (pokemon.current_HP/pokemon.HP)
            current_text = self.name+' used '+ move.name
            if miss:
                attackUpdate()
                current_text = 'The move missed'
            elif isCrit:
                attackUpdate()
                current_text = 'A critical hit!'
            if not(miss):
                if typemul >= 2:
                    attackUpdate()
                    current_text = "It's super effective!"
                    effect = pygame.mixer.Sound('HitSuperEffective.wav')
                    effect.play()
                elif typemul == 0:
                    attackUpdate()
                    current_text = "It doesn't affect the opposing Pokemon"
                elif typemul <1:
                    attackUpdate()
                    current_text = "It's not very effective."
                    effect = pygame.mixer.Sound('HitNotVeryEffective.wav')
                    effect.play()
                else:
                    effect = pygame.mixer.Sound('HitNormal.wav')
                    effect.play()


        if self.recharge:
            current_text = self.name + ' needs to recharge'
            drawText()
            self.recharge = False
        else:
            #damage calculation for physical
            if move.cat == 'Physical':
                damage = math.ceil(((120/250)*(self.__atk/pokemon.__def)*move.pwr+2)*mod)
                damageThings(damage,pokemon)

                if move.name == 'Flare Blitz':
                    attackUpdate()
                    self.current_HP -= (damage*(1/3))//1
                    self.HP_percent = (self.current_HP/self.HP)
                    current_text = self.name + ' took recoil damage'
                    attackUpdate()
                elif move.name == 'Wild Charge':
                    attackUpdate()
                    self.current_HP -= (damage*(1/4))//1
                    self.HP_percent = (self.current_HP/self.HP)
                    current_text = self.name + ' took recoil damage'
                    attackUpdate()

            #damage calculation for special
            elif move.cat == 'Special':
                damage = math.ceil(((120/250)*(self.__spatk/pokemon.spdef)*move.pwr+2)*mod)
                damageThings(damage,pokemon)

            if move.name in ['Blast Burn','Frenzy Plant','Hydro Cannon','Giga Impact']:
                self.recharge = True

#charizard attacks
blast_burn = Move('Blast Burn', 'fire', 'Special', 90, 150)#recharge
flare_blitz = Move('Flare Blitz', 'fire', 'Physical', 120, 100)#recoil
air_slash = Move('Air Slash', 'flying', 'Special', 75, 95)
dragon_pulse = Move('Dragon Pulse', 'dragon', 'Special', 85, 100)

#Lapras moves
body_slam = Move('Body Slam','normal','Physical',85,100)
brine = Move('Brine','water','Special',100,65,0)#add brine things
blizzard = Move('Blizzard','water','Special',70,110)
psychic = Move('Psychic','psychic','Special',100,90)

#snorlax moves
shadow_ball = Move('Shadow Ball','ghost','Special',100,90)
crunch = Move('Crunch','dark','Physical',100,80)
giga_impact = Move('Giga Impact','normal','Physical',90,150)# force recharge
#uses blizzard from lapras

#venusarur moves
frenzy_plant = Move('Frenzy Plant','grass','Special',90,150)#recharge
giga_drain = Move('Giga Drain','grass','Special',100,75)#hp drain
sludge_bomb = Move('Sludge Bomb','poison','Special,',100,90)
earthquake = Move('Earthquake','ground','Physical',100,100)

#blastoise moves
hydro_cannon = Move('Hydro Cannon','water','Special',90,150)#recharge
flash_cannon = Move('Flash Cannon','steel','Special',100,80)
focus_blast = Move('Focus Blast','fighting','Special',70,120)
#also uses blizzard for some reason

#raichu moves
thunder_punch = Move('Thunder Punch','electric','Physical',100,70)
slam = Move('Slam','normal','Physical',100,80)
brick_break = Move('Brick Break','fighting','Physical',100,75)
wild_charge = Move('Wild Charge','electric','Physical',100,90)#recoil

#pikachu attacks
thunderbolt = Move('Thunderbolt', 'electric', 'Special', 100, 90)
thunder = Move('Thunder', 'electric', 'Special',70 , 110)
quick_attack = Move('Quick Attack', 'normal', 'Physical', 100, 40, 1)
iron_tail = Move('Iron Tail', 'steel', 'Physical', 75, 100)

#crobat attacks
aerial_ace = Move('Aerial Ace','flying','Physical',999,60)
zen_headbutt = Move('Zen Headbutt','psychic','Physical',90,80)
cross_poison = Move('Cross Poison','poison','Physical',100,70)
# uses shadow ball too

#omastar moves
hydro_pump = Move('Hydro Pump','water','Special',80,110)
ice_beam = Move('Ice Beam','ice','Special',100,90)
rock_slide = Move('Rock Slide','rock','Physical',90,75)
earth_power = Move('Earth Power','ground','Special',100,90)

#weavile moves
ice_punch = Move('Ice Punch','ice','Physical',100,75)
night_slash = Move('Night Slash','dark','Physical',100,70)
shadow_claw = Move('Shadow Claw','ghost','Physical',100,70)
#brick break

#scizor moves
bullet_punch = Move('Bullet Punch','steel','Physical',100,30,1)
x_scissor = Move('X-Scissor','bug','Physical',100,80)
razor_wind = Move('Razor Wind','normal','Special',100,80)
iron_head = Move('Iron Head','steel','Physical',100,80)

#sanslash moves
slash = Move('Slash','normal','Physical',100,70)
#earthquake
#iron tail
#rock slide

# REDS POKEMON
#charizard object
charizard = Pokemon('Charizard', 138, 80, 74, 102, 81, 94, blast_burn, flare_blitz, air_slash, dragon_pulse, 'fire',fire, 'flying',flying)
#lapras object
lapras = Pokemon('Lapras',190,81,76,81,90,58,body_slam,brine,blizzard,psychic, 'water',water,'ice',ice)
#snorlax object
snorlax = Pokemon('Snorlax',220,103,63,63,103,31,shadow_ball,crunch,giga_impact,blizzard,'normal',normal)
#venusarur object
venusaur = Pokemon('Venusaur',140,78,79,94,94,76,frenzy_plant,giga_drain,sludge_bomb,earthquake,'grass',grass,'poison',poison)
#blastoise object
blastoise = Pokemon('Blastoise',139,79,94,81,99,74,hydro_cannon,flash_cannon,focus_blast,blizzard,'water',water)
#raichu object
raichu = Pokemon('Raichu',120,120,54,85,76,120,thunder_punch,slam,brick_break,wild_charge,'electric',electric)

#PLAYERS POKEMON
#pikachu object
pikachu = Pokemon('Pikachu',105,76,49,72,58,112,thunderbolt,thunder,quick_attack,iron_tail, 'electric', electric)
#crobat
crobat = Pokemon('Crobat',145,85,76,67,76,121,aerial_ace,zen_headbutt,cross_poison,shadow_ball,'poison',poison,'flying',flying)
#omastar
omastar = Pokemon('LORD HELIX',130,60,117,108,67,54,hydro_pump,ice_beam,rock_slide,earth_power,'water',water,'rock',rock)
#weavile
weavile = Pokemon('Weavile',130,112,63,45,81,117,ice_punch,night_slash,shadow_claw,brick_break,'ice',ice,'dark',dark)
#scizor
scizor = Pokemon('Scizor',130,121,94,54,76,63,bullet_punch,x_scissor,razor_wind,iron_head,'bug',bug,'steel',steel)
#sandslash
sandslash = Pokemon('Sandslash',135,94,112,27,63,63,earthquake,iron_tail,rock_slide,slash,'ground',ground)

partyPokemon1 = pikachu
partyPokemon2 = crobat
partyPokemon3 = omastar
partyPokemon4 = weavile
partyPokemon5 = scizor
partyPokemon6 = sandslash

redParty = [charizard,lapras,snorlax,venusaur,blastoise,raichu]

#button class for making clickable buttons with text
class button():
    def __init__(self, colour, x,y, width,height, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        self.hitbox = pygame.draw.rect(win, self.colour, (self.x,self.y,self.width,self.height),0)

        #BIG button text
        if self.text != '' and self.text not in movesList:
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        else:
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True


    def get_pos(self):
        return (self.x,self.y)

        return False

#display updates for inside functions
def attackUpdate():
    timeDelay = 1000
    drawText()
    drawHP()
    pygame.display.update()
    pygame.time.delay(timeDelay)

# speed calculation and enemy "AI" functions
def fight(num):
    #choice for enemy pokemon's move
    global current_text
    ranNum = random.randint(0,3)
    #updates text after each attack interval

    #if player wins speed calc
    if active_pokemon.speed > enemy_pokemon.speed or active_pokemon.moves[num].prio>enemy_pokemon.moves[ranNum].prio:
        active_pokemon.attack(enemy_pokemon,num)
        attackUpdate()

        if enemy_pokemon.current_HP <= 0:
            current_text = enemy_pokemon.name + ' has fainted'
            enemy_pokemon.isFainted = True
            attackUpdate()

        else:
            enemy_pokemon.attack(active_pokemon,ranNum)
            attackUpdate()

            if active_pokemon.current_HP <= 0:
                current_text = active_pokemon.name + ' has fainted'
                active_pokemon.isFainted = True
                attackUpdate()

    #if computer wins speed calc
    else:
        enemy_pokemon.attack(active_pokemon,ranNum)
        attackUpdate()

        if active_pokemon.current_HP <= 0:
            current_text = active_pokemon.name + ' has fainted'
            active_pokemon.isFainted = True
            attackUpdate()

        else:
            active_pokemon.attack(enemy_pokemon,num)
            attackUpdate()

            if enemy_pokemon.current_HP <= 0:
                current_text = enemy_pokemon.name + ' has fainted'
                enemy_pokemon.isFainted = True
                attackUpdate()

    drawDefaultUI()
#setup
global active_pokemon
active_pokemon = pikachu
enemy_pokemon = charizard

#buttons
boxWidth = 190
boxHeight = 50

fightButton = button((0,0,0),480,455,boxWidth,boxHeight, "FIGHT")
bagButton = button((0,0,0),680,455,boxWidth,boxHeight, "BAG")
pokemonButton = button((0,0,0),480, 515,boxWidth,boxHeight, "PKMN")
runButton = button((0,0,0),680, 515,boxWidth,boxHeight, "RUN")

move1 = button((255,255,255),480, 455,boxWidth,boxHeight,active_pokemon.moves[0].name)
move2 = button((255,255,255),680, 455,boxWidth,boxHeight,active_pokemon.moves[1].name)
move3 = button((255,255,255),480, 515,boxWidth,boxHeight,active_pokemon.moves[2].name)
move4 = button((255,255,255),680, 515,boxWidth,boxHeight,active_pokemon.moves[3].name)


pBoxWidth = 300
pBoxHeight = 100
pokemon1 = button((56,144,216),140,50,pBoxWidth,pBoxHeight, partyPokemon1.name)
pokemon2 = button((56,144,216),140,200,pBoxWidth,pBoxHeight, partyPokemon2.name)
pokemon3 = button((56,144,216),140,350,pBoxWidth,pBoxHeight, partyPokemon3.name)
pokemon4 = button((56,144,216),520,50,pBoxWidth,pBoxHeight, partyPokemon4.name)
pokemon5 = button((56,144,216),520,200,pBoxWidth,pBoxHeight, partyPokemon5.name)
pokemon6 = button((56,144,216),520,350,pBoxWidth,pBoxHeight, partyPokemon6.name)
backButton = button((255,50,50),690,515,boxWidth+7,boxHeight,'Back')

#Drawings
def drawDefaultUI():
    # the box that is used when the user is deciding what to do
    window.blit(shortBox, (0,420))

    runButton.draw(window,(0,0,0))
    pokemonButton.draw(window,(0,0,0))
    bagButton.draw(window,(0,0,0))
    fightButton.draw(window,(0,0,0))

def drawFightUI():
    global current_text
    current_text = 'What will ' + active_pokemon.name + ' do?'
    drawText()
    window.blit(attackBox, (0,420))

    move1.draw(window,(0,0,0))
    move2.draw(window,(0,0,0))
    move3.draw(window,(0,0,0))
    move4.draw(window,(0,0,0))
    movesList = [active_pokemon.moves[0].name,active_pokemon.moves[1].name,active_pokemon.moves[2].name,active_pokemon.moves[3].name]

def drawHP():
    # enemy health, will increase and decrease in size and change colour - must be moved beneath the enemy information after the sprite is made.

    eBarLength = int(190*(enemy_pokemon.HP_percent)//1)
    if enemy_pokemon.HP_percent >= 0.5:
        eHP_colour = (104, 204, 136)
    elif enemy_pokemon.HP_percent >= 0.1:
        eHP_colour = (255,245,101)
    else:
        eHP_colour = (255, 0, 0)
    if enemy_pokemon.current_HP <= 0:
        eBarLength = 0
    pygame.draw.rect(window,(255,255,255),((190, 115), (190, 25)))
    eHealt = pygame.draw.rect(window,(eHP_colour),((190, 115), (eBarLength, 25)))

    #active pokemon HP
    aBarLength = int(190*(active_pokemon.HP_percent)//1)
    if active_pokemon.HP_percent >= 0.5:
        aHP_colour = (104, 204, 136)
    elif active_pokemon.HP_percent >= 0.1:
        aHP_colour = (255,245,101)
    else:
        aHP_colour = (255, 0, 0)
    if active_pokemon.current_HP <= 0:
        aBarLength = 0
    pygame.draw.rect(window,(255,255,255),((648, 333), (190, 25)))
    aHealt = pygame.draw.rect(window,(aHP_colour),((648, 333), (aBarLength, 25)))

    window.blit(enemyInfo, (50,60))
    window.blit(activeInfo, (477,278))

def drawText():
    #text that appears in the textbox
    drawDefaultUI()
    text = myFont.render(current_text, True, (0,0,0))
    window.blit(text,(30,500))

#pokemon select menu
def drawPokemonUI():
    current_text = ''
    window.blit(pkmnSelectBg, (0,0))
    pokemon1.draw(window,(0,0,0))
    pokemon2.draw(window,(0,0,0))
    pokemon3.draw(window,(0,0,0))
    pokemon4.draw(window,(0,0,0))
    pokemon5.draw(window,(0,0,0))
    pokemon6.draw(window,(0,0,0))
    backButton.draw(window,(0,0,0))

#same as pokemon menu without back button in order to force switch
def drawPokemonUI2():
    current_text = 'Choose a Pokemon'
    window.blit(pkmnSelectBg, (0,0))
    window.blit(attackBox, (0,500))
    pokemon1.draw(window,(0,0,0))
    pokemon2.draw(window,(0,0,0))
    pokemon3.draw(window,(0,0,0))
    pokemon4.draw(window,(0,0,0))
    pokemon5.draw(window,(0,0,0))
    pokemon6.draw(window,(0,0,0))

# initialization
pygame.init()


bgm = pygame.mixer.music.load('Battle Music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()
# size of display window. do not change this.
window = pygame.display.set_mode((900, 600))
template = pygame.image.load("template.png")
background = pygame.image.load("background.png")
pkmnSelectBg = pygame.image.load("pkmnselectmenu.png")

shortBox = pygame.image.load("options.png")
attackBox = pygame.image.load("attack.png")

charizardImg = pygame.image.load("charizard.png")
blastoiseImg = pygame.image.load("blastoise.png")
venusaurImg = pygame.image.load("venusaur.png")
laprasImg = pygame.image.load("lapras.png")
snorlaxImg = pygame.image.load("snorlax.png")
raichuImg = pygame.image.load("raichu.png")

pikachuImg = pygame.image.load("pikachu.png")
crobatImg = pygame.image.load("crobat.png")
omastarImg = pygame.image.load("omastar.png")
weavileImg = pygame.image.load("weavile.png")
scizorImg = pygame.image.load("scizor.png")
sandslashImg = pygame.image.load("sandslash.png")

pikachuInfo = pygame.image.load("pikachuinfo.png")
crobatInfo = pygame.image.load("crobatinfo.png")
omastarInfo = pygame.image.load("omastarinfo.png")
weavileInfo = pygame.image.load("weavileinfo.png")
scizorInfo = pygame.image.load("scizorinfo.png")
sandslashInfo = pygame.image.load("sandslashinfo.png")

charizardInfo = pygame.image.load("charizardinfo.png")
blastoiseInfo = pygame.image.load("blastoiseinfo.png")
venusaurInfo = pygame.image.load("venusaurinfo.png")
laprasInfo = pygame.image.load("laprasinfo.png")
snorlaxInfo = pygame.image.load("snorlaxinfo.png")
raichuInfo = pygame.image.load("raichuinfo.png")

redInfo = [charizardInfo,laprasInfo,snorlaxInfo,venusaurInfo,blastoiseInfo,raichuInfo]
redImg = [charizardImg,laprasImg,snorlaxImg,venusaurImg,blastoiseImg,raichuImg]
# template transparency
template.set_alpha(00)

# game title
pygame.display.set_caption("Pokemon")

# game icon (havent selected one yet)
# icon = pygame.image.load("icon.png")
# pygame.display.set_icon(icon)

#font things
white = (255,255,255)
black = (0,0,0)
myFont = pygame.font.SysFont('pokemon_fire_red.tff',36)
buttonFont = pygame.font.SysFont('pokemon_fire_red.tff',5)

# main/game loop
running = True
default_UI = True
text_UI = False
fight_UI = False
pokemon_UI = False
pokemon_UI2 = False
totalPokemon = [pikachu.isFainted,crobat.isFainted,sandslash.isFainted,scizor.isFainted,omastar.isFainted,weavile.isFainted]
enemyImg = charizardImg
activeImg = pikachuImg
interuptTxt = True
current_text = 'What will you do?'
enemyInfo = charizardInfo
activeInfo = pikachuInfo
while running:
    # background colour
    window.fill((72,66,67))
    window.blit(background, (0,00))
    window.blit(activeImg, (150,237))
    window.blit(enemyImg, (555, 67))


    window.blit(enemyInfo, (50,60))
    window.blit(activeInfo, (477,278))

    def drawFightUI():
        global current_text
        current_text = 'What will ' + active_pokemon.name + ' do?'
        drawText()
        window.blit(attackBox, (0,420))

        move1.draw(window,(0,0,0))
        move2.draw(window,(0,0,0))
        move3.draw(window,(0,0,0))
        move4.draw(window,(0,0,0))

    move1 = button((255,255,255),480, 455,boxWidth,boxHeight,active_pokemon.moves[0].name)
    move2 = button((255,255,255),680, 455,boxWidth,boxHeight,active_pokemon.moves[1].name)
    move3 = button((255,255,255),480, 515,boxWidth,boxHeight,active_pokemon.moves[2].name)
    move4 = button((255,255,255),680, 515,boxWidth,boxHeight,active_pokemon.moves[3].name)
    movesList = [active_pokemon.moves[0].name,active_pokemon.moves[1].name,active_pokemon.moves[2].name,active_pokemon.moves[3].name]

    drawHP()
    if enemy_pokemon.isFainted:
        if redParty:
            redParty.pop(0)
            redImg.pop(0)
            redInfo.pop(0)
        if not(redParty):
            default_UI = False
            game_over_text = "YOU WIN"
            myFont = pygame.font.SysFont('pokemon_fire_red.tff',120)
            # Display the game over screen
            pygame.draw.rect(window,(0,0,0),((0,0), (999,999)))
            game_over_text = myFont.render(game_over_text, True, (255, 255, 255))
            window.blit(game_over_text, (250, 250))
        else:
            enemy_pokemon = redParty[0]
            enemyImg = redImg[0]
            enemyInfo = redInfo[0]
            current_text = 'Trainer Red sent out ' + redParty[0].name
            drawText()
            pygame.time.delay(1000)

    if active_pokemon.isFainted:
        totalPokemon = [pikachu.isFainted,crobat.isFainted,sandslash.isFainted,scizor.isFainted,omastar.isFainted,weavile.isFainted]
        if totalPokemon.count(True) == 6:
            default_UI = False
            game_over_text = "GAME OVER"
            myFont = pygame.font.SysFont('pokemon_fire_red.tff',120)
            # Display the game over screen
            pygame.draw.rect(window,(0,0,0),((0,0), (999,999)))
            game_over_text = myFont.render(game_over_text, True, (255, 255, 255))
            window.blit(game_over_text, (250, 250))
        else:
            pokemon_UI2 = True
            default_UI = False
            drawPokemonUI2()

    # used to select bag, item, pokemon, or item
    if default_UI:
        drawDefaultUI()
    elif fight_UI:
        current_text = 'What will ' + active_pokemon.name + ' do?'
        drawFightUI()
    elif pokemon_UI:
        drawPokemonUI()
    elif pokemon_UI2:
        drawPokemonUI2()

    #text that appears in the textbox
    text = myFont.render(current_text, True, (0,0,0))
    window.blit(text,(30,500))

    window.blit(template, (0, 0))


    # checking for events such as key/mouse presses or mouse movemement
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos() #mouse position

    #as mouse button is released position of cursor is checked to see if it is in the same location as one  of the buttons
        if event.type == pygame.MOUSEBUTTONUP:
            if default_UI:
                if fightButton.hitbox.collidepoint(pos):
                    default_UI = False
                    fight_UI = True
                if pokemonButton.hitbox.collidepoint(pos):
                    pokemon_UI = True
                    default_UI = False
                if runButton.hitbox.collidepoint(pos):
                    current_text = "You can't run from a trainer battle"
                    drawText()
                    drawDefaultUI()

                if bagButton.hitbox.collidepoint(pos):
                    current_text = "Your bag is empty"
                    drawText()
                    drawDefaultUI()

            #hitbox detection for moves
            elif fight_UI:
                if move1.hitbox.collidepoint(pos):
                    fight_UI = False
                    default_UI = True
                    fight(0)
                elif move2.hitbox.collidepoint(pos):
                    fight_UI = False
                    default_UI = True
                    fight(1)
                elif move3.hitbox.collidepoint(pos):
                    fight_UI = False
                    default_UI = True
                    fight(2)
                elif move4.hitbox.collidepoint(pos):
                    fight_UI = False
                    default_UI = True
                    fight(3)

            elif pokemon_UI or pokemon_UI2:
                if pokemon_UI:
                    if backButton.hitbox.collidepoint(pos):
                        pokemon_UI = False
                        default_UI = True
                        pokemon_UI2 = False
                def pokeButton(pokemon,partyPokemon):
                    global active_pokemon
                    global current_text
                    global pokemon_UI
                    global default_UI
                    if pokemon.hitbox.collidepoint(pos):
                        if active_pokemon == partyPokemon:
                            current_text = 'This pokemon is already out'
                            drawText()
                        elif partyPokemon.isFainted:
                            current_text = 'This pokemon is unable to battle'
                            drawText()
                        else:
                            active_pokemon = partyPokemon
                            current_text = 'Go '+active_pokemon.name +'!'
                            pokemon_UI = False
                            default_UI = True
                            drawText()
                            drawHP()
                            pygame.time.delay(700)

                if pokemon1.hitbox.collidepoint(pos):
                    pokeButton(pokemon1,partyPokemon1)
                    activeImg = pikachuImg
                    activeInfo = pikachuInfo
                    pokemon_UI2 = False
                if pokemon2.hitbox.collidepoint(pos):
                    pokeButton(pokemon2,partyPokemon2)
                    activeImg = crobatImg
                    activeInfo = crobatInfo
                    pokemon_UI2 = False
                if pokemon3.hitbox.collidepoint(pos):
                    pokeButton(pokemon3,partyPokemon3)
                    activeImg = omastarImg
                    activeInfo = omastarInfo
                    pokemon_UI2 = False
                if pokemon4.hitbox.collidepoint(pos):
                    pokeButton(pokemon4,partyPokemon4)
                    activeImg = weavileImg
                    activeInfo = weavileInfo
                    pokemon_UI2 = False
                if pokemon5.hitbox.collidepoint(pos):
                    pokeButton(pokemon5,partyPokemon5)
                    activeImg = scizorImg
                    activeInfo = scizorInfo
                    pokemon_UI2 = False
                if pokemon6.hitbox.collidepoint(pos):
                    pokeButton(pokemon6,partyPokemon6)
                    activeImg = sandslashImg
                    activeInfo = sandslashInfo
                    pokemon_UI2 = False


        #checks if any box is hovered and changes the colour
        if event.type == pygame.MOUSEMOTION:
            #base button hovers
            if runButton.isOver(pos):
                runButton.colour = (248, 255, 245)
            else:
                runButton.colour = (215, 227, 211)

            if pokemonButton.isOver(pos):
                pokemonButton.colour = (248, 255, 245)
            else:
                pokemonButton.colour = (215, 227, 211)

            if bagButton.isOver(pos):
                bagButton.colour = (248, 255, 245)
            else:
                bagButton.colour = (215, 227, 211)

            if fightButton.isOver(pos):
                fightButton.colour = (248, 255, 245)
            else:
                fightButton.colour = (215, 227, 211)

            #move button hovers
            if move1.isOver(pos):
                move1.colour = (248, 255, 245)
            else:
                move1.colour = (215, 227, 211)

            if move2.isOver(pos):
                move2.colour = (248, 255, 245)
            else:
                move2.colour = (215, 227, 211)

            if move3.isOver(pos):
                move3.colour = (248, 255, 245)
            else:
                move3.colour = (215, 227, 211)

            if move4.isOver(pos):
                move4.colour = (248, 255, 245)
            else:
                move4.colour = (215, 227, 211)

            #pokemon button hovers
            if pokemon1.isOver(pos):
                pokemon1.colour = (120,208,232)
            elif partyPokemon1.isFainted:
                pokemon1.colour = (220,70,10)
            else:
                pokemon1.colour = (56,144,216)

            if pokemon2.isOver(pos):
                pokemon2.colour = (120,208,232)
            elif partyPokemon2.isFainted:
                pokemon2.colour = (220,70,10)
            else:
                pokemon2.colour = (56,144,216)

            if pokemon3.isOver(pos):
                pokemon3.colour = (120,208,232)
            elif partyPokemon3.isFainted:
                pokemon3.colour = (220,70,10)
            else:
                pokemon3.colour = (56,144,216)

            if pokemon4.isOver(pos):
                pokemon4.colour = (120,208,232)
            elif partyPokemon4.isFainted:
                pokemon4.colour = (220,70,10)
            else:
                pokemon4.colour = (56,144,216)

            if pokemon5.isOver(pos):
                pokemon5.colour = (120,208,232)
            elif partyPokemon5.isFainted:
                pokemon5.colour = (220,70,10)
            else:
                pokemon5.colour = (56,144,216)

            if pokemon6.isOver(pos):
                pokemon6.colour = (120,208,232)
            elif partyPokemon6.isFainted:
                pokemon6.colour = (220,70,10)
            else:
                pokemon6.colour = (56,144,216)

            if backButton.isOver(pos):
                backButton.colour = (158,144,196)
            else:
                backButton.colour = (112,88,176)
        #if the user clicks the "x" in the top right corner the game closes
        if event.type == pygame.QUIT:
            running = False

    # end of main/game loop. do not place anything after this.
    pygame.display.update()


pygame.quit()
