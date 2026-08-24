# =============================================================================
# ARQUIVO: mercado/supabase_db.py
# OBJETIVO: Gerenciar a vitrine de jogadores e o cadastro do sistema FifaKaz.
# =============================================================================
from conexao import conectar_supabase


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
