'use client';

import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { CheckCircle } from 'lucide-react';

export default function BitcoinBasics() {
  const { language, addAchievement, completeModule, addXp, completedModules } = useStore();
  const isCompleted = completedModules.includes('basics');

  const handleComplete = () => {
    if (!isCompleted) {
      addAchievement('ach_first_lesson');
      completeModule('basics');
      addXp(20);
    }
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('module_basics', language)}</h2>

      <div className="card">
        <h3 className="text-xl font-semibold text-bitcoin-orange mb-4">{t('what_is_bitcoin', language)}</h3>
        <div className="prose prose-invert max-w-none">
          <p className="text-gray-300 whitespace-pre-line">{t('bitcoin_intro', language)}</p>
        </div>

        <div className="mt-6 flex justify-center">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png"
            alt="Bitcoin Logo"
            className="w-32 h-32"
          />
        </div>
      </div>

      <div className="card">
        <h3 className="text-xl font-semibold text-bitcoin-orange mb-4">{t('why_el_salvador', language)}</h3>
        <p className="text-gray-300 whitespace-pre-line">{t('el_salvador_reasons', language)}</p>
      </div>

      <button
        onClick={handleComplete}
        disabled={isCompleted}
        className={`btn-bitcoin w-full flex items-center justify-center gap-2 ${isCompleted ? 'opacity-50 cursor-not-allowed' : ''}`}
      >
        <CheckCircle size={20} />
        {isCompleted ? '✓ ' : ''}{t('mark_complete', language)}
      </button>
    </div>
  );
}
