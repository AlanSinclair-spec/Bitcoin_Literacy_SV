'use client';

import { useState } from 'react';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { DollarSign, Home, Car, PiggyBank, Music, Utensils, CheckCircle, RotateCcw } from 'lucide-react';

const MONTHLY_INCOME = 750;

const CATEGORIES = [
  { key: 'food', icon: Utensils, color: 'text-orange-400', max: 300 },
  { key: 'housing', icon: Home, color: 'text-blue-400', max: 400 },
  { key: 'transport', icon: Car, color: 'text-purple-400', max: 200 },
  { key: 'savings', icon: PiggyBank, color: 'text-bitcoin-orange', max: 300 },
  { key: 'entertainment', icon: Music, color: 'text-pink-400', max: 150 },
];

export default function BudgetingGame() {
  const { language, budgetAllocations, setBudgetAllocation, resetBudget, addAchievement, addXp, completedModules, completeModule } = useStore();
  const [showResult, setShowResult] = useState(false);

  const totalSpent = Object.values(budgetAllocations).reduce((a, b) => a + b, 0);
  const remaining = MONTHLY_INCOME - totalSpent;
  const isBalanced = remaining >= 0 && remaining <= 50;
  const isOver = remaining < 0;
  const isUnder = remaining > 50;

  const checkBudget = () => {
    setShowResult(true);
    if (isBalanced && !completedModules.includes('budget')) {
      addAchievement('ach_budget_pro');
      completeModule('budget');
      addXp(30);
    }
  };

  const handleReset = () => {
    resetBudget();
    setShowResult(false);
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('budget_title', language)}</h2>
      <p className="text-gray-300">{t('budget_intro', language)}</p>

      {/* Income Display */}
      <div className="card bg-green-500/10 border-green-500/30">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <DollarSign className="text-green-400" size={24} />
            <span className="font-semibold text-green-400">{t('monthly_income', language)}</span>
          </div>
          <span className="text-2xl font-bold text-green-400">${MONTHLY_INCOME}</span>
        </div>
      </div>

      {/* Budget Sliders */}
      <div className="card">
        <h3 className="text-lg font-semibold text-bitcoin-orange mb-4">{t('allocate_budget', language)}</h3>
        <div className="space-y-6">
          {CATEGORIES.map(({ key, icon: Icon, color, max }) => (
            <div key={key}>
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-2">
                  <Icon className={color} size={20} />
                  <span className="text-gray-300">{t(key as any, language)}</span>
                </div>
                <span className="font-mono font-bold">${budgetAllocations[key]}</span>
              </div>
              <input
                type="range"
                min="0"
                max={max}
                step="10"
                value={budgetAllocations[key]}
                onChange={(e) => setBudgetAllocation(key, Number(e.target.value))}
                className="w-full h-2 bg-bitcoin-dark rounded-lg appearance-none cursor-pointer accent-bitcoin-orange"
              />
            </div>
          ))}
        </div>
      </div>

      {/* Total & Remaining */}
      <div className={`card ${isOver ? 'border-red-500 bg-red-500/10' : isBalanced ? 'border-green-500 bg-green-500/10' : ''}`}>
        <div className="flex justify-between items-center">
          <span className="text-gray-300">{language === 'en' ? 'Total Allocated:' : 'Total Asignado:'}</span>
          <span className={`text-xl font-bold ${isOver ? 'text-red-500' : 'text-white'}`}>${totalSpent}</span>
        </div>
        <div className="flex justify-between items-center mt-2">
          <span className="text-gray-300">{language === 'en' ? 'Remaining:' : 'Restante:'}</span>
          <span className={`text-xl font-bold ${isOver ? 'text-red-500' : remaining > 0 ? 'text-green-400' : 'text-white'}`}>
            ${remaining}
          </span>
        </div>
      </div>

      {/* Result Message */}
      {showResult && (
        <div className={`card ${isBalanced ? 'bg-green-500/20 border-green-500' : isOver ? 'bg-red-500/20 border-red-500' : 'bg-yellow-500/20 border-yellow-500'}`}>
          <p className={`text-center font-semibold ${isBalanced ? 'text-green-400' : isOver ? 'text-red-400' : 'text-yellow-400'}`}>
            {isBalanced ? t('budget_balanced', language) : isOver ? t('budget_over', language) : t('budget_under', language)}
          </p>
        </div>
      )}

      {/* Buttons */}
      <div className="flex gap-4">
        <button onClick={checkBudget} className="btn-bitcoin flex-1 flex items-center justify-center gap-2">
          <CheckCircle size={20} />
          {t('check_budget', language)}
        </button>
        <button onClick={handleReset} className="btn-secondary flex items-center justify-center gap-2">
          <RotateCcw size={20} />
          {t('reset', language)}
        </button>
      </div>
    </div>
  );
}
