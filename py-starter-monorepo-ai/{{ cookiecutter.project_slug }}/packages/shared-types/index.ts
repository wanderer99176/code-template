/**
 * 共享类型定义
 * 
 * 此包包含前后端共享的 TypeScript 类型定义
 * 类型从 FastAPI 的 OpenAPI 规范自动生成
 */

// 导出自动生成的 API 类型
export type { paths, components } from './types'

// 通用类型定义

/**
 * API 响应包装器
 */
export interface ApiResponse<T = any> {
  success: boolean
  data?: T
  error?: ApiError
  message?: string
}

/**
 * API 错误
 */
export interface ApiError {
  code: string
  message: string
  details?: Record<string, any>
}

/**
 * 分页参数
 */
export interface PaginationParams {
  page?: number
  pageSize?: number
  sortBy?: string
  sortOrder?: 'asc' | 'desc'
}

/**
 * 分页响应
 */
export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  pageSize: number
  totalPages: number
}

/**
 * 用户角色
 */
export enum UserRole {
  Admin = 'admin',
  User = 'user',
  Guest = 'guest',
}

/**
 * 用户状态
 */
export enum UserStatus {
  Active = 'active',
  Inactive = 'inactive',
  Suspended = 'suspended',
}

// 常用类型工具

/**
 * 使所有属性可选
 */
export type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P]
}

/**
 * 使所有属性必需
 */
export type DeepRequired<T> = {
  [P in keyof T]-?: T[P] extends object ? DeepRequired<T[P]> : T[P]
}

/**
 * 排除空值
 */
export type NonNullableFields<T> = {
  [P in keyof T]: NonNullable<T[P]>
}

