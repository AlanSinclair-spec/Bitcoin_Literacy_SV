'use client';

import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { ArrowRight } from 'lucide-react';

export default function HistoryOfMoney() {
  const { language } = useStore();

  const eras = [
    { key: 'barter', emoji: '🔄', color: 'bg-amber-600' },
    { key: 'commodity', emoji: '🐚', color: 'bg-yellow-600' },
    { key: 'gold', emoji: '🥇', color: 'bg-yellow-500' },
    { key: 'fiat', emoji: '💵', color: 'bg-green-600' },
    { key: 'bitcoin', emoji: '₿', color: 'bg-bitcoin-orange' },
  ];

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('history_title', language)}</h2>

      <div className="relative">
        {/* Timeline */}
        <div className="absolute left-8 top-0 bottom-0 w-1 bg-gradient-to-b from-amber-600 via-yellow-500 to-bitcoin-orange" />

        <div className="space-y-8">
          {eras.map((era, index) => (
            <div key={era.key} className="relative flex items-start gap-6 pl-4">
              {/* Timeline dot */}
              <div className={`${era.color} w-10 h-10 rounded-full flex items-center justify-center text-xl z-10 flex-shrink-0`}>
                {era.emoji}
              </div>

              {/* Content card */}
              <div className="card flex-1">
                <h3 className="text-lg font-semibold text-bitcoin-orange mb-2">
                  {t(`${era.key}_era` as any, language)}
                </h3>
                <p className="text-gray-300">{t(`${era.key}_desc` as any, language)}</p>
              </div>

              {/* Arrow to next */}
              {index < eras.length - 1 && (
                <ArrowRight className="absolute left-[26px] -bottom-6 text-bitcoin-orange/50 z-20" size={20} />
              )}
            </div>
          ))}
        </div>
      </div>

      <div className="card bg-bitcoin-orange/10 border-bitcoin-orange">
        <p className="text-center text-lg">
          {language === 'en'
            ? 'Bitcoin represents the next evolution in money: digital, scarce, and decentralized!'
            : 'Bitcoin representa la siguiente evolucion del dinero: digital, escaso y descentralizado!'}
        </p>
      </div>
    </div>
  );
}
