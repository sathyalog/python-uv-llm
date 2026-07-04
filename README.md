`uv init`

uv will take care of virtual environments when you add 1 package

how to add packages?
`uv add langchain`

`uv add ipykernel` - to make jupyter notebook works in vscode

how to activate virtual environment?
`source .venv/bin/activate`

how to work with .env files?
install python-dotenv library using `uv add python-dotenv`

how to run python file?
`uv run main.py`

Lets use LLM?
visit console.groq.com and create new API key
choose a model and i choose llama-3.3-70b-versatile

add these GROQ_API_KEY and MODEL in .env file

Example `.env`:
```
GROQ_API_KEY=gsk_your_key_here
MODEL=llama-3.3-70b-versatile
```

as we already have python-dotenv library but we would still need groq library to use LLM and hence run this command `uv add groq`

update main.py with relevant code and run using 

`uv run main.py`


