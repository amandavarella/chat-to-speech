# Interacting with OpenAI in Python

Sign up to OpenAI: https://platform.openai.com/signup
Then create an API key at: https://platform.openai.com/account/api-keys

Set your OPENAI_API_KEY environment variable:

```bash
export OPENAI_API_KEY=sk-...
```

Create a virtual environment and install the requirements:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
brew install portaudio && pip install pyaudio
```

Run the example:

```bash
python3 app.py
```
