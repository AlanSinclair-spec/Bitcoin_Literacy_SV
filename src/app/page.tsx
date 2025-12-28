'use client';

import { useState } from 'react';
import Sidebar from '@/components/Sidebar';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import {
  Bitcoin,
  Shield,
  History,
  PiggyBank,
  Send,
  HelpCircle,
  BookOpen,
  Menu,
  X
} from 'lucide-react';

// Module Components
import BitcoinBasics from '@/components/modules/BitcoinBasics';
import WalletSecurity from '@/components/modules/WalletSecurity';
import HistoryOfMoney from '@/components/modules/HistoryOfMoney';
import BudgetingGame from '@/components/modules/BudgetingGame';
import TransactionSimulator from '@/components/modules/TransactionSimulator';
import Quiz from '@/components/modules/Quiz';
import Stories from '@/components/modules/Stories';

type ModuleKey = 'basics' | 'wallet' | 'history' | 'budget' | 'simulator' | 'quiz' | 'stories';

const MODULES: { key: ModuleKey; icon: typeof Bitcoin; label: string }[] = [
  { key: 'basics', icon: Bitcoin, label: 'module_basics' },
  { key: 'wallet', icon: Shield, label: 'module_wallet' },
  { key: 'history', icon: History, label: 'module_history' },
  { key: 'budget', icon: PiggyBank, label: 'module_budget' },
  { key: 'simulator', icon: Send, label: 'module_simulator' },
  { key: 'quiz', icon: HelpCircle, label: 'module_quiz' },
  { key: 'stories', icon: BookOpen, label: 'module_stories' },
];

const MODULE_COMPONENTS: Record<ModuleKey, React.ComponentType> = {
  basics: BitcoinBasics,
  wallet: WalletSecurity,
  history: HistoryOfMoney,
  budget: BudgetingGame,
  simulator: TransactionSimulator,
  quiz: Quiz,
  stories: Stories,
};

export default function Home() {
  const { language, completedModules } = useStore();
  const [selectedModule, setSelectedModule] = useState<ModuleKey | null>(null);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const ModuleComponent = selectedModule ? MODULE_COMPONENTS[selectedModule] : null;

  return (
    <div className="flex min-h-screen">
      {/* Mobile sidebar toggle */}
      <button
        onClick={() => setSidebarOpen(!sidebarOpen)}
        className="lg:hidden fixed top-4 left-4 z-50 btn-bitcoin p-2"
      >
        {sidebarOpen ? <X size={24} /> : <Menu size={24} />}
      </button>

      {/* Sidebar */}
      <div className={`
        fixed lg:static inset-y-0 left-0 z-40 transform
        ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}
        lg:translate-x-0 transition-transform duration-300
      `}>
        <Sidebar />
      </div>

      {/* Overlay for mobile */}
      {sidebarOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-30 lg:hidden"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* Main Content */}
      <main className="flex-1 p-6 lg:p-8 overflow-y-auto">
        {/* Header */}
        <div className="mb-8 pt-12 lg:pt-0">
          <h1 className="text-4xl lg:text-5xl font-bold text-bitcoin-gradient mb-2">
            {t('app_title', language)}
          </h1>
          <p className="text-gray-400 text-lg">{t('welcome', language)}</p>
        </div>

        {!selectedModule ? (
          <>
            {/* Module Selection */}
            <h2 className="text-xl font-semibold text-bitcoin-orange mb-6">
              {t('select_module', language)}
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {MODULES.map(({ key, icon: Icon, label }) => (
                <button
                  key={key}
                  onClick={() => setSelectedModule(key)}
                  className="module-btn group relative overflow-hidden"
                >
                  {completedModules.includes(key) && (
                    <div className="absolute top-2 right-2 w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                      <span className="text-white text-xs">✓</span>
                    </div>
                  )}
                  <Icon
                    className="text-bitcoin-orange mb-3 group-hover:scale-110 transition-transform"
                    size={32}
                  />
                  <h3 className="font-semibold text-white">{t(label as any, language)}</h3>
                </button>
              ))}
            </div>

            {/* Quick Stats */}
            <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="card text-center">
                <div className="text-4xl font-bold text-bitcoin-orange mb-2">
                  {completedModules.length}
                </div>
                <div className="text-gray-400">
                  {language === 'en' ? 'Modules Completed' : 'Modulos Completados'}
                </div>
              </div>
              <div className="card text-center">
                <div className="text-4xl font-bold text-bitcoin-orange mb-2">
                  {MODULES.length}
                </div>
                <div className="text-gray-400">
                  {language === 'en' ? 'Total Modules' : 'Modulos Totales'}
                </div>
              </div>
              <div className="card text-center">
                <div className="text-4xl font-bold text-bitcoin-orange mb-2">
                  {Math.round((completedModules.length / MODULES.length) * 100)}%
                </div>
                <div className="text-gray-400">
                  {language === 'en' ? 'Progress' : 'Progreso'}
                </div>
              </div>
            </div>
          </>
        ) : (
          <>
            {/* Back Button */}
            <button
              onClick={() => setSelectedModule(null)}
              className="btn-secondary mb-6 flex items-center gap-2"
            >
              ← {language === 'en' ? 'Back to Modules' : 'Volver a Modulos'}
            </button>

            {/* Module Content */}
            {ModuleComponent && <ModuleComponent />}
          </>
        )}
      </main>
    </div>
  );
}
