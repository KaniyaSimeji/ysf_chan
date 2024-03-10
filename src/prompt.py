from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages.system import SystemMessage
from langchain_core.prompts.chat import HumanMessage


class CharactorPrompt():
    """docstring for CharactorPrompt."""

    def __init__(self, system_message: str):
        super(CharactorPrompt, self).__init__()
        self.system = ChatPromptTemplate.from_messages([
            SystemMessage(content=system_message),
            HumanMessage(content="{input}")
        ])
