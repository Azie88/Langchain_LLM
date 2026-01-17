import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain_core._api.deprecation")


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from decouple import config

# Load OpenAI API key
OPENAI_API_KEY = config("OPENAI_API_KEY")

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    "Please tell me which foods are famous in {place}"
)

# Initialize GPT-4 model
model = ChatOpenAI(
    model="gpt-4-turbo",
    temperature=0,
    openai_api_key=OPENAI_API_KEY
)

# Get user input
place = input("Enter a location to learn about its famous foods: ")

# Format the prompt and invoke
formatted_prompt = prompt.format_messages(place=place)

# Run the model
response = model.invoke(formatted_prompt)

# Print output
print(f"\nGPT-4 says:\n{response.content}")