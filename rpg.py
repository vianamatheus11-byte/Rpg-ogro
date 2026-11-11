import os
import random
import time
class Arqueiro:
    def __init__(self, nome, vida = 90, ataque = 20, nivel = 1, xp = 0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        self.xp = xp

    def esta_vivo(self):
            return self.vida > 0    

    
    def atacar(self, inimigo):
            inimigo.vida -= self.ataque
            print(f"{self.nome} atacou {inimigo.nome} e causou {self.ataque} de dano!")             
            print("------------------------------------------------------------------------")
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida restante.")
            print("------------------------------------------------------------------------")
            time.sleep(1)

class Mago:
    def __init__(self, nome, vida = 120, ataque = 10, nivel = 1, xp = 0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        self.xp = xp

    def esta_vivo(self):

            return self.vida > 0    

    
    def atacar(self, inimigo):
            inimigo.vida -= self.ataque
            print(f"{self.nome} atacou {inimigo.nome} e causou {self.ataque} de dano!")             
            print("------------------------------------------------------------------------")
            print(f"{inimigo.nome} agora tem {inimigo.vida} de vida restante.")
            print("------------------------------------------------------------------------")
            time.sleep(1)

class Hero:
    def __init__(self, nome, vida = 100, ataque = 10 , nivel = 1 , xp = 0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        self.xp = xp
    

    def esta_vivo(self):
        return self.vida > 0    
    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} atacou {inimigo.nome} e causou {self.ataque} de dano!")             
        print("------------------------------------------------------------------------")
        print(f"{inimigo.nome} agora tem {inimigo.vida} de vida restante.")
        print("------------------------------------------------------------------------")
        time.sleep(1)

class Goblin:
    def __init__(self, nome):
        self.nome = nome
        self.vida = random.randint (20, 50)
        self.ataque = random.randint(5, 15) 

    def atacar(self, heroi):
        heroi.vida -= self.ataque
        print(f"{self.nome} atacou {heroi.nome} e causou {self.ataque} de dano!")
        print("------------------------------------------------------------------------")
        print(f"{heroi.nome} agora tem {heroi.vida} de vida restante.") 
        print("------------------------------------------------------------------------")
        time.sleep(1)

    def esta_vivo(self):
        return self.vida > 0
class Ogro:
    def __init__(self, nome):
        self.nome = nome
        self.vida = random.randint (40, 100)
        self.ataque = random.randint(12, 30) 

    def atacar(self, heroi):
        heroi.vida -= self.ataque
        print(f"{self.nome} atacou {heroi.nome} e causou {self.ataque} de dano!")
        print("------------------------------------------------------------------------")
        print(f"{heroi.nome} agora tem {heroi.vida} de vida restante.") 
        print("------------------------------------------------------------------------")
        time.sleep(1)

    def esta_vivo(self):
        return self.vida > 0



itens = ["Espada", "Escudo", "Poção de Vida", "Fruta Mágica"]


print("Bem-vindo ao jogo de RPG!")
print("Aperte enter para criar seu heroi")
input() 
print("Qual heroi você deseja ser?")
print("1. Mago - Vida: 120, Ataque: 10")
print("2. Guerreiro - Vida: 100, Ataque: 15")
print ("3. Arqueiro - Vida: 90, Ataque: 20")
opcao = input()
if opcao == "1":
    meu_heroi = Mago("Mago")
    os.system('cls' if os.name == 'nt' else 'clear')
elif opcao == "2":
    meu_heroi = Hero("Guerreiro")
    os.system('cls' if os.name == 'nt' else 'clear')
elif opcao == "3":
    meu_heroi = Arqueiro("Arqueiro")
    os.system('cls' if os.name == 'nt' else 'clear')

else:
    print("Opção inválida!")

    
    

while meu_heroi.esta_vivo():
    
    inimigo_ogro = Ogro("Ogro")
    inimigo_goblin = Goblin("Goblin")
    inimigo = random.choice([inimigo_ogro, inimigo_goblin])

    print(f"Um inimigo {inimigo.nome} apareceu!")
    print("Vida do Inimigo:", inimigo.vida)
    print( "Ataque do Inimigo:", inimigo.ataque)
    print("----------------------------------------")
    print ("Seu herói é:", meu_heroi.nome)
    print("Vida do Herói:", meu_heroi.vida)
    print("Ataque do Herói:", meu_heroi.ataque)
    print("Nível do Herói:", meu_heroi.nivel)
    print("Experiência do Herói:", meu_heroi.xp)
    print("----------------------------------------")
    print("Deseja atacar o inimigo? (s/n)")

    resposta = input()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    if resposta == "n":
        print("Você fugiu da luta!")
        print("------------------------------------------------------------------------")
        print("Caminhando pelo pantano...")
        time.sleep(2)
        print(f"Há um monstro a frente!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    if resposta == "s":
        
        while meu_heroi.esta_vivo() and inimigo.esta_vivo():
            meu_heroi.atacar(inimigo)
            if inimigo.esta_vivo():
                inimigo.atacar(meu_heroi)

 

        if meu_heroi.esta_vivo() and not inimigo.esta_vivo():
            item_ganho = random.choice(itens)
            xp_ganho = random.randint(5, 15)
            meu_heroi.xp += xp_ganho
            print(f"{meu_heroi.nome} ganhou {xp_ganho} pontos de experiência!")
            while meu_heroi.xp >= 100:
                meu_heroi.nivel += 1
                meu_heroi.xp -= 100
                print(f"{meu_heroi.nome} subiu para o nível {meu_heroi.nivel}!")    
                time.sleep(2)
                
                os.system('cls' if os.name == 'nt' else 'clear')
            print("Você venceu a luta!")
            print("------------------------------------------------------------------------")
            print(f"Você ganhou um {item_ganho}!")
            print("Aperte enter para adicionar")
            print("------------------------------------------------------------------------")
            input()
            print (f"Adicionando {item_ganho} ao herói...")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("caminhando pelo pantano...")
            time.sleep(2)   

            if item_ganho == "Espada":
                meu_heroi.ataque += 10
                print(f"Seu ataque aumentou para {meu_heroi.ataque}")
                os.system('cls' if os.name == 'nt' else 'clear')

            elif item_ganho == "Escudo":
                meu_heroi.vida += 30
                print(f"Sua vida aumentou para {meu_heroi.vida}")
                os.system('cls' if os.name == 'nt' else 'clear')

                os.system('cls' if os.name == 'nt' else 'clear')

            elif item_ganho == "Poção de Vida":
                meu_heroi.vida += 50
                print(f"Sua vida aumentou para {meu_heroi.vida}")
                os.system('cls' if os.name == 'nt' else 'clear')
                

            elif item_ganho == "Fruta Mágica":
                meu_heroi.ataque += 10
                meu_heroi.vida += 30
                print(f"Sua vida aumentou para {meu_heroi.vida}")
                print(f"Seu ataque aumentou para {meu_heroi.ataque}")
                os.system('cls' if os.name == 'nt' else 'clear')
    
                
        if meu_heroi.vida <= 0:
           print("Você perdeu a luta!")


