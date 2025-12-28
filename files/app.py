"""
🇸🇻 BitcoinEd El Salvador - AI-Powered Financial Literacy
Complementing El Salvador's "What Is Money?" program and Grok integration
"""

import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime, timedelta
import random
import time

# =============================================================================
# CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="BitcoinEd El Salvador 🇸🇻",
    page_icon="₿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Language translations
TRANSLATIONS = {
    "en": {
        "title": "BitcoinEd El Salvador",
        "subtitle": "Learn Bitcoin & Financial Literacy with AI",
        "welcome": "Welcome, young HODLer! 🚀",
        "select_module": "Select a Learning Module",
        "modules": {
            "basics": "₿ Bitcoin Basics",
            "wallet": "👛 Wallet Security",
            "history": "📜 History of Money",
            "budget": "💰 Budgeting Game",
            "simulator": "🔄 Transaction Simulator",
            "quiz": "❓ Quiz Challenge",
            "story": "📖 Story Time"
        },
        "current_price": "Current Bitcoin Price",
        "ask_grok": "Ask Grok anything about Bitcoin...",
        "send_btn": "Send",
        "progress": "Your Progress",
        "level": "Level",
        "xp": "XP Points",
        "streak": "Day Streak",
        "achievements": "Achievements",
        "loading": "Loading...",
        "correct": "Correct! Great job! 🎉",
        "incorrect": "Not quite, but keep learning! 💪",
        "next_question": "Next Question",
        "your_balance": "Your Balance",
        "send_btc": "Send BTC",
        "receive_btc": "Receive BTC",
        "transaction_history": "Transaction History",
        "budget_goal": "Savings Goal",
        "income": "Income",
        "expenses": "Expenses",
        "savings": "Savings"
    },
    "es": {
        "title": "BitcoinEd El Salvador",
        "subtitle": "Aprende Bitcoin y Educación Financiera con IA",
        "welcome": "¡Bienvenido, joven HODLer! 🚀",
        "select_module": "Selecciona un Módulo de Aprendizaje",
        "modules": {
            "basics": "₿ Fundamentos de Bitcoin",
            "wallet": "👛 Seguridad de Billetera",
            "history": "📜 Historia del Dinero",
            "budget": "💰 Juego de Presupuesto",
            "simulator": "🔄 Simulador de Transacciones",
            "quiz": "❓ Desafío de Quiz",
            "story": "📖 Hora del Cuento"
        },
        "current_price": "Precio Actual de Bitcoin",
        "ask_grok": "Pregúntale a Grok sobre Bitcoin...",
        "send_btn": "Enviar",
        "progress": "Tu Progreso",
        "level": "Nivel",
        "xp": "Puntos XP",
        "streak": "Días Seguidos",
        "achievements": "Logros",
        "loading": "Cargando...",
        "correct": "¡Correcto! ¡Excelente! 🎉",
        "incorrect": "No exactamente, ¡pero sigue aprendiendo! 💪",
        "next_question": "Siguiente Pregunta",
        "your_balance": "Tu Balance",
        "send_btc": "Enviar BTC",
        "receive_btc": "Recibir BTC",
        "transaction_history": "Historial de Transacciones",
        "budget_goal": "Meta de Ahorro",
        "income": "Ingresos",
        "expenses": "Gastos",
        "savings": "Ahorros"
    }
}

# Story content inspired by "The Little HODLer" themes
STORIES = {
    "en": [
        {
            "title": "Luna's First Satoshi",
            "character": "Luna the Little HODLer",
            "chapters": [
                {
                    "text": "Luna was curious about the orange coin everyone talked about. 'Abuela, what is Bitcoin?' she asked. Her grandmother smiled warmly.",
                    "lesson": "Bitcoin is digital money that belongs to everyone, not just banks!",
                    "image_emoji": "👧🏽💭₿"
                },
                {
                    "text": "'Imagine money that can fly around the world in minutes,' Abuela explained. 'No borders can stop it, just like a bird!'",
                    "lesson": "Bitcoin can be sent anywhere in the world, instantly and cheaply.",
                    "image_emoji": "🐦💨🌎"
                },
                {
                    "text": "Luna learned that only 21 million Bitcoin would ever exist. 'It's like a treasure that can never grow,' she realized. 'That makes each piece special!'",
                    "lesson": "Bitcoin is scarce - there will only ever be 21 million. This helps it keep its value!",
                    "image_emoji": "💎✨🔢"
                }
            ]
        },
        {
            "title": "The Village Saves Together",
            "character": "Marco the Wise Farmer",
            "chapters": [
                {
                    "text": "In a small village in El Salvador, Marco noticed something: every time people saved colones, they lost value. Prices kept going up!",
                    "lesson": "Inflation means your money buys less over time. This is why saving in a strong currency matters.",
                    "image_emoji": "🏘️📉😟"
                },
                {
                    "text": "When Bitcoin became legal in El Salvador, Marco started saving small amounts - just like saving seeds for next season's crop.",
                    "lesson": "You don't need a lot to start. Even small amounts of Bitcoin (called satoshis) can grow!",
                    "image_emoji": "🌱💰📱"
                },
                {
                    "text": "Years passed. Marco's Bitcoin savings grew while his neighbors' cash lost value. He taught the whole village about 'stacking sats.'",
                    "lesson": "HODLing means holding Bitcoin for the long term. Patience is rewarded!",
                    "image_emoji": "📈👨‍🌾🎓"
                }
            ]
        }
    ],
    "es": [
        {
            "title": "El Primer Satoshi de Luna",
            "character": "Luna la Pequeña HODLer",
            "chapters": [
                {
                    "text": "Luna tenía curiosidad sobre la moneda naranja de la que todos hablaban. '¿Abuela, qué es Bitcoin?' preguntó. Su abuela sonrió con cariño.",
                    "lesson": "¡Bitcoin es dinero digital que pertenece a todos, no solo a los bancos!",
                    "image_emoji": "👧🏽💭₿"
                },
                {
                    "text": "'Imagina dinero que puede volar por el mundo en minutos,' explicó Abuela. '¡Ninguna frontera puede detenerlo, como un pájaro!'",
                    "lesson": "Bitcoin se puede enviar a cualquier parte del mundo, instantáneamente y barato.",
                    "image_emoji": "🐦💨🌎"
                },
                {
                    "text": "Luna aprendió que solo existirán 21 millones de Bitcoin. '¡Es como un tesoro que nunca puede crecer,' se dio cuenta. '¡Eso hace que cada pieza sea especial!'",
                    "lesson": "Bitcoin es escaso - solo habrá 21 millones. ¡Esto ayuda a mantener su valor!",
                    "image_emoji": "💎✨🔢"
                }
            ]
        },
        {
            "title": "El Pueblo Ahorra Junto",
            "character": "Marco el Agricultor Sabio",
            "chapters": [
                {
                    "text": "En un pequeño pueblo de El Salvador, Marco notó algo: cada vez que la gente ahorraba colones, perdían valor. ¡Los precios seguían subiendo!",
                    "lesson": "La inflación significa que tu dinero compra menos con el tiempo. Por eso importa ahorrar en una moneda fuerte.",
                    "image_emoji": "🏘️📉😟"
                },
                {
                    "text": "Cuando Bitcoin se hizo legal en El Salvador, Marco comenzó a ahorrar pequeñas cantidades - como guardar semillas para la próxima cosecha.",
                    "lesson": "No necesitas mucho para empezar. ¡Incluso pequeñas cantidades de Bitcoin (llamadas satoshis) pueden crecer!",
                    "image_emoji": "🌱💰📱"
                },
                {
                    "text": "Pasaron los años. Los ahorros en Bitcoin de Marco crecieron mientras el efectivo de sus vecinos perdía valor. Enseñó a todo el pueblo sobre 'apilar sats.'",
                    "lesson": "HODL significa mantener Bitcoin a largo plazo. ¡La paciencia es recompensada!",
                    "image_emoji": "📈👨‍🌾🎓"
                }
            ]
        }
    ]
}

