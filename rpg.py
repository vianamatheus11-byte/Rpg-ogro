import random
import time
itens = ["Espada", "Escudo", "Poção de Vida", "Fruta Mágica"]


print("Bem-vindo ao jogo de RPG!")
print("Aperte enter para criar seu heroi")
input() 

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



    ## criacao do heroi

meu_heroi = Hero("Herói")


while meu_heroi.esta_vivo():
    ##criacao do inimigo
    inimigo_ogro = Ogro("Ogro")
    print("Um inimigo Ogro apareceu!")
    print("Vida do Ogro:", inimigo_ogro.vida)
    print( "Ataque do Ogro:", inimigo_ogro.ataque)
    print("----------------------------------------")
    print("Vida do Herói:", meu_heroi.vida)
    print("Ataque do Herói:", meu_heroi.ataque)
    print("Nível do Herói:", meu_heroi.nivel)
    print("Experiência do Herói:", meu_heroi.xp)
    print("----------------------------------------")
    print("Deseja atacar o Ogro? (s/n)")
    resposta = input()
    if resposta == "s":
        
        while meu_heroi.esta_vivo() and inimigo_ogro.esta_vivo():
            meu_heroi.atacar(inimigo_ogro)
            if inimigo_ogro.esta_vivo():
                inimigo_ogro.atacar(meu_heroi)

 

        if meu_heroi.esta_vivo() and not inimigo_ogro.esta_vivo():
            item_ganho = random.choice(itens)
            xp_ganho = random.randint(5, 15)
            meu_heroi.xp += xp_ganho
            print(f"{meu_heroi.nome} ganhou {xp_ganho} pontos de experiência!")
            while meu_heroi.xp >= 100:
                meu_heroi.nivel += 1
                meu_heroi.xp -= 100
                print(f"{meu_heroi.nome} subiu para o nível {meu_heroi.nivel}!")    

            print("Você venceu a luta!")
            print("------------------------------------------------------------------------")
            print("voce ganhou um "+ item_ganho)
            print("Aperte enter para adicionar")
            print("------------------------------------------------------------------------")
            input()
                    
            if item_ganho == "Espada":
                meu_heroi.ataque += 10
                print("Seu ataque aumentou para", meu_heroi.ataque)

            elif item_ganho == "Escudo":
                meu_heroi.vida += 30
                print("Sua vida aumentou para", meu_heroi.vida)

            elif item_ganho == "Poção de Vida":
                meu_heroi.vida += 50
                print("Sua vida aumentou para", meu_heroi.vida)

            elif item_ganho == "Fruta Mágica":
                meu_heroi.ataque += 10
                meu_heroi.vida += 30
                print("Sua vida aumentou para", meu_heroi.vida)
                print("Seu ataque aumentou para", meu_heroi.ataque)
    
        if meu_heroi.vida <= 0:
                print("Você perdeu a luta!")            



