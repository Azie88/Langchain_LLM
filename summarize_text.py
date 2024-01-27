from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Please tell me which foods are famous in {place}"
)

model = ChatOpenAI()
chain = prompt | model