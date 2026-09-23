# 🗺️ Calculadora Cartográfica

Uma aplicação desenvolvida em **Python** para auxiliar em cálculos básicos relacionados à **Cartografia**, utilizando uma interface gráfica construída com **CustomTkinter**.

O projeto foi desenvolvido como uma iniciativa de estudo e prática, tendo como referência os conteúdos trabalhados na **cadeia de Cartografia Básica da Universidade Estadual do Ceará (UECE)**.

> **Observação:** este é um projeto independente e acadêmico/pessoal, desenvolvido com finalidade educacional. Não se trata de um software oficial da UECE.

---

## 📌 Sobre o projeto

A **Calculadora Cartográfica** tem como objetivo reunir, em uma única aplicação, ferramentas para realizar cálculos básicos utilizados em atividades cartográficas e topográficas.

O projeto também tem como objetivo servir como prática de:

* 🐍 Programação em Python
* 🧱 Programação Orientada a Objetos
* 🖥️ Desenvolvimento de interfaces gráficas
* 🗺️ Cartografia
* 📐 Cálculos com coordenadas
* 🧮 Implementação de fórmulas matemáticas
* 📁 Organização de projetos Python

---

## 🧭 Funcionalidades

Atualmente o projeto possui ferramentas para:

### 📍 Distância UTM

Calcula a distância entre dois pontos utilizando suas coordenadas UTM.

O usuário informa:

* Longitude/E do Ponto A
* Latitude/N do Ponto A
* Longitude/E do Ponto B
* Latitude/N do Ponto B

E a aplicação realiza o cálculo da distância entre os pontos.

---

### 👣 Cálculo de Passos

Calcula aproximadamente quantos passos são necessários para percorrer uma determinada distância.

O usuário informa:

* Tamanho do passo
* Distância em metros

A aplicação retorna a quantidade estimada de passos.

---

### 🧲 Dispersão Magnética

Ferramenta destinada ao cálculo da **dispersão magnética**, permitindo trabalhar com a variação angular da direção magnética ao longo do tempo.

O recurso busca auxiliar na compreensão e aplicação de conceitos relacionados ao **campo magnético terrestre** e às variações da direção indicada pelo norte magnético.

---

### 🧭 Rumo

Ferramenta para obtenção do rumo a partir do azimute e do quadrante correspondente.

O projeto trabalha com os quadrantes:

```text
NE → Nordeste
SE → Sudeste
SW → Sudoeste
NW → Noroeste
```

Exemplo:

```text
Azimute: 135°
Quadrante: SE

Rumo = 180° - 135°
Rumo = 45° SE
```

---

# 🖥️ Interface

A interface gráfica foi desenvolvida utilizando **CustomTkinter**, proporcionando uma aparência moderna em relação ao Tkinter tradicional.

A aplicação possui:

* Tema escuro
* Botões personalizados
* Campos de entrada
* Menus de seleção
* Mensagens de erro
* Mensagens de resultado
* Separação das ferramentas em diferentes telas

---

# 🛠️ Tecnologias utilizadas

## Python

Linguagem principal utilizada no desenvolvimento.

## CustomTkinter

Biblioteca utilizada para construção da interface gráfica.

```bash
pip install customtkinter
```

---

# 📂 Estrutura do projeto

A estrutura atual do projeto segue uma organização semelhante a:

```text
Calculadora-Cartografica/
│
├── main.py
│
├── Cartografia.py
│
├── menu_dist.py
│
├── menu_passos.py
│
├── menu_dispercao.py
│
├── menu_rumo.py
│
└── README.md
```

### `main.py`

Responsável pela tela principal da aplicação e pelo acesso às diferentes ferramentas.

### `Cartografia.py`

Contém a classe responsável pelos cálculos cartográficos.

Exemplo:

```python
class CartografiaCalculos:
    ...
```

A ideia é manter as fórmulas e cálculos separados da interface gráfica.

### `menu_dist.py`

Responsável pela interface da calculadora de distância UTM.

### `menu_passos.py`

Responsável pela interface do cálculo de passos.

### `menu_dispercao.py`

Responsável pela interface do cálculo de dispersão magnética.

### `menu_rumo.py`

Responsável pela interface do cálculo de rumo.

---

# 🧱 Arquitetura do projeto

