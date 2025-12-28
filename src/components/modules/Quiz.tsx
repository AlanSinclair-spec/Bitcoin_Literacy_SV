'use client';

import { useState } from 'react';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { CheckCircle, XCircle, ArrowRight, RotateCcw, Trophy } from 'lucide-react';

const QUIZ_QUESTIONS = {
  en: [
    {
      question: "How many Bitcoin will ever exist?",
      options: ["Unlimited", "21 million", "100 million", "1 billion"],
      correct: 1,
      explanation: "Bitcoin has a fixed supply cap of 21 million coins, making it scarce like gold."
    },
    {
      question: "What year did El Salvador make Bitcoin legal tender?",
      options: ["2019", "2020", "2021", "2022"],
      correct: 2,
      explanation: "El Salvador became the first country to adopt Bitcoin as legal tender in September 2021."
    },
    {
      question: "What is a satoshi?",
      options: ["A Bitcoin wallet", "The smallest unit of Bitcoin", "A type of transaction", "The founder of Bitcoin"],
      correct: 1,
      explanation: "A satoshi is the smallest unit of Bitcoin. 1 BTC = 100,000,000 satoshis."
    },
    {
      question: "What should you NEVER share?",
      options: ["Your Bitcoin address", "Your seed phrase", "Your transaction history", "Your wallet app name"],
      correct: 1,
      explanation: "Your seed phrase gives complete access to your Bitcoin. Never share it with anyone!"
    },
    {
      question: "What is Lightning Network used for?",
      options: ["Mining Bitcoin", "Fast, cheap transactions", "Creating new Bitcoin", "Storing passwords"],
      correct: 1,
      explanation: "Lightning Network enables instant, low-cost Bitcoin transactions - perfect for everyday payments."
    }
  ],
  es: [
    {
      question: "Cuantos Bitcoin existiran en total?",
      options: ["Ilimitados", "21 millones", "100 millones", "1 billon"],
      correct: 1,
      explanation: "Bitcoin tiene un limite fijo de 21 millones de monedas, haciendolo escaso como el oro."
    },
    {
      question: "En que ano El Salvador hizo a Bitcoin moneda legal?",
      options: ["2019", "2020", "2021", "2022"],
      correct: 2,
      explanation: "El Salvador se convirtio en el primer pais en adoptar Bitcoin como moneda legal en septiembre 2021."
    },
    {
      question: "Que es un satoshi?",
      options: ["Una billetera Bitcoin", "La unidad mas pequena de Bitcoin", "Un tipo de transaccion", "El fundador de Bitcoin"],
      correct: 1,
      explanation: "Un satoshi es la unidad mas pequena de Bitcoin. 1 BTC = 100,000,000 satoshis."
    },
    {
      question: "Que NUNCA debes compartir?",
      options: ["Tu direccion Bitcoin", "Tu frase semilla", "Tu historial de transacciones", "El nombre de tu app"],
      correct: 1,
      explanation: "Tu frase semilla da acceso completo a tu Bitcoin. Nunca la compartas con nadie!"
    },
    {
      question: "Para que se usa Lightning Network?",
      options: ["Minar Bitcoin", "Transacciones rapidas y baratas", "Crear nuevo Bitcoin", "Guardar contrasenas"],
      correct: 1,
      explanation: "Lightning Network permite transacciones instantaneas y de bajo costo - perfecto para pagos diarios."
    }
  ]
};

