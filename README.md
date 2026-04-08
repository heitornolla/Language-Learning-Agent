# Anki Card Agent

An LLM agent that generates vocabulary flashcards and automatically adds them to Anki using the **Clanki MCP server**.

The agent can:

- Sample words from language datasets
- Filter by difficulty
- Translate between languages
- Create Anki decks and cards automatically

---

## Setup

### 1. Add Word Lists

Place your language data inside:

```
data/<language>/<language>.txt
```

and run the ``build_dataset.ipynb` notebook.

---

### 2. Install Anki

https://docs.ankiweb.net/platform/linux/installing.html

---

### 3. Install AnkiConnect

https://ankiweb.net/shared/info/2055492159

- Anki must be open while running the agent
- Works with WSL

---

### 4. Install Dependencies

Python:

```
pip install -r requirements.txt
```

Node (for Clanki MCP):

```
cd clanki
npm install
npm run build
```

---

### 5. Run Local Models (Ollama)

```
ollama pull qwen3:8b
ollama pull llama3.2:3b
```

---

## How It Works

The agent is built using LangGraph and follows a tool-calling workflow.

---

### Usage

```
python main.py
```

Example prompt:

```
Please get 10 easy words in German, translate them to English, and create a new Anki deck with them called German::Easy.
```

---

## Notes

- Anki must be running
- AnkiConnect must be enabled
- Ensure datasets exist before running

Built with help from [t-redactyl](https://github.com/t-redactyl).
