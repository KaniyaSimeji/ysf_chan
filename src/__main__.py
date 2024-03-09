from langchain_community.llms.ollama import Ollama
from prompt import CharactorPrompt
from chain import CharactorChain


def main():
    llm = Ollama(model="llama2")
    prompt = CharactorPrompt(
        system_message="You are a student at a school called Yokohama Science Frontier High School")
    chain = CharactorChain(prompt, llm)
    res = chain.invoke("Are you student?")
    print(res)


if __name__ == "__main__":
    main()
