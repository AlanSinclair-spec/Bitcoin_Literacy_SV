export type Language = 'en' | 'es';

export const translations = {
  en: {
    // Navigation
    app_title: "Bitcoin Literacy El Salvador",
    welcome: "Welcome to Bitcoin Education!",
    select_module: "Select a Learning Module",
    language: "Language",

    // Modules
    module_basics: "Bitcoin Basics",
    module_wallet: "Wallet Security",
    module_history: "History of Money",
    module_budget: "Budgeting Game",
    module_simulator: "Transaction Simulator",
    module_quiz: "Bitcoin Quiz",
    module_stories: "Bitcoin Stories",
    module_tutor: "AI Tutor",

    // Progress
    your_progress: "Your Progress",
    level: "Level",
    xp: "XP",
    achievements: "Achievements",
    xp_earned: "+XP earned!",

    // Bitcoin Basics
    what_is_bitcoin: "What is Bitcoin?",
    bitcoin_intro: `Bitcoin is digital money that works without banks or governments. Think of it like digital gold that you can send to anyone in the world instantly!

**Key Facts:**
- Created in 2009 by Satoshi Nakamoto
- Only 21 million Bitcoin will ever exist
- El Salvador made it legal tender in 2021
- 1 Bitcoin = 100,000,000 satoshis`,
    why_el_salvador: "Why Bitcoin in El Salvador?",
    el_salvador_reasons: `El Salvador became the first country to adopt Bitcoin as legal tender. Here's why:

- **Remittances**: Salvadorans abroad send ~$6 billion yearly to family. Bitcoin reduces fees from 10-20% to nearly 0%
- **Financial Inclusion**: 70% of Salvadorans don't have bank accounts. Bitcoin only needs a phone
- **Economic Freedom**: Protection against inflation and currency devaluation`,

    // Wallet Security
    seed_warning: "NEVER share your seed phrase with anyone! Not even family or 'support' staff.",
    security_tips: `**Essential Security Rules:**
1. Write down your 12/24 word seed phrase on paper
2. Store it in a safe place (not digitally!)
3. Never share it with anyone
4. Use a strong PIN/password
5. Enable 2FA when available`,
    wallet_types: "Types of Wallets",
    hot_wallet: "Hot Wallet (Phone/Computer) - For daily spending, like a physical wallet",
    cold_wallet: "Cold Wallet (Hardware) - For savings, like a bank vault",

    // History of Money
    history_title: "The Evolution of Money",
    barter_era: "Barter Era",
    barter_desc: "People traded goods directly - a chicken for some corn",
    commodity_era: "Commodity Money",
    commodity_desc: "Salt, shells, and metals became money",
    gold_era: "Gold Standard",
    gold_desc: "Gold backed paper money",
    fiat_era: "Fiat Currency",
    fiat_desc: "Government-controlled money (USD, Colones)",
    bitcoin_era: "Bitcoin Era",
    bitcoin_desc: "Digital, decentralized, limited supply",

    // Budgeting Game
    budget_title: "Family Budget Challenge",
    budget_intro: "Help the Martinez family manage their monthly budget using Bitcoin!",
    monthly_income: "Monthly Income",
    allocate_budget: "Allocate Your Budget",
    food: "Food",
    housing: "Housing",
    transport: "Transportation",
    savings: "Savings (Bitcoin)",
    entertainment: "Entertainment",
    check_budget: "Check My Budget",
    budget_balanced: "Budget balanced! Great job!",
    budget_over: "Over budget! Reduce expenses.",
    budget_under: "Under budget! Consider saving more in Bitcoin.",

    // Transaction Simulator
    simulator_title: "Bitcoin Transaction Simulator",
    simulator_intro: "Practice sending Bitcoin without real money! Learn how transactions work.",
    your_wallet: "Your Wallet Balance",
    send_to: "Send to Address",
    amount_sats: "Amount (satoshis)",
    network_fee: "Network Fee",
    send_transaction: "Send Transaction",
    transaction_success: "Transaction sent successfully!",
    transaction_details: "Transaction Details",

    // Quiz
    quiz_title: "Bitcoin Knowledge Quiz",
    quiz_intro: "Test your Bitcoin knowledge! Answer correctly to earn XP.",
    question: "Question",
    submit_answer: "Submit Answer",
    correct: "Correct! +10 XP",
    incorrect: "Incorrect. The correct answer is:",
    next_question: "Next Question",
    quiz_complete: "Quiz Complete!",

    // Stories
    stories_title: "Bitcoin Stories",
    stories_intro: "Real stories of how Bitcoin helps Salvadorans",
    story_1_title: "Maria's Remittance",
    story_1: `Maria works in the US and sends money home every month. Before Bitcoin, she paid $50 in fees to send $500. Now with Lightning Network, she sends the full amount in seconds for just a few cents!

Her mother receives the money instantly on her phone, no bank needed.`,
    story_2_title: "Carlos the Fisherman",
    story_2: `Carlos sells fish at the beach in El Zonte. Tourists pay him in Bitcoin using their phones. He doesn't need a bank account or credit card machine.

He saves some in Bitcoin and converts the rest to dollars for daily expenses.`,
    story_3_title: "The Pupusa Lady",
    story_3: `Dona Rosa has sold pupusas for 30 years. When Bitcoin came, she was nervous. Her grandson taught her to accept Lightning payments.

Now tourists from around the world buy her pupusas with Bitcoin. Her business has grown 40%!`,

    // AI Tutor
    tutor_title: "AI Bitcoin Tutor",
    tutor_placeholder: "Ask me anything about Bitcoin...",
    suggested_questions: "Suggested Questions",
    sq_1: "What is Bitcoin?",
    sq_2: "How do I keep my Bitcoin safe?",
    sq_3: "What is Lightning Network?",
    sq_4: "Why did El Salvador adopt Bitcoin?",

    // Achievements
    ach_first_lesson: "First Lesson Complete",
    ach_security_master: "Security Master",
    ach_quiz_champion: "Quiz Champion",
    ach_budget_pro: "Budget Pro",
    ach_story_reader: "Story Reader",

    // Chatbot
    chatbot_title: "Ask Me Anything",
    mode_socratic: "Socratic",
    mode_teacher: "Teach Me",
    mode_voice: "Simple",
    mode_curriculum: "Curriculum",
    socratic_desc: "I'll guide you with questions",
    teacher_desc: "Explain to me, I'll ask questions",
    voice_desc: "Simple, conversational answers",
    curriculum_desc: "Follow the Bitcoin curriculum",
    send: "Send",
    clear_chat: "Clear",
    chat_placeholder: "Ask anything about Bitcoin...",

    // Bitcoin Price
    current_price: "Current Bitcoin Price",
    sats_per_dollar: "satoshis per $1 USD",

    // Common
    mark_complete: "Mark as Complete",
    reset: "Reset",
  },
  es: {
    // Navigation
    app_title: "Educacion Bitcoin El Salvador",
    welcome: "Bienvenido a la Educacion Bitcoin!",
    select_module: "Selecciona un Modulo de Aprendizaje",
    language: "Idioma",

    // Modules
    module_basics: "Conceptos de Bitcoin",
    module_wallet: "Seguridad de Billetera",
    module_history: "Historia del Dinero",
    module_budget: "Juego de Presupuesto",
    module_simulator: "Simulador de Transacciones",
    module_quiz: "Quiz de Bitcoin",
    module_stories: "Historias de Bitcoin",
    module_tutor: "Tutor IA",

    // Progress
    your_progress: "Tu Progreso",
    level: "Nivel",
    xp: "XP",
    achievements: "Logros",
    xp_earned: "+XP ganado!",

    // Bitcoin Basics
    what_is_bitcoin: "Que es Bitcoin?",
    bitcoin_intro: `Bitcoin es dinero digital que funciona sin bancos ni gobiernos. Piensa en el como oro digital que puedes enviar a cualquier persona en el mundo al instante!

**Datos Clave:**
- Creado en 2009 por Satoshi Nakamoto
- Solo existiran 21 millones de Bitcoin
- El Salvador lo hizo moneda legal en 2021
- 1 Bitcoin = 100,000,000 satoshis`,
    why_el_salvador: "Por que Bitcoin en El Salvador?",
    el_salvador_reasons: `El Salvador se convirtio en el primer pais en adoptar Bitcoin como moneda legal. Estas son las razones:

- **Remesas**: Los salvadorenos en el exterior envian ~$6 mil millones al ano. Bitcoin reduce las comisiones del 10-20% a casi 0%
- **Inclusion Financiera**: El 70% de los salvadorenos no tienen cuenta bancaria. Bitcoin solo necesita un telefono
- **Libertad Economica**: Proteccion contra la inflacion y devaluacion`,

    // Wallet Security
    seed_warning: "NUNCA compartas tu frase semilla con nadie! Ni con familia ni 'soporte tecnico'.",
    security_tips: `**Reglas Esenciales de Seguridad:**
1. Escribe tu frase de 12/24 palabras en papel
2. Guardala en un lugar seguro (no digitalmente!)
3. Nunca la compartas con nadie
4. Usa un PIN/contrasena fuerte
5. Activa 2FA cuando este disponible`,
    wallet_types: "Tipos de Billeteras",
    hot_wallet: "Billetera Caliente (Telefono/Computadora) - Para gastos diarios",
    cold_wallet: "Billetera Fria (Hardware) - Para ahorros, como una boveda",

    // History of Money
    history_title: "La Evolucion del Dinero",
    barter_era: "Era del Trueque",
    barter_desc: "La gente intercambiaba bienes directamente - una gallina por maiz",
    commodity_era: "Dinero Mercancia",
    commodity_desc: "Sal, conchas y metales se convirtieron en dinero",
    gold_era: "Patron Oro",
    gold_desc: "El oro respaldaba el papel moneda",
    fiat_era: "Moneda Fiat",
    fiat_desc: "Dinero controlado por gobiernos (USD, Colones)",
    bitcoin_era: "Era Bitcoin",
    bitcoin_desc: "Digital, descentralizado, oferta limitada",

    // Budgeting Game
    budget_title: "Desafio de Presupuesto Familiar",
    budget_intro: "Ayuda a la familia Martinez a manejar su presupuesto mensual usando Bitcoin!",
    monthly_income: "Ingreso Mensual",
    allocate_budget: "Asigna Tu Presupuesto",
    food: "Comida",
    housing: "Vivienda",
    transport: "Transporte",
    savings: "Ahorros (Bitcoin)",
    entertainment: "Entretenimiento",
    check_budget: "Revisar Mi Presupuesto",
    budget_balanced: "Presupuesto balanceado! Excelente!",
    budget_over: "Sobre presupuesto! Reduce gastos.",
    budget_under: "Bajo presupuesto! Considera ahorrar mas en Bitcoin.",

    // Transaction Simulator
    simulator_title: "Simulador de Transacciones Bitcoin",
    simulator_intro: "Practica enviar Bitcoin sin dinero real! Aprende como funcionan las transacciones.",
    your_wallet: "Saldo de Tu Billetera",
    send_to: "Enviar a Direccion",
    amount_sats: "Cantidad (satoshis)",
    network_fee: "Comision de Red",
    send_transaction: "Enviar Transaccion",
    transaction_success: "Transaccion enviada exitosamente!",
    transaction_details: "Detalles de Transaccion",

    // Quiz
    quiz_title: "Quiz de Conocimiento Bitcoin",
    quiz_intro: "Pon a prueba tu conocimiento de Bitcoin! Responde correctamente para ganar XP.",
    question: "Pregunta",
    submit_answer: "Enviar Respuesta",
    correct: "Correcto! +10 XP",
    incorrect: "Incorrecto. La respuesta correcta es:",
    next_question: "Siguiente Pregunta",
    quiz_complete: "Quiz Completado!",

    // Stories
    stories_title: "Historias de Bitcoin",
    stories_intro: "Historias reales de como Bitcoin ayuda a los salvadorenos",
    story_1_title: "La Remesa de Maria",
    story_1: `Maria trabaja en EEUU y envia dinero a casa cada mes. Antes de Bitcoin, pagaba $50 en comisiones para enviar $500. Ahora con Lightning Network, envia el monto completo en segundos por centavos!

Su madre recibe el dinero al instante en su telefono, sin necesidad de banco.`,
    story_2_title: "Carlos el Pescador",
    story_2: `Carlos vende pescado en la playa de El Zonte. Los turistas le pagan en Bitcoin usando sus telefonos. No necesita cuenta bancaria ni terminal de tarjetas.

Ahorra algo en Bitcoin y convierte el resto a dolares para gastos diarios.`,
    story_3_title: "La Pupusera",
    story_3: `Dona Rosa ha vendido pupusas por 30 anos. Cuando llego Bitcoin, estaba nerviosa. Su nieto le enseno a aceptar pagos Lightning.

Ahora turistas de todo el mundo compran sus pupusas con Bitcoin. Su negocio ha crecido 40%!`,

    // AI Tutor
    tutor_title: "Tutor IA de Bitcoin",
    tutor_placeholder: "Preguntame lo que quieras sobre Bitcoin...",
    suggested_questions: "Preguntas Sugeridas",
    sq_1: "Que es Bitcoin?",
    sq_2: "Como mantengo mi Bitcoin seguro?",
    sq_3: "Que es Lightning Network?",
    sq_4: "Por que El Salvador adopto Bitcoin?",

    // Achievements
    ach_first_lesson: "Primera Leccion Completada",
    ach_security_master: "Maestro de Seguridad",
    ach_quiz_champion: "Campeon del Quiz",
    ach_budget_pro: "Profesional del Presupuesto",
    ach_story_reader: "Lector de Historias",

    // Chatbot
    chatbot_title: "Preguntame",
    mode_socratic: "Socratico",
    mode_teacher: "Enseñame",
    mode_voice: "Simple",
    mode_curriculum: "Curriculo",
    socratic_desc: "Te guio con preguntas",
    teacher_desc: "Explicame, te hare preguntas",
    voice_desc: "Respuestas simples y conversacionales",
    curriculum_desc: "Sigue el curriculo de Bitcoin",
    send: "Enviar",
    clear_chat: "Limpiar",
    chat_placeholder: "Pregunta lo que quieras sobre Bitcoin...",

    // Bitcoin Price
    current_price: "Precio Actual de Bitcoin",
    sats_per_dollar: "satoshis por $1 USD",

    // Common
    mark_complete: "Marcar como Completado",
    reset: "Reiniciar",
  }
};

export type TranslationKey = keyof typeof translations.en;

export function t(key: TranslationKey, lang: Language): string {
  return translations[lang][key] || translations.en[key] || key;
}