# Quiz questions
QUIZ_QUESTIONS = {
    "en": [
        {
            "question": "How many Bitcoin will ever exist?",
            "options": ["Unlimited", "21 million", "100 million", "1 billion"],
            "correct": 1,
            "explanation": "Only 21 million Bitcoin will ever be created. This scarcity is built into Bitcoin's code!"
        },
        {
            "question": "What is the smallest unit of Bitcoin called?",
            "options": ["Mini-coin", "Satoshi", "Bit", "Micro-BTC"],
            "correct": 1,
            "explanation": "A satoshi is the smallest unit, named after Bitcoin's creator. 1 Bitcoin = 100,000,000 satoshis!"
        },
        {
            "question": "When did Bitcoin become legal tender in El Salvador?",
            "options": ["2019", "2020", "2021", "2022"],
            "correct": 2,
            "explanation": "El Salvador became the first country to adopt Bitcoin as legal tender on September 7, 2021!"
        },
        {
            "question": "What does 'HODL' mean?",
            "options": ["Sell quickly", "Hold on for dear life", "Trade daily", "Buy more"],
            "correct": 1,
            "explanation": "HODL means to hold your Bitcoin for the long term, no matter the price changes!"
        },
        {
            "question": "What is a Bitcoin wallet?",
            "options": ["A leather wallet", "A bank account", "Software to store your Bitcoin keys", "A website"],
            "correct": 2,
            "explanation": "A Bitcoin wallet is software that stores your private keys, which let you access and send your Bitcoin."
        },
        {
            "question": "Who controls Bitcoin?",
            "options": ["The government", "A company", "Banks", "No one - it's decentralized"],
            "correct": 3,
            "explanation": "Bitcoin is decentralized! No single person, company, or government controls it."
        },
        {
            "question": "What is the name of El Salvador's official Bitcoin wallet?",
            "options": ["Chivo Wallet", "Bitcoin SV", "Salvadoran Coin", "ES Wallet"],
            "correct": 0,
            "explanation": "Chivo Wallet is El Salvador's official Bitcoin wallet app for citizens!"
        },
        {
            "question": "Why is Bitcoin compared to 'digital gold'?",
            "options": ["It's yellow colored", "It's scarce and valuable", "You can dig for it", "Banks love it"],
            "correct": 1,
            "explanation": "Like gold, Bitcoin is scarce (limited supply) and can store value over time!"
        }
    ],
    "es": [
        {
            "question": "¿Cuántos Bitcoin existirán?",
            "options": ["Ilimitados", "21 millones", "100 millones", "1 billón"],
            "correct": 1,
            "explanation": "¡Solo se crearán 21 millones de Bitcoin! Esta escasez está integrada en el código de Bitcoin."
        },
        {
            "question": "¿Cómo se llama la unidad más pequeña de Bitcoin?",
            "options": ["Mini-moneda", "Satoshi", "Bit", "Micro-BTC"],
            "correct": 1,
            "explanation": "Un satoshi es la unidad más pequeña, nombrada en honor al creador de Bitcoin. ¡1 Bitcoin = 100,000,000 satoshis!"
        },
        {
            "question": "¿Cuándo Bitcoin se convirtió en moneda legal en El Salvador?",
            "options": ["2019", "2020", "2021", "2022"],
            "correct": 2,
            "explanation": "¡El Salvador fue el primer país en adoptar Bitcoin como moneda legal el 7 de septiembre de 2021!"
        },
        {
            "question": "¿Qué significa 'HODL'?",
            "options": ["Vender rápido", "Mantener a toda costa", "Comerciar diario", "Comprar más"],
            "correct": 1,
            "explanation": "¡HODL significa mantener tu Bitcoin a largo plazo, sin importar los cambios de precio!"
        },
        {
            "question": "¿Qué es una billetera Bitcoin?",
            "options": ["Una cartera de cuero", "Una cuenta bancaria", "Software para guardar tus claves Bitcoin", "Un sitio web"],
            "correct": 2,
            "explanation": "Una billetera Bitcoin es software que guarda tus claves privadas, que te permiten acceder y enviar tu Bitcoin."
        },
        {
            "question": "¿Quién controla Bitcoin?",
            "options": ["El gobierno", "Una empresa", "Los bancos", "Nadie - es descentralizado"],
            "correct": 3,
            "explanation": "¡Bitcoin es descentralizado! Ninguna persona, empresa o gobierno lo controla."
        },
        {
            "question": "¿Cómo se llama la billetera oficial de Bitcoin de El Salvador?",
            "options": ["Chivo Wallet", "Bitcoin SV", "Salvadoran Coin", "ES Wallet"],
            "correct": 0,
            "explanation": "¡Chivo Wallet es la aplicación oficial de billetera Bitcoin de El Salvador!"
        },
        {
            "question": "¿Por qué se compara Bitcoin con el 'oro digital'?",
            "options": ["Es de color amarillo", "Es escaso y valioso", "Se puede excavar", "Los bancos lo aman"],
            "correct": 1,
            "explanation": "¡Como el oro, Bitcoin es escaso (oferta limitada) y puede almacenar valor con el tiempo!"
        }
    ]
}

