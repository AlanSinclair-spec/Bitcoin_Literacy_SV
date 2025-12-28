'use client';

import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { Language } from '@/lib/translations';

export type ChatMode = 'socratic' | 'teacher' | 'voice' | 'curriculum';

interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
}

interface StoreState {
  // Language
  language: Language;
  setLanguage: (lang: Language) => void;

  // Progress
  xp: number;
  level: number;
  achievements: string[];
  completedModules: string[];
  addXp: (amount: number) => void;
  addAchievement: (achievement: string) => void;
  completeModule: (module: string) => void;

  // Quiz
  quizIndex: number;
  quizScore: number;
  setQuizIndex: (index: number) => void;
  incrementQuizScore: () => void;
  resetQuiz: () => void;

  // Budget Game
  budgetAllocations: Record<string, number>;
  setBudgetAllocation: (category: string, amount: number) => void;
  resetBudget: () => void;

  // Transaction Simulator
  simulationWallet: number;
  deductFromWallet: (amount: number) => void;
  resetWallet: () => void;

  // Chatbot
  chatbotMode: ChatMode;
  chatHistory: ChatMessage[];
  curriculumTopic: number;
  setChatbotMode: (mode: ChatMode) => void;
  addChatMessage: (message: ChatMessage) => void;
  clearChatHistory: () => void;
  setCurriculumTopic: (index: number) => void;

  // Bitcoin Price
  bitcoinPrice: number | null;
  priceChange24h: number;
  setBitcoinPrice: (price: number, change: number) => void;
}

export const useStore = create<StoreState>()(
  persist(
    (set, get) => ({
      // Language
      language: 'es',
      setLanguage: (lang) => set({ language: lang }),

      // Progress
      xp: 0,
      level: 1,
      achievements: [],
      completedModules: [],
      addXp: (amount) => {
        const newXp = get().xp + amount;
        const newLevel = Math.floor(newXp / 100) + 1;
        set({ xp: newXp, level: newLevel });
      },
      addAchievement: (achievement) => {
        const current = get().achievements;
        if (!current.includes(achievement)) {
          set({ achievements: [...current, achievement] });
          get().addXp(25);
        }
      },
      completeModule: (module) => {
        const current = get().completedModules;
        if (!current.includes(module)) {
          set({ completedModules: [...current, module] });
        }
      },

      // Quiz
      quizIndex: 0,
      quizScore: 0,
      setQuizIndex: (index) => set({ quizIndex: index }),
      incrementQuizScore: () => set({ quizScore: get().quizScore + 1 }),
      resetQuiz: () => set({ quizIndex: 0, quizScore: 0 }),

      // Budget Game
      budgetAllocations: { food: 200, housing: 300, transport: 100, savings: 100, entertainment: 50 },
      setBudgetAllocation: (category, amount) =>
        set({ budgetAllocations: { ...get().budgetAllocations, [category]: amount } }),
      resetBudget: () =>
        set({ budgetAllocations: { food: 200, housing: 300, transport: 100, savings: 100, entertainment: 50 } }),

      // Transaction Simulator
      simulationWallet: 1000000,
      deductFromWallet: (amount) => set({ simulationWallet: get().simulationWallet - amount }),
      resetWallet: () => set({ simulationWallet: 1000000 }),

      // Chatbot
      chatbotMode: 'socratic',
      chatHistory: [],
      curriculumTopic: 0,
      setChatbotMode: (mode) => set({ chatbotMode: mode }),
      addChatMessage: (message) => set({ chatHistory: [...get().chatHistory, message] }),
      clearChatHistory: () => set({ chatHistory: [] }),
      setCurriculumTopic: (index) => set({ curriculumTopic: index }),

      // Bitcoin Price
      bitcoinPrice: null,
      priceChange24h: 0,
      setBitcoinPrice: (price, change) => set({ bitcoinPrice: price, priceChange24h: change }),
    }),
    {
      name: 'bitcoin-literacy-storage',
      partialize: (state) => ({
        language: state.language,
        xp: state.xp,
        level: state.level,
        achievements: state.achievements,
        completedModules: state.completedModules,
      }),
    }
  )
);
