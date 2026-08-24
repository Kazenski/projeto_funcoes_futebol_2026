# =============================================================================
# ARQUIVO: funcoes.py
# OBJETIVO: Regras de negócio, sorteio de jogadas (chances de gol) e narrativa.
# =============================================================================
import random

def tentar_gol(atk_atacante, def_defensor):
    """
    Simula uma jogada de ataque. 
    Retorna True (Gol) ou False (Defesa/Para fora).
    """
    fator_sorte = random.randint(1, 20)
    forca_chute = atk_atacante + fator_sorte
    forca_zaga = def_defensor + 10 # 10 é a dificuldade base do goleiro
    
    if fator_sorte == 20:
        return True, fator_sorte # Golaço indefensável
    elif fator_sorte == 1:
        return False, fator_sorte # Isolou a bola
    elif forca_chute > forca_zaga:
        return True, fator_sorte
    else:
        return False, fator_sorte

def narrar_lance(nome_atacante, gol, sorte):
    if sorte == 20:
        return f"⚽ GOLAÇO DE PLACA! {nome_atacante} acerta no ângulo! A torcida vai à loucura!"
    elif sorte == 1:
        return f"❌ QUE BIZARRO! {nome_atacante} tropeça na bola e chuta para a lateral."
    elif gol:
        return f"⚽ GOOOOOL! Lindo chute de {nome_atacante} que balança as redes!"
    else:
        return f"🧤 Defesa espetacular! A zaga bloqueia o ataque de {nome_atacante}."