 
import sys
import os

# Adiciona o caminho da pasta raiz do projeto
 
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from langchain.agents import AgentExecutor
 
from agente import AgenteOpenAIFUnctions

 
from dotenv import load_dotenv


load_dotenv()


# pergunta = "Compare o perfil acadêmico da Ana com o da Bianca"
# pergunta = "Busque dados da USP "
# pergunta = "Dentre uni camp e USP, qual você recomenda para a Ana?"
# pergunta = "Dentre todas as universidades listadas, qual você recomenda para a Ana?"

pergunta = """
Dentre todas as universidades listadas, qual você recomenda para a 
Ana desconsiderando as preferencias pessoais ou geograficas
"""
# pergunta = """ 
# Gostaria que apresente uma lista de todas as universidades e suas 
# localizações apenas 
# """

agente = AgenteOpenAIFUnctions()

executor = AgentExecutor(agent = agente.agente,
                         tools= agente.tools,
                         verbose= True,
                         handle_parsing_errors=True)

resposta = executor.invoke({"input": pergunta})

print(resposta)