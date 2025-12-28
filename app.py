"""
Bitcoin Financial Literacy App for El Salvador
A bilingual (Spanish/English) educational platform for learning about Bitcoin
"""

import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import random
import json
import os
from openai import OpenAI

# ============================================================================
# TRANSLATIONS - Bilingual Support (Spanish/English)
# ============================================================================

TRANSLATIONS = {
    "en": {
        # Navigation
        "app_title": "🟠 Bitcoin Literacy El Salvador",
        "welcome": "Welcome to Bitcoin Education!",
        "select_module": "Select a Learning Module",
        "language": "Language",

        # Modules
        "module_basics": "₿ Bitcoin Basics",
        "module_wallet": "🔐 Wallet Security",
        "module_history": "📜 History of Money",
        "module_budget": "💰 Budgeting Game",
        "module_simulator": "⚡ Transaction Simulator",
        "module_quiz": "🎯 Quiz Challenge",
        "module_stories": "📖 Bitcoin Stories",
        "module_tutor": "🤖 AI Tutor",

        # Gamification
        "your_progress": "Your Progress",
        "level": "Level",
        "xp": "XP",
        "achievements": "Achievements",
        "xp_earned": "XP Earned!",

        # Bitcoin Basics
        "what_is_bitcoin": "What is Bitcoin?",
        "bitcoin_intro": """
Bitcoin is digital money that works without banks or governments.
It was created in 2009 by someone using the name Satoshi Nakamoto.

**Key Features:**
- 🌐 **Decentralized**: No single person or company controls it
- 🔒 **Secure**: Protected by advanced mathematics (cryptography)
- 💎 **Scarce**: Only 21 million Bitcoin will ever exist
- ⚡ **Fast**: Send money anywhere in the world in minutes
- 💸 **Low Fees**: Especially with Lightning Network
        """,
        "why_el_salvador": "Why El Salvador Adopted Bitcoin",
        "el_salvador_reasons": """
In September 2021, El Salvador became the first country to adopt Bitcoin as legal tender!

**Benefits for Salvadorans:**
- 📱 70% of citizens didn't have bank accounts - now they can save and transact
- 💵 Remittances: $6 billion sent home yearly with lower fees
- 🌍 Financial inclusion for everyone
- 🏦 Independence from traditional banking system
        """,

        # Wallet Security
        "wallet_title": "Secure Your Bitcoin Wallet",
        "seed_phrase": "Seed Phrase (12-24 words)",
        "seed_warning": "⚠️ NEVER share your seed phrase with anyone!",
        "security_tips": """
**Essential Security Tips:**

1. 📝 **Write down your seed phrase** on paper (not digital!)
2. 🔒 **Store it safely** - consider a fireproof safe
3. 🚫 **Never share** your private keys or seed phrase
4. 🔐 **Use strong PINs** - avoid birthdays or simple patterns
5. 📱 **Keep your phone secure** - use screen lock
6. ⚠️ **Beware of scams** - Bitcoin transactions cannot be reversed!
        """,
        "wallet_types": "Types of Wallets",
        "hot_wallet": "🔥 Hot Wallet (On your phone - convenient but less secure)",
        "cold_wallet": "❄️ Cold Wallet (Hardware device - most secure for savings)",

        # History of Money
        "history_title": "The Evolution of Money",
        "history_intro": "Money has evolved over thousands of years...",
        "barter": "🔄 Barter System",
        "barter_desc": "Trading goods directly (5000+ years ago)",
        "commodity": "🐚 Commodity Money",
        "commodity_desc": "Salt, shells, cattle as currency",
        "metal": "🪙 Metal Coins",
        "metal_desc": "Gold and silver coins (600 BC)",
        "paper": "📄 Paper Money",
        "paper_desc": "Banknotes backed by gold",
        "fiat": "🏦 Fiat Currency",
        "fiat_desc": "Government-issued money (not backed by gold)",
        "crypto": "₿ Cryptocurrency",
        "crypto_desc": "Digital, decentralized money (2009)",

        # Budgeting Game
        "budget_title": "Budgeting Challenge",
        "budget_intro": "Learn to manage your satoshis wisely!",
        "monthly_income": "Monthly Income (satoshis)",
        "allocate_budget": "Allocate Your Budget",
        "needs": "🏠 Needs (rent, food, utilities)",
        "wants": "🎮 Wants (entertainment, dining out)",
        "savings": "💎 Savings (HODL for the future)",
        "emergency": "🚨 Emergency Fund",
        "budget_feedback": "Budget Feedback",
        "good_budget": "✅ Great job! You're saving for the future!",
        "review_budget": "⚠️ Consider saving more for emergencies",

        # Transaction Simulator
        "simulator_title": "Bitcoin Transaction Simulator",
        "simulator_intro": "Practice sending Bitcoin safely (no real BTC used!)",
        "sender_wallet": "Your Wallet Address",
        "recipient_wallet": "Recipient Address",
        "amount_sats": "Amount (satoshis)",
        "network_fee": "Network Fee",
        "send_transaction": "Send Transaction",
        "transaction_success": "✅ Transaction Successful!",
        "transaction_details": "Transaction Details",

        # Quiz
        "quiz_title": "Test Your Knowledge",
        "quiz_intro": "Answer questions to earn XP!",
        "question": "Question",
        "submit_answer": "Submit Answer",
        "correct": "✅ Correct! +10 XP",
        "incorrect": "❌ Incorrect. The correct answer is:",
        "next_question": "Next Question",
        "quiz_complete": "🎉 Quiz Complete!",

        # Stories
        "stories_title": "Bitcoin Stories",
        "stories_intro": "Learn through stories inspired by 'The Little HODLer'",
        "story_1_title": "🌟 Maria's First Satoshis",
        "story_1": """
Maria lived in a small village in El Salvador. She had never had a bank account
because the nearest bank was too far away. One day, her cousin in the United States
sent her some Bitcoin using the Lightning Network.

"What is this?" Maria asked her friend Carlos.

"It's digital money," Carlos explained. "You can save it, spend it, or send it
to anyone in the world - all from your phone!"

Maria learned to use her Chivo wallet. She started saving small amounts of satoshis
each week. "Each satoshi is like a tiny seed," she thought. "If I'm patient and HODL,
my seeds will grow into a beautiful garden."

**Lesson**: Bitcoin gives everyone access to financial tools, no matter where they live.
        """,
        "story_2_title": "🏔️ The Mountain of 21 Million",
        "story_2": """
Young Pedro asked his grandfather, "Why is Bitcoin special?"

Grandfather smiled and told a story: "Imagine a mountain made of exactly 21 million
golden coins. No one can add more coins to the mountain - not kings, not presidents,
not anyone. These coins are divided among everyone who believes in the mountain."

"But what if someone wants more?" asked Pedro.

"That's the beauty," said grandfather. "Because there will only ever be 21 million,
each coin becomes more valuable as more people want them. Unlike the paper money
that governments can print forever, these coins are truly rare."

Pedro understood. "So if I save my coins..."

"They may grow in value over time. That's why we call it 'digital gold.'"

**Lesson**: Bitcoin's fixed supply makes it resistant to inflation.
        """,
        "story_3_title": "⚡ Lightning Fast",
        "story_3": """
Sofia wanted to buy pupusas from Don Roberto's stand. "Do you accept Bitcoin?" she asked.

Don Roberto showed her a QR code. "With Lightning Network, it's instant and almost free!"

Sofia scanned the code with her phone. In less than a second, the payment was complete.

"Amazing!" she said. "In the old days, sending money to my family abroad took days
and cost a lot in fees."

Don Roberto nodded. "Now, whether I'm selling pupusas or receiving payment from a
customer in Japan, it happens in the blink of an eye. That's the power of Lightning!"

**Lesson**: Lightning Network makes Bitcoin fast and cheap for everyday purchases.
        """,

        # AI Tutor
        "tutor_title": "AI Bitcoin Tutor",
        "tutor_intro": "Ask me anything about Bitcoin!",
        "tutor_placeholder": "Type your question here...",
        "tutor_ask": "Ask Question",
        "tutor_response": "AI Response:",
        "tutor_coming_soon": "🤖 AI Tutor coming soon! This will be powered by Grok API.",

        # Price
        "current_price": "Current Bitcoin Price",
        "price_updated": "Last updated",
        "sats_per_dollar": "satoshis per $1 USD",

        # Achievements
        "ach_first_lesson": "📚 First Lesson Complete",
        "ach_security_master": "🔐 Security Master",
        "ach_quiz_champion": "🏆 Quiz Champion",
        "ach_budget_pro": "💰 Budget Pro",
        "ach_story_reader": "📖 Story Reader",
        "ach_great_teacher": "👨‍🏫 Great Teacher",
        "ach_story_explorer": "🗺️ Story Explorer",
        "ach_luna_friend": "🌙 Luna's Friend",

        # Character Tutor Modes
        "select_mode": "Select Mode",
        "learn_with_luna": "🌙 Learn with Luna",
        "teach_pedrito": "👦 Teach Pedrito",
        "adventure_mode": "📖 Adventure",
        "reset_conversation": "Reset Chat",
        "enter_your_name": "Enter your name to begin the adventure:",
        "start_adventure": "Start Adventure",
        "chapter": "Chapter",
        "coming_soon": "Coming Soon",
        "luna_intro": "¡Hola! I'm Luna 🌙 My abuela taught me everything about Bitcoin when the volcanoes started mining! Want me to tell you what I learned?",
        "pedrito_intro": "¡Hola profe! I'm Pedrito 👦 They told me Bitcoin is like magic internet money that comes from volcanoes... is that true? Can you teach me?",
        "teaching_tip": "💡 Tip: Teach Pedrito about Bitcoin! Use terms like '21 million', 'decentralized', 'satoshi', 'wallet', 'blockchain' to earn bonus XP!",
        "great_teaching": "🎉 Great teaching! Pedrito understood! +15 XP",
        "adventure_intro": "Welcome to the Bitcoin Adventure! You'll join Luna on an exciting journey through El Salvador learning about Bitcoin.",
        "chapter_1_title": "First Satoshis",
        "chapter_2_title": "The Chivo Wallet",
        "chapter_3_title": "Lightning Speed",
        "chapter_4_title": "The Volcano",
        "chapter_5_title": "Sending Home",
    },
    "es": {
        # Navigation
        "app_title": "🟠 Educación Bitcoin El Salvador",
        "welcome": "¡Bienvenido a la Educación Bitcoin!",
        "select_module": "Selecciona un Módulo de Aprendizaje",
        "language": "Idioma",

        # Modules
        "module_basics": "₿ Fundamentos de Bitcoin",
        "module_wallet": "🔐 Seguridad de Billetera",
        "module_history": "📜 Historia del Dinero",
        "module_budget": "💰 Juego de Presupuesto",
        "module_simulator": "⚡ Simulador de Transacciones",
        "module_quiz": "🎯 Desafío de Preguntas",
        "module_stories": "📖 Historias de Bitcoin",
        "module_tutor": "🤖 Tutor IA",

        # Gamification
        "your_progress": "Tu Progreso",
        "level": "Nivel",
        "xp": "XP",
        "achievements": "Logros",
        "xp_earned": "¡XP Ganado!",

        # Bitcoin Basics
        "what_is_bitcoin": "¿Qué es Bitcoin?",
        "bitcoin_intro": """
Bitcoin es dinero digital que funciona sin bancos ni gobiernos.
Fue creado en 2009 por alguien usando el nombre Satoshi Nakamoto.

**Características Principales:**
- 🌐 **Descentralizado**: Ninguna persona o empresa lo controla
- 🔒 **Seguro**: Protegido por matemáticas avanzadas (criptografía)
- 💎 **Escaso**: Solo existirán 21 millones de Bitcoin
- ⚡ **Rápido**: Envía dinero a cualquier parte del mundo en minutos
- 💸 **Bajas Comisiones**: Especialmente con Lightning Network
        """,
        "why_el_salvador": "Por qué El Salvador Adoptó Bitcoin",
        "el_salvador_reasons": """
¡En septiembre de 2021, El Salvador se convirtió en el primer país en adoptar Bitcoin como moneda de curso legal!

**Beneficios para los Salvadoreños:**
- 📱 70% de los ciudadanos no tenían cuentas bancarias - ahora pueden ahorrar y hacer transacciones
- 💵 Remesas: $6 mil millones enviados a casa anualmente con menores comisiones
- 🌍 Inclusión financiera para todos
- 🏦 Independencia del sistema bancario tradicional
        """,

        # Wallet Security
        "wallet_title": "Asegura tu Billetera Bitcoin",
        "seed_phrase": "Frase Semilla (12-24 palabras)",
        "seed_warning": "⚠️ ¡NUNCA compartas tu frase semilla con nadie!",
        "security_tips": """
**Consejos Esenciales de Seguridad:**

1. 📝 **Escribe tu frase semilla** en papel (¡no digital!)
2. 🔒 **Guárdala segura** - considera una caja fuerte a prueba de fuego
3. 🚫 **Nunca compartas** tus claves privadas o frase semilla
4. 🔐 **Usa PINs fuertes** - evita cumpleaños o patrones simples
5. 📱 **Mantén tu teléfono seguro** - usa bloqueo de pantalla
6. ⚠️ **Cuidado con las estafas** - ¡las transacciones de Bitcoin no se pueden revertir!
        """,
        "wallet_types": "Tipos de Billeteras",
        "hot_wallet": "🔥 Billetera Caliente (En tu teléfono - conveniente pero menos segura)",
        "cold_wallet": "❄️ Billetera Fría (Dispositivo hardware - más segura para ahorros)",

        # History of Money
        "history_title": "La Evolución del Dinero",
        "history_intro": "El dinero ha evolucionado durante miles de años...",
        "barter": "🔄 Sistema de Trueque",
        "barter_desc": "Intercambio directo de bienes (hace más de 5000 años)",
        "commodity": "🐚 Dinero Mercancía",
        "commodity_desc": "Sal, conchas, ganado como moneda",
        "metal": "🪙 Monedas de Metal",
        "metal_desc": "Monedas de oro y plata (600 AC)",
        "paper": "📄 Papel Moneda",
        "paper_desc": "Billetes respaldados por oro",
        "fiat": "🏦 Moneda Fiat",
        "fiat_desc": "Dinero emitido por el gobierno (no respaldado por oro)",
        "crypto": "₿ Criptomoneda",
        "crypto_desc": "Dinero digital, descentralizado (2009)",

        # Budgeting Game
        "budget_title": "Desafío de Presupuesto",
        "budget_intro": "¡Aprende a administrar tus satoshis sabiamente!",
        "monthly_income": "Ingreso Mensual (satoshis)",
        "allocate_budget": "Asigna tu Presupuesto",
        "needs": "🏠 Necesidades (renta, comida, servicios)",
        "wants": "🎮 Deseos (entretenimiento, salir a comer)",
        "savings": "💎 Ahorros (HODL para el futuro)",
        "emergency": "🚨 Fondo de Emergencia",
        "budget_feedback": "Retroalimentación del Presupuesto",
        "good_budget": "✅ ¡Excelente trabajo! ¡Estás ahorrando para el futuro!",
        "review_budget": "⚠️ Considera ahorrar más para emergencias",

        # Transaction Simulator
        "simulator_title": "Simulador de Transacciones Bitcoin",
        "simulator_intro": "Practica enviando Bitcoin de forma segura (¡no se usa BTC real!)",
        "sender_wallet": "Dirección de tu Billetera",
        "recipient_wallet": "Dirección del Destinatario",
        "amount_sats": "Cantidad (satoshis)",
        "network_fee": "Comisión de Red",
        "send_transaction": "Enviar Transacción",
        "transaction_success": "✅ ¡Transacción Exitosa!",
        "transaction_details": "Detalles de la Transacción",

        # Quiz
        "quiz_title": "Pon a Prueba tu Conocimiento",
        "quiz_intro": "¡Responde preguntas para ganar XP!",
        "question": "Pregunta",
        "submit_answer": "Enviar Respuesta",
        "correct": "✅ ¡Correcto! +10 XP",
        "incorrect": "❌ Incorrecto. La respuesta correcta es:",
        "next_question": "Siguiente Pregunta",
        "quiz_complete": "🎉 ¡Quiz Completado!",

        # Stories
        "stories_title": "Historias de Bitcoin",
        "stories_intro": "Aprende a través de historias inspiradas en 'The Little HODLer'",
        "story_1_title": "🌟 Los Primeros Satoshis de María",
        "story_1": """
María vivía en un pequeño pueblo de El Salvador. Nunca había tenido una cuenta bancaria
porque el banco más cercano estaba muy lejos. Un día, su primo en Estados Unidos
le envió algo de Bitcoin usando la Red Lightning.

"¿Qué es esto?" preguntó María a su amigo Carlos.

"Es dinero digital," explicó Carlos. "¡Puedes ahorrarlo, gastarlo o enviarlo
a cualquier persona en el mundo - todo desde tu teléfono!"

María aprendió a usar su billetera Chivo. Comenzó a ahorrar pequeñas cantidades de satoshis
cada semana. "Cada satoshi es como una pequeña semilla," pensó. "Si soy paciente y hago HODL,
mis semillas crecerán en un hermoso jardín."

**Lección**: Bitcoin da a todos acceso a herramientas financieras, sin importar dónde vivan.
        """,
        "story_2_title": "🏔️ La Montaña de 21 Millones",
        "story_2": """
El joven Pedro le preguntó a su abuelo: "¿Por qué Bitcoin es especial?"

El abuelo sonrió y contó una historia: "Imagina una montaña hecha de exactamente 21 millones
de monedas de oro. Nadie puede agregar más monedas a la montaña - ni reyes, ni presidentes,
nadie. Estas monedas se dividen entre todos los que creen en la montaña."

"¿Pero qué pasa si alguien quiere más?" preguntó Pedro.

"Esa es la belleza," dijo el abuelo. "Como solo habrá 21 millones,
cada moneda se vuelve más valiosa a medida que más personas las quieren. A diferencia del dinero
de papel que los gobiernos pueden imprimir para siempre, estas monedas son verdaderamente raras."

Pedro entendió. "Entonces si guardo mis monedas..."

"Pueden crecer en valor con el tiempo. Por eso lo llamamos 'oro digital.'"

**Lección**: La oferta fija de Bitcoin lo hace resistente a la inflación.
        """,
        "story_3_title": "⚡ Rápido como el Rayo",
        "story_3": """
Sofía quería comprar pupusas del puesto de Don Roberto. "¿Acepta Bitcoin?" preguntó.

Don Roberto le mostró un código QR. "¡Con Lightning Network, es instantáneo y casi gratis!"

Sofía escaneó el código con su teléfono. En menos de un segundo, el pago estaba completo.

"¡Increíble!" dijo. "En los viejos tiempos, enviar dinero a mi familia en el extranjero
tomaba días y costaba mucho en comisiones."

Don Roberto asintió. "Ahora, ya sea que esté vendiendo pupusas o recibiendo pago de un
cliente en Japón, sucede en un abrir y cerrar de ojos. ¡Ese es el poder de Lightning!"

**Lección**: Lightning Network hace que Bitcoin sea rápido y barato para compras diarias.
        """,

        # AI Tutor
        "tutor_title": "Tutor IA de Bitcoin",
        "tutor_intro": "¡Pregúntame cualquier cosa sobre Bitcoin!",
        "tutor_placeholder": "Escribe tu pregunta aquí...",
        "tutor_ask": "Hacer Pregunta",
        "tutor_response": "Respuesta de la IA:",
        "tutor_coming_soon": "🤖 ¡Tutor IA próximamente! Será impulsado por Grok API.",

        # Price
        "current_price": "Precio Actual de Bitcoin",
        "price_updated": "Última actualización",
        "sats_per_dollar": "satoshis por $1 USD",

        # Achievements
        "ach_first_lesson": "📚 Primera Lección Completada",
        "ach_security_master": "🔐 Maestro de Seguridad",
        "ach_quiz_champion": "🏆 Campeón del Quiz",
        "ach_budget_pro": "💰 Profesional del Presupuesto",
        "ach_story_reader": "📖 Lector de Historias",
        "ach_great_teacher": "👨‍🏫 Gran Maestro",
        "ach_story_explorer": "🗺️ Explorador de Historias",
        "ach_luna_friend": "🌙 Amigo de Luna",

        # Character Tutor Modes
        "select_mode": "Selecciona Modo",
        "learn_with_luna": "🌙 Aprende con Luna",
        "teach_pedrito": "👦 Enseña a Pedrito",
        "adventure_mode": "📖 Aventura",
        "reset_conversation": "Reiniciar Chat",
        "enter_your_name": "Escribe tu nombre para comenzar la aventura:",
        "start_adventure": "Iniciar Aventura",
        "chapter": "Capítulo",
        "coming_soon": "Próximamente",
        "luna_intro": "¡Hola! Soy Luna 🌙 Mi abuela me enseñó todo sobre Bitcoin cuando los volcanes empezaron a minar. ¿Quieres que te cuente lo que aprendí?",
        "pedrito_intro": "¡Hola profe! Soy Pedrito 👦 Me dijeron que Bitcoin es como dinero mágico de internet que sale de los volcanes... ¿es verdad? ¿Me puedes enseñar?",
        "teaching_tip": "💡 Consejo: ¡Enséñale a Pedrito sobre Bitcoin! Usa términos como '21 millones', 'descentralizado', 'satoshi', 'billetera', 'blockchain' para ganar XP extra!",
        "great_teaching": "🎉 ¡Excelente enseñanza! ¡Pedrito entendió! +15 XP",
        "adventure_intro": "¡Bienvenido a la Aventura Bitcoin! Acompañarás a Luna en un emocionante viaje por El Salvador aprendiendo sobre Bitcoin.",
        "chapter_1_title": "Primeros Satoshis",
        "chapter_2_title": "La Billetera Chivo",
        "chapter_3_title": "Velocidad Lightning",
        "chapter_4_title": "El Volcán",
        "chapter_5_title": "Enviando a Casa",
    }
}