# Educational content
LESSONS = {
    "en": {
        "basics": {
            "title": "Bitcoin Basics",
            "content": [
                {
                    "topic": "What is Bitcoin?",
                    "text": """
                    Bitcoin is **digital money** that works without banks! 🏦❌
                    
                    Think of it like this:
                    - **Regular money**: You need a bank to send it to someone
                    - **Bitcoin**: You can send it directly, like handing cash but over the internet!
                    
                    Bitcoin was created in 2009 by someone named Satoshi Nakamoto (we don't know who they really are - it's a mystery! 🕵️)
                    """,
                    "key_points": ["Digital money", "No banks needed", "Created in 2009", "Only 21 million will exist"]
                },
                {
                    "topic": "Why 21 Million?",
                    "text": """
                    Unlike dollars or colones, no one can print more Bitcoin! 🖨️❌
                    
                    **Only 21 million Bitcoin will EVER exist.** This is written in the code and can't be changed.
                    
                    Why does this matter?
                    - When governments print more money, your savings lose value (inflation 📉)
                    - Bitcoin can't be inflated - it's like digital gold! 🥇
                    """,
                    "key_points": ["Fixed supply", "Can't be printed", "Protection from inflation", "Digital gold"]
                },
                {
                    "topic": "Satoshis - Bitcoin's Small Change",
                    "text": """
                    Don't worry if you can't afford a whole Bitcoin! 💰
                    
                    Each Bitcoin can be divided into **100 million tiny pieces** called **satoshis** (or 'sats').
                    
                    Example:
                    - 1 Bitcoin = 100,000,000 satoshis
                    - Even $1 can buy you thousands of sats!
                    
                    In El Salvador, many people save in satoshis - it's called "stacking sats!" 📚
                    """,
                    "key_points": ["1 BTC = 100M sats", "Anyone can start small", "Stacking sats is saving"]
                }
            ]
        },
        "wallet": {
            "title": "Wallet Security",
            "content": [
                {
                    "topic": "What is a Bitcoin Wallet?",
                    "text": """
                    A Bitcoin wallet is like a special app that holds your Bitcoin keys! 🔑
                    
                    **Important**: Your wallet doesn't actually store Bitcoin - it stores the **keys** that prove the Bitcoin is yours.
                    
                    Think of it like:
                    - The Bitcoin network is like a big, shared notebook 📓
                    - Your wallet holds the special pen that only YOU can use to write in your section
                    """,
                    "key_points": ["Stores keys, not coins", "Private key = your proof", "Many wallet options exist"]
                },
                {
                    "topic": "Seed Phrase - Your Master Key",
                    "text": """
                    When you create a wallet, you get a **seed phrase** - usually 12 or 24 words.
                    
                    ⚠️ **SUPER IMPORTANT** ⚠️
                    - NEVER share your seed phrase with anyone!
                    - Write it on paper (not digitally)
                    - Store it somewhere safe
                    - If someone gets your seed phrase, they can take ALL your Bitcoin!
                    
                    Your seed phrase is like the master key to your treasure! 🗝️💎
                    """,
                    "key_points": ["12-24 words", "Never share", "Write on paper", "Store safely"]
                },
                {
                    "topic": "Chivo Wallet in El Salvador",
                    "text": """
                    El Salvador has its own official Bitcoin wallet: **Chivo Wallet** 🐐
                    
                    Features:
                    - Free to use for all Salvadorans
                    - Send Bitcoin or USD instantly
                    - No fees for transactions
                    - Government gave $30 in Bitcoin to each user who signed up!
                    
                    You can use Chivo to pay at stores, send money to family, or save for the future!
                    """,
                    "key_points": ["Official SV wallet", "Free transactions", "BTC and USD", "$30 bonus for signups"]
                }
            ]
        },
        "history": {
            "title": "History of Money",
            "content": [
                {
                    "topic": "Before Money - Barter System",
                    "text": """
                    Long ago, people traded things directly! 🔄
                    
                    **Barter**: "I'll give you 3 chickens for your bag of corn"
                    
                    Problems with barter:
                    - What if you have chickens but the corn seller wants fish? 🐔➡️🌽❌
                    - How do you save chickens for later? They get old!
                    - How many chickens = one cow? It's confusing!
                    
                    People needed something better... 🤔
                    """,
                    "key_points": ["Direct trade", "Hard to match wants", "Can't save easily", "Needed improvement"]
                },
                {
                    "topic": "Gold and Silver",
                    "text": """
                    Gold became money because it's **scarce** and **durable**! ✨
                    
                    Why gold worked:
                    - Rare - can't just find it everywhere
                    - Doesn't rot or rust
                    - Easy to divide into coins
                    - Everyone agreed it was valuable
                    
                    For thousands of years, gold = wealth! But it was heavy to carry... 🏋️
                    """,
                    "key_points": ["Scarce", "Durable", "Divisible", "Universally valued"]
                },
                {
                    "topic": "Paper Money and Banks",
                    "text": """
                    Paper money started as receipts for gold stored in banks! 🏦
                    
                    The problem? Banks started printing MORE receipts than gold they had! 
                    
                    Today's money:
                    - Not backed by gold anymore (since 1971)
                    - Governments can print as much as they want
                    - This causes **inflation** - your money buys less over time 📉
                    
                    In some countries, inflation is so bad that money becomes almost worthless!
                    """,
                    "key_points": ["Started as gold receipts", "No longer backed by gold", "Can be printed infinitely", "Causes inflation"]
                },
                {
                    "topic": "Enter Bitcoin - Digital Scarcity",
                    "text": """
                    In 2009, Bitcoin solved the printing problem! 💡
                    
                    Bitcoin combines the best of everything:
                    - **Scarce like gold** - only 21 million ever
                    - **Easy to send like digital money** - instant, worldwide
                    - **No bank needed** - you control it yourself
                    - **Can't be faked** - cryptography keeps it secure
                    
                    El Salvador saw this potential and made history in 2021! 🇸🇻
                    """,
                    "key_points": ["Combines best features", "Digital gold", "Self-custody", "El Salvador pioneer"]
                }
            ]
        }
    },
    "es": {
        "basics": {
            "title": "Fundamentos de Bitcoin",
            "content": [
                {
                    "topic": "¿Qué es Bitcoin?",
                    "text": """
                    ¡Bitcoin es **dinero digital** que funciona sin bancos! 🏦❌
                    
                    Piénsalo así:
                    - **Dinero regular**: Necesitas un banco para enviarlo a alguien
                    - **Bitcoin**: ¡Puedes enviarlo directamente, como dar efectivo pero por internet!
                    
                    Bitcoin fue creado en 2009 por alguien llamado Satoshi Nakamoto (no sabemos quién es realmente - ¡es un misterio! 🕵️)
                    """,
                    "key_points": ["Dinero digital", "Sin bancos necesarios", "Creado en 2009", "Solo existirán 21 millones"]
                },
                {
                    "topic": "¿Por qué 21 Millones?",
                    "text": """
                    ¡A diferencia de dólares o colones, nadie puede imprimir más Bitcoin! 🖨️❌
                    
                    **Solo 21 millones de Bitcoin existirán SIEMPRE.** Esto está escrito en el código y no se puede cambiar.
                    
                    ¿Por qué importa esto?
                    - Cuando los gobiernos imprimen más dinero, tus ahorros pierden valor (inflación 📉)
                    - Bitcoin no puede ser inflado - ¡es como oro digital! 🥇
                    """,
                    "key_points": ["Oferta fija", "No se puede imprimir", "Protección contra inflación", "Oro digital"]
                },
                {
                    "topic": "Satoshis - El Cambio Pequeño de Bitcoin",
                    "text": """
                    ¡No te preocupes si no puedes comprar un Bitcoin completo! 💰
                    
                    Cada Bitcoin se puede dividir en **100 millones de pedacitos** llamados **satoshis** (o 'sats').
                    
                    Ejemplo:
                    - 1 Bitcoin = 100,000,000 satoshis
                    - ¡Incluso $1 te puede comprar miles de sats!
                    
                    En El Salvador, muchas personas ahorran en satoshis - ¡se llama "apilar sats"! 📚
                    """,
                    "key_points": ["1 BTC = 100M sats", "Cualquiera puede empezar pequeño", "Apilar sats es ahorrar"]
                }
            ]
        },
        "wallet": {
            "title": "Seguridad de Billetera",
            "content": [
                {
                    "topic": "¿Qué es una Billetera Bitcoin?",
                    "text": """
                    ¡Una billetera Bitcoin es como una app especial que guarda tus claves Bitcoin! 🔑
                    
                    **Importante**: Tu billetera no guarda Bitcoin realmente - guarda las **claves** que prueban que el Bitcoin es tuyo.
                    
                    Piénsalo como:
                    - La red Bitcoin es como un gran cuaderno compartido 📓
                    - Tu billetera tiene el bolígrafo especial que solo TÚ puedes usar para escribir en tu sección
                    """,
                    "key_points": ["Guarda claves, no monedas", "Clave privada = tu prueba", "Existen muchas opciones de billetera"]
                },
                {
                    "topic": "Frase Semilla - Tu Llave Maestra",
                    "text": """
                    Cuando creas una billetera, obtienes una **frase semilla** - usualmente 12 o 24 palabras.
                    
                    ⚠️ **SÚPER IMPORTANTE** ⚠️
                    - ¡NUNCA compartas tu frase semilla con nadie!
                    - Escríbela en papel (no digitalmente)
                    - Guárdala en un lugar seguro
                    - ¡Si alguien obtiene tu frase semilla, pueden tomar TODO tu Bitcoin!
                    
                    ¡Tu frase semilla es como la llave maestra de tu tesoro! 🗝️💎
                    """,
                    "key_points": ["12-24 palabras", "Nunca compartir", "Escribir en papel", "Guardar seguro"]
                },
                {
                    "topic": "Chivo Wallet en El Salvador",
                    "text": """
                    El Salvador tiene su propia billetera Bitcoin oficial: **Chivo Wallet** 🐐
                    
                    Características:
                    - Gratis para todos los salvadoreños
                    - Envía Bitcoin o USD instantáneamente
                    - Sin comisiones por transacciones
                    - ¡El gobierno dio $30 en Bitcoin a cada usuario que se registró!
                    
                    ¡Puedes usar Chivo para pagar en tiendas, enviar dinero a la familia, o ahorrar para el futuro!
                    """,
                    "key_points": ["Billetera oficial SV", "Transacciones gratis", "BTC y USD", "Bono de $30 por registro"]
                }
            ]
        },
        "history": {
            "title": "Historia del Dinero",
            "content": [
                {
                    "topic": "Antes del Dinero - Sistema de Trueque",
                    "text": """
                    ¡Hace mucho tiempo, la gente intercambiaba cosas directamente! 🔄
                    
                    **Trueque**: "Te doy 3 gallinas por tu bolsa de maíz"
                    
                    Problemas con el trueque:
                    - ¿Qué pasa si tienes gallinas pero el vendedor de maíz quiere pescado? 🐔➡️🌽❌
                    - ¿Cómo guardas gallinas para después? ¡Se hacen viejas!
                    - ¿Cuántas gallinas = una vaca? ¡Es confuso!
                    
                    La gente necesitaba algo mejor... 🤔
                    """,
                    "key_points": ["Intercambio directo", "Difícil coincidir deseos", "No se puede ahorrar fácil", "Necesitaba mejora"]
                },
                {
                    "topic": "Oro y Plata",
                    "text": """
                    ¡El oro se convirtió en dinero porque es **escaso** y **duradero**! ✨
                    
                    Por qué funcionó el oro:
                    - Raro - no lo encuentras en todas partes
                    - No se pudre ni oxida
                    - Fácil de dividir en monedas
                    - Todos acordaron que era valioso
                    
                    ¡Por miles de años, oro = riqueza! Pero era pesado para cargar... 🏋️
                    """,
                    "key_points": ["Escaso", "Duradero", "Divisible", "Universalmente valorado"]
                },
                {
                    "topic": "Dinero de Papel y Bancos",
                    "text": """
                    ¡El dinero de papel empezó como recibos por oro guardado en bancos! 🏦
                    
                    ¿El problema? ¡Los bancos empezaron a imprimir MÁS recibos que oro tenían!
                    
                    El dinero de hoy:
                    - Ya no está respaldado por oro (desde 1971)
                    - Los gobiernos pueden imprimir cuanto quieran
                    - Esto causa **inflación** - tu dinero compra menos con el tiempo 📉
                    
                    ¡En algunos países, la inflación es tan mala que el dinero se vuelve casi sin valor!
                    """,
                    "key_points": ["Empezó como recibos de oro", "Ya no respaldado por oro", "Se puede imprimir infinitamente", "Causa inflación"]
                },
                {
                    "topic": "Entra Bitcoin - Escasez Digital",
                    "text": """
                    ¡En 2009, Bitcoin resolvió el problema de la impresión! 💡
                    
                    Bitcoin combina lo mejor de todo:
                    - **Escaso como el oro** - solo 21 millones siempre
                    - **Fácil de enviar como dinero digital** - instantáneo, mundial
                    - **Sin banco necesario** - tú lo controlas
                    - **No se puede falsificar** - la criptografía lo mantiene seguro
                    
                    ¡El Salvador vio este potencial e hizo historia en 2021! 🇸🇻
                    """,
                    "key_points": ["Combina mejores características", "Oro digital", "Auto-custodia", "El Salvador pionero"]
                }
            ]
        }
    }
}

# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

def init_session_state():
    """Initialize all session state variables"""
    if "language" not in st.session_state:
        st.session_state.language = "es"  # Default to Spanish for El Salvador
    if "xp" not in st.session_state:
        st.session_state.xp = 0
    if "level" not in st.session_state:
        st.session_state.level = 1
    if "streak" not in st.session_state:
        st.session_state.streak = 0
    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = []
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    if "current_quiz_index" not in st.session_state:
        st.session_state.current_quiz_index = 0
    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = False
    if "btc_balance" not in st.session_state:
        st.session_state.btc_balance = 0.001  # Start with some sats for simulation
    if "transactions" not in st.session_state:
        st.session_state.transactions = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "budget_data" not in st.session_state:
        st.session_state.budget_data = {
            "income": 0,
            "expenses": [],
            "savings_goal": 100
        }
    if "story_chapter" not in st.session_state:
        st.session_state.story_chapter = 0
    if "current_story" not in st.session_state:
        st.session_state.current_story = 0
    if "achievements" not in st.session_state:
        st.session_state.achievements = []
    if "btc_price" not in st.session_state:
        st.session_state.btc_price = None
    if "last_price_fetch" not in st.session_state:
        st.session_state.last_price_fetch = None

init_session_state()

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_text(key):
    """Get translated text for current language"""
    lang = st.session_state.language
    keys = key.split(".")
    value = TRANSLATIONS[lang]
    for k in keys:
        value = value[k]
    return value