Uma das ideias principais do projeto é separar a **interface gráfica** da **lógica matemática**.

A estrutura conceitual é:

```text
                CALCULADORA CARTOGRÁFICA
                         │
                         ▼
                ┌─────────────────┐
                │   Interface     │
                │  CustomTkinter  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Cartografia   │
                │    Calculos     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Resultado   │
                └─────────────────┘
```

Dessa forma, a interface fica responsável pela interação com o usuário, enquanto a classe `CartografiaCalculos` concentra as operações matemáticas.

---

# 🎓 Relação com a Cartografia Básica

O projeto foi desenvolvido tendo como referência os conhecimentos relacionados à **Cartografia Básica**, buscando transformar alguns dos conceitos estudados em ferramentas computacionais.

Entre os conceitos abordados pelo projeto estão:

* Coordenadas UTM
* Distância entre pontos
* Rumo
* Dispersão magnética
* Direções e quadrantes
* Relações angulares utilizadas na representação espacial
* Conceitos relacionados ao campo magnético terrestre

A proposta é utilizar a programação como uma ferramenta complementar ao aprendizado cartográfico.

---

# 🎯 Objetivos do projeto

O projeto possui dois objetivos principais.

### Objetivo acadêmico

Praticar conceitos relacionados à Cartografia Básica através da implementação de cálculos em Python.

### Objetivo computacional

Desenvolver conhecimentos em:

```text
Python
   ↓
Programação Orientada a Objetos
   ↓
Interfaces gráficas
   ↓
Organização de código
   ↓
Implementação de cálculos
   ↓
Aplicação voltada à Geografia
```

---

# 🚀 Como executar

## 1. Instale o Python

É necessário possuir uma versão recente do Python instalada.

Verifique através do terminal:

```bash
python --version
```

---

## 2. Clone o projeto

```bash
git clone https://github.com/max1337xyz/CalculadoraCartogr-fica-1.0
```

Entre na pasta:

```bash
cd Calculadora-Cartografica
```

---

## 3. Instale as dependências

```bash
pip install customtkinter
```

---

## 4. Execute o programa

```bash
python main.py
```

---

# 🔮 Próximos objetivos

O projeto ainda está em desenvolvimento e pode receber novas ferramentas cartográficas.

Algumas funcionalidades planejadas são:

* [X] Conversão de coordenadas
* [ ] Cálculo de área
* [ ] Cálculo de perímetro
* [ ] Escalas cartográficas
* [ ] Conversão entre unidades
* [ ] Declividade
* [ ] Distância geográfica
* [ ] Conversão entre azimute e rumo
* [ ] Melhorias na validação dos dados
* [ ] Histórico dos cálculos
* [ ] Exportação dos resultados
* [X] Interface mais completa
* [ ] Integração com mapas

---

# 📚 Contexto acadêmico

Este projeto foi desenvolvido como uma aplicação prática dos conhecimentos relacionados à **cadeia de Cartografia Básica da Universidade Estadual do Ceará (UECE)**.

A proposta é aproximar os conhecimentos de **Geografia e Cartografia** da área de **Programação**, utilizando Python para transformar conceitos cartográficos em ferramentas computacionais.

---

# 👨‍💻 Desenvolvimento

Projeto desenvolvido para fins de:

* Estudo
* Prática de programação
* Aplicação de conhecimentos cartográficos
* Desenvolvimento acadêmico
* Experimentação com Python e interfaces gráficas

---

# ⚠️ Observação

Os resultados fornecidos pela aplicação dependem dos dados inseridos pelo usuário e das fórmulas implementadas no projeto.

O software possui finalidade **educacional e experimental**, não devendo ser utilizado como única fonte para levantamentos cartográficos, topográficos ou trabalhos que exijam precisão profissional.

---

# 📜 Licença

Este projeto pode ser disponibilizado sob a licença que o autor escolher.

Exemplo:

```text
MIT License
```

Caso uma licença seja adicionada, consulte o arquivo `LICENSE` para conhecer as condições de utilização.

---

## 🗺️ Calculadora Cartográfica

> **Python + Cartografia + Geografia + Programação**

Um projeto de estudo que busca unir conhecimentos de **Cartografia Básica** com desenvolvimento de software, transformando conceitos cartográficos em ferramentas computacionais.