# Quiz questions in both languages
QUIZ_QUESTIONS = {
    "en": [
        {
            "question": "How many Bitcoin will ever exist?",
            "options": ["21 million", "100 million", "Unlimited", "1 billion"],
            "correct": 0,
            "explanation": "Bitcoin has a fixed supply cap of 21 million coins."
        },
        {
            "question": "What is a 'satoshi'?",
            "options": ["The founder of Bitcoin", "The smallest unit of Bitcoin (0.00000001 BTC)", "A type of wallet", "A mining machine"],
            "correct": 1,
            "explanation": "A satoshi is the smallest unit of Bitcoin, named after its creator."
        },
        {
            "question": "When did El Salvador adopt Bitcoin as legal tender?",
            "options": ["2019", "2020", "2021", "2022"],
            "correct": 2,
            "explanation": "El Salvador became the first country to adopt Bitcoin as legal tender in September 2021."
        },
        {
            "question": "What is the Lightning Network?",
            "options": ["A weather app", "A second layer for fast, cheap Bitcoin transactions", "A type of Bitcoin", "A mining pool"],
            "correct": 1,
            "explanation": "Lightning Network enables instant, low-cost Bitcoin transactions."
        },
        {
            "question": "What should you NEVER share with anyone?",
            "options": ["Your Bitcoin address", "Your seed phrase", "Your wallet app name", "Your transaction history"],
            "correct": 1,
            "explanation": "Your seed phrase gives complete access to your Bitcoin. Never share it!"
        },
        {
            "question": "What makes Bitcoin 'decentralized'?",
            "options": ["It's controlled by one company", "No single entity controls it", "Only governments can use it", "It only works in certain countries"],
            "correct": 1,
            "explanation": "Bitcoin is maintained by a global network of computers, not controlled by any single entity."
        },
        {
            "question": "What is 'HODL'?",
            "options": ["A type of wallet", "Holding Bitcoin long-term instead of selling", "A Bitcoin exchange", "A mining technique"],
            "correct": 1,
            "explanation": "HODL means holding Bitcoin for the long term, regardless of price fluctuations."
        },
        {
            "question": "What is a 'cold wallet'?",
            "options": ["A wallet stored in a freezer", "An offline wallet for secure storage", "A wallet that's not working", "A free wallet"],
            "correct": 1,
            "explanation": "A cold wallet is an offline device that provides maximum security for your Bitcoin."
        },
    ],
    "es": [
        {
            "question": "¿Cuántos Bitcoin existirán en total?",
            "options": ["21 millones", "100 millones", "Ilimitados", "1 mil millones"],
            "correct": 0,
            "explanation": "Bitcoin tiene un suministro fijo máximo de 21 millones de monedas."
        },
        {
            "question": "¿Qué es un 'satoshi'?",
            "options": ["El fundador de Bitcoin", "La unidad más pequeña de Bitcoin (0.00000001 BTC)", "Un tipo de billetera", "Una máquina de minería"],
            "correct": 1,
            "explanation": "Un satoshi es la unidad más pequeña de Bitcoin, nombrada en honor a su creador."
        },
        {
            "question": "¿Cuándo adoptó El Salvador Bitcoin como moneda de curso legal?",
            "options": ["2019", "2020", "2021", "2022"],
            "correct": 2,
            "explanation": "El Salvador se convirtió en el primer país en adoptar Bitcoin como moneda de curso legal en septiembre de 2021."
        },
        {
            "question": "¿Qué es la Lightning Network?",
            "options": ["Una aplicación del clima", "Una segunda capa para transacciones rápidas y baratas de Bitcoin", "Un tipo de Bitcoin", "Un grupo de minería"],
            "correct": 1,
            "explanation": "Lightning Network permite transacciones de Bitcoin instantáneas y de bajo costo."
        },
        {
            "question": "¿Qué NUNCA debes compartir con nadie?",
            "options": ["Tu dirección de Bitcoin", "Tu frase semilla", "El nombre de tu app de billetera", "Tu historial de transacciones"],
            "correct": 1,
            "explanation": "Tu frase semilla da acceso completo a tu Bitcoin. ¡Nunca la compartas!"
        },
        {
            "question": "¿Qué hace que Bitcoin sea 'descentralizado'?",
            "options": ["Es controlado por una empresa", "Ninguna entidad única lo controla", "Solo los gobiernos pueden usarlo", "Solo funciona en ciertos países"],
            "correct": 1,
            "explanation": "Bitcoin es mantenido por una red global de computadoras, no controlada por ninguna entidad única."
        },
        {
            "question": "¿Qué es 'HODL'?",
            "options": ["Un tipo de billetera", "Mantener Bitcoin a largo plazo en lugar de vender", "Un exchange de Bitcoin", "Una técnica de minería"],
            "correct": 1,
            "explanation": "HODL significa mantener Bitcoin a largo plazo, independientemente de las fluctuaciones de precio."
        },
        {
            "question": "¿Qué es una 'billetera fría'?",
            "options": ["Una billetera guardada en el congelador", "Una billetera offline para almacenamiento seguro", "Una billetera que no funciona", "Una billetera gratis"],
            "correct": 1,
            "explanation": "Una billetera fría es un dispositivo offline que proporciona máxima seguridad para tu Bitcoin."
        },
    ]
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_text(key: str) -> str:
    """Get translated text based on current language"""
    lang = st.session_state.get("language", "es")
    return TRANSLATIONS.get(lang, TRANSLATIONS["es"]).get(key, key)


def get_bitcoin_price() -> dict:
    """Fetch current Bitcoin price from CoinGecko API"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "usd",
            "include_24hr_change": "true"
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        price = data["bitcoin"]["usd"]
        change_24h = data["bitcoin"].get("usd_24h_change", 0)
        sats_per_dollar = int(100_000_000 / price)

        return {
            "price": price,
            "change_24h": change_24h,
            "sats_per_dollar": sats_per_dollar,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {
            "price": None,
            "change_24h": None,
            "sats_per_dollar": None,
            "timestamp": None,
            "error": str(e)
        }


def initialize_session_state():
    """Initialize all session state variables"""
    if "language" not in st.session_state:
        st.session_state.language = "es"  # Default to Spanish

    if "xp" not in st.session_state:
        st.session_state.xp = 0

    if "level" not in st.session_state:
        st.session_state.level = 1

    if "achievements" not in st.session_state:
        st.session_state.achievements = []

    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = []

    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    if "simulation_wallet" not in st.session_state:
        st.session_state.simulation_wallet = 1_000_000  # 1 million satoshis

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Character-based tutor modes
    if "tutor_mode" not in st.session_state:
        st.session_state.tutor_mode = "luna"  # luna, pedrito, adventure

    if "luna_chat_history" not in st.session_state:
        st.session_state.luna_chat_history = []

    if "pedrito_chat_history" not in st.session_state:
        st.session_state.pedrito_chat_history = []

    if "adventure_chat_history" not in st.session_state:
        st.session_state.adventure_chat_history = []

    if "student_name" not in st.session_state:
        st.session_state.student_name = ""

    if "story_chapter" not in st.session_state:
        st.session_state.story_chapter = 1

    if "story_path" not in st.session_state:
        st.session_state.story_path = ""

    if "teaching_score" not in st.session_state:
        st.session_state.teaching_score = 0

    if "luna_conversations" not in st.session_state:
        st.session_state.luna_conversations = 0


def add_xp(amount: int):
    """Add XP and handle level ups"""
    st.session_state.xp += amount
    new_level = (st.session_state.xp // 100) + 1
    if new_level > st.session_state.level:
        st.session_state.level = new_level
        st.balloons()


def add_achievement(achievement_key: str):
    """Add an achievement if not already earned"""
    if achievement_key not in st.session_state.achievements:
        st.session_state.achievements.append(achievement_key)
        add_xp(25)
        st.toast(f"🏆 {get_text(achievement_key)}")


def generate_wallet_address() -> str:
    """Generate a fake Bitcoin wallet address for simulation"""
    chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    prefix = random.choice(["bc1q", "3", "1"])
    length = 34 if prefix in ["3", "1"] else 42
    return prefix + "".join(random.choice(chars) for _ in range(length - len(prefix)))


def get_xai_api_key() -> str:
    """Get xAI API key from secrets or environment"""
    # Try Streamlit secrets first
    try:
        if hasattr(st, 'secrets') and 'XAI_API_KEY' in st.secrets:
            return st.secrets['XAI_API_KEY']
    except Exception:
        pass

    # Fall back to environment variable
    return os.environ.get('XAI_API_KEY', '')


def get_grok_response(user_message: str, chat_history: list, language: str) -> str:
    """Get response from Grok/xAI API for Bitcoin education"""
    api_key = get_xai_api_key()

    if not api_key:
        if language == "es":
            return "⚠️ API de xAI no configurada. Por favor, configura tu clave API de xAI para habilitar el tutor de IA."
        return "⚠️ xAI API not configured. Please set your xAI API key to enable the AI tutor."

    # Bilingual system prompt for Bitcoin education
    system_prompt = """You are a friendly Bitcoin educator for El Salvador. Your role is to help people learn about Bitcoin in simple, clear terms.

Key guidelines:
- Explain Bitcoin concepts simply, suitable for beginners
- Focus on practical topics: wallets, Lightning Network, security, remittances, savings
- Use examples relevant to El Salvador (pupusas, remittances from the US, Chivo wallet)
- Be encouraging and patient with learners
- If asked in Spanish, respond in Spanish. If asked in English, respond in English.
- Keep responses concise but informative (2-3 paragraphs max)
- Emphasize security best practices (never share seed phrases, beware of scams)
- Explain both benefits and risks honestly

You are an AI tutor in a Bitcoin literacy app for El Salvador, the first country to adopt Bitcoin as legal tender."""

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.x.ai/v1"
        )

        # Build messages with conversation history
        messages = [{"role": "system", "content": system_prompt}]

        # Add recent chat history (last 10 messages for context)
        for msg in chat_history[-10:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Add current user message
        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="grok-beta",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        if language == "es":
            return f"❌ Error al conectar con el tutor IA: {error_msg}"
        return f"❌ Error connecting to AI tutor: {error_msg}"


# ============================================================================
# CHARACTER PROMPTS FOR TUTOR MODES
# ============================================================================

LUNA_PROMPT_ES = """Eres Luna, una niña curiosa de 10 años de El Salvador que aprendió sobre Bitcoin de su abuela.

Personalidad:
- Habla en primera persona como Luna
- Referencia tu propio viaje aprendiendo Bitcoin
- Usa expresiones salvadoreñas: "¡Qué chivo!", "cipote/cipota", "puchica", "va pues"
- Sé alentadora, curiosa y amigable
- Comparte historias de cómo tu abuela te enseñó sobre el dinero y Bitcoin
- Menciona lugares de El Salvador: el mercado, los volcanes, la playa

Directrices:
- Explica conceptos de Bitcoin de manera simple, para principiantes
- Usa ejemplos de la vida cotidiana en El Salvador (pupusas, remesas, Chivo wallet)
- Mantén respuestas concisas (2-3 párrafos máximo)
- Enfatiza la seguridad (nunca compartir frase semilla)

Siempre comienza con un saludo cálido referenciando tu personaje."""

LUNA_PROMPT_EN = """You are Luna, a curious 10-year-old girl from El Salvador who learned about Bitcoin from her grandmother.

Personality:
- Speak in first person as Luna
- Reference your own Bitcoin learning journey
- Use Salvadoran expressions: "¡Qué chivo!", "cipote/cipota", "puchica", "va pues"
- Be encouraging, curious, and friendly
- Share stories about your abuela teaching you about money and Bitcoin
- Mention places in El Salvador: the market, volcanoes, the beach

Guidelines:
- Explain Bitcoin concepts simply, for beginners
- Use everyday examples from El Salvador (pupusas, remittances, Chivo wallet)
- Keep responses concise (2-3 paragraphs max)
- Emphasize security (never share seed phrase)

Always start with a warm greeting referencing your character."""

PEDRITO_PROMPT_ES = """Eres Pedrito, un estudiante confundido de 7 años tratando de aprender sobre Bitcoin. El USUARIO es tu maestro/profe.

Comportamiento:
- Haz preguntas ingenuas sobre Bitcoin
- Comete errores intencionales para que el usuario te corrija
- Di cosas como "¿Entonces Bitcoin es como los colones?" o "¿El gobierno puede imprimir más Bitcoin?"
- Cuando te corrijan correctamente, di "¡Ahhhh, ya entendí!" y haz una pregunta de seguimiento
- Sé curioso pero ten conceptos erróneos comunes
- NUNCA des información correcta sobre Bitcoin - siempre sé el estudiante
- Usa lenguaje de niño pequeño

Ejemplos de preguntas confundidas:
- "Profe, ¿Bitcoin es como el dinero que mi mamá guarda en el banco?"
- "¿Puedo tocar un Bitcoin? ¿Es como una moneda de oro?"
- "Si se va la luz, ¿se pierden los Bitcoin?"
- "¿Mi tío puede copiar sus Bitcoin y darnos a todos?"

Recuerda: TÚ eres el estudiante. El usuario te está enseñando."""

PEDRITO_PROMPT_EN = """You are Pedrito, a confused 7-year-old student trying to learn about Bitcoin. The USER is your teacher.

Behavior:
- Ask naive questions about Bitcoin
- Make intentional mistakes for the user to correct
- Say things like "So Bitcoin is like colones?" or "Can the government print more Bitcoin?"
- When corrected properly, say "¡Ahhhh, ya entendí!" (Ohhh, now I understand!) and ask a follow-up
- Be curious but have common misconceptions
- NEVER give correct Bitcoin information - always be the student
- Use child-like language

Examples of confused questions:
- "Teacher, is Bitcoin like the money my mom keeps in the bank?"
- "Can I touch a Bitcoin? Is it like a gold coin?"
- "If the power goes out, do the Bitcoins disappear?"
- "Can my uncle copy his Bitcoin and give some to everyone?"

Remember: YOU are the student. The user is teaching you."""

ADVENTURE_PROMPT_ES = """Eres el narrador de una aventura interactiva de aprendizaje de Bitcoin protagonizada por Luna y {student_name}.

Capítulo actual: {chapter}
Historial de elecciones del jugador: {story_path}

Formato:
- Escribe segmentos de historia en segunda persona ("Tú y Luna caminan hacia el mercado...")
- Termina CADA segmento con exactamente 2 opciones etiquetadas [A] y [B]
- Enseña UN concepto de Bitcoin por segmento de historia
- Las opciones deben ser significativas y llevar a diferentes aprendizajes
- Mantén el tono aventurero pero educativo
- Referencias a lugares de El Salvador: volcanes, mercados, playas, pueblos

Capítulos disponibles:
1. Primeros Satoshis - Introducción a Bitcoin (¿Qué es Bitcoin? ¿Por qué es especial?)
2. La Billetera Chivo - Configuración y seguridad (Cómo guardar Bitcoin de forma segura)

Usa el historial de elecciones para mantener continuidad narrativa y referenciar decisiones pasadas.
Si no hay historial, comienza el capítulo desde el principio."""

ADVENTURE_PROMPT_EN = """You are narrating an interactive Bitcoin learning adventure starring Luna and {student_name}.

Current chapter: {chapter}
Player's choice history: {story_path}

Format:
- Write story segments in 2nd person ("You and Luna walk to the market...")
- End EVERY segment with exactly 2 choices labeled [A] and [B]
- Teach ONE Bitcoin concept per story segment
- Choices should be meaningful and lead to different learnings
- Keep the tone adventurous but educational
- Reference places in El Salvador: volcanoes, markets, beaches, villages

Available chapters:
1. First Satoshis - Introduction to Bitcoin (What is Bitcoin? Why is it special?)
2. The Chivo Wallet - Setup and security (How to store Bitcoin safely)

Use the choice history to maintain narrative continuity and reference past decisions.
If no history, start the chapter from the beginning."""

# Teaching keywords for Pedrito mode
TEACHING_KEYWORDS = [
    "21 million", "21 millones",
    "decentralized", "descentralizado", "descentralizada",
    "satoshi", "satoshis",
    "blockchain", "cadena de bloques",
    "lightning", "rayo",
    "private key", "clave privada",
    "seed phrase", "frase semilla",
    "wallet", "billetera",
    "mining", "minería", "minar",
    "hash", "nodo", "node",
    "peer to peer", "p2p",
    "digital", "escaso", "scarce",
    "inmutable", "immutable"
]

# Adventure chapters configuration
ADVENTURE_CHAPTERS = {
    1: {"title_en": "First Satoshis", "title_es": "Primeros Satoshis", "available": True},
    2: {"title_en": "The Chivo Wallet", "title_es": "La Billetera Chivo", "available": True},
    3: {"title_en": "Lightning Speed", "title_es": "Velocidad Lightning", "available": False},
    4: {"title_en": "The Volcano", "title_es": "El Volcán", "available": False},
    5: {"title_en": "Sending Home", "title_es": "Enviando a Casa", "available": False},
}


def check_teaching_success(message: str) -> bool:
    """Check if user's message contains teaching keywords for Pedrito mode"""
    message_lower = message.lower()
    return any(keyword.lower() in message_lower for keyword in TEACHING_KEYWORDS)


def get_character_response(user_message: str, chat_history: list, language: str, mode: str,
                           student_name: str = "", chapter: int = 1, story_path: str = "") -> str:
    """Get AI response based on current tutor mode and character"""
    api_key = get_xai_api_key()

    if not api_key:
        if language == "es":
            return "⚠️ API de xAI no configurada. Por favor, configura tu clave API de xAI para habilitar el tutor de IA."
        return "⚠️ xAI API not configured. Please set your xAI API key to enable the AI tutor."

    # Select appropriate prompt based on mode and language
    if mode == "luna":
        system_prompt = LUNA_PROMPT_ES if language == "es" else LUNA_PROMPT_EN
    elif mode == "pedrito":
        system_prompt = PEDRITO_PROMPT_ES if language == "es" else PEDRITO_PROMPT_EN
    elif mode == "adventure":
        base_prompt = ADVENTURE_PROMPT_ES if language == "es" else ADVENTURE_PROMPT_EN
        system_prompt = base_prompt.format(
            student_name=student_name or "Aventurero",
            chapter=chapter,
            story_path=story_path or "ninguno/none"
        )
    else:
        # Fallback to Luna
        system_prompt = LUNA_PROMPT_ES if language == "es" else LUNA_PROMPT_EN

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.x.ai/v1"
        )

        messages = [{"role": "system", "content": system_prompt}]

        # Add recent chat history (last 10 messages for context)
        for msg in chat_history[-10:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="grok-beta",
            messages=messages,
            max_tokens=600,
            temperature=0.8
        )

        return response.choices[0].message.content

    except Exception as e:
        error_msg = str(e)
        if language == "es":
            return f"❌ Error al conectar con el tutor IA: {error_msg}"
        return f"❌ Error connecting to AI tutor: {error_msg}"