def add_xp(amount):
    """Add XP and check for level up"""
    st.session_state.xp += amount
    # Level up every 100 XP
    new_level = (st.session_state.xp // 100) + 1
    if new_level > st.session_state.level:
        st.session_state.level = new_level
        st.balloons()
        return True
    return False

def get_bitcoin_price():
    """Fetch current Bitcoin price from CoinGecko"""
    # Cache for 5 minutes
    now = datetime.now()
    if st.session_state.btc_price and st.session_state.last_price_fetch:
        if (now - st.session_state.last_price_fetch).seconds < 300:
            return st.session_state.btc_price
    
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bitcoin", "vs_currencies": "usd"},
            timeout=5
        )
        if response.status_code == 200:
            price = response.json()["bitcoin"]["usd"]
            st.session_state.btc_price = price
            st.session_state.last_price_fetch = now
            return price
    except:
        pass
    return st.session_state.btc_price or 100000  # Fallback

def format_btc(amount):
    """Format BTC amount nicely"""
    if amount >= 0.001:
        return f"₿{amount:.8f}"
    else:
        sats = int(amount * 100_000_000)
        return f"{sats:,} sats"

def simulate_ai_response(question, lang):
    """Simulate AI tutor response (replace with real Grok API call)"""
    # This would be replaced with actual Grok/xAI API call
    responses = {
        "en": {
            "default": "That's a great question about Bitcoin! Let me explain...",
            "wallet": "A Bitcoin wallet is like a digital vault for your Bitcoin keys. Remember, you don't store actual Bitcoin in it - you store the keys that prove ownership!",
            "price": f"Bitcoin's price changes constantly. Right now it's around ${get_bitcoin_price():,.2f}. Remember, you can buy tiny amounts called satoshis!",
            "salvador": "El Salvador made history in 2021 as the first country to make Bitcoin legal tender! The government created Chivo Wallet to help everyone participate.",
            "satoshi": "A satoshi is the smallest unit of Bitcoin - there are 100 million satoshis in 1 Bitcoin! Even with a few dollars, you can own thousands of sats."
        },
        "es": {
            "default": "¡Esa es una gran pregunta sobre Bitcoin! Déjame explicarte...",
            "wallet": "Una billetera Bitcoin es como una bóveda digital para tus claves Bitcoin. ¡Recuerda, no guardas Bitcoin real en ella - guardas las claves que prueban propiedad!",
            "price": f"El precio de Bitcoin cambia constantemente. Ahora mismo está alrededor de ${get_bitcoin_price():,.2f}. ¡Recuerda, puedes comprar cantidades pequeñas llamadas satoshis!",
            "salvador": "¡El Salvador hizo historia en 2021 como el primer país en hacer Bitcoin moneda legal! El gobierno creó Chivo Wallet para ayudar a todos a participar.",
            "satoshi": "Un satoshi es la unidad más pequeña de Bitcoin - ¡hay 100 millones de satoshis en 1 Bitcoin! Incluso con unos pocos dólares, puedes tener miles de sats."
        }
    }
    
    question_lower = question.lower()
    if "wallet" in question_lower or "billetera" in question_lower:
        return responses[lang]["wallet"]
    elif "price" in question_lower or "precio" in question_lower:
        return responses[lang]["price"]
    elif "salvador" in question_lower:
        return responses[lang]["salvador"]
    elif "satoshi" in question_lower or "sat" in question_lower:
        return responses[lang]["satoshi"]
    else:
        return responses[lang]["default"]

