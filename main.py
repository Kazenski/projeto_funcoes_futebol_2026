# =============================================================================
# ARQUIVO: main.py
# OBJETIVO: Orquestrar o pré-jogo, o mercado da bola e os lances da partida.
# =============================================================================

from time.clube import criar_clube, contratar_jogador, calcular_forca_total
from time.logPartida import registrar_lance, exportar_sumula_txt
from tecnico.supabase_tecnico import obter_times_adversarios, obter_jogadores_mercado, cadastrar_novo_time
from funcoes import tentar_gol, narrar_lance
import time # Para dar pausas dramáticas

def iniciar_jogo():
    print("=" * 50)
    print(f"{'🏆 SIMULADOR DE MANAGER DE FUTEBOL':^50}")
    print("=" * 50)
    
    meu_time = criar_clube()
    
    # Mercado da Bola
    print("\n🌍 Buscando jogadores no mercado (Supabase)...")
    mercado = obter_jogadores_mercado()
    if mercado:
        print("Quem você quer contratar como Estrela do time?")
        for i, jog in enumerate(mercado):
            print(f"[{i}] {jog['nome']} (+{jog['bonus_atk']} ATK, +{jog['bonus_def']} DEF)")
        escolha_jog = int(input("Escolha o número: "))
        contratar_jogador(meu_time, mercado[escolha_jog])
    
    # Escolha do Adversário
    print("\n🆚 Buscando adversários na Liga...")
    adversarios = obter_times_adversarios()
    for i, adv in enumerate(adversarios):
        print(f"[{i}] {adv['nome']} (ATK: {adv['atk']} | DEF: {adv['def']})")
    escolha_adv = int(input("Quem você quer enfrentar? "))
    rival = adversarios[escolha_adv]
    rival["GOLS"] = 0 # Inicializa placar do rival
    
    # APITO INICIAL
    atk_real, def_real = calcular_forca_total(meu_time)
    print("\n" + "=" * 50)
    print(f"APITA O ÁRBITRO! COMEÇA O JOGO: {meu_time['nome']} x {rival['nome']}")
    print("=" * 50)
    
    # Loop da Partida (5 lances de perigo)
    for lance in range(1, 6):
        print(f"\n⏱️ {lance * 18} Minutos de jogo...")
        time.sleep(1) # Pausa dramática para os alunos verem
        
        # Turno de Ataque do Usuário
        gol_meu, sorte_minha = tentar_gol(atk_real, rival['def'])
        narrativa_minha = narrar_lance(meu_time['nome'], gol_meu, sorte_minha)
        print(narrativa_minha)
        registrar_lance(narrativa_minha)
        if gol_meu: meu_time["GOLS"] += 1
        
        time.sleep(1)
        
        # Turno de Ataque do Computador
        gol_rival, sorte_rival = tentar_gol(rival['atk'], def_real)
        narrativa_rival = narrar_lance(rival['nome'], gol_rival, sorte_rival)
        print(narrativa_rival)
        registrar_lance(narrativa_rival)
        if gol_rival: rival["GOLS"] += 1
        
        print(f"📊 PLACAR: {meu_time['nome']} {meu_time['GOLS']} x {rival['GOLS']} {rival['nome']}")
        input("Pressione ENTER para o próximo lance...")

    # FIM DE JOGO
    print("\n" + "=" * 50)
    print("FIM DE PAPO! O ÁRBITRO ENCERRA A PARTIDA!")
    if meu_time["GOLS"] > rival["GOLS"]:
        print("🏆 GRANDE VITÓRIA DO SEU TIME!")
    elif meu_time["GOLS"] < rival["GOLS"]:
        print("💔 DERROTA AMARGA...")
    else:
        print("⚖️ EMPATE SUADO!")
        
    exportar_sumula_txt(meu_time['nome'], rival['nome'], meu_time['GOLS'], rival['GOLS'])

if __name__ == "__main__":
    iniciar_jogo()