# =============================================================================
# ARQUIVO: operacoes.py (A Fábrica de Ferramentas)
# OBJETIVO: Guardar as funções que serão usadas por outros arquivos.
# =============================================================================

def saudar_usuario(nome):
    """
    Recebe um nome (parâmetro) e retorna uma mensagem de boas-vindas.
    """
    # O 'return' devolve o valor silenciosamente, ao invés de apenas
    # exibir na tela como o 'print'. Isso permite guardar o dado depois!
    return f"Olá, {nome}! Que bom ter você aqui."


def somar_valores(a, b):
    """
    Recebe dois números (parâmetros), soma-os e retorna o resultado.
    """
    resultado = a + b
    return resultado