# =============================================================================
# UI COMPONENTS
# =============================================================================

def render_sidebar():
    """Render the sidebar with progress and settings"""
    with st.sidebar:
        # Language selector
        st.selectbox(
            "🌐 Language / Idioma",
            options=["es", "en"],
            format_func=lambda x: "🇸🇻 Español" if x == "es" else "🇺🇸 English",
            key="language"
        )
        
        st.divider()
        
        # Progress section
        st.subheader(f"📊 {get_text('progress')}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric(get_text("level"), st.session_state.level)
        with col2:
            st.metric(get_text("xp"), st.session_state.xp)
        
        # XP Progress bar to next level
        xp_to_next = 100 - (st.session_state.xp % 100)
        st.progress((100 - xp_to_next) / 100)
        st.caption(f"{xp_to_next} XP to next level")
        
        st.metric(f"🔥 {get_text('streak')}", st.session_state.streak)
        
        st.divider()
        
        # Bitcoin price widget
        price = get_bitcoin_price()
        st.subheader(f"📈 {get_text('current_price')}")
        st.metric("Bitcoin (BTC)", f"${price:,.2f}")
        
        st.divider()
        
        # Achievements
        st.subheader(f"🏆 {get_text('achievements')}")
        achievements_display = {
            "first_lesson": "📖 First Lesson",
            "quiz_master": "🎯 Quiz Master",
            "hodler": "💎 HODLer",
            "storyteller": "📚 Story Lover",
            "budgeter": "💰 Budget Pro"
        }
        
        if st.session_state.achievements:
            for ach in st.session_state.achievements:
                st.success(achievements_display.get(ach, ach))
        else:
            st.info("Complete modules to earn achievements!")

def render_home():
    """Render the home/welcome screen"""
    st.title(f"₿ {get_text('title')} 🇸🇻")
    st.subheader(get_text("subtitle"))
    
    # Welcome message with character
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #f5af19 0%, #f12711 100%); 
                padding: 20px; border-radius: 15px; color: white; text-align: center;'>
        <h2>{get_text('welcome')}</h2>
        <p style='font-size: 48px;'>👧🏽💭₿</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Module selection
    st.subheader(f"📚 {get_text('select_module')}")
    
    cols = st.columns(3)
    
    modules = [
        ("basics", "₿", "Learn the fundamentals"),
        ("wallet", "👛", "Keep your Bitcoin safe"),
        ("history", "📜", "From barter to Bitcoin"),
        ("budget", "💰", "Manage your money"),
        ("simulator", "🔄", "Practice transactions"),
        ("quiz", "❓", "Test your knowledge"),
        ("story", "📖", "Fun Bitcoin stories"),
    ]
    
    for i, (module_id, emoji, desc) in enumerate(modules):
        with cols[i % 3]:
            if st.button(
                f"{emoji} {get_text(f'modules.{module_id}')}",
                key=f"module_{module_id}",
                use_container_width=True
            ):
                st.session_state.current_module = module_id
                st.rerun()

def render_lessons(module):
    """Render educational lesson content"""
    lang = st.session_state.language
    lesson_data = LESSONS[lang].get(module)
    
    if not lesson_data:
        st.warning("Module content coming soon!")
        return
    
    st.title(f"📖 {lesson_data['title']}")
    
    for i, lesson in enumerate(lesson_data["content"]):
        with st.expander(f"📌 {lesson['topic']}", expanded=(i == 0)):
            st.markdown(lesson["text"])
            
            st.markdown("**Key Points:**")
            for point in lesson["key_points"]:
                st.markdown(f"- ✓ {point}")
            
            if st.button(f"✅ Mark Complete", key=f"complete_{module}_{i}"):
                lesson_id = f"{module}_{i}"
                if lesson_id not in st.session_state.completed_lessons:
                    st.session_state.completed_lessons.append(lesson_id)
                    add_xp(25)
                    
                    # Check for first lesson achievement
                    if "first_lesson" not in st.session_state.achievements:
                        st.session_state.achievements.append("first_lesson")
                        st.success("🏆 Achievement Unlocked: First Lesson!")
                    
                    st.success("+25 XP!")
                    st.rerun()

def render_quiz():
    """Render the quiz module"""
    lang = st.session_state.language
    questions = QUIZ_QUESTIONS[lang]
    
    st.title(f"❓ {get_text('modules.quiz')}")
    
    # Progress
    st.progress((st.session_state.current_quiz_index) / len(questions))
    st.caption(f"Question {st.session_state.current_quiz_index + 1} of {len(questions)}")
    
    if st.session_state.current_quiz_index >= len(questions):
        # Quiz complete
        st.balloons()
        st.success(f"🎉 Quiz Complete! Score: {st.session_state.quiz_score}/{len(questions)}")
        
        if st.session_state.quiz_score >= len(questions) * 0.8:
            if "quiz_master" not in st.session_state.achievements:
                st.session_state.achievements.append("quiz_master")
                st.success("🏆 Achievement Unlocked: Quiz Master!")
        
        if st.button("🔄 Restart Quiz"):
            st.session_state.current_quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.rerun()
        return
    
    # Current question
    q = questions[st.session_state.current_quiz_index]
    
    st.subheader(q["question"])
    
    # Answer options
    for i, option in enumerate(q["options"]):
        if st.button(
            option, 
            key=f"option_{i}",
            disabled=st.session_state.quiz_answered,
            use_container_width=True
        ):
            st.session_state.quiz_answered = True
            if i == q["correct"]:
                st.session_state.quiz_score += 1
                add_xp(20)
                st.success(get_text("correct"))
            else:
                st.error(get_text("incorrect"))
            st.info(f"💡 {q['explanation']}")
    
    if st.session_state.quiz_answered:
        if st.button(get_text("next_question")):
            st.session_state.current_quiz_index += 1
            st.session_state.quiz_answered = False
            st.rerun()

def render_simulator():
    """Render the Bitcoin transaction simulator"""
    st.title(f"🔄 {get_text('modules.simulator')}")
    
    price = get_bitcoin_price()
    
    # Balance display
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            get_text("your_balance"),
            format_btc(st.session_state.btc_balance),
            f"≈ ${st.session_state.btc_balance * price:,.2f}"
        )
    with col2:
        sats = int(st.session_state.btc_balance * 100_000_000)
        st.metric("In Satoshis", f"{sats:,} sats")
    
    st.divider()
    
    # Transaction actions
    tab1, tab2 = st.tabs([f"📤 {get_text('send_btc')}", f"📥 {get_text('receive_btc')}"])
    
    with tab1:
        st.subheader("Send Bitcoin (Simulation)")
        send_amount = st.number_input(
            "Amount (BTC)", 
            min_value=0.0, 
            max_value=st.session_state.btc_balance,
            value=0.0001,
            format="%.8f"
        )
        recipient = st.text_input("Recipient Address (fake for simulation)", "sv1qxyz...demo")
        
        if st.button("📤 Send Transaction"):
            if send_amount > 0 and send_amount <= st.session_state.btc_balance:
                st.session_state.btc_balance -= send_amount
                st.session_state.transactions.append({
                    "type": "send",
                    "amount": send_amount,
                    "to": recipient,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "usd_value": send_amount * price
                })
                add_xp(10)
                st.success(f"✅ Sent {format_btc(send_amount)} successfully!")
                st.rerun()
    
    with tab2:
        st.subheader("Receive Bitcoin (Simulation)")
        st.code("sv1qABC123...YourDemoAddress", language=None)
        st.caption("Share this address to receive Bitcoin (this is a demo)")
        
        receive_amount = st.number_input(
            "Simulate receiving (BTC)",
            min_value=0.0,
            max_value=0.01,
            value=0.0001,
            format="%.8f"
        )
        
        if st.button("📥 Simulate Receive"):
            st.session_state.btc_balance += receive_amount
            st.session_state.transactions.append({
                "type": "receive",
                "amount": receive_amount,
                "from": "External Wallet",
                "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "usd_value": receive_amount * price
            })
            add_xp(10)
            
            if "hodler" not in st.session_state.achievements:
                st.session_state.achievements.append("hodler")
                st.success("🏆 Achievement Unlocked: HODLer!")
            
            st.success(f"✅ Received {format_btc(receive_amount)}!")
            st.rerun()
    
    # Transaction history
    st.divider()
    st.subheader(f"📋 {get_text('transaction_history')}")
    
    if st.session_state.transactions:
        for tx in reversed(st.session_state.transactions[-5:]):
            icon = "📤" if tx["type"] == "send" else "📥"
            color = "red" if tx["type"] == "send" else "green"
            st.markdown(f"""
            {icon} **{tx['type'].upper()}** | {format_btc(tx['amount'])} (${tx['usd_value']:.2f})  
            *{tx['time']}*
            """)
    else:
        st.info("No transactions yet. Try sending or receiving!")

