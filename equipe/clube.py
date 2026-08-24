# =============================================================================
# ARQUIVO: time/clube.py
# OBJETIVO: Criar o time do jogador, calcular atributos e gerenciar o placar.
# =============================================================================

def criar_clube():
    print("-" * 40)
    print(f"{'FUNDAÇÃO DO SEU CLUBE':^40}")
    print("-" * 40)
    
    nome = input("Digite o nome do seu time: ")
    atk = int(input("Nota de Ataque do time (0-20): "))
    def_val = int(input("Nota de Defesa do time (0-20): "))
    
    clube = {
        "nome": nome,
        "ATK_BASE": atk,
        "DEF_BASE": def_val,
        "GOLS": 0,
        "jogador_estrela": None
    }
    return clube

def contratar_jogador(clube, jogador):
    clube["jogador_estrela"] = jogador
    print(f"\n✍️ CONTRATAÇÃO FECHADA! {jogador['nome']} ({jogador['posicao']}) chegou ao {clube['nome']}!")

def calcular_forca_total(clube):
    """Soma a base do clube com o bônus do jogador estrela."""
    if not clube["jogador_estrela"]:
        return clube["ATK_BASE"], clube["DEF_BASE"]
        
    craque = clube["jogador_estrela"]
    atk_total = clube["ATK_BASE"] + craque["bonus_atk"]
    def_total = clube["DEF_BASE"] + craque["bonus_def"]
    
    return atk_total, def_total