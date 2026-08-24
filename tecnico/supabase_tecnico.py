# =============================================================================
# ARQUIVO: tecnico/supabase_tecnico.py
# OBJETIVO: Olheiro do time (Busca adversários e possíveis contratações no banco).
# =============================================================================
from conexao import conectar_supabase

def obter_times_adversarios():
    db = conectar_supabase()
    if not db: return []
    return db.table("times_adversarios").select("*").execute().data

def obter_jogadores_mercado():
    db = conectar_supabase()
    if not db: return []
    return db.table("jogadores").select("*").execute().data

def cadastrar_novo_time(nome, atk, def_val):
    db = conectar_supabase()
    if db:
        dados = {"nome": nome, "atk": atk, "def": def_val}
        db.table("times_adversarios").insert(dados).execute()
        print(f"✅ Time '{nome}' registrado na liga com sucesso!")