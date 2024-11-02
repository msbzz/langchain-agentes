# langchain-agentes

- Este projeto é fruto do curso de 'LangChain: Desenvolva agentes de inteligência artificial' da plataforma ALURA

## Introdução

Esse projeto tem como objetivo apresentar a biblioteca  **LangChain** que facilita o desenvolvimento de aplicações de IA 
baseadas em modelos de linguagem (LLMs) de grande escala . Ela fornece uma estrutura para conectar modelos de linguagem, 
como o GPT da OpenAI, com várias fontes de dados, ferramentas e pipelines de processamento. O objetivo da LangChain é 
ajudar desenvolvedores a construir agentes de IA que podem realizar tarefas complexas ao utilizar diferentes 
componentes e fluxos de trabalho.

## Exemplos de Uso

- Chatbots avançados: Um chatbot pode acessar uma base de conhecimento para responder a perguntas complexas e, ao mesmo 
tempo, interagir com outras APIs para realizar ações.
- Assistentes de pesquisa: Um agente que acessa bancos de dados, processa documentos e fornece 
respostas ou insights.

- Automação de tarefas: Automatizar fluxos de trabalho em empresas, como verificação de dados, 
respostas automáticas a e-mails e geração de relatórios.
 

## Apresentação do projeto

 - O projeto apresenta um exemplo de questionamento baseado num contexto escolar 
 é feita uma avaliação de melhor direcionamento do aluno em função de suas notas, e preferencias. Dessa forma se tentam otimizar a continuidade dessa formação 
 dentro de um contexto limitado de informações existentes naquele ambiente 
 acadêmico que no caso são duas planilhas '.csv' com informações sobre seus
 colegas de classe e universidades e seus cursos.

 - estudantes

 <img src="/img/estudantes.png" alt="estudantes" width="500"/>

- universidades

<img src="/img/universidades.png" alt="universidades" width="500"/>


## Instalação do Projeto

### 1. Clonar o Repositório

Primeiramente, faça o download do código fonte deste repositório no GitHub utilizando o comando:

```bash
git clone https://github.com/msbzz/langchain-agentes.git
```

### 2. Instalar as Dependências

Navegue até a pasta do projeto **langchain-agentes** ative o ambiente virtual
e em seguida instale todas as dependências necessárias  

### venv no Windows:

```bash
python -m venv venv-langchain2
venv-langchain2\Scripts\activate
```


### venv no Mac/Linux:

```bash
python3 -m venv venv-langchain2
source venv-langchain2/bin/activate
```

Em seguida, instale os pacotes utilizando:

```bash
pip install -r requirements.txt
```

## Aplicativos de Interface de Usuário (IU)

Neste projeto utilizei o **vscode** mas é compatível com qualquer editor de código

- **Visual Studio Code**: Um editor leve e poderoso para desenvolvimento de aplicações web. Você pode baixá-lo [aqui](https://code.visualstudio.com/).


### Executando o Projeto

Estando com seu projeto pronto o ambiente virtual instalado e suasdependências instaladas  utilize comando:

```bash
python main.py
```

### Inscrições necessárias para utilização do projeto

Para obter as credenciais necessárias, você precisará estar inscrito nos seguintes serviços:

1. **OpenAI** - Para a variável `OPENAI_API_KEY`, você precisa ter uma conta na [OpenAI](https://platform.openai.com/). Essa chave permite acessar os modelos de linguagem da OpenAI, como o GPT-4. Após criar uma conta, você poderá gerar a chave API na seção "API keys" do painel de controle da OpenAI.

2. **LangChain Hub / LangChain Smith** - Para as variáveis `LANGCHAIN_TRACING_V2`, `LANGCHAIN_ENDPOINT`, `LANGCHAIN_API_KEY` e `LANGCHAIN_PROJECT`, é necessário estar inscrito no LangChain Hub (ou LangSmith). Esse serviço pode ser encontrado em [LangChain](https://smith.langchain.com/). O LangChain Hub oferece ferramentas para gerenciar agentes e fluxos de trabalho de IA e monitorar o uso dos modelos.

Essas chaves esão necessárias para que o projeto possa se comunicar com os serviços externos da OpenAI e do LangChain para processar consultas e interações com modelos de IA.

### Tópicos abordados no curso

- Criar e manipular dados de universidades em um novo arquivo Python.
- Carregar informações de um arquivo CSV e realizar queries ignorando maiúsculas e minúsculas usando a biblioteca Pandas.
- Implementar funções para buscar dados específicos e gerais de universidades.
- Criar ferramentas em forma de classes que herdam de BasicTool.
- Utilizar o JSONOutputParser e configurar prompt templates.
- Ajustar o código para lidar com inconsistências de entrada de dados.
- Formular perguntas complexas e entender o impacto dos detalhes na interpretação da LLM.
- Registrar e testar novas ferramentas desenvolvidas no sistema.
   