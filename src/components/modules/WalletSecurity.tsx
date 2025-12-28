'use client';

import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { Shield, Smartphone, HardDrive, AlertTriangle, CheckCircle } from 'lucide-react';

export default function WalletSecurity() {
  const { language, addAchievement, completeModule, addXp, completedModules } = useStore();
  const isCompleted = completedModules.includes('wallet');

  const handleComplete = () => {
    if (!isCompleted) {
      addAchievement('ach_security_master');
      completeModule('wallet');
      addXp(20);
    }
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('module_wallet', language)}</h2>

      <div className="card border-2 border-yellow-500/50 bg-yellow-500/10">
        <div className="flex items-start gap-3">
          <AlertTriangle className="text-yellow-500 flex-shrink-0 mt-1" size={24} />
          <p className="text-yellow-200 font-semibold">{t('seed_warning', language)}</p>
        </div>
      </div>

      <div className="card">
        <div className="flex items-center gap-2 mb-4">
          <Shield className="text-bitcoin-orange" size={24} />
          <h3 className="text-xl font-semibold text-bitcoin-orange">
            {language === 'en' ? 'Security Tips' : 'Consejos de Seguridad'}
          </h3>
        </div>
        <p className="text-gray-300 whitespace-pre-line">{t('security_tips', language)}</p>
      </div>

      <div className="card">
        <h3 className="text-xl font-semibold text-bitcoin-orange mb-4">{t('wallet_types', language)}</h3>
        <div className="grid md:grid-cols-2 gap-4">
          <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
            <div className="flex items-center gap-2 mb-2">
              <Smartphone className="text-blue-400" size={20} />
              <span className="font-semibold text-blue-400">Hot Wallet</span>
            </div>
            <p className="text-gray-300 text-sm">{t('hot_wallet', language)}</p>
            <p className="text-xs text-gray-400 mt-2">Examples: Chivo, Muun, Blue Wallet</p>
          </div>
          <div className="bg-green-500/10 border border-green-500/30 rounded-xl p-4">
            <div className="flex items-center gap-2 mb-2">
              <HardDrive className="text-green-400" size={20} />
              <span className="font-semibold text-green-400">Cold Wallet</span>
            </div>
            <p className="text-gray-300 text-sm">{t('cold_wallet', language)}</p>
            <p className="text-xs text-gray-400 mt-2">Examples: Ledger, Trezor, Coldcard</p>
          </div>
        </div>
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
