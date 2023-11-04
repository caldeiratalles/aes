import os
from aes_cipher import encrypt_file, decrypt_file, load_key, generate_and_save_key


def main():
    while True:
        print("Menu:")
        print("1. Criptografar arquivo")
        print("2. Descriptografar arquivo")
        print("3. Sair")

        choice = input("Escolha a opção: ")
        key = generate_and_save_key()

        if choice == '1':
            input_file = input("Digite o nome do arquivo de entrada: ")
            output_file = input("Digite o nome do arquivo de saída cifrado: ")
            encrypt_file(input_file, output_file, key)
            print(f"Arquivo criptografado com sucesso como '{output_file}'.")
            print(f"Chave utilizada '{key}'.")

        elif choice == '2':
            input_file = input("Digite o nome do arquivo de entrada cifrado: ")
            output_file = input("Digite o nome do arquivo de saída descriptografado: ")
            decrypt_file(input_file, output_file, load_key())
            print(f"Arquivo descriptografado com sucesso como '{output_file}'.")

        elif choice == '3':
            break


if __name__ == '__main__':
    main()
