import js from '@eslint/js'
import tsParser from '@typescript-eslint/parser'
import tsPlugin from '@typescript-eslint/eslint-plugin'

export default [
  {
    ignores: ['dist/**', 'build/**', 'node_modules/**', '.eslintrc.*', 'eslint.config.*'],
  },
  {
    ...js.configs.recommended,
    files: ['src/**/*.{ts,tsx}'],
    languageOptions: {
      ...js.configs.recommended.languageOptions,
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: { jsx: true },
        project: './tsconfig.json',
        // ESLint expects a plain string path, not a URL object.
        tsconfigRootDir: process.cwd(),
      },
      globals: {
        ...js.configs.recommended.languageOptions?.globals,
        window: 'readonly',
        document: 'readonly',
        navigator: 'readonly',
      },
    },
    plugins: {
      '@typescript-eslint': tsPlugin,
    },
    rules: {
      ...tsPlugin.configs.recommended.rules,
      ...tsPlugin.configs.stylistic.rules,
    },
  },
  {
    files: ['*.config.ts', '*.config.js', '*.config.cjs', '*.config.mjs'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        project: './tsconfig.node.json',
        tsconfigRootDir: process.cwd(),
      },
    },
    plugins: {
      '@typescript-eslint': tsPlugin,
    },
    rules: {
      ...tsPlugin.configs.recommended.rules,
      ...tsPlugin.configs.stylistic.rules,
    },
  },
]
