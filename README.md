# uv-project

This project is a simple Python chat app that uses the Groq API to talk to an LLM from the terminal.

It is already set up to work with `uv`, which manages Python dependencies and the virtual environment for you.

## 1. Prerequisites

Make sure you have the following installed on your machine:

- Python 3.14 or newer
- VS Code
- Git
- `uv`

### Install `uv`

On macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify the installation:

```bash
uv --version
```

## 2. Open the project in VS Code

1. Open the project folder in VS Code.
2. Open the integrated terminal.
3. Make sure you are inside the project root.

## 3. Install the required VS Code extensions

Recommended extensions:

- Python
- Jupyter
- Pylance

These extensions help with Python syntax, IntelliSense, notebook support, and interpreter selection.

## 4. Install Python dependencies

From the project root, run:

```bash
uv sync
```

This will create the virtual environment and install the packages listed in `pyproject.toml`.

## 5. Activate the virtual environment (optional, but helpful)

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

If you do not want to activate it manually, you can still run commands through `uv` directly.

## 6. Set up your environment variables

This project uses a `.env` file for configuration.

Create a file named `.env` in the project root and add the following:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL=llama-3.3-70b-versatile
```

### Where to get the API key

1. Go to https://console.groq.com/
2. Create or sign in to your account.
3. Create an API key.
4. Paste it into the `.env` file.

> Important: Do not commit your `.env` file or share your API key publicly.

## 7. Run the application

From the project root, run:

```bash
uv run main.py
```

You will see a chat prompt like:

```text
You:
```

Type your message and press Enter. To exit the chat, type:

```text
exit
```

## 8. Optional: use Jupyter Notebook

If you want to use the notebook file in VS Code to play with python(not relevant to this project):

```bash
uv add ipykernel
```

Then in VS Code:

1. Open the notebook file.
2. Select the Python interpreter from the `.venv` environment.
3. Run the cells.

## 9. Useful `uv` commands

- Add a package:

```bash
uv add package-name
```

- Run a Python file:

```bash
uv run main.py
```

- Open a shell in the project environment:

```bash
uv shell
```

## Troubleshooting

### `uv` is not recognized

Restart the terminal after installation or check that the install path is available in your shell.

### `ModuleNotFoundError`

Run:

```bash
uv sync
```

### Authentication failed

Check that:

- Your Groq API key is correct.
- The `.env` file is in the project root.
- The `MODEL` value is valid for your account.

### VS Code does not see the correct interpreter

Open the Command Palette and choose:

- Python: Select Interpreter

Then select the interpreter from the `.venv` folder inside this project.


