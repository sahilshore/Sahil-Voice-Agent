# 🎤 Sahil AI Voice Agent

### %%Project Overview%%

Sahil AI Voice Agent is a %%production-oriented, voice-first conversational AI system%% designed to demonstrate modern agent-based reasoning, Retrieval-Augmented Generation (RAG), and real-time speech interaction.

The project emphasizes %%reliable browser-based voice interaction%%, short confident responses, and deterministic behavior suitable for interviews, assessments, and live demos.

---

## ### %%Problem Statement%%

Most AI chat applications focus heavily on text-based interaction and ignore real-world constraints of voice systems such as latency, browser permissions, and response clarity.

This project addresses:
- How to build a %%voice-first AI assistant%%
- How to %%ground responses using retrieval%%
- How to %%design agent routing logic%%
- How to %%deploy reliably on cloud platforms%%

---

## ### %%Core Objectives%%

- Build a %%speech-to-speech AI agent%% with minimal user friction  
- Use %%RAG%% to ground answers in domain knowledge  
- Demonstrate %%agent-based decision making%%  
- Ensure %%deployment stability%% on Streamlit Cloud  
- Maintain %%clear, human-like response style%%  

---

## ### %%Key Capabilities%%

### %%Voice Interaction%%
- Captures microphone input directly from the browser
- Converts spoken input into structured agent queries
- Returns synthesized voice responses in near real-time

### %%Retrieval-Augmented Generation (RAG)%%
- Loads domain-specific documents into FAISS
- Performs semantic similarity search at runtime
- Injects retrieved context into the agent prompt

### %%Agent-Based Reasoning%%
- Uses LangChain + LangGraph agents
- Routes queries based on intent (profile, company, general)
- Optionally invokes web tools when required

### %%Fallback Reliability%%
- Designed to continue functioning even if voice input fails
- Ensures predictable behavior across browsers

---

## ### %%System Architecture%%

### %%High-Level Flow%%


#### Browser (Voice Input)
####    ↓
#### Streamlit Frontend
####    ↓
#### LangChain Agent
####    ↓
#### FAISS Vector Retrieval (RAG)
####    ↓
#### OpenAI GPT-4o-mini
####    ↓
#### Voice Response Output



### %%Design Philosophy%%
- %%Short answers over long explanations%%
- %%Low-latency execution%%
- %%Explicit routing logic%%
- %%Production realism over experimentation%%

---

## ### %%Technology Stack%%

- %%Language%%: Python  
- %%Frontend%%: Streamlit  
- %%LLM%%: OpenAI GPT-4o-mini  
- %%Agent Framework%%: LangChain, LangGraph  
- %%Vector Store%%: FAISS  
- %%Speech APIs%%: OpenAI (voice input/output)  
- %%Deployment%%: Streamlit Cloud  

---

## ### %%Project Structure%%

    Sahil-Voice-Agent/
    ├── frontend.py # UI, microphone handling, voice playback
    ├── ai_agent.py # Agent logic, RAG, routing, memory
    ├── data/ # Knowledge sources
    │ ├── sahil_profile.pdf
    │ └── 100x_profile.pdf
    ├── requirements.txt # Dependency list
    ├── README.md
    └── .gitignore



---

## ### %%Local Development Setup%%

### %%Step 1: Clone Repository%%

%%Step 2: Create Virtual Environment%%

        python -m venv .venv
        source .venv/bin/activate

%%Step 3: Install Dependencies%%

        pip install -r requirements.txt

%%Step 4: Environment Variables%%

Create a .env file:
    
    OPENAI_API_KEY=your_openai_api_key
    TAVILY_API_KEY=your_tavily_api_key

%%Step 5: Run Application%%

    mlit run frontend.py

### %%Cloud Deployment (Streamlit Cloud)%%

Push repository to GitHub

Open Streamlit Cloud and connect repository

Set %%Main file%% to:

    frontend.py


Add secrets in Streamlit Cloud:
    
    OPENAI_API_KEY = "your_openai_api_key"
    TAVILY_API_KEY = "your_tavily_api_key"


Deploy application

### %%Browser Compatibility%%

%%Google Chrome%% — Best performance and microphone support

%%Brave%% — May block mic due to aggressive privacy rules

%%Microsoft Edge%% — Voice input may require manual permission enable

For best experience, %%Chrome is recommended%%.

### %%Performance Considerations%%

Vector stores are cached to reduce reload time

Chat memory is intentionally limited to save tokens

Voice processing latency depends on network and browser

### %%Limitations%%

Browser-based voice input is subject to permission policies

Streamlit Cloud may introduce cold-start latency

Designed for demo and evaluation, not large-scale production

### %%Intended Use Cases%%

AI Engineer / ML Engineer interviews

Technical assessments

Voice-based AI demonstrations

RAG + agent architecture showcases

