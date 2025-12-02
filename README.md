# Máquina Enigma Avançada

Este projeto é uma releitura moderna e digital da clássica Máquina Enigma, expandindo seus conceitos com criptografia Base32, funções de deslocamento não-lineares e capacidades de hashing.

## Funcionalidades

### Métodos de Criptografia e Hashing
O sistema oferece múltiplos modos de operação selecionáveis:

1.  **Enigma (Base32)**:
    *   Cifra polialfabética reversível baseada em 10 rotores virtuais.
    *   Entrada de texto é convertida para Base32 (A-Z, 2-7) antes da cifra.
    *   Suporta "Alfabeto Galáctico" para ofuscação visual.
    *   **Equações de Deslocamento**:
        *   *Super ENIGMA*: Combinação complexa de somas, produtos e potências.
        *   *Soma Simples/Quadrática/Cúbica*: Operações matemáticas básicas sobre o vetor de rotores.
        *   *Produto*: Multiplicação dos valores dos rotores.
    
2.  **Base64**:
    *   Codificação padrão Base64 para interoperabilidade.

3.  **SHA-1**:
    *   Gera um hash de 160 bits (40 hex chars) do texto de entrada.
    *   *Nota: Unidirecional (não pode ser descriptografado).*

4.  **SHA-256**:
    *   Gera um hash de 256 bits (64 hex chars). Padrão moderno de segurança.
    *   *Nota: Unidirecional.*

5.  **Cascata (Base32 > SHA1 > SHA256)**:
    *   Pipeline de processamento: Converte Texto para Base32 -> Hash SHA-1 -> Hash SHA-256.
    *   Útil para assinaturas digitais ou provas de trabalho.

### Interface
*   **Controle de Rotores**: 10 rotores independentes com ajuste manual (0-25).
*   **Rotação Automática**: Simula o mecanismo de odômetro da Enigma original, mas com uma torção dinâmica:
    *   *Internamente*: Os rotores avançam baseados no resultado da equação matemática escolhida (fator de passo variável).
    *   *Visualmente*: A interface permanece na posição inicial escolhida pelo usuário, facilitando a reutilização da chave.
*   **Visual Dark Mode**: Interface moderna e responsiva.

## Como Usar

1.  Clone o repositório ou baixe os arquivos.
2.  Abra o arquivo `index.html` em qualquer navegador moderno.
3.  Selecione o método desejado (Enigma, SHA, etc).
4.  Digite o texto no campo "Texto de Entrada".
5.  Clique em "Processar/Criptografar".
6.  Para reverter (apenas Enigma e Base64), clique em "Descriptografar" com o texto cifrado no campo de entrada.

## Detalhes Técnicos

### Estrutura de Arquivos
*   `index.html`: Estrutura da aplicação.
*   `css/style.css`: Estilização (Dark Theme).
*   `js/script.js`: Lógica de criptografia, hashing e controle de UI.

### Lógica "Super Enigma"
A equação "Super Enigma" calcula o deslocamento dos rotores combinando múltiplas operações para maximizar a entropia do deslocamento a cada passo.

```javascript
Shift = ( (Sum * Prod) + (SumSq + SumCu) ) % Modulo
```

Isso garante que pequenos padrões nos rotores não resultem em padrões lineares no texto cifrado.

## Documentação Formal
A documentação técnica completa e a análise matemática do sistema encontram-se disponíveis no arquivo [`docs/enigma.tex`](docs/enigma.tex), formatado para compilação em LaTeX.

## Créditos
Desenvolvido como uma ferramenta educacional e experimental de criptografia.
Baseado em conceitos históricos da Máquina Enigma da Segunda Guerra Mundial.
