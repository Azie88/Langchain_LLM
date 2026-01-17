# LangChain & OpenAI API Learning Project 🤖

A beginner-friendly project to learn how to use LangChain with OpenAI's API. This example script asks GPT-4 about famous foods from different locations around the world.

## What Does This Do?

This project demonstrates the basics of:
- Setting up LangChain with OpenAI's API
- Creating prompt templates
- Sending requests to GPT-4
- Processing AI responses

The example script lets you type in any city, country, or region, and GPT-4 will tell you what foods that place is famous for:
- Type "Italy" → Learn about pizza, pasta, gelato
- Type "Tokyo" → Learn about sushi, ramen, tempura
- Type "Mexico" → Learn about tacos, mole, tamales

Once you understand how this works, you can modify it to ask GPT-4 anything else!

## Setup Instructions

### 1. Install Python
Make sure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Get an OpenAI API Key
1. Go to [OpenAI's website](https://platform.openai.com/)
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key and copy it

### 3. Set Up the Project

**Step 1: Clone the Repository**
```bash
git clone https://github.com/Azie88/Langchain_LLM.git
cd Langchain_LLM
```

**Step 2: Create a virtual environment**
```bash
python -m venv .venv
```

**Step 3: Activate the virtual environment**

On Windows (PowerShell):
```powershell
.venv\Scripts\Activate
```

On Mac/Linux:
```bash
source .venv/bin/activate
```

**Step 4: Install required packages**
```bash
pip install -r requirements.txt
```

**Step 5: Create a `.env` file**

Create a file named `.env` in the same folder as your script and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

Replace `your-api-key-here` with the actual API key you got from OpenAI.

**Step 6: Run the Script**
```bash
python summarize_text.py
```

### 4. Requirements

All required packages are listed in the `requirements.txt` file (generated using `pip freeze`).

### 5. Usage

1. Run the script
2. When prompted, type a location (country, city, region)
3. Press Enter
4. The AI will tell you about famous foods from that place
5. Type another location or type 'quit' to exit


### Cost Warning ⚠️

This script uses OpenAI's API which costs money. Each query costs a small amount (typically a few cents). Check your OpenAI account for current pricing.

### Files You Should Have

```
your-project-folder/
├── summarize_text.py      # The main script
├── requirements.txt       # List of required packages
├── .env                   # Your API key (DON'T share this!)
└── .venv/                 # Virtual environment folder (created automatically)
```

**Note:** Never share your `.env` file or commit it to GitHub. It contains your secret API key!

## Contributions :handshake:

Open an issue, submit a pull request or contact me for any contributions.

## Author :writing_hand:

Andrew Obando

<a href="https://www.linkedin.com/in/andrewobando/"><img align="left" src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Andrew Obando | LinkedIn"/></a>
<a href="https://medium.com/@obandoandrew8">
![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)
</a>

---

Feel free to star ⭐ this repository if you find it helpful!