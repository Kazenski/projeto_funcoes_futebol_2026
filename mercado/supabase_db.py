# =============================================================================
# ARQUIVO: mercado/supabase_db.py
# OBJETIVO: Gerenciar a vitrine de jogadores e o cadastro do sistema FifaKaz.
# =============================================================================
from conexao import conectar_supabase
import random


def obter_jogadores_loja():
    """Busca todos os jogadores disponíveis para compra."""
    db = conectar_supabase()
    if not db:
        return []
    return db.table("jogadores_fifakaz").select("*").execute().data


def cadastrar_jogador_fifakaz(nome, posicao, valor, atk, def_val):
    """Função de Administrador para popular o mercado."""
    db = conectar_supabase()
    if db:
        dados = {"nome": nome, "posicao": posicao,
                 "valor": valor, "atk": atk, "def": def_val}
        db.table("jogadores_fifakaz").insert(dados).execute()
        print(
            f"✅ BOMBOU NO MERCADO! {nome} adicionado ao FifaKaz por {valor} Kaz Coins!")


def popular_banco_aleatorio():
    """Gera 50 jogadores com atributos aleatórios e cadastra no banco."""
    db = conectar_supabase()
    if not db:
        return

    nomes = ["Kaz", "Pelé", "Maradona", "Zico", "Messi", "CR7",
             "Neymar", "Mbappé", "Haaland", "Vini Jr", "Ronaldinho", "Ronaldo"]
    sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues",
                  "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Fenômeno"]
    posicoes = ["Atacante", "Meio-Campo", "Zagueiro", "Goleiro", "Lateral"]

    print("\n" + "=" * 40)
    print("⏳ GERANDO 50 CRAQUES NO LABORATÓRIO FIFAKAZ...")
    print("=" * 40)

    # Laço for que repete exatamente 50 vezes
    for _ in range(50):
        # Sorteia as informações
        nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        pos = random.choice(posicoes)
        valor = random.randint(100, 1000)
        atk = random.randint(10, 99)
        def_val = random.randint(10, 99)

        # Insere direto no banco
        dados = {"nome": nome_completo, "posicao": pos,
                 "valor": valor, "atk": atk, "def": def_val}
        db.table("jogadores_fifakaz").insert(dados).execute()

    print("✅ Sucesso! 50 novos jogadores foram lançados no mercado da bola!")
