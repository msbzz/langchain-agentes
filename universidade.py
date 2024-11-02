from langchain.tools import BaseTool
# import json
import os
# from typing import List
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import Field, BaseModel
from dotenv import load_dotenv

load_dotenv()

def busca_dados_da_universidade(universidade):
    dados = pd.read_csv("documentos/universidades.csv")
    
    # Normaliza o texto da coluna para evitar problemas de case e espaços
    dados["NOME_FACULDADE"] = dados["NOME_FACULDADE"].str.lower().str.strip()
    universidade = universidade.lower().strip()

    # Filtra o DataFrame pela universidade fornecida
    dados_com_essa_universidade = dados[dados["NOME_FACULDADE"] == universidade]
    if dados_com_essa_universidade.empty:
        print("Universidade não encontrada:", universidade)
        return {"error": "Universidade não encontrada"}
    
    # Converte para JSON o primeiro registro encontrado
    resultado = dados_com_essa_universidade.iloc[:1].to_dict(orient="records")[0]
    print("Universidade encontrada:", resultado)
    return resultado

def busca_dados_das_universidades(universidade):
    dados = pd.read_csv("documentos/universidades.csv")
    return dados.to_dict(orient="records")

class ExtratorDeUniversidade(BaseModel):
    universidade: str = Field("Nome da universidade informado, sempre em letras minúsculas.")


class ExtratorDeUniversidades(BaseModel):
    universidade: str = Field("Todas as universidades devem ser considerada.")


class DadosDaUniversidade(BaseTool):
    name = "DadosDaUniversidade"
    description = """Esta ferramenta extrai os dados de uma universidade.
    Passe para essa ferramenta como argumento o nome da universidade.
    """
    
    def _run(self, input: str) -> str:
        llm = ChatOpenAI(model="gpt-4",
                         api_key=os.getenv("OPENAI_API_KEY"))

        parser = JsonOutputParser(pydantic_object=ExtratorDeUniversidade)
        template = PromptTemplate(
            template="""Você deve Analisar a entrada a seguir : "{input}" e extrair o nome da universidade em minúsculo informado.
            Formato de saída:
            {formato_saida}""",
            input_variables=["input"],
            partial_variables={"formato_saida": parser.get_format_instructions()}
        )

        cadeia = template | llm | parser
        resposta = cadeia.invoke({"input": input})
        universidade = resposta['universidade']
        universidade = universidade.lower().strip()
        
        # Chama a função de busca e obtém os dados da universidade
        dados = busca_dados_da_universidade(universidade)
        print('Universidade encontrada:', dados)
        
        # Retorna o dicionário diretamente
        return dados


class TodasUniversidades(BaseTool):
    name="TodasUniversidades"
    description="""Carrega os dados de todas as universidades. Não é necessário nenhum parâmetro de entrada por isso desconsidere caso haja algum."""
    
    def _run(self, input:str)->str:
        universidades = busca_dados_das_universidades(None)
        return universidades
    
 
