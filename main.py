from langchain.llms import OpenAI

from dotenv import load_dotenv


load_dotenv()






llm = OpenAI()


result = llm("write a short sentence about machine learning")


print("result: ", result)