# ============================================================================
# MODULE FUNCTIONS
# ============================================================================

def show_sidebar():
    """Display the sidebar with progress and navigation"""
    with st.sidebar:
        # Language selector
        lang_options = {"English": "en", "Español": "es"}
        selected_lang = st.selectbox(
            get_text("language"),
            options=list(lang_options.keys()),
            index=1 if st.session_state.language == "es" else 0
        )
        st.session_state.language = lang_options[selected_lang]

        st.divider()

        # Progress display
        st.subheader(get_text("your_progress"))
        col1, col2 = st.columns(2)
        with col1:
            st.metric(get_text("level"), st.session_state.level)
        with col2:
            st.metric(get_text("xp"), st.session_state.xp)

        # XP Progress bar
        xp_for_next_level = st.session_state.level * 100
        current_level_xp = st.session_state.xp % 100
        st.progress(current_level_xp / 100)

        st.divider()

        # Achievements
        if st.session_state.achievements:
            st.subheader(get_text("achievements"))
            for ach in st.session_state.achievements:
                st.write(get_text(ach))

        st.divider()

        # Bitcoin Price
        st.subheader(get_text("current_price"))
        price_data = get_bitcoin_price()
        if price_data.get("price"):
            price_color = "green" if price_data["change_24h"] > 0 else "red"
            st.metric(
                "BTC/USD",
                f"${price_data['price']:,.2f}",
                f"{price_data['change_24h']:.2f}%"
            )
            st.caption(f"≈ {price_data['sats_per_dollar']:,} {get_text('sats_per_dollar')}")
        else:
            st.warning("Price unavailable")


