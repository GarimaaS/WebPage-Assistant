from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")

prompt = PromptTemplate(
        template = "You are a helpful assistant. Tell about {topic} from the given text -\n {text}",
        input_variables = ['text','topic']
    )

parser = StrOutputParser()

chain = prompt | model | parser

class PageAssistant:

    def initChain(url):
        loader = WebBaseLoader(url)
        docs = loader.load()
        return docs

    def getAns(topic,doc):
        return chain.invoke({'topic':topic, 'text':doc[0].page_content})
