# 🤖 SemFundo Bot

Um bot de Discord simples e eficiente para processar imagens, com funcionalidades como remover o fundo e converter para preto e branco, diretamente do chat.


### 📋 Pré-requisitos

Certifique-se de ter o Python 3.8+ instalado em sua máquina.

### 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/diegoolinek/semfundo-bot.git
cd semfundo-bot
pip install -r requirements.txt
```

### ⚙️ Configurando localmente:

Crie um arquivo .env na pasta raíz do projeto e adicione o seu token do discord da seguinte maneira:

```bash
DISCORD_TOKEN=seu_discord_token
```

### 📂 Estrutura do Projeto

```bash
semfundo-bot/
├── main.py            # Arquivo principal - para inicializar o bot
├── commands.py        # Comandos do bot
├── bot_config.py      # Configurações
├── requirements.txt   # Dependências
├── .env               # Variáveis locais
└── .gitignore         # Arquivos ignorados pelo Git
```

### 🛠️ Tecnologias

- Python
- discord.py (biblioteca)
- rembg (biblioteca)


### 📄 Licença
Este projeto está sob a licença MIT
