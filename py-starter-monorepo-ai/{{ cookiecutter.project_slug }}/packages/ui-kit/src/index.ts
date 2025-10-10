/**
 * UI Kit - 共享 UI 组件库
 * 
 * 提供可在整个应用中复用的 Vue 组件
 */

// 导出所有组件
export { default as Button } from './components/Button.vue'
export { default as Card } from './components/Card.vue'
export { default as Input } from './components/Input.vue'
export { default as Modal } from './components/Modal.vue'
export { default as Spinner } from './components/Spinner.vue'

// 导出类型
export type { ButtonProps } from './components/Button.vue'
export type { CardProps } from './components/Card.vue'
export type { InputProps } from './components/Input.vue'
export type { ModalProps } from './components/Modal.vue'

// 导出工具函数
export * from './utils/colors'
export * from './utils/formatters'

