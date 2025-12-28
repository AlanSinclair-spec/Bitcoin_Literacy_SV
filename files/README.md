# 🇸🇻 BitcoinEd El Salvador

**AI-Powered Bitcoin & Financial Literacy Education for El Salvador**

A free, bilingual educational app complementing El Salvador's national "What Is Money?" program and the 2025 xAI/Grok school integration initiative.

![Bitcoin Education](https://img.shields.io/badge/Bitcoin-Education-orange)
![El Salvador](https://img.shields.io/badge/🇸🇻-El%20Salvador-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

## 🎯 Mission

Empowering El Salvador's next generation with Bitcoin and financial literacy through:
- **Interactive AI tutoring** (Grok-powered conversations)
- **Safe transaction simulations** (no real funds at risk)
- **Engaging storytelling** (inspired by "The Little HODLer")
- **Gamified learning** (XP, achievements, progress tracking)
- **Bilingual support** (Spanish/English)

## 🚀 Features

### 📚 Learning Modules
- **₿ Bitcoin Basics** - What is Bitcoin, 21M supply, satoshis
- **👛 Wallet Security** - Seed phrases, Chivo Wallet, self-custody
- **📜 History of Money** - From barter to Bitcoin
- **💰 Budgeting Game** - Learn to save and "stack sats"
- **🔄 Transaction Simulator** - Practice sending/receiving BTC safely
- **❓ Quiz Challenges** - Test your knowledge
- **📖 Story Time** - Bitcoin stories inspired by Lina Seiche's books

### 🎮 Gamification
- XP points for completing lessons
- Level progression system
- Achievement badges
- Day streak tracking

### 🌐 Live Data
- Real-time Bitcoin prices via CoinGecko API
- USD value calculations
- Satoshi conversion displays

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Data**: Pandas
- **API**: CoinGecko (free tier)
- **AI**: Ready for Grok/xAI API integration
- **Deployment**: Streamlit Community Cloud

## 📦 Installation

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/bitcoined-el-salvador.git
cd bitcoined-el-salvador

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Deploy to Streamlit Cloud

1. Push code to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and `app.py`
5. Click "Deploy"

## 🔌 API Integration

### Adding Real Grok/xAI API

Replace the `simulate_ai_response()` function in `app.py` with:

```python
import openai  # xAI uses OpenAI-compatible API

def get_grok_response(question, lang):
    client = openai.OpenAI(
        api_key=st.secrets["XAI_API_KEY"],
        base_url="https://api.x.ai/v1"
    )
    
    system_prompt = """You are a friendly Bitcoin education tutor for 
    El Salvador students ages 7-18. Explain concepts simply using 
    examples relevant to El Salvador. Always be encouraging and 
    age-appropriate."""
    
    response = client.chat.completions.create(
        model="grok-beta",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    
    return response.choices[0].message.content
```

Add your API key to `.streamlit/secrets.toml`:
```toml
XAI_API_KEY = "your-api-key-here"
```

## 📊 Alignment with National Programs

| Initiative | How BitcoinEd Complements |
|------------|---------------------------|
| "What Is Money?" Program | Digital companion for La Libertad pilot, extends reach to rural areas |
| xAI School Partnership | Provides structured curriculum alongside Grok tutoring |
| Chivo Wallet | Teaches wallet security before real-world use |
| Bitcoin Curriculum (3 hrs/week) | Extra practice and self-study resource |

## 🎨 Content Attribution

- Story characters and themes inspired by **Lina Seiche's "The Little HODLer"** book series
- Educational framework aligned with El Salvador's Ministry of Education Bitcoin curriculum
- Quiz questions based on official "What Is Money?" program materials

## 🌍 Localization

Currently supports:
- 🇸🇻 Spanish (default)
- 🇺🇸 English

Adding new languages: Extend the `TRANSLATIONS`, `STORIES`, `QUIZ_QUESTIONS`, and `LESSONS` dictionaries in `app.py`.

## 📱 Offline Support (Coming Soon)

Future versions will include:
- PWA support for offline access
- Cached lesson content
- Sync progress when online

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Additional story content
- More quiz questions
- Offline mode implementation
- Additional language translations
- Accessibility improvements

## 📄 License

MIT License - Free for educational use

## 🙏 Acknowledgments

- **El Salvador Ministry of Education** - For pioneering Bitcoin education
- **Lina Seiche** - For "The Little HODLer" inspiration
- **xAI** - For bringing Grok to El Salvador schools
- **Mi Primer Bitcoin** - For community education resources

---

**Built for the Bitcoin generation of El Salvador** 🇸🇻⚡

*"La educación es la herramienta más poderhat para cambiar el mundo." - Nelson Mandela*
