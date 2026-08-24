# Simulador de Combate Modular em Python

Projeto educacional desenvolvido para o ensino de programação orientada a módulos, separação de responsabilidades, importação de arquivos e lógica de jogos em Python. Ideal para aulas de cursos técnicos de desenvolvimento de sistemas.

## Arquitetura do Projeto

O código está estruturado de forma modular para demonstrar aos alunos como organizar um projeto do mundo real:

```
projeto_fifakaz/
│
├── mercado/
│   ├── clube.py          # Gestão do time, carteira de Kaz Coins e compras
│   └── supabase_db.py    # Comunicação com o banco (Cadastrar e Listar)
│
├── conexao.py            # Setup do Supabase
└── main.py               # Menu principal (Modo Jogador vs Modo FifaKaz)
```

# Como Executar e Testar
Certifique-se de ter o Python 3.10+ instalado na sua máquina.

Clone este repositório ou baixe os arquivos mantendo a mesma árvore de diretórios apresentada acima.

Abra o terminal (ou VS Code) na pasta raiz do projeto.

Execute o arquivo principal digitando:

```
Bash
python main.py
```

# Siga as instruções no terminal:

Digite o nome do seu herói e distribua/insira seus atributos (ATK, DEF, EVA).
Escolha qual monstro deseja enfrentar na lista gerada pelo Mestre.
Utilize as opções de combate para atacar e testar a rolagem dos dados baseada no d20.

# Conceitos Didáticos Aplicados

Modularização: Como isolar lógicas em arquivos separados utilizando pastas e subpastas (from pasta.arquivo import funcao).
Estruturas de Dados: Uso intensivo de Dicionários (dict) para modelar personagens e inimigos, e Listas (list) para registros e logs.
Game Loop e Condicionais: Utilização de laços while e estruturas if-elif-else para controlar o fluxo de vida e turnos.
Randomização: Uso da biblioteca nativa random para simular a imprevisibilidade de um RPG de mesa tradicional.


# Como Conectar o Python ao Supabase
Para conectar o projeto ao Supabase, utilizamos a biblioteca oficial do Python chamada supabase.

# Passo a passo para os alunos:
No terminal do VS Code, instalar a biblioteca oficial:

Bash

```
pip install supabase
python.exe -m pip install --upgrade pip
```

No painel do Supabase: Criar um projeto, ir nas configurações (Project Settings > API) e copiar a URL do projeto e a chave secreta anon public (ou service_role).

Para evitar expor chaves de segurança no GitHub, ensinamos os alunos a usarem variáveis de ambiente ou a criarem um arquivo de configuração isolado (conexao.py).

# Configurações do Supabase:
Primeiro crie um projeto, dando-lhe um nome.
<img width="1398" height="571" alt="image" src="https://github.com/user-attachments/assets/afdfaed6-b2dc-489a-82e5-9dd9583e1439" />

Vamos encontrar as credenciais para conectar o nosso Código Python ao Supabase:
<img width="1577" height="821" alt="image" src="https://github.com/user-attachments/assets/435ff5e8-aa49-41c2-8293-ab4517b11b70" />

Agora procure pelo Project URL conforme a imagem:
<img width="1551" height="581" alt="image" src="https://github.com/user-attachments/assets/c3d678d5-c5d4-4fd7-9d4a-f6731151a667" />

Agora procure pela credencial conforme as imagens:
<img width="1605" height="729" alt="image" src="https://github.com/user-attachments/assets/fa953bf8-948c-45aa-8ae6-c307ee0a217b" />

<img width="1114" height="522" alt="image" src="https://github.com/user-attachments/assets/09e571de-fc81-40ef-95f5-c212947a8ab6" />

<img width="1279" height="550" alt="image" src="https://github.com/user-attachments/assets/68fbd561-63f4-4c90-bcf6-fb0c2ce4ebc9" />

Agora crie a estrutura da sua base de dados:

<img width="1730" height="831" alt="image" src="https://github.com/user-attachments/assets/585e2e4a-eddc-405c-abf9-1225219ac14f" />

<img width="1872" height="914" alt="image" src="https://github.com/user-attachments/assets/f84ee9ee-e2e7-43bd-b840-9b52b25fcbd4" />

Cole o seguinte código para criar a estrutura das entidades, atributos, seus tipos e esquemas necessários:

