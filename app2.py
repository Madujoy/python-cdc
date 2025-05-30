#python
#Importa o modulo random para seleçao aleatoria de palavras
import random

#Lista de palavras para o jogo (banco de palavras)
palavras = ['maça', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    """
    Funçao principal que gerencia toda a logica o jogo da forca:
    - Seleçao da palavra
    - Controle e tentativas
    - Validaçao das letras
    - Exibiçao do estado do jogo
    """

    # Seleciona aleatorimente uma palavra da lista
    palavra_secreta = random.choice(palavras)

    # Lista para armaenar a letras decobertas (inicialmente todas ocultas)
    letras_corretas = ['_'] * len(palavra_secreta)

    # Lista para registrar letras incorretas digitadas
    letras_erradas = []

    # Define o numero maximo de tehntativas permitidas
    tentativas_restantes = 6

    # Mensagem inicial do jogo
    print("\Bem-vindo ao jogo da forca!")
    print(f"Voce tem {tentativas_restantes} tentativa pra adivinhar a palavra.\n")

    # Loop principal do jogo: continua enquanto houver tentativasve letras faltando
    while tentativas_restantes > 0 and '_' in letras_corretas:
        # Exibe o progresso atual do jogador
        print(' '.join(letras_corretas))

        # Solicita e procassa a tentativa do jogador
        tentativa = input("\nDigite uma letra: ").lower()  # Converte para minuscula

        # Verifica se a letra esta na palavra secreta
        if tentativa in palavra_secreta:
            # Atualiza as letras corretas reveladas
            for indice, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_corretas[indice] = tentativa

        else:
            # Trata letra incorreta
            letras_erradas.append(tentativa)  # Registra a tentativa errada
            tentativas_restantes -= 1         # Reduz o numero de tentativas

            # Feedback imediato para o jogador
            print(f"\nLetra incorreta! Tentativas restantes:{tentativas_restantes}")
            if letras_erradas: # So mostra se houver letras erradas
                print(f"Letra erradas:{', '.join(letras_erradas)}")

        # Verificaçao final do resultado do jogo
        if '_' not in letras_corretas:
            # Vitoria: todas as letras foram reveladas
            print(f"\Parabens! Voce ganhou! A palavra era: {palavra_secreta}")
        else:
            # Derrota: acabaram as tentativas
            print(f"\Voce perdeu! A palavra era: {palavra_secreta}")
        
# Inicia o jogo quando o script e executado
if __name__ == "__main__":
    jogo_da_forca()