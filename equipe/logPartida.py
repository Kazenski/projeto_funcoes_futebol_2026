# =============================================================================
# ARQUIVO: time/logPartida.py
# OBJETIVO: Gravar os lances da partida e exportar a súmula final.
# =============================================================================

sumula_partida = []

def registrar_lance(detalhe):
    sumula_partida.append(detalhe)

def exportar_sumula_txt(time_casa, time_fora, gols_casa, gols_fora):
    with open("sumula_partida.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"{'SÚMULA OFICIAL DA PARTIDA':^50}\n")
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"PLACAR FINAL: {time_casa} {gols_casa} x {gols_fora} {time_fora}\n\n")
        
        arquivo.write("LANCES DA PARTIDA:\n")
        for i, lance in enumerate(sumula_partida, 1):
            arquivo.write(f"{i}º Lance: {lance}\n")
            
    print("\n📁 Súmula da partida salva em 'sumula_partida.txt'!")