```
CREATE TABLE jogadores_fifakaz (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    posicao TEXT NOT NULL,
    valor INT NOT NULL, -- Preço em Kaz Coins
    atk INT NOT NULL,
    def INT NOT NULL
);

-- Inserindo alguns craques iniciais para a loja não começar vazia
INSERT INTO jogadores_fifakaz (nome, posicao, valor, atk, def) VALUES 
('Kazenski', 'Atacante', 500, 95, 40),
('Pelé', 'Meio-Campo', 900, 99, 50),
('Maldini', 'Zagueiro', 400, 30, 95),
('Neuer', 'Goleiro', 300, 10, 90);
```

Também temos o código para gerar dados aleatórios na base de dados digital:

```
-- Gerando 100 jogadores aleatórios puramente com PostgreSQL no Supabase
INSERT INTO jogadores_fifakaz (nome, posicao, valor, atk, def)
SELECT 
    -- 1. Sorteia um nome e concatena (||) com um sobrenome
    (ARRAY['Kaz', 'Pelé', 'Maradona', 'Zico', 'Messi', 'CR7', 'Neymar', 'Mbappé', 'Haaland', 'Vini Jr'])[floor(random() * 10 + 1)] || ' ' || 
    (ARRAY['Silva', 'Santos', 'Oliveira', 'Souza', 'Ferreira', 'Lima', 'Gomes'])[floor(random() * 7 + 1)],
    
    -- 2. Sorteia a posição
    (ARRAY['Atacante', 'Meio-Campo', 'Zagueiro', 'Goleiro', 'Lateral'])[floor(random() * 5 + 1)],
    
    -- 3. Sorteia Valor (100 a 1000 KC)
    floor(random() * 900 + 100)::INT,
    
    -- 4. Sorteia ATK (10 a 99)
    floor(random() * 89 + 10)::INT,
    
    -- 5. Sorteia DEF (10 a 99)
    floor(random() * 89 + 10)::INT

-- O "Laço For" do SQL: Geração de 50 séries numéricas
FROM generate_series(1, 100);
```

<img width="1843" height="917" alt="image" src="https://github.com/user-attachments/assets/6024d8d2-646c-4145-85f3-e5606bf96207" />

<img width="693" height="894" alt="image" src="https://github.com/user-attachments/assets/913622dd-9efe-4411-86ee-295f22895f54" />

Você deverá ter visto a seguinte mensagem: "Success. No rows returned."


# O Mistério da Pasta __pycache__

Quando vocês rodam um arquivo simples em Python (tudo em um arquivo só), o Python lê o texto e executa. Mas quando começamos a criar sistemas profissionais e usamos o import para chamar funções de outros arquivos (como fizemos importando a ficha e os inimigos), o Python tenta ser mais inteligente e rápido.

<img width="1659" height="824" alt="image" src="https://github.com/user-attachments/assets/031c860b-4f0a-4a26-bb40-293192008e51" />

## O que é exatamente esse cache?
O computador não entende o nosso texto em Python (código-fonte). Ele precisa traduzir isso para "Bytecode" (uma linguagem intermediária mais próxima da máquina).
Para não ter que traduzir os módulos importados toda vez que você roda o jogo, o Python faz a tradução na primeira vez e salva uma cópia rápida dentro da pasta __pycache__.

## Analogia para a lousa: Imagine que você tem que ler um livro em inglês para a turma, mas você demora para traduzir mentalmente. Na primeira vez, você traduz e anota tudo em um caderno à parte. Na aula seguinte, você não traduz de novo, você apenas lê o seu caderno. O __pycache__ é esse "caderno de anotações" do Python!

## Isso é lixo? Posso apagar?

Não é lixo, é uma otimização de performance! Ele serve para deixar o carregamento do seu jogo muito mais rápido nas próximas execuções.
Porém, sim, você pode apagar a qualquer momento sem medo. Se você deletar essa pasta, o seu projeto não vai quebrar. O único "problema" é que, na próxima vez que você der Play no jogo, o Python vai gastar alguns milissegundos a mais para traduzir tudo de novo e recriará a pasta automaticamente.

## Dissecando o nome do arquivo (ficha.cpython-313.pyc)
Olhando a sua imagem, vemos arquivos com uma extensão esquisita. Explique aos alunos o que cada parte significa:

```
ficha: É o nome original do seu módulo.
cpython: É o nome do "motor" padrão do Python (escrito em linguagem C) que está rodando no seu computador.
313: Representa a versão do Python instalada na sua máquina (Python 3.13).
.pyc: Significa Python Compiled (Python Compilado / Bytecode).
```