def module_bitcoin_basics():
    """Bitcoin Basics Module"""
    st.header(get_text("module_basics"))

    st.subheader(get_text("what_is_bitcoin"))
    st.markdown(get_text("bitcoin_intro"))

    st.divider()

    st.subheader(get_text("why_el_salvador"))
    st.markdown(get_text("el_salvador_reasons"))

    # Add image placeholder for Bitcoin logo
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png", width=150)

    if st.button("✅ " + ("Mark as Complete" if st.session_state.language == "en" else "Marcar como Completado")):
        add_achievement("ach_first_lesson")
        if "basics" not in st.session_state.completed_modules:
            st.session_state.completed_modules.append("basics")
            add_xp(20)
            st.success(get_text("xp_earned"))


def module_wallet_security():
    """Wallet Security Module"""
    st.header(get_text("module_wallet"))

    st.warning(get_text("seed_warning"))

    st.markdown(get_text("security_tips"))

    st.divider()

    st.subheader(get_text("wallet_types"))

    col1, col2 = st.columns(2)
    with col1:
        st.info(get_text("hot_wallet"))
        st.write("Examples: Chivo, Muun, Blue Wallet")

    with col2:
        st.success(get_text("cold_wallet"))
        st.write("Examples: Ledger, Trezor, Coldcard")

    st.divider()

    # Interactive seed phrase example (not real)
    st.subheader(get_text("seed_phrase"))
    example_words = ["ocean", "forest", "mountain", "river", "thunder", "lightning",
                     "eagle", "volcano", "sunset", "crystal", "harmony", "freedom"]

    st.code(" ".join(f"{i+1}. {word}" for i, word in enumerate(example_words[:6])))
    st.code(" ".join(f"{i+7}. {word}" for i, word in enumerate(example_words[6:])))

    st.caption("⚠️ This is an EXAMPLE. Never use this phrase for a real wallet!")

    if st.button("✅ " + ("Mark as Complete" if st.session_state.language == "en" else "Marcar como Completado")):
        add_achievement("ach_security_master")
        if "security" not in st.session_state.completed_modules:
            st.session_state.completed_modules.append("security")
            add_xp(20)
            st.success(get_text("xp_earned"))


