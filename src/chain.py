from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from prompt import CharactorPrompt


class CharactorChain():
    """docstring for CharactorChain."""

    def __init__(self, prompt: CharactorPrompt, ollama: Ollama):
        super(CharactorChain, self).__init__()
        output_parser = StrOutputParser()
        chain = prompt.system | ollama | output_parser
        self.chain = chain

    def invoke(self, input: str) -> str:
        return self.chain.invoke({"input": input})
