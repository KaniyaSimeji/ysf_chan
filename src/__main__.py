from langchain_community.llms.ollama import Ollama
from prompt import CharactorPrompt
from chain import CharactorChain


def main():
    llm = Ollama(model="vicuna")
    prompt = CharactorPrompt(
        system_message="あなたは横浜サイエンスフロンィア高校の生徒です")
    chain = CharactorChain(prompt, llm)
    res = chain.invoke("あなたはサイエンスフロンティア高校の生徒ですか")
    print(res)


if __name__ == "__main__":
    main()
