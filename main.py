# =============================================================================
# ARQUIVO: main.py
# OBJETIVO: Menu interativo separando o Administrador (FifaKaz) do Usuário (Clube).
# =============================================================================
from mercado.clube import criar_clube, comprar_jogador, exibir_time, gerar_time_adversario
from mercado.supabase_db import obter_jogadores_loja, cadastrar_jogador_fifakaz
from funcoes import saudar_usuario
import funcoes


def iniciar_sistema():
    print("=" * 50)
    print(f"{'🎮 BEM-VINDO AO FIFAKAZ 2026':^50}")
    print("=" * 50)

    while True:
        print("\n[1] MODO TREINADOR (Criar time e comprar jogadores)")
        print("[2] MODO FIFAKAZ (Cadastrar novas cartas no mercado)")
        print("[3] SAIR")

        opcao = input("Escolha seu modo de jogo: ").strip()

        if opcao == "1":
            meu_time = criar_clube()

            while True:
                vitrine = obter_jogadores_loja()
                print("\n" + "-" * 40)
                print(
                    f"🛒 MERCADO DA BOLA | Seu Saldo: {meu_time['kaz_coins']} Kaz Coins")
                print("-" * 40)

                for i, jog in enumerate(vitrine):
                    print(
                        f"[{i}] {jog['nome']:<12} | {jog['posicao']:<10} | 🪙 {jog['valor']} KC")

                print("[ S ] Sair do mercado e ir para a partida")
                escolha = input(
                    "Digite o número do jogador para comprar: ").strip().upper()

                if escolha == "S":
                    break
                elif escolha.isdigit() and 0 <= int(escolha) < len(vitrine):
                    comprar_jogador(meu_time, vitrine[int(escolha)])
                else:
                    print("Opção inválida.")

            # Hora da Partida: Exibir os times
            time_rival = gerar_time_adversario(vitrine)
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


if __name__ == "__main__":
    iniciar_sistema()
