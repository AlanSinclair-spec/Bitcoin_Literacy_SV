'use client';

import { useState } from 'react';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { BookOpen, CheckCircle } from 'lucide-react';

export default function Stories() {
  const { language, addAchievement, completeModule, addXp, completedModules } = useStore();
  const [activeTab, setActiveTab] = useState(0);
  const isCompleted = completedModules.includes('stories');

  const stories = [
    { title: t('story_1_title', language), content: t('story_1', language), emoji: '💸' },
    { title: t('story_2_title', language), content: t('story_2', language), emoji: '🐟' },
    { title: t('story_3_title', language), content: t('story_3', language), emoji: '🫓' },
  ];

  const handleComplete = () => {
    if (!isCompleted) {
      addAchievement('ach_story_reader');
      completeModule('stories');
      addXp(25);
    }
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('stories_title', language)}</h2>
      <p className="text-gray-300">{t('stories_intro', language)}</p>

      {/* Tabs */}
      <div className="flex gap-2 overflow-x-auto pb-2">
        {stories.map((story, idx) => (
          <button
            key={idx}
            onClick={() => setActiveTab(idx)}
            className={`flex items-center gap-2 px-4 py-2 rounded-full whitespace-nowrap transition-all ${
              activeTab === idx
                ? 'bg-bitcoin-orange text-white'
                : 'bg-bitcoin-dark-secondary text-gray-400 hover:text-white'
            }`}
          >
            <span>{story.emoji}</span>
            <span>{story.title}</span>
          </button>
        ))}
      </div>

      {/* Story Content */}
      <div className="card">
        <div className="flex items-center gap-3 mb-4">
          <span className="text-4xl">{stories[activeTab].emoji}</span>
          <h3 className="text-xl font-semibold text-bitcoin-orange">{stories[activeTab].title}</h3>
        </div>
        <div className="prose prose-invert max-w-none">
          <p className="text-gray-300 whitespace-pre-line leading-relaxed">{stories[activeTab].content}</p>
        </div>
      </div>

      {/* Navigation Dots */}
      <div className="flex justify-center gap-2">
        {stories.map((_, idx) => (
          <button
            key={idx}
            onClick={() => setActiveTab(idx)}
            className={`w-3 h-3 rounded-full transition-all ${
              activeTab === idx ? 'bg-bitcoin-orange scale-125' : 'bg-bitcoin-dark-secondary hover:bg-bitcoin-orange/50'
            }`}
          />
        ))}
      </div>

      {/* Complete Button */}
      <button
        onClick={handleComplete}
        disabled={isCompleted}
        className={`btn-bitcoin w-full flex items-center justify-center gap-2 ${isCompleted ? 'opacity-50 cursor-not-allowed' : ''}`}
      >
        <BookOpen size={20} />
        {isCompleted ? '✓ ' : ''}{language === 'en' ? "I've read all stories" : 'He leido todas las historias'}
      </button>
    </div>
  );
}
