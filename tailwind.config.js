/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        bitcoin: {
          orange: '#F7931A',
          'orange-light': '#FFA500',
          dark: '#1a1a2e',
          'dark-secondary': '#16213e',
        },
      },
      backgroundImage: {
        'gradient-bitcoin': 'linear-gradient(135deg, #F7931A 0%, #FFA500 100%)',
        'gradient-dark': 'linear-gradient(180deg, #1a1a2e 0%, #16213e 100%)',
      },
    },
  },
  plugins: [],
}
