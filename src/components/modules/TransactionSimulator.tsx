'use client';

import { useState } from 'react';
import { useStore } from '@/store/useStore';
import { t } from '@/lib/translations';
import { Send, Zap, Rocket, Turtle, RotateCcw, CheckCircle, Wallet } from 'lucide-react';

export default function TransactionSimulator() {
  const { language, simulationWallet, deductFromWallet, resetWallet, addXp } = useStore();
  const [recipient, setRecipient] = useState('bc1q' + Array(40).fill(0).map(() => 'abcdef0123456789'[Math.floor(Math.random() * 16)]).join('').slice(0, 40));
  const [amount, setAmount] = useState(10000);
  const [feeType, setFeeType] = useState<'lightning' | 'priority' | 'economy'>('lightning');
  const [showSuccess, setShowSuccess] = useState(false);
  const [txId, setTxId] = useState('');

  const fees = {
    lightning: 1,
    priority: Math.floor(amount * 0.001),
    economy: Math.floor(amount * 0.0005),
  };

  const fee = fees[feeType];
  const total = amount + fee;

  const handleSend = () => {
    if (total <= simulationWallet) {
      deductFromWallet(total);
      setTxId(Array(64).fill(0).map(() => '0123456789abcdef'[Math.floor(Math.random() * 16)]).join(''));
      setShowSuccess(true);
      addXp(15);
    }
  };

  const handleReset = () => {
    resetWallet();
    setShowSuccess(false);
  };

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold text-bitcoin-gradient">{t('simulator_title', language)}</h2>
      <p className="text-gray-300">{t('simulator_intro', language)}</p>

      {/* Wallet Balance */}
      <div className="card bg-bitcoin-orange/10 border-bitcoin-orange">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Wallet className="text-bitcoin-orange" size={24} />
            <span className="font-semibold">{t('your_wallet', language)}</span>
          </div>
          <span className="text-2xl font-bold text-bitcoin-orange">{simulationWallet.toLocaleString()} sats</span>
        </div>
      </div>

      {!showSuccess ? (
        <>
          {/* Recipient */}
          <div className="card">
            <label className="block text-gray-300 mb-2">{t('send_to', language)}</label>
            <input
              type="text"
              value={recipient}
              onChange={(e) => setRecipient(e.target.value)}
              className="w-full bg-bitcoin-dark border border-bitcoin-orange/30 rounded-lg px-4 py-3 font-mono text-sm focus:outline-none focus:border-bitcoin-orange"
            />
          </div>

          {/* Amount */}
          <div className="card">
            <label className="block text-gray-300 mb-2">{t('amount_sats', language)}</label>
            <input
              type="number"
              value={amount}
              onChange={(e) => setAmount(Math.min(Number(e.target.value), simulationWallet))}
              min={1}
              max={simulationWallet}
              step={1000}
              className="w-full bg-bitcoin-dark border border-bitcoin-orange/30 rounded-lg px-4 py-3 text-xl font-bold focus:outline-none focus:border-bitcoin-orange"
            />
          </div>

          {/* Fee Selection */}
          <div className="card">
            <label className="block text-gray-300 mb-3">{t('network_fee', language)}</label>
            <div className="grid grid-cols-3 gap-3">
              <button
                onClick={() => setFeeType('lightning')}
                className={`p-4 rounded-xl border-2 transition-all ${feeType === 'lightning' ? 'border-bitcoin-orange bg-bitcoin-orange/20' : 'border-bitcoin-dark-secondary hover:border-bitcoin-orange/50'}`}
              >
                <Zap className="mx-auto mb-2 text-yellow-400" size={24} />
                <div className="text-sm font-semibold">Lightning</div>
                <div className="text-xs text-gray-400">Instant</div>
                <div className="text-bitcoin-orange font-bold mt-1">{fees.lightning} sats</div>
              </button>
              <button
                onClick={() => setFeeType('priority')}
                className={`p-4 rounded-xl border-2 transition-all ${feeType === 'priority' ? 'border-bitcoin-orange bg-bitcoin-orange/20' : 'border-bitcoin-dark-secondary hover:border-bitcoin-orange/50'}`}
              >
                <Rocket className="mx-auto mb-2 text-purple-400" size={24} />
                <div className="text-sm font-semibold">Priority</div>
                <div className="text-xs text-gray-400">~10 min</div>
                <div className="text-bitcoin-orange font-bold mt-1">{fees.priority} sats</div>
              </button>
              <button
                onClick={() => setFeeType('economy')}
                className={`p-4 rounded-xl border-2 transition-all ${feeType === 'economy' ? 'border-bitcoin-orange bg-bitcoin-orange/20' : 'border-bitcoin-dark-secondary hover:border-bitcoin-orange/50'}`}
              >
                <Turtle className="mx-auto mb-2 text-green-400" size={24} />
                <div className="text-sm font-semibold">Economy</div>
                <div className="text-xs text-gray-400">~1 hour</div>
                <div className="text-bitcoin-orange font-bold mt-1">{fees.economy} sats</div>
              </button>
            </div>
          </div>

          {/* Total */}
          <div className="card bg-bitcoin-dark">
            <div className="flex justify-between text-lg">
              <span>Total:</span>
              <span className="font-bold">{amount.toLocaleString()} + {fee.toLocaleString()} = <span className="text-bitcoin-orange">{total.toLocaleString()} sats</span></span>
            </div>
          </div>

          {/* Send Button */}
          <button
            onClick={handleSend}
            disabled={total > simulationWallet}
            className={`btn-bitcoin w-full flex items-center justify-center gap-2 ${total > simulationWallet ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            <Send size={20} />
            {t('send_transaction', language)}
          </button>
        </>
      ) : (
        <>
          {/* Success Message */}
          <div className="card bg-green-500/20 border-green-500">
            <div className="flex items-center gap-3 mb-4">
              <CheckCircle className="text-green-400" size={32} />
              <span className="text-xl font-bold text-green-400">{t('transaction_success', language)}</span>
            </div>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-400">TX ID:</span>
                <span className="font-mono text-xs">{txId.slice(0, 20)}...</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Amount:</span>
                <span>{amount.toLocaleString()} sats</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Fee:</span>
                <span>{fee.toLocaleString()} sats</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-400">Status:</span>
                <span className="text-green-400">Confirmed</span>
              </div>
            </div>
          </div>

          <button onClick={() => setShowSuccess(false)} className="btn-bitcoin w-full">
            {language === 'en' ? 'Send Another' : 'Enviar Otra'}
          </button>
        </>
      )}

      {/* Reset Button */}
      <button onClick={handleReset} className="btn-secondary w-full flex items-center justify-center gap-2">
        <RotateCcw size={20} />
        {language === 'en' ? 'Reset Wallet' : 'Reiniciar Billetera'}
      </button>
    </div>
  );
}
