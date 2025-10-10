<script setup lang="ts">
/**
 * Card 组件 - 卡片容器组件
 */

export interface CardProps {
  /** 是否有边框 */
  bordered?: boolean
  /** 是否有阴影 */
  shadow?: boolean
  /** 是否可悬停 */
  hoverable?: boolean
  /** 内边距大小 */
  padding?: 'none' | 'sm' | 'md' | 'lg'
}

withDefaults(defineProps<CardProps>(), {
  bordered: true,
  shadow: true,
  hoverable: false,
  padding: 'md',
})
</script>

<template>
  <div
    :class="[
      'card',
      { 'card-bordered': bordered },
      { 'card-shadow': shadow },
      { 'card-hoverable': hoverable },
      `card-padding-${padding}`,
    ]"
  >
    <div v-if="$slots.header" class="card-header">
      <slot name="header" />
    </div>
    <div class="card-body">
      <slot />
    </div>
    <div v-if="$slots.footer" class="card-footer">
      <slot name="footer" />
    </div>
  </div>
</template>

<style scoped>
.card {
  background-color: white;
  border-radius: 0.5rem;
  overflow: hidden;
}

.card-bordered {
  border: 1px solid #e5e7eb;
}

.card-shadow {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
}

.card-hoverable {
  transition: all 0.3s ease;
  cursor: pointer;
}

.card-hoverable:hover {
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  transform: translateY(-2px);
}

.card-padding-none {
  padding: 0;
}

.card-padding-sm > .card-body {
  padding: 0.75rem;
}

.card-padding-md > .card-body {
  padding: 1.25rem;
}

.card-padding-lg > .card-body {
  padding: 2rem;
}

.card-header {
  padding: 1rem 1.25rem;
  border-bottom: 1px solid #e5e7eb;
  font-weight: 600;
}

.card-footer {
  padding: 1rem 1.25rem;
  border-top: 1px solid #e5e7eb;
  background-color: #f9fafb;
}
</style>

