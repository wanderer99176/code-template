/**
 * 共享的 ESLint 配置
 * 
 * 用于所有 TypeScript/JavaScript 项目
 */

module.exports = {
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:vue/vue3-recommended',
    'prettier',
  ],
  parser: '@typescript-eslint/parser',
  plugins: ['@typescript-eslint', 'vue'],
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: 'module',
  },
  rules: {
    // TypeScript 规则
    '@typescript-eslint/no-explicit-any': 'warn',
    '@typescript-eslint/no-unused-vars': [
      'error',
      {
        argsIgnorePattern: '^_',
        varsIgnorePattern: '^_',
      },
    ],
    '@typescript-eslint/explicit-function-return-type': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-non-null-assertion': 'warn',

    // Vue 规则
    'vue/multi-word-component-names': 'off',
    'vue/require-default-prop': 'off',
    'vue/html-self-closing': [
      'error',
      {
        html: {
          void: 'always',
          normal: 'always',
          component: 'always',
        },
        svg: 'always',
        math: 'always',
      },
    ],

    // 通用规则
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'prefer-const': 'error',
    'no-var': 'error',
  },
  ignorePatterns: [
    'node_modules',
    'dist',
    '.nuxt',
    '.output',
    'coverage',
    '*.d.ts',
  ],
}

