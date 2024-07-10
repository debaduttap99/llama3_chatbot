# 🦙📚 LlamaIndex - Chat with the Streamlit docs

Build a chatbot powered by LlamaIndex that augments Llama3 with the contents of the Streamlit docs (or your own data). The bot will use RAG to retrieve data from all the documents within the netscout_data folder.

## Setup

1. If you don’t have Python installed, install it [from Python.org](https://www.python.org/downloads/).

2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository.

3. Navigate into the project directory:

   ```bash
   $ cd llama3_chatbot
   ```

4. Create a new virtual environment:

   - macOS:

     ```bash
     $ python -m venv venv
     $ . venv/bin/activate
     ```

   - Windows:
     ```cmd
     > python -m venv venv
     > .\venv\Scripts\activate
     ```

5. Install the requirements:

   ```cmd
   pip install -r requirements.txt
   ```

6. Run the app:

   ```cmd
   cd llamaragbot
   ```

To test if llama3 is working run:
   ```cmd
   python basics.py
   ```

To launch the app:
   ```cmd
   streamlit run app.py
   ```
