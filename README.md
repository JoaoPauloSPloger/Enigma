# Enigma – Browser-Based Enigma Machine (Proof of Concept)

A lightweight, educational proof of concept of the historic Enigma cipher machine, implemented for the browser using simple code. The repository is organized by versions to make it easy to try a stable build, explore the newest ideas, or review older iterations.

- Repository: [JoaoPauloSPloger/Enigma](https://github.com/JoaoPauloSPloger/Enigma)
- License: [MIT](./LICENSE)
- Main language: HTML
- Versions:
  - Stable: [STABLE](./STABLE/)
  - Latest (work in progress): [NEWEST](./NEWEST/)
  - Older iterations: [OLD_VER](./OLD_VER/)

> Nota: descrição original do projeto (PT-BR): “Este é um repositório cujo intuito é construir uma prova de conceito. Uma máquina de enigma feita usando código simples para funcionamento.”

---

## Table of Contents

- Overview
- Features and Highlights
- Project Structure
- Getting Started
- How to Use
- Educational Notes (How Enigma Works)
- Roadmap
- Contributing
- License
- Português (versão em PT-BR)

---

## Overview

This project is an educational rendition of the Enigma machine designed to:
- Demonstrate classical rotor-based cryptography concepts in a browser.
- Keep the code approachable for learning and experimentation.
- Separate versions so you can choose stability or explore the latest changes.

Because Enigma is symmetric, the same configuration used to encrypt text will also decrypt it. This project focuses on clarity and simplicity over performance or historical completeness.

---

## Features and Highlights

- Web-based proof of concept
  - Runs locally in your browser (no backend required).
  - Zero external build tools by design.
- Versioned development flow
  - [STABLE](./STABLE/): Recommended for first-time users.
  - [NEWEST](./NEWEST/): Latest experiments and improvements.
  - [OLD_VER](./OLD_VER/): Historic versions for reference/learning.
- Educational emphasis
  - Great for learning about rotor ciphers, reflectors, and plugboards.
  - Clear separation of concerns to support tinkering.
- Lightweight and permissive
  - MIT-licensed for maximum reuse.
  - Minimal dependencies (HTML-first approach).

Note: Specific UI options (e.g., rotor selection, ring settings, plugboard pairs) and advanced behaviors may vary by version. Use the STABLE folder for the most consistent experience.

---

## Project Structure

- `/STABLE` – A stable, recommended snapshot to use and demo.
- `/NEWEST` – The latest iteration; may change frequently.
- `/OLD_VER` – Previous versions to compare and study.
- `/LICENSE` – MIT License file.
- `/README.md` – You’re here.

---

## Getting Started

Prerequisites:
- A modern web browser (Chrome, Firefox, Edge, Safari).

Steps:
1. Clone or download this repository.
2. Open the main HTML file located inside the [STABLE](./STABLE/) folder in your browser.
3. Optionally, explore [NEWEST](./NEWEST/) to see the latest updates or [OLD_VER](./OLD_VER/) to review older iterations.

Because this is a static, browser-based project, no build or server is required for basic usage.

---

## How to Use

Typical Enigma usage involves:
1. Choosing a machine configuration (e.g., rotor order, initial rotor positions).
2. Setting ring settings (Ringstellung) and plugboard pairs (Steckerbrett) if available in the UI.
3. Typing or pasting your plaintext; the machine outputs ciphertext.
4. Using the exact same settings to decrypt.

Tip: Keep a record of your configuration so you can reproduce the same settings to decrypt messages.

---

## Educational Notes (How Enigma Works)

At a high level:
- Rotors: Each keystroke advances the rotor(s) and maps letters through internal wiring.
- Ring settings: Shift the internal wiring relative to the rotor positions.
- Plugboard: Swaps pairs of letters before and after the rotor mappings.
- Reflector: Sends the signal back through the rotors, making encryption symmetric (encryption and decryption share the same process with identical settings).

This project is designed to make those ideas tangible and interactive in the browser.

---

## Roadmap

Potential improvements and exploration areas:
- Clearer controls for rotor order, ring settings, and plugboard mapping.
- Persisting configurations in the browser.
- Visualizing signal flow through rotors.
- Additional historical rotor/reflector sets for educational comparison.
- Accessibility and mobile-friendly refinements.

Check the [NEWEST](./NEWEST/) folder for the latest experimental changes.

---

## Contributing

Contributions are welcome!
- Try the [STABLE](./STABLE/) version first for a baseline.
- Explore [NEWEST](./NEWEST/) if you want to work on recent ideas.
- Open issues and pull requests with clear descriptions and reproduction steps where helpful.

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Português (PT-BR)

### Visão Geral

Uma prova de conceito da máquina Enigma para o navegador, com foco educacional e código simples. O repositório é dividido por versões para facilitar o teste de uma versão estável, explorar novidades ou consultar iterações antigas.

- Recomendado: [STABLE](./STABLE/)
- Últimas mudanças: [NEWEST](./NEWEST/)
- Versões antigas: [OLD_VER](./OLD_VER/)

### Destaques

- Funciona direto no navegador, sem backend.
- Sem ferramentas de build obrigatórias.
- Estrutura por versões (estável, mais recente, antigo).
- Foco educacional em cifragem por rotores e plugboard.
- Licença MIT e dependências mínimas.

### Como Começar

1. Baixe ou clone o repositório.
2. Abra o arquivo HTML principal dentro de [STABLE](./STABLE/) no seu navegador.
3. Explore [NEWEST](./NEWEST/) para novidades ou [OLD_VER](./OLD_VER/) para versões anteriores.

### Como Usar

- Configure a máquina (ordem de rotores, posições iniciais).
- Ajuste Ringstellung e pares do plugboard, se disponíveis.
- Digite o texto; o resultado cifrado é gerado.
- Para decifrar, utilize exatamente as mesmas configurações.

### Licença

Licenciado sob [MIT](./LICENSE).
