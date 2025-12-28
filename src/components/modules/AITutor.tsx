'use client';

import { useState } from 'react';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { Send, Trash2, Brain, GraduationCap, Mic, BookOpen, CheckCircle, AlertCircle } from 'lucide-react';

const CURRICULUM_TOPICS = [
  { en: "What is Bitcoin?", es: "Que es Bitcoin?" },
  { en: "Why Bitcoin in El Salvador?", es: "Por que Bitcoin en El Salvador?" },
  { en: "Satoshis & Units", es: "Satoshis y Unidades" },
  { en: "Wallets & Security", es: "Billeteras y Seguridad" },
  { en: "Lightning Network", es: "Red Lightning" },
  { en: "HODL & Saving", es: "HODL y Ahorro" },
  { en: "Avoiding Scams", es: "Evitando Estafas" },
];

export default function AITutor() {
  const {
    language,
    chatbotMode,
    setChatbotMode,
    chatHistory,
    addChatMessage,
    clearChatHistory,
    curriculumTopic,
    setCurriculumTopic,
    addXp,
  } = useStore();

  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const modes = [
    { key: 'socratic', icon: Brain, label: 'mode_socratic', desc: 'socratic_desc' },
    { key: 'teacher', icon: GraduationCap, label: 'mode_teacher', desc: 'teacher_desc' },
    { key: 'voice', icon: Mic, label: 'mode_voice', desc: 'voice_desc' },
    { key: 'curriculum', icon: BookOpen, label: 'mode_curriculum', desc: 'curriculum_desc' },
  ] as const;

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setInput('');
    addChatMessage({ role: 'user', content: userMessage });
    setIsLoading(true);

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: userMessage,
          mode: chatbotMode,
          language,
          curriculumTopic,
          history: chatHistory,
        }),
      });

      const data = await res.json();
      if (data.response) {
        addChatMessage({ role: 'assistant', content: data.response });
        addXp(5);
      } else {
        addChatMessage({ role: 'assistant', content: data.error || 'Error' });
      }
    } catch (error) {
      addChatMessage({ role: 'assistant', content: 'Error connecting to AI' });
    } finally {
      setIsLoading(false);
    }
  };

  // Check if API key exists (server-side only shows error in response)
  const hasApiKey = true; // We'll show error if API fails

  return (
    <div className="space-y-6 h-full flex flex-col">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('tutor_title', language)}</h2>

      {/* API Status */}
      <div className="flex items-center gap-2 text-sm">
        <CheckCircle className="text-green-400" size={16} />
        <span className="text-green-400">
          {language === 'en' ? 'AI Tutor Ready' : 'Tutor IA Listo'}
        </span>
      </div>

      {/* Mode Selector */}
      <div className="card">
        <h3 className="text-lg font-semibold text-bitcoin-orange mb-4">
          {language === 'en' ? 'Select Learning Mode' : 'Selecciona Modo de Aprendizaje'}
        </h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {modes.map(({ key, icon: Icon, label }) => (
            <button
              key={key}
              onClick={() => setChatbotMode(key)}
              className={`p-4 rounded-xl border-2 transition-all flex flex-col items-center gap-2 ${
                chatbotMode === key
                  ? 'border-bitcoin-orange bg-bitcoin-orange/20'
                  : 'border-bitcoin-dark-secondary hover:border-bitcoin-orange/50'
              }`}
            >
              <Icon size={24} className={chatbotMode === key ? 'text-bitcoin-orange' : 'text-gray-400'} />
              <span className="text-sm font-medium">{t(label as any, language)}</span>
            </button>
          ))}
        </div>
        <p className="text-sm text-gray-400 mt-3">
          {t(`${chatbotMode}_desc` as any, language)}
        </p>
      </div>

      {/* Curriculum Topic Selector */}
      {chatbotMode === 'curriculum' && (
        <div className="card">
          <h3 className="text-lg font-semibold text-bitcoin-orange mb-3">
            {language === 'en' ? 'Current Topic' : 'Tema Actual'}
          </h3>
          <select
            value={curriculumTopic}
            onChange={(e) => setCurriculumTopic(Number(e.target.value))}
            className="w-full bg-bitcoin-dark border border-bitcoin-orange/30 rounded-lg p-3 focus:outline-none focus:border-bitcoin-orange"
          >
            {CURRICULUM_TOPICS.map((topic, idx) => (
              <option key={idx} value={idx}>
                {idx + 1}. {topic[language]}
              </option>
            ))}
          </select>
        </div>
      )}

      {/* Chat Area */}
      <div className="flex-1 card flex flex-col min-h-[400px]">
        {/* Messages */}
        <div className="flex-1 overflow-y-auto space-y-4 mb-4">
          {chatHistory.length === 0 ? (
            <div className="text-center text-gray-400 py-8">
              <Brain className="mx-auto mb-4 opacity-50" size={48} />
              <p>{language === 'en' ? 'Start a conversation!' : 'Inicia una conversacion!'}</p>
            </div>
          ) : (
            chatHistory.map((msg, idx) => (
              <div
                key={idx}
                className={`chat-message ${msg.role === 'user' ? 'chat-message-user' : 'chat-message-assistant'}`}
              >
                <div className="flex items-start gap-2">
                  <span className="text-lg">{msg.role === 'user' ? '👤' : '🤖'}</span>
                  <p className="whitespace-pre-wrap">{msg.content}</p>
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="chat-message chat-message-assistant">
              <div className="flex items-center gap-2">
                <span className="text-lg">🤖</span>
                <span className="animate-pulse">{language === 'en' ? 'Thinking...' : 'Pensando...'}</span>
              </div>
            </div>
          )}
        </div>

        {/* Input */}
        <div className="flex gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            placeholder={t('chat_placeholder', language)}
            className="flex-1 bg-bitcoin-dark border border-bitcoin-orange/30 rounded-xl px-4 py-3 focus:outline-none focus:border-bitcoin-orange"
          />
          <button
            onClick={handleSend}
            disabled={isLoading || !input.trim()}
            className="btn-bitcoin px-6"
          >
            <Send size={20} />
          </button>
          <button onClick={clearChatHistory} className="btn-secondary px-4">
            <Trash2 size={20} />
          </button>
        </div>
      </div>
    </div>
  );
}
