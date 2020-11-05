# **Py-Snake**

Py-snake é uma reprodução simples do jogo Snake (1997). Através de Py-Snake é possível desfrutar desse notálgico jogo no seu computador de forma simples e fácil.

<p align="center">
  <img src="https://i.ibb.co/dKTrSKG/Lorem.png" style="border-radius: 15px; max-width: 600px; width: 100%">
</p><br>

## **Recursos**

- Criação de jogo
- Armazenamento de maior score
- Tela de restart

## **Principais tecnologias**

- Python v3.8
- pygame v2.0

## **Instalação local**

Primeiro, é necessário instalar as dependências do game. Como ele foi escrito em python, é necessário tê-lo instalado e também algum gerenciador de pacotes (preferencialmente o PIP). Depois disso, basta instalar oos módulos python utilizados do projeto, segue o exemplo utilizando o PIP. Primeiramente, as boas práticas dizem que é necessário criar um ambiente virtual python, para isso basta executar as seguintes linhas:

```bash
$ python -m venv venv
$ venv/bin/activate # ou venv/scripts/activate no windows

(venv) ~$ python -m pip install --upgrade pip
(venv) ~$ pip install -r requirements.txt
(venv) -$ python main.py
```

Depois dessas linhas de código o jogo deve ser inicializado.

## **Jogabilidade**

O controle da cobrinha é utiliza o padrão WSDA ou seja:

- W - cima
- S - baixo
- D - direita
- A - esquerda

Espero que o jogador se divirta com esse projeto!
