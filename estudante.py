from langchain.tools import BaseTool
import json
 
import os
from typing import List
import pandas as pd
 
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import Field, BaseModel
from dotenv import load_dotenv

load_dotenv()

def busca_dados_estudante(estudante):
    dados = pd.read_csv("documentos/estudantes.csv")
    dados_com_esse_estudante = dados[dados["USUARIO"]== estudante]
    if dados_com_esse_estudante.empty:
        return {}
    return dados_com_esse_estudante.iloc[:1].to_dict()
 
class ExtratorDeEstudante(BaseModel):
    estudante: str = Field("Nome do estudante informado, sempre em letras minúsculas. Exemplo: joão, carlos, joana, carla")


class Nota(BaseModel):
     area:str = Field("Nome da área de conhecimento")
     nota:float=Field("Nota da área de conhecimento")

class PerfilAcademicoDeEstudante(BaseModel):
    nome:str = Field("nome do estudante")
    ano_de_conclusai:int = Field("ano de conclusão")
    notas:List[Nota] = Field("Lista de notas das disciplinas e areas de conhecimento")
    resumo:str = Field("Resumo das principais caracteristicas desse estudante de forma a torna-lo único e um ótimo potencial para as faculdades. Exemplo: só esse estudante tem bla bla bla")

class DadosDeEstudante(BaseTool):
    name = "DadosDeEstudante"
    description = """Esta ferramenta extrai o histórico e preferências de um estudante de acordo com seu histórico
    Passe para essa ferramenta como argumento o nome do estudante.
    """
    
    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4o",
                                api_key=os.getenv("OPENAI_API_KEY"))
 
        parser = JsonOutputParser(pydantic_object=ExtratorDeEstudante)
        template = PromptTemplate(template="""Você deve Analisar a entrada a seguir : "{input}" e extrair o nome em minúsculo                                  informado.
        Formato de saída:
        {formato_saida}""",
        input_variables=["input"],
        partial_variables={"formato_saida" : parser.get_format_instructions()})

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input" : input}) 
        estudante= resposta['estudante']
        # estudante= input
        estudante = estudante.lower().strip()
        dados = busca_dados_estudante(estudante)
        print('Estudande encontrado')
        print(dados)
        return json.dumps(dados)

class PerfilAcademico(BaseTool):

    name="PerfilAcademico"
    description="""Cria um perfil acadêmico de um estudante.
    Esta ferramenta requer como entrada todos os dados do estudante.
    Eu sou incapaz de buscar dados do estudante. Você tem que buscar
    dados do estudante antes de me invocar.
    """
    def _run(self,input:str)-> str:
        llm = ChatOpenAI(model="gpt-4o",
                            api_key=os.getenv("OPENAI_API_KEY"))

        parser = JsonOutputParser(pydantic_object=PerfilAcademicoDeEstudante)
     
        template = PromptTemplate(template="""- Formate o estudante para seu perfil acadêmico. 
                                  - Com os dados identifique as opções de universidades
                                  sugeridas e cursos compatíveis com o interesse do aluno
                                  - Destaque o perfil do aluno dando enfase principalmente
                                  naquilo que faz sentido para as instituições de interesse
                                  do aluno
                                  
                                  Persona : voce é uma consultora de carreira que precisa indicar
                                  com detalhes, riqueza, mas direta ao ponto e faculdade as opções
                                  e conseguencias possíveis.
                                  Informações atuais:

                                  {dados_do_estudante}
                                  {formato_de_saida}
                                  """,
                                  input_variables=["dados_de_estudante"],
                                  partial_variables={"formato_de_saida": parser.get_format_instructions()})
        cadeia = template | llm | parser
        resposta = cadeia.invoke({"dados_do_estudante": input})     
        print(resposta)  