def module_history_of_money():
    """History of Money Module"""
    st.header(get_text("module_history"))
    st.markdown(get_text("history_intro"))

    # Timeline
    timeline_data = [
        ("barter", "barter_desc", "5000+ BC"),
        ("commodity", "commodity_desc", "3000 BC"),
        ("metal", "metal_desc", "600 BC"),
        ("paper", "paper_desc", "1000 AD"),
        ("fiat", "fiat_desc", "1971"),
        ("crypto", "crypto_desc", "2009"),
    ]

    for item, desc, year in timeline_data:
        with st.expander(f"{get_text(item)} - {year}"):
            st.write(get_text(desc))

    st.divider()

    # Inflation visualization
    st.subheader("📉 " + ("Purchasing Power Over Time" if st.session_state.language == "en" else "Poder Adquisitivo a lo Largo del Tiempo"))

    years = list(range(1950, 2025, 5))
    usd_value = [100 / (1.03 ** (year - 1950)) for year in years]

    chart_data = pd.DataFrame({
        "Year": years,
        "USD Value": usd_value
    })
    st.line_chart(chart_data.set_index("Year"))
    st.caption("$100 in 1950 → $" + f"{usd_value[-1]:.2f} today (adjusted for inflation)")


def module_budgeting_game():
    """Budgeting Game Module"""
    st.header(get_text("budget_title"))
    st.write(get_text("budget_intro"))

    # Monthly income slider
    income = st.slider(
        get_text("monthly_income"),
        min_value=100_000,
        max_value=10_000_000,
        value=1_000_000,
        step=100_000,
        format="%d sats"
    )

    st.subheader(get_text("allocate_budget"))

    # Budget allocation
    col1, col2 = st.columns(2)

    with col1:
        needs = st.slider(get_text("needs"), 0, 100, 50, key="needs_slider")
        wants = st.slider(get_text("wants"), 0, 100, 20, key="wants_slider")

    with col2:
        savings = st.slider(get_text("savings"), 0, 100, 20, key="savings_slider")
        emergency = st.slider(get_text("emergency"), 0, 100, 10, key="emergency_slider")

    total_allocation = needs + wants + savings + emergency

    # Visualization
    if total_allocation > 0:
        budget_data = pd.DataFrame({
            "Category": [get_text("needs"), get_text("wants"), get_text("savings"), get_text("emergency")],
            "Percentage": [needs, wants, savings, emergency],
            "Satoshis": [int(income * p / 100) for p in [needs, wants, savings, emergency]]
        })

        st.bar_chart(budget_data.set_index("Category")["Satoshis"])

        st.divider()

        # Feedback
        st.subheader(get_text("budget_feedback"))

        if total_allocation != 100:
            st.warning(f"⚠️ Total: {total_allocation}% (should be 100%)")
        elif savings + emergency >= 20:
            st.success(get_text("good_budget"))
            if "budget" not in st.session_state.completed_modules:
                add_achievement("ach_budget_pro")
                st.session_state.completed_modules.append("budget")
                add_xp(30)
        else:
            st.info(get_text("review_budget"))


