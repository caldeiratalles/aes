# Readme - Programa de Criptografia e Descriptografia AES
TALLES MARCELO 20/0060295


Este programa permite criptografar e descriptografar arquivos usando o algoritmo de criptografia AES (Advanced Encryption Standard). Ele oferece uma interface de linha de comando simples para realizar essas operações.

## Requisitos

Antes de usar o programa, certifique-se de que você tenha o Python instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

## Instalação

1. Clone ou faça o download deste repositório para o seu computador.

2. Navegue até a pasta onde o repositório foi clonado ou descompactado.

3. Execute o programa com o seguinte comando:

   ```bash
   python aes_program.py
   ```

## Uso

O programa apresenta um menu simples com as seguintes opções:

1. Criptografar arquivo
2. Descriptografar arquivo
3. Sair

### 1. Criptografar arquivo

Escolha a opção "1" no menu. Você será solicitado a fornecer as seguintes informações:

- Nome do arquivo de entrada: Digite o caminho para o arquivo que você deseja criptografar.

- Nome do arquivo de saída cifrado: Especifique o nome do arquivo de saída onde os dados criptografados serão salvos.

- Número de rodadas (10 por padrão): O programa usa 10 rodadas de criptografia por padrão, mas você pode especificar um número diferente, se desejar.

O programa gerará uma chave aleatória e usará o AES para criptografar o arquivo de entrada. O arquivo criptografado será salvo com o nome especificado, e a chave usada será exibida na tela.

### 2. Descriptografar arquivo

Escolha a opção "2" no menu. Você será solicitado a fornecer as seguintes informações:

- Nome do arquivo de entrada cifrado: Digite o caminho para o arquivo que você deseja descriptografar.

- Nome do arquivo de saída descriptografado: Especifique o nome do arquivo de saída onde os dados descriptografados serão salvos.

- Número de rodadas (10 por padrão): O programa usa 10 rodadas de descriptografia por padrão, mas você pode especificar um número diferente, se desejar.

O programa usará a chave gerada na operação de criptografia para descriptografar o arquivo de entrada. O arquivo descriptografado será salvo com o nome especificado.

### 3. Sair

Escolha a opção "3" no menu para encerrar o programa.

## Importante

- Certifique-se de manter a chave de criptografia segura, pois ela é necessária para descriptografar os arquivos.

- O programa usa o modo de operação CTR (Counter Mode) para criptografia. Certifique-se de entender como esse modo funciona para garantir a segurança adequada.

- Este programa oferece uma interface de linha de comando simples e pode ser estendido ou integrado em outros projetos conforme necessário.