def render_budget_game():
    """Render the budgeting game module"""
    st.title(f"💰 {get_text('modules.budget')}")
    
    lang = st.session_state.language
    
    if lang == "es":
        st.markdown("""
        ### 🎮 ¡Aprende a Presupuestar!
        Imagina que tienes un trabajo de medio tiempo y ganas $200 al mes.
        ¿Puedes ahorrar para comprar tus primeros satoshis?
        """)
    else:
        st.markdown("""
        ### 🎮 Learn to Budget!
        Imagine you have a part-time job and earn $200 per month.
        Can you save up to buy your first satoshis?
        """)
    
    # Income
    income = st.slider(
        get_text("income") + " ($)", 
        min_value=100, 
        max_value=500, 
        value=200,
        step=25
    )
    
    st.subheader(get_text("expenses"))
    
    # Expense categories
    expenses = {}
    expense_categories = {
        "en": ["Food", "Transportation", "Entertainment", "Phone/Internet", "Clothing"],
        "es": ["Comida", "Transporte", "Entretenimiento", "Teléfono/Internet", "Ropa"]
    }
    
    cols = st.columns(2)
    for i, category in enumerate(expense_categories[lang]):
        with cols[i % 2]:
            expenses[category] = st.slider(
                f"{category} ($)",
                min_value=0,
                max_value=100,
                value=30,
                step=5
            )
    
    total_expenses = sum(expenses.values())
    savings = income - total_expenses
    
    st.divider()
    
    # Results
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(get_text("income"), f"${income}")
    with col2:
        st.metric(get_text("expenses"), f"${total_expenses}")
    with col3:
        st.metric(
            get_text("savings"), 
            f"${savings}",
            delta=f"{(savings/income*100):.0f}%" if income > 0 else "0%"
        )
    
    # Savings goal visualization
    price = get_bitcoin_price()
    sats_can_buy = int((savings / price) * 100_000_000) if savings > 0 else 0
    
    st.subheader("🎯 " + (f"¡Con ${savings} puedes comprar {sats_can_buy:,} satoshis!" if lang == "es" 
                         else f"With ${savings} you can buy {sats_can_buy:,} satoshis!"))
    
    if savings > 0:
        st.progress(min(savings / 100, 1.0))
        
        if savings >= 50:
            st.success("🌟 " + ("¡Excelente trabajo ahorrando!" if lang == "es" else "Excellent saving!"))
            if "budgeter" not in st.session_state.achievements:
                st.session_state.achievements.append("budgeter")
                add_xp(50)
                st.success("🏆 Achievement Unlocked: Budget Pro!")
    elif savings < 0:
        st.error("⚠️ " + ("¡Cuidado! Estás gastando más de lo que ganas." if lang == "es" 
                         else "Warning! You're spending more than you earn."))
    
    # Tips
    with st.expander("💡 " + ("Consejos de Ahorro" if lang == "es" else "Saving Tips")):
        tips = {
            "en": [
                "Try to save at least 20% of your income",
                "Track every expense - small purchases add up!",
                "Consider 'stacking sats' - regular small Bitcoin purchases",
                "Needs vs Wants: Always prioritize necessities",
                "Emergency fund first, then investment savings"
            ],
            "es": [
                "Intenta ahorrar al menos 20% de tus ingresos",
                "Registra cada gasto - ¡las compras pequeñas se acumulan!",
                "Considera 'apilar sats' - compras pequeñas regulares de Bitcoin",
                "Necesidades vs Deseos: Siempre prioriza lo necesario",
                "Primero fondo de emergencia, luego ahorros de inversión"
            ]
        }
        for tip in tips[lang]:
            st.markdown(f"- {tip}")

