# 🌤️ AI Weather Agent

An AI-powered Weather Agent built using **Python**, **Google Gemini API**, **Streamlit**, and the **wttr.in Weather API**.

## 🚀 Features

- 🌦️ Get real-time weather information
- 🤖 AI-generated natural language responses using Gemini
- 💬 Interactive Streamlit chat interface
- 🔐 Secure API key management using `.env`
- 🌍 Uses a free weather API (wttr.in)

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Streamlit
- Requests
- Python Dotenv

## 📂 Project Structure

```
Weather_Agent/
│── app.py
│── main.py
│── tools.py
│── prompts.py
│── memory.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-agent.git
```

### Go to the project folder

```bash
cd weather-agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
MODEL=gemini-2.5-flash
```

### Run the application

```bash
streamlit run app.py
```

## 📌 Example

**User**

```
Weather in Coimbatore
```

**Assistant**

```
The current weather in Coimbatore is sunny with a temperature of 31°C and humidity of 72%.
```

## 🔄 Workflow

```
User
   │
   ▼
Streamlit UI
   │
   ▼
Gemini AI
   │
   ▼
Weather Tool
   │
   ▼
Weather API
   │
   ▼
Gemini AI
   │
   ▼
Response
```

## 📚 APIs Used

- Gemini API
- wttr.in Weather API

## 👨‍💻 Author

Vedhaharini