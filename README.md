# WebPage Assistant 🤖📄

AI-powered chatbot that loads webpages and answers questions about their content using Google Gemini AI.

---

## ✨ Features

- 🌐 Load any public webpage
- 💬 Interactive chat with message history
- 🧠 AI responses using Google Gemini
- ⚡ Fast and efficient

---

## 📦 Prerequisites

- Python 3.8+
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))

---

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/webpage-assistant.git
cd webpage-assistant
```

### 2. Install Dependencies
```bash
pip install streamlit langchain-google-genai langchain-core langchain-community python-dotenv
```

### 3. Setup Environment
Create `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 📁 Project Structure
```
webpage-assistant/
├── chain.py          # AI logic
├── main.py           # Streamlit UI
├── .env              # API key (create this)
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

---

## 🎯 Usage

### Start Application
```bash
streamlit run main.py
```

### How to Use
1. **Load Page**: Enter URL in sidebar and click "Load"
2. **Ask Questions**: Type questions in chat input
3. **Get Answers**: AI responds based on page content

---

## 💡 Example Queries
```
"What is this page about?"
"Summarize the main points"
"Tell me about [specific topic] from this page"
"What are the key features mentioned?"
```

---

## 🐛 Troubleshooting

### API Key Error
- Check `.env` file has correct key
- Ensure no extra spaces
- Restart Streamlit server

### Module Not Found
```bash
pip install -r requirements.txt
```

### Page Won't Load
- Verify URL is correct
- Check URL is publicly accessible
- Try different webpage

---

## ⚠️ Limitations

- Cannot access login-required pages
- Works best with text-heavy content
- No JavaScript-rendered content
- One page at a time
- Session-based (history clears on refresh)

---

**Made with ❤️ using Streamlit & LangChain**