def render_story():
    """Render the story/narrative module"""
    lang = st.session_state.language
    stories = STORIES[lang]
    
    st.title(f"📖 {get_text('modules.story')}")
    
    # Story selector
    story_titles = [s["title"] for s in stories]
    selected_story = st.selectbox(
        "Choose a story" if lang == "en" else "Elige una historia",
        options=range(len(stories)),
        format_func=lambda x: story_titles[x]
    )
    
    story = stories[selected_story]
    
    st.subheader(f"📚 {story['title']}")
    st.caption(f"Featuring: {story['character']}")
    
    st.divider()
    
    # Chapter navigation
    total_chapters = len(story["chapters"])
    chapter_idx = st.session_state.story_chapter % total_chapters
    chapter = story["chapters"][chapter_idx]
    
    # Story display
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 30px; border-radius: 15px; color: white; text-align: center;
                font-size: 48px; margin-bottom: 20px;'>
        {chapter['image_emoji']}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"### Chapter {chapter_idx + 1}")
    st.markdown(f"*{chapter['text']}*")
    
    # Lesson learned
    with st.expander("💡 " + ("Lección" if lang == "es" else "Lesson"), expanded=True):
        st.info(chapter["lesson"])
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if chapter_idx > 0:
            if st.button("⬅️ Previous"):
                st.session_state.story_chapter -= 1
                st.rerun()
    
    with col2:
        st.progress((chapter_idx + 1) / total_chapters)
        st.caption(f"Chapter {chapter_idx + 1} of {total_chapters}")
    
    with col3:
        if chapter_idx < total_chapters - 1:
            if st.button("Next ➡️"):
                st.session_state.story_chapter += 1
                add_xp(15)
                st.rerun()
        else:
            if st.button("🎉 Finish"):
                add_xp(30)
                if "storyteller" not in st.session_state.achievements:
                    st.session_state.achievements.append("storyteller")
                    st.success("🏆 Achievement Unlocked: Story Lover!")
                st.session_state.story_chapter = 0
                st.balloons()
                st.rerun()

def render_ai_tutor():
    """Render the AI tutor chat interface"""
    lang = st.session_state.language
    
    st.subheader("🤖 " + ("Pregúntale a Grok" if lang == "es" else "Ask Grok"))
    st.caption("AI-powered Bitcoin tutor" if lang == "en" else "Tutor de Bitcoin con IA")
    
    # Chat container
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state.chat_history[-5:]:  # Show last 5 messages
            if msg["role"] == "user":
                st.chat_message("user").write(msg["content"])
            else:
                st.chat_message("assistant").write(msg["content"])
    
    # Input
    user_input = st.chat_input(get_text("ask_grok"))
    
    if user_input:
        # Add user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Generate response (replace with real API call)
        response = simulate_ai_response(user_input, lang)
        
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })
        
        add_xp(5)
        st.rerun()

# =============================================================================
# MAIN APP
# =============================================================================

def main():
    """Main application entry point"""
    
    # Sidebar
    render_sidebar()
    
    # Initialize current module if not set
    if "current_module" not in st.session_state:
        st.session_state.current_module = "home"
    
    # Module navigation
    module = st.session_state.current_module
    
    # Back button (except on home)
    if module != "home":
        if st.button("← Back to Home" if st.session_state.language == "en" else "← Volver al Inicio"):
            st.session_state.current_module = "home"
            st.rerun()
    
    # Render appropriate module
    if module == "home":
        render_home()
    elif module in ["basics", "wallet", "history"]:
        render_lessons(module)
    elif module == "quiz":
        render_quiz()
    elif module == "simulator":
        render_simulator()
    elif module == "budget":
        render_budget_game()
    elif module == "story":
        render_story()
    
    # AI Tutor always available at bottom
    st.divider()
    render_ai_tutor()
    
    # Footer
    st.markdown("---")
    st.caption("""
    🇸🇻 BitcoinEd El Salvador | Supporting the "What Is Money?" Program  
    Inspired by Lina Seiche's "The Little HODLer" | Complementing El Salvador's Bitcoin Education Initiative
    """)

if __name__ == "__main__":
    main()
