
# 📜 MagoBot

Conheça o **MagoBot**, um bot de WhatsApp **100% em Python** criado com o propósito de ser **Fácil** e **Livre Para Todos**! Feito para quem quer controle total e fácil customização. Se você já programou ou quer se aprofundar no mundo dos bots, o MagoBot é a ferramenta ideal. 🚀

Com o código totalmente aberto, você tem infinitas possibilidades de funcionalidades e melhorias, esta versão ainda está na sua base e em breve espero acrescentar
mais recursos nativos do bot.

Feito completamente em Python, é **MUITO FÁCIL** de configurá-lo e colocá-lo para funcionar, basta seguir os passo a seguir e ser feliz!

---

## ✨ Principais Funcionalidades

- **Respostas Automáticas**: Configure o bot para enviar respostas específicas com base em comandos recebidos.
- **Envio de Mídias**: Mande fotos, vídeos e arquivos com apenas um comando.
- **Lógica Personalizada**: Monte uma estrutura de comandos facilmente usando `match-case` do Python.
- **Atualização em Tempo Real**: O bot verifica constantemente a presença de mensagens novas para não perder nada.
- **Código Aberto e Personalizável**: Todo o código está bem documentado para que você possa estender o bot dos "pès à cabeça".

---

## 🚀 Começando com o MagoBot

Para começar, você precisará de:

- **Python 3.10+** (para usar a estrutura `match-case`)
- **Bibliotecas** especificadas em `requirements.txt`

Siga as instruções abaixo para configurar o MagoBot no seu ambiente.

### 1. Clone o Repositório

```terminal
git clone https://github.com/mago-programador/MagoBot.git
cd MagoBot
```

### 2. Instale as Dependências

Instale as dependências necessárias com o comando:

```terminal
pip install -r requirements.txt
```

### 3. Configure o Bot

Personalize o comportamento do bot editando o método `config` na classe `MagoBotClient`.

**Exemplo**:

```python
def config(self, mensagem):
    match mensagem:
        case "Oi": --> Comando recebido
            self.send("Olá! Como posso ajudar?") --> Mensagem enviada
        case "Ajuda": --> Comando recebido
            self.send("Aqui estão os comandos que você pode usar...") --> Mensagem enviada
```

### 4. Execute o Bot

Inicie o MagoBot com o seguinte comando:

```terminal
python magobot.py
```

---

## 🧙‍♂️ Como Funciona o MagoBot?

O MagoBot usa uma estrutura de verificação de mensagens recebidas e envia respostas automáticas conforme sua configuração. O método `main()` garante que o bot fique sempre em execução, escutando mensagens novas, e o método `config()` permite configurar comandos e respostas de maneira rápida e intuitiva.

---

## 💡 Exemplos de Uso

Aqui estão algumas maneiras criativas de usar o MagoBot:

- **Atendimento Automatizado**: Crie respostas automáticas para perguntas frequentes.
- **Gestão de Tarefas**: Use o bot para receber lembretes ou gerenciar listas de tarefas utilizando a biblioteca **schedule**, que será adicionada nativamente em
próximas versões do bot.
- **Integração com APIs**: Conecte o MagoBot a outras APIs para criar um assistente poderoso que busca informações externas.

---
## 💬 Participe da nossa comunidade!

- **WhatsApp**: [Clique aqui para entrar no grupo](https://chat.whatsapp.com/EXxoqugdVTQ3zhQaTmXW6D)
- **TikTok**: [Siga-me no TikTok](https://www.tiktok.com/@mago.programador)

---

## ⚙️ Tecnologias Utilizadas

- **Python** - O coração do MagoBot.
- **WhatsApp Web** - Interface para comunicação.
- **Biblioteca Selenium** - O "tradutor", o Selenium que dita ao navegador o que será feito e toma as decisões com base no que é devolvido pelo chrome.

---

## 🎉 Contribuindo com o Projeto

Achou que o MagoBot poderia ser ainda mais poderoso? Quer sugerir melhorias? Sinta-se à vontade para contribuir! Basta abrir uma *issue* ou enviar um *pull request*. Todo tipo de ajuda é bem-vinda!

---

## 📜 Licença

Este projeto é licenciado sob a **Licença Apache 2.0**.

---

## 📞 Contato

Dúvidas ou sugestões? Entre em contato em xfr3p@protonmail.com.