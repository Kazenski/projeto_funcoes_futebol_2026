# =============================================================================
# ARQUIVO: main.py
# OBJETIVO: Menu interativo separando o Administrador (FifaKaz) do Usuário (Clube).
# =============================================================================
from mercado.clube import criar_clube, comprar_jogador, exibir_time, gerar_time_adversario
from mercado.supabase_db import obter_jogadores_loja, cadastrar_jogador_fifakaz, popular_banco_aleatorio
from funcoes import saudar_usuario


def iniciar_sistema():
    print("=" * 50)
    print(f"{'🎮 BEM-VINDO AO FIFAKAZ 2026':^50}")
    print("=" * 50)

    while True:
        print("\n[1] MODO TREINADOR (Criar time e comprar jogadores)")
        print("[2] MODO FIFAKAZ (Cadastrar novas cartas no mercado)")
        print("[3] SAIR")
        print("[4] ⚙️ ADMIN: Gerar 50 Jogadores Aleatórios no Banco")

        opcao = input("Escolha seu modo de jogo: ").strip()

        if opcao == "1":
            meu_time = criar_clube()

            # Puxamos os jogadores do banco APENAS UMA VEZ antes de entrar no mercado
            vitrine = obter_jogadores_loja()

            while True:
                print("\n" + "-" * 50)
                print(
                    f"🛒 MERCADO DA BOLA | Seu Saldo: {meu_time['kaz_coins']} Kaz Coins")
                print("-" * 50)

                # Se a vitrine ficar vazia, avisamos o usuário
                if not vitrine:
                    print("O mercado está vazio! Todos os jogadores foram comprados.")
                    break

                for i, jog in enumerate(vitrine):
                    print(
                        f"[{i:02d}] {jog['nome']:<18} | {jog['posicao']:<10} | 🪙 {jog['valor']}  KC")

                print("\n[ S ] Sair do mercado e ir para a partida")
                escolha = input(
                    "Digite o número do jogador para comprar: ").strip().upper()

                if escolha == "S":
                    break
                elif escolha.isdigit() and 0 <= int(escolha) < len(vitrine):
                    indice = int(escolha)

                    # Tentamos comprar o jogador
                    sucesso = comprar_jogador(meu_time, vitrine[indice])

                    # Se comprou com sucesso, REMOVEMOS da lista da vitrine usando .pop()
                    if sucesso:
                        vitrine.pop(indice)
                else:
                    print("Opção inválida.")

            # Hora da Partida: Exibir os times
            # O rival sorteia do banco original
            time_rival = gerar_time_adversario(obter_jogadores_loja())
            exibir_time(meu_time['nome'], meu_time['elenco'])
            exibir_time("BOMBA PATCH F.C. (Adversário)", time_rival)

        elif opcao == "2":
            print("\n--- 📝 CENTRAL DE CADASTRO FIFAKAZ ---")
            nome = input("Nome do Jogador: ")
            pos = input("Posição: ")
            valor = int(input("Valor em Kaz Coins: "))
            atk = int(input("Nota de Ataque: "))
            defesa = int(input("Nota de Defesa: "))
            cadastrar_jogador_fifakaz(nome, pos, valor, atk, defesa)

        elif opcao == "3":
            print("Saindo do FifaKaz... Até a próxima temporada!")
            break

        elif opcao == "4":
            # Chama a nossa nova função automática
            popular_banco_aleatorio()


if __name__ == "__main__":
    iniciar_sistema()