export default function Quiz() {
  const { language, quizIndex, quizScore, setQuizIndex, incrementQuizScore, resetQuiz, addAchievement, addXp } = useStore();
  const [selectedAnswer, setSelectedAnswer] = useState<number | null>(null);
  const [showResult, setShowResult] = useState(false);

  const questions = QUIZ_QUESTIONS[language];
  const currentQuestion = questions[quizIndex];
  const isComplete = quizIndex >= questions.length;

  const handleAnswer = () => {
    if (selectedAnswer === null) return;
    setShowResult(true);
    if (selectedAnswer === currentQuestion.correct) {
      incrementQuizScore();
      addXp(10);
    }
  };

  const handleNext = () => {
    setSelectedAnswer(null);
    setShowResult(false);
    setQuizIndex(quizIndex + 1);

    if (quizIndex + 1 >= questions.length && quizScore >= questions.length * 0.7) {
      addAchievement('ach_quiz_champion');
    }
  };

  const handleReset = () => {
    resetQuiz();
    setSelectedAnswer(null);
    setShowResult(false);
  };

  if (isComplete) {
    return (
      <div className="space-y-6">
        <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('quiz_title', language)}</h2>

        <div className="card text-center">
          <Trophy className="mx-auto text-bitcoin-orange mb-4" size={64} />
          <h3 className="text-2xl font-bold mb-2">{t('quiz_complete', language)}</h3>
          <div className="text-4xl font-bold text-bitcoin-orange my-4">
            {quizScore} / {questions.length}
          </div>
          <p className="text-gray-400">
            {quizScore >= questions.length * 0.7
              ? (language === 'en' ? 'Excellent work! You\'re a Bitcoin expert!' : 'Excelente trabajo! Eres un experto en Bitcoin!')
              : (language === 'en' ? 'Keep learning and try again!' : 'Sigue aprendiendo e intentalo de nuevo!')}
          </p>
        </div>

        <button onClick={handleReset} className="btn-bitcoin w-full flex items-center justify-center gap-2">
          <RotateCcw size={20} />
          {language === 'en' ? 'Try Again' : 'Intentar de Nuevo'}
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('quiz_title', language)}</h2>
      <p className="text-gray-300">{t('quiz_intro', language)}</p>

      {/* Progress */}
      <div className="flex items-center gap-4">
        <span className="text-gray-400">{t('question', language)} {quizIndex + 1}/{questions.length}</span>
        <div className="flex-1 progress-bar">
          <div className="progress-bar-fill" style={{ width: `${((quizIndex) / questions.length) * 100}%` }} />
        </div>
      </div>

      {/* Question */}
      <div className="card">
        <h3 className="text-xl font-semibold mb-6">{currentQuestion.question}</h3>

        <div className="space-y-3">
          {currentQuestion.options.map((option, idx) => (
            <button
              key={idx}
              onClick={() => !showResult && setSelectedAnswer(idx)}
              disabled={showResult}
              className={`w-full p-4 rounded-xl border-2 text-left transition-all ${
                showResult
                  ? idx === currentQuestion.correct
                    ? 'border-green-500 bg-green-500/20'
                    : idx === selectedAnswer
                    ? 'border-red-500 bg-red-500/20'
                    : 'border-bitcoin-dark-secondary'
                  : selectedAnswer === idx
                  ? 'border-bitcoin-orange bg-bitcoin-orange/20'
                  : 'border-bitcoin-dark-secondary hover:border-bitcoin-orange/50'
              }`}
            >
              <div className="flex items-center gap-3">
                {showResult && idx === currentQuestion.correct && <CheckCircle className="text-green-400" size={20} />}
                {showResult && idx === selectedAnswer && idx !== currentQuestion.correct && <XCircle className="text-red-400" size={20} />}
                <span>{option}</span>
              </div>
            </button>
          ))}
        </div>
      </div>

      {/* Result */}
      {showResult && (
        <div className={`card ${selectedAnswer === currentQuestion.correct ? 'bg-green-500/20 border-green-500' : 'bg-red-500/20 border-red-500'}`}>
          <p className={`font-semibold mb-2 ${selectedAnswer === currentQuestion.correct ? 'text-green-400' : 'text-red-400'}`}>
            {selectedAnswer === currentQuestion.correct ? t('correct', language) : t('incorrect', language)}
          </p>
          <p className="text-gray-300 text-sm">{currentQuestion.explanation}</p>
        </div>
      )}

      {/* Buttons */}
      {!showResult ? (
        <button
          onClick={handleAnswer}
          disabled={selectedAnswer === null}
          className={`btn-bitcoin w-full ${selectedAnswer === null ? 'opacity-50 cursor-not-allowed' : ''}`}
        >
          {t('submit_answer', language)}
        </button>
      ) : (
        <button onClick={handleNext} className="btn-bitcoin w-full flex items-center justify-center gap-2">
          {t('next_question', language)}
          <ArrowRight size={20} />
        </button>
      )}
    </div>
  );
}
