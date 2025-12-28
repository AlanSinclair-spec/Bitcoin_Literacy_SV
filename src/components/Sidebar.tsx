'use client';

import { useState, useEffect } from 'react';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import {
  Globe,
  Trophy,
  TrendingUp,
  TrendingDown,
  Send,
  Trash2,
  Brain,
  GraduationCap,
  Mic,
  BookOpen
} from 'lucide-react';

const CURRICULUM_TOPICS = [
  { en: "What is Bitcoin?", es: "Que es Bitcoin?" },
  { en: "Why Bitcoin in El Salvador?", es: "Por que Bitcoin en El Salvador?" },
  { en: "Satoshis & Units", es: "Satoshis y Unidades" },
  { en: "Wallets & Security", es: "Billeteras y Seguridad" },
  { en: "Lightning Network", es: "Red Lightning" },
  { en: "HODL & Saving", es: "HODL y Ahorro" },
  { en: "Avoiding Scams", es: "Evitando Estafas" },
];

export default function Sidebar() {
  const {
    language,
    setLanguage,
    xp,
    level,
    achievements,
    chatbotMode,
    setChatbotMode,
    chatHistory,
    addChatMessage,
    clearChatHistory,
    curriculumTopic,
    setCurriculumTopic,
    addXp,
    bitcoinPrice,
    priceChange24h,
    setBitcoinPrice,
  } = useStore();

  const [chatInput, setChatInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Fetch Bitcoin price
  useEffect(() => {
    const fetchPrice = async () => {
      try {
        const res = await fetch(
          'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true'
        );
        const data = await res.json();
        setBitcoinPrice(data.bitcoin.usd, data.bitcoin.usd_24h_change);
      } catch (error) {
        console.error('Failed to fetch Bitcoin price:', error);
      }
    };
    fetchPrice();
    const interval = setInterval(fetchPrice, 60000);
    return () => clearInterval(interval);
  }, [setBitcoinPrice]);

  const handleSendMessage = async () => {
    if (!chatInput.trim() || isLoading) return;

    const userMessage = chatInput.trim();
    setChatInput('');
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
        addChatMessage({ role: 'assistant', content: data.error || 'Error getting response' });
      }
    } catch (error) {
      addChatMessage({ role: 'assistant', content: 'Error connecting to AI' });
    } finally {
      setIsLoading(false);
    }
  };

  const modes = [
    { key: 'socratic', icon: Brain, label: 'mode_socratic' },
    { key: 'teacher', icon: GraduationCap, label: 'mode_teacher' },
    { key: 'voice', icon: Mic, label: 'mode_voice' },
    { key: 'curriculum', icon: BookOpen, label: 'mode_curriculum' },
  ] as const;

  const satsPerDollar = bitcoinPrice ? Math.round(100000000 / bitcoinPrice) : 0;

  return (
    <aside className="w-80 bg-bitcoin-dark-secondary border-r border-bitcoin-orange/20 h-screen overflow-y-auto p-4 flex flex-col">
      {/* Language Toggle */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2 text-bitcoin-orange">
          <Globe size={20} />
          <span className="font-semibold">{t('language', language)}</span>
        </div>
        <div className="flex gap-1">
          <button
            onClick={() => setLanguage('en')}
            className={`px-3 py-1 rounded-full text-sm transition-all ${
              language === 'en'
                ? 'bg-bitcoin-orange text-white'
                : 'bg-bitcoin-dark text-gray-400 hover:text-white'
            }`}
          >
            EN
          </button>
          <button
            onClick={() => setLanguage('es')}
            className={`px-3 py-1 rounded-full text-sm transition-all ${
              language === 'es'
                ? 'bg-bitcoin-orange text-white'
                : 'bg-bitcoin-dark text-gray-400 hover:text-white'
            }`}
          >
            ES
          </button>
        </div>
      </div>

      {/* Progress */}
      <div className="card mb-4">
        <h3 className="text-bitcoin-orange font-semibold mb-3">{t('your_progress', language)}</h3>
        <div className="flex gap-4 mb-3">
          <div className="text-center">
            <div className="text-2xl font-bold text-bitcoin-orange">{level}</div>
            <div className="text-xs text-gray-400">{t('level', language)}</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-white">{xp}</div>
            <div className="text-xs text-gray-400">{t('xp', language)}</div>
          </div>
        </div>
        <div className="progress-bar">
          <div className="progress-bar-fill" style={{ width: `${(xp % 100)}%` }} />
        </div>
      </div>

      {/* Achievements */}
      {achievements.length > 0 && (
        <div className="card mb-4">
          <div className="flex items-center gap-2 text-bitcoin-orange mb-2">
            <Trophy size={18} />
            <span className="font-semibold">{t('achievements', language)}</span>
          </div>
          <div className="flex flex-wrap gap-1">
            {achievements.map((ach) => (
              <span key={ach} className="text-xs bg-bitcoin-dark px-2 py-1 rounded-full">
                {t(ach as any, language)}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Bitcoin Price */}
      {bitcoinPrice && (
        <div className="card mb-4">
          <h3 className="text-bitcoin-orange font-semibold mb-2">{t('current_price', language)}</h3>
          <div className="flex items-center gap-2">
            <span className="text-xl font-bold">${bitcoinPrice.toLocaleString()}</span>
            <span className={`flex items-center text-sm ${priceChange24h >= 0 ? 'text-green-500' : 'text-red-500'}`}>
              {priceChange24h >= 0 ? <TrendingUp size={16} /> : <TrendingDown size={16} />}
              {priceChange24h.toFixed(2)}%
            </span>
          </div>
          <div className="text-xs text-gray-400 mt-1">
            {satsPerDollar.toLocaleString()} {t('sats_per_dollar', language)}
          </div>
        </div>
      )}

      {/* Floating Chatbot */}
      <div className="flex-1 flex flex-col min-h-0">
        <h3 className="text-bitcoin-orange font-semibold mb-2">
          {t('chatbot_title', language)}
        </h3>

        {/* Mode Selector */}
        <div className="grid grid-cols-4 gap-1 mb-2">
          {modes.map(({ key, icon: Icon }) => (
            <button
              key={key}
              onClick={() => setChatbotMode(key)}
              className={`p-2 rounded-lg transition-all ${
                chatbotMode === key
                  ? 'bg-bitcoin-orange text-white'
                  : 'bg-bitcoin-dark text-gray-400 hover:text-white hover:bg-bitcoin-dark/80'
              }`}
              title={t(`mode_${key}` as any, language)}
            >
              <Icon size={18} className="mx-auto" />
            </button>
          ))}
        </div>

        {/* Mode Description */}
        <p className="text-xs text-gray-400 mb-2">
          {t(`${chatbotMode}_desc` as any, language)}
        </p>

        {/* Curriculum Topic Selector */}
        {chatbotMode === 'curriculum' && (
          <select
            value={curriculumTopic}
            onChange={(e) => setCurriculumTopic(Number(e.target.value))}
            className="w-full bg-bitcoin-dark border border-bitcoin-orange/30 rounded-lg p-2 text-sm mb-2 focus:outline-none focus:border-bitcoin-orange"
          >
            {CURRICULUM_TOPICS.map((topic, idx) => (
              <option key={idx} value={idx}>
                {topic[language]}
              </option>
            ))}
          </select>
        )}

        {/* Chat Messages */}
        <div className="flex-1 overflow-y-auto space-y-2 mb-2 min-h-[150px] max-h-[250px] bg-bitcoin-dark/50 rounded-lg p-2">
          {chatHistory.slice(-6).map((msg, idx) => (
            <div
              key={idx}
              className={`text-sm p-2 rounded-lg ${
                msg.role === 'user'
                  ? 'bg-bitcoin-orange/20 ml-4'
                  : 'bg-bitcoin-dark border border-bitcoin-orange/20 mr-4'
              }`}
            >
              <span className="mr-1">{msg.role === 'user' ? '👤' : '🤖'}</span>
              {msg.content.length > 150 ? msg.content.slice(0, 150) + '...' : msg.content}
            </div>
          ))}
          {isLoading && (
            <div className="text-sm p-2 rounded-lg bg-bitcoin-dark border border-bitcoin-orange/20 mr-4">
              <span className="mr-1">🤖</span>
              <span className="animate-pulse">...</span>
            </div>
          )}
        </div>

        {/* Chat Input */}
        <div className="flex gap-2">
          <input
            type="text"
            value={chatInput}
            onChange={(e) => setChatInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder={t('chat_placeholder', language)}
            className="flex-1 bg-bitcoin-dark border border-bitcoin-orange/30 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-bitcoin-orange"
          />
          <button
            onClick={handleSendMessage}
            disabled={isLoading}
            className="btn-bitcoin p-2"
          >
            <Send size={18} />
          </button>
          <button
            onClick={clearChatHistory}
            className="btn-secondary p-2"
          >
            <Trash2 size={18} />
          </button>
        </div>
      </div>
    </aside>
  );
}
