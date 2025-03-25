from senha import gerar_senha


def main():
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

    senha = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos)
    print(f"\nSenha gerada: {senha}")

if __name__ == "__main__":
    main()