def module_transaction_simulator():
    """Transaction Simulator Module"""
    st.header(get_text("simulator_title"))
    st.write(get_text("simulator_intro"))

    # Display current balance
    st.metric(
        "Your Balance / Tu Saldo",
        f"{st.session_state.simulation_wallet:,} sats",
        delta=None
    )

    st.divider()

    # Transaction form
    col1, col2 = st.columns(2)

    with col1:
        sender = generate_wallet_address()
        st.text_input(get_text("sender_wallet"), value=sender, disabled=True)

    with col2:
        recipient = st.text_input(
            get_text("recipient_wallet"),
            value=generate_wallet_address(),
            help="Enter a Bitcoin address or use the generated one"
        )

    amount = st.number_input(
        get_text("amount_sats"),
        min_value=1,
        max_value=st.session_state.simulation_wallet,
        value=min(10000, st.session_state.simulation_wallet),
        step=1000
    )

    # Fee estimation
    fee_options = {
        "⚡ Lightning (Instant)": 1,
        "🚀 Priority (10 min)": int(amount * 0.001),
        "🐢 Economy (1 hour)": int(amount * 0.0005),
    }

    selected_fee = st.radio(get_text("network_fee"), list(fee_options.keys()))
    fee = fee_options[selected_fee]

    total = amount + fee

    st.info(f"Total: {amount:,} + {fee:,} fee = **{total:,} sats**")

    if st.button(get_text("send_transaction"), type="primary"):
        if total <= st.session_state.simulation_wallet:
            # Simulate transaction
            with st.spinner("Processing transaction..."):
                import time
                time.sleep(2)  # Simulate network delay

            st.session_state.simulation_wallet -= total

            st.success(get_text("transaction_success"))

            # Show transaction details
            with st.expander(get_text("transaction_details")):
                tx_id = "".join(random.choice("0123456789abcdef") for _ in range(64))
                st.code(f"TX ID: {tx_id}")
                st.write(f"**From:** {sender[:20]}...")
                st.write(f"**To:** {recipient[:20]}...")
                st.write(f"**Amount:** {amount:,} sats")
                st.write(f"**Fee:** {fee:,} sats")
                st.write(f"**Status:** ✅ Confirmed")

            add_xp(15)
        else:
            st.error("Insufficient balance! / ¡Saldo insuficiente!")

    # Reset balance button
    if st.button("🔄 Reset Balance / Reiniciar Saldo"):
        st.session_state.simulation_wallet = 1_000_000
        st.rerun()


def module_quiz():
    """Quiz Module"""
    st.header(get_text("quiz_title"))
    st.write(get_text("quiz_intro"))

    lang = st.session_state.language
    questions = QUIZ_QUESTIONS[lang]

    if st.session_state.quiz_index < len(questions):
        current_q = questions[st.session_state.quiz_index]

        st.subheader(f"{get_text('question')} {st.session_state.quiz_index + 1}/{len(questions)}")
        st.write(f"**{current_q['question']}**")

        # Radio buttons for answers
        answer = st.radio(
            "Select your answer:",
            current_q["options"],
            key=f"quiz_q_{st.session_state.quiz_index}"
        )

        if st.button(get_text("submit_answer")):
            selected_index = current_q["options"].index(answer)

            if selected_index == current_q["correct"]:
                st.success(get_text("correct"))
                st.session_state.quiz_score += 1
                add_xp(10)
            else:
                st.error(f"{get_text('incorrect')} {current_q['options'][current_q['correct']]}")

            st.info(f"💡 {current_q['explanation']}")

            # Move to next question
            if st.button(get_text("next_question")):
                st.session_state.quiz_index += 1
                st.rerun()
    else:
        # Quiz complete
        st.success(get_text("quiz_complete"))
        st.metric("Score", f"{st.session_state.quiz_score}/{len(questions)}")

        if st.session_state.quiz_score >= len(questions) * 0.7:
            add_achievement("ach_quiz_champion")

        if st.button("🔄 Restart Quiz / Reiniciar Quiz"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.rerun()


def module_stories():
    """Bitcoin Stories Module"""
    st.header(get_text("stories_title"))
    st.write(get_text("stories_intro"))

    # Story tabs
    tabs = st.tabs([
        get_text("story_1_title"),
        get_text("story_2_title"),
        get_text("story_3_title")
    ])

    with tabs[0]:
        st.markdown(get_text("story_1"))

    with tabs[1]:
        st.markdown(get_text("story_2"))

    with tabs[2]:
        st.markdown(get_text("story_3"))

    st.divider()

    if st.button("✅ " + ("I've read all stories" if st.session_state.language == "en" else "He leído todas las historias")):
        add_achievement("ach_story_reader")
        if "stories" not in st.session_state.completed_modules:
            st.session_state.completed_modules.append("stories")
            add_xp(25)
            st.success(get_text("xp_earned"))


def module_ai_tutor():
    """AI Tutor Module with Character-Based Learning Modes"""
    st.header(get_text("tutor_title"))

    lang = st.session_state.language

    # Check API configuration status
    api_key = get_xai_api_key()
    if api_key:
        st.success("✅ " + ("xAI/Grok API connected" if lang == "en" else "API xAI/Grok conectada"))
    else:
        st.warning("⚠️ " + ("Set XAI_API_KEY to enable AI" if lang == "en" else "Configura XAI_API_KEY para habilitar IA"))

    st.divider()

    # ==================== MODE SELECTOR ====================
    st.subheader("🎭 " + get_text("select_mode"))

    mode_col1, mode_col2, mode_col3 = st.columns(3)

    with mode_col1:
        if st.button(get_text("learn_with_luna"), key="mode_luna", use_container_width=True,
                     type="primary" if st.session_state.tutor_mode == "luna" else "secondary"):
            if st.session_state.tutor_mode != "luna":
                st.session_state.tutor_mode = "luna"
                # Auto-send intro if chat is empty
                if not st.session_state.luna_chat_history:
                    st.session_state.luna_chat_history.append({
                        "role": "assistant",
                        "content": get_text("luna_intro")
                    })
                st.rerun()

    with mode_col2:
        if st.button(get_text("teach_pedrito"), key="mode_pedrito", use_container_width=True,
                     type="primary" if st.session_state.tutor_mode == "pedrito" else "secondary"):
            if st.session_state.tutor_mode != "pedrito":
                st.session_state.tutor_mode = "pedrito"
                # Auto-send intro if chat is empty
                if not st.session_state.pedrito_chat_history:
                    st.session_state.pedrito_chat_history.append({
                        "role": "assistant",
                        "content": get_text("pedrito_intro")
                    })
                st.rerun()

    with mode_col3:
        if st.button(get_text("adventure_mode"), key="mode_adventure", use_container_width=True,
                     type="primary" if st.session_state.tutor_mode == "adventure" else "secondary"):
            if st.session_state.tutor_mode != "adventure":
                st.session_state.tutor_mode = "adventure"
                st.rerun()

    st.divider()

    mode = st.session_state.tutor_mode

    # ==================== LUNA MODE ====================
    if mode == "luna":
        st.markdown("### 🌙 Luna")
        st.caption("Luna" + (" will teach you about Bitcoin!" if lang == "en" else " te enseñará sobre Bitcoin!"))

        # Get the correct chat history
        chat_history = st.session_state.luna_chat_history

        # Display chat with Luna avatar
        for message in chat_history:
            avatar = "🌙" if message["role"] == "assistant" else "👤"
            with st.chat_message(message["role"], avatar=avatar):
                st.write(message["content"])

        # Chat input
        user_input = st.chat_input(get_text("tutor_placeholder"))

        if user_input:
            st.session_state.luna_chat_history.append({"role": "user", "content": user_input})

            with st.spinner("🌙 " + ("Luna is thinking..." if lang == "en" else "Luna está pensando...")):
                response = get_character_response(
                    user_input,
                    st.session_state.luna_chat_history[:-1],
                    lang,
                    "luna"
                )

            st.session_state.luna_chat_history.append({"role": "assistant", "content": response})
            st.session_state.luna_conversations += 1
            add_xp(5)

            # Check for Luna's Friend achievement
            if st.session_state.luna_conversations >= 10:
                add_achievement("ach_luna_friend")

            st.rerun()

        # Reset button
        if st.button("🔄 " + get_text("reset_conversation"), key="reset_luna"):
            st.session_state.luna_chat_history = []
            st.rerun()

    # ==================== PEDRITO MODE ====================
    elif mode == "pedrito":
        st.markdown("### 👦 Pedrito")
        st.info(get_text("teaching_tip"))

        chat_history = st.session_state.pedrito_chat_history

        # Display chat with Pedrito avatar
        for message in chat_history:
            avatar = "👦" if message["role"] == "assistant" else "👨‍🏫"
            with st.chat_message(message["role"], avatar=avatar):
                st.write(message["content"])

        # Chat input
        user_input = st.chat_input("Teach Pedrito..." if lang == "en" else "Enseña a Pedrito...")

        if user_input:
            st.session_state.pedrito_chat_history.append({"role": "user", "content": user_input})

            # Check if user used teaching keywords
            teaching_success = check_teaching_success(user_input)

            with st.spinner("👦 " + ("Pedrito is thinking..." if lang == "en" else "Pedrito está pensando...")):
                response = get_character_response(
                    user_input,
                    st.session_state.pedrito_chat_history[:-1],
                    lang,
                    "pedrito"
                )

            st.session_state.pedrito_chat_history.append({"role": "assistant", "content": response})

            # Award bonus XP for good teaching
            if teaching_success:
                st.session_state.teaching_score += 1
                add_xp(15)
                st.toast(get_text("great_teaching"))

                # Check for Great Teacher achievement
                if st.session_state.teaching_score >= 5:
                    add_achievement("ach_great_teacher")
            else:
                add_xp(3)

            st.rerun()

        # Reset button
        if st.button("🔄 " + get_text("reset_conversation"), key="reset_pedrito"):
            st.session_state.pedrito_chat_history = []
            st.rerun()

    # ==================== ADVENTURE MODE ====================
    elif mode == "adventure":
        st.markdown("### 📖 " + ("Bitcoin Adventure" if lang == "en" else "Aventura Bitcoin"))
        st.caption(get_text("adventure_intro"))

        # Chapter selector
        st.subheader(get_text("chapter") + " " + ("Selection" if lang == "en" else "Selección"))

        chapter_cols = st.columns(5)
        for i, (ch_num, ch_info) in enumerate(ADVENTURE_CHAPTERS.items()):
            with chapter_cols[i]:
                title = ch_info["title_en"] if lang == "en" else ch_info["title_es"]
                if ch_info["available"]:
                    if st.button(f"{ch_num}. {title}", key=f"ch_{ch_num}",
                                 type="primary" if st.session_state.story_chapter == ch_num else "secondary"):
                        st.session_state.story_chapter = ch_num
                        st.session_state.adventure_chat_history = []
                        st.session_state.story_path = ""
                        st.rerun()
                else:
                    st.button(f"🔒 {ch_num}", key=f"ch_{ch_num}", disabled=True)
                    st.caption(get_text("coming_soon"))

        st.divider()

        # Check if student name is set
        if not st.session_state.student_name:
            st.write(get_text("enter_your_name"))
            name_input = st.text_input("", key="adventure_name_input", placeholder="Tu nombre / Your name")
            if st.button(get_text("start_adventure"), key="start_adv"):
                if name_input:
                    st.session_state.student_name = name_input
                    # Generate initial story
                    intro_prompt = f"Start chapter {st.session_state.story_chapter}. My name is {name_input}."
                    with st.spinner("📖 " + ("Creating your adventure..." if lang == "en" else "Creando tu aventura...")):
                        response = get_character_response(
                            intro_prompt,
                            [],
                            lang,
                            "adventure",
                            student_name=name_input,
                            chapter=st.session_state.story_chapter,
                            story_path=""
                        )
                    st.session_state.adventure_chat_history.append({"role": "assistant", "content": response})
                    st.rerun()
        else:
            # Show current chapter and path
            st.caption(f"📍 {get_text('chapter')} {st.session_state.story_chapter} | " +
                       ("Path" if lang == "en" else "Camino") + f": {st.session_state.story_path or '🆕'}")

            chat_history = st.session_state.adventure_chat_history

            # Display story with book avatar
            for message in chat_history:
                avatar = "📖" if message["role"] == "assistant" else "🧑‍🎤"
                with st.chat_message(message["role"], avatar=avatar):
                    st.write(message["content"])

            # Choice buttons
            st.divider()
            choice_col1, choice_col2 = st.columns(2)

            with choice_col1:
                if st.button("🅰️ " + ("Choice A" if lang == "en" else "Opción A"), key="choice_a", use_container_width=True):
                    st.session_state.story_path += "A"
                    st.session_state.adventure_chat_history.append({"role": "user", "content": "I choose [A]"})

                    with st.spinner("📖..."):
                        response = get_character_response(
                            "I chose option [A]. Continue the story.",
                            st.session_state.adventure_chat_history[:-1],
                            lang,
                            "adventure",
                            student_name=st.session_state.student_name,
                            chapter=st.session_state.story_chapter,
                            story_path=st.session_state.story_path
                        )

                    st.session_state.adventure_chat_history.append({"role": "assistant", "content": response})
                    add_xp(10)
                    st.rerun()

            with choice_col2:
                if st.button("🅱️ " + ("Choice B" if lang == "en" else "Opción B"), key="choice_b", use_container_width=True):
                    st.session_state.story_path += "B"
                    st.session_state.adventure_chat_history.append({"role": "user", "content": "I choose [B]"})

                    with st.spinner("📖..."):
                        response = get_character_response(
                            "I chose option [B]. Continue the story.",
                            st.session_state.adventure_chat_history[:-1],
                            lang,
                            "adventure",
                            student_name=st.session_state.student_name,
                            chapter=st.session_state.story_chapter,
                            story_path=st.session_state.story_path
                        )

                    st.session_state.adventure_chat_history.append({"role": "assistant", "content": response})
                    add_xp(10)
                    st.rerun()

            # Or type custom response
            user_input = st.chat_input("Ask Luna something..." if lang == "en" else "Pregunta algo a Luna...")
            if user_input:
                st.session_state.adventure_chat_history.append({"role": "user", "content": user_input})

                with st.spinner("📖..."):
                    response = get_character_response(
                        user_input,
                        st.session_state.adventure_chat_history[:-1],
                        lang,
                        "adventure",
                        student_name=st.session_state.student_name,
                        chapter=st.session_state.story_chapter,
                        story_path=st.session_state.story_path
                    )

                st.session_state.adventure_chat_history.append({"role": "assistant", "content": response})
                add_xp(5)
                st.rerun()

            # Reset adventure button
            if st.button("🔄 " + get_text("reset_conversation"), key="reset_adventure"):
                st.session_state.adventure_chat_history = []
                st.session_state.story_path = ""
                st.session_state.student_name = ""
                st.rerun()

            # Check for Story Explorer achievement
            if len(st.session_state.story_path) >= 5:
                add_achievement("ach_story_explorer")


# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application entry point"""
    # Initialize session state
    initialize_session_state()

    # Page config
    st.set_page_config(
        page_title="Bitcoin Literacy El Salvador",
        page_icon="🟠",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        }
        .main-header {
            background: linear-gradient(90deg, #F7931A 0%, #FFA500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-weight: bold;
        }
        .stButton>button {
            background-color: #F7931A;
            color: white;
            border-radius: 20px;
            border: none;
            padding: 10px 25px;
        }
        .stButton>button:hover {
            background-color: #FFA500;
        }
        </style>
    """, unsafe_allow_html=True)

    # Show sidebar
    show_sidebar()

    # Main content
    st.markdown(f'<h1 class="main-header">{get_text("app_title")}</h1>', unsafe_allow_html=True)
    st.write(get_text("welcome"))

    st.divider()

    # Module selection
    st.subheader(get_text("select_module"))

    modules = {
        get_text("module_basics"): module_bitcoin_basics,
        get_text("module_wallet"): module_wallet_security,
        get_text("module_history"): module_history_of_money,
        get_text("module_budget"): module_budgeting_game,
        get_text("module_simulator"): module_transaction_simulator,
        get_text("module_quiz"): module_quiz,
        get_text("module_stories"): module_stories,
        get_text("module_tutor"): module_ai_tutor,
    }

    # Create module buttons in a grid
    cols = st.columns(4)
    selected_module = None

    for idx, (name, func) in enumerate(modules.items()):
        with cols[idx % 4]:
            if st.button(name, key=f"module_{idx}", use_container_width=True):
                selected_module = func
                st.session_state.selected_module = func

    st.divider()

    # Display selected module or default to basics
    if "selected_module" in st.session_state:
        st.session_state.selected_module()
    else:
        module_bitcoin_basics()


if __name__ == "__main__":
    main()
