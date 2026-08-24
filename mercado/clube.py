# =============================================================================
# ARQUIVO: mercado/clube.py
# OBJETIVO: Gerenciar a carteira e o elenco do usuário.
# =============================================================================
import random


def criar_clube():
    """Inicializa o clube com a verba inicial concedida pela diretoria."""
    nome = input("Digite o nome do seu Clube: ")
    clube = {
        "nome": nome,
        "kaz_coins": 1500,  # Orçamento inicial para compras
        "elenco": []       # Lista que guardará os dicionários dos jogadores comprados
    }
    return clube


def comprar_jogador(clube, jogador):
    """Processa a compra validando o saldo e retorna o status da transação."""
    if clube["kaz_coins"] >= jogador["valor"]:
        clube["kaz_coins"] -= jogador["valor"]
        clube["elenco"].append(jogador)
        print(
            f"🎉 CONTRATADO! {jogador['nome']} agora veste a camisa do {clube['nome']}!")
        print(f"💰 Saldo Restante: {clube['kaz_coins']} Kaz Coins.")
        return True  # A compra foi um sucesso!
    else:
        print(
            f"❌ SALDO INSUFICIENTE! Você precisa de {jogador['valor']} Kaz Coins.")
        return False  # A compra falhou.


def exibir_time(nome_time, lista_jogadores):
    """Formata e imprime a escalação de um time."""
    print("\n" + "=" * 40)
    print(f"📋 ESCALAÇÃO: {nome_time.upper()}")
    print("=" * 40)
    if not lista_jogadores:
        print("Time sem jogadores registrados.")
    else:
        for jog in lista_jogadores:
            print(
                f"- {jog['nome']} ({jog['posicao']}) | ATK: {jog['atk']} | DEF: {jog['def']}")
    print("=" * 40)


def gerar_time_adversario(todos_jogadores_db):
    """Cria um time aleatório para simular um adversário."""
    # Se houver menos de 3 jogadores no banco, pega todos. Senão, sorteia 3.
    qtd = min(3, len(todos_jogadores_db))
    time_sorteado = random.sample(todos_jogadores_db, qtd)
    return time_sorteado
