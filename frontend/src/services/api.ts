import axios from 'axios';
import {
  AuthToken, LoginCredentials, RegisterPayload, User,
  Category, ServiceItem, ServiceCreatePayload
} from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api/v1';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Inject Authorization header if token exists in localStorage
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token && config.headers) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export const authService = {
  login: async (credentials: LoginCredentials): Promise<AuthToken> => {
    const response = await api.post<AuthToken>('/auth/login', credentials);
    return response.data;
  },

  register: async (payload: RegisterPayload): Promise<User> => {
    const response = await api.post<User>('/auth/register', payload);
    return response.data;
  },

  getCurrentUser: async (): Promise<User> => {
    const response = await api.get<User>('/auth/me');
    return response.data;
  },

  getTechnicians: async (): Promise<User[]> => {
    const response = await api.get<User[]>('/auth/technicians');
    return response.data;
  },

  updateProfile: async (payload: Partial<User>): Promise<User> => {
    const response = await api.put<User>('/auth/me', payload);
    return response.data;
  }
};

export const catalogService = {
  getCategories: async (): Promise<Category[]> => {
    const response = await api.get<Category[]>('/services/categories');
    return response.data;
  },

  getServices: async (categoryId?: number, search?: string): Promise<ServiceItem[]> => {
    const params: Record<string, any> = {};
    if (categoryId) params.category_id = categoryId;
    if (search) params.search = search;
    const response = await api.get<ServiceItem[]>('/services/items', { params });
    return response.data;
  },

  getServiceById: async (id: number): Promise<ServiceItem> => {
    const response = await api.get<ServiceItem>(`/services/items/${id}`);
    return response.data;
  },

  createService: async (payload: ServiceCreatePayload): Promise<ServiceItem> => {
    const response = await api.post<ServiceItem>('/services/items', payload);
    return response.data;
  },

  updateService: async (id: number, payload: Partial<ServiceCreatePayload>): Promise<ServiceItem> => {
    const response = await api.put<ServiceItem>(`/services/items/${id}`, payload);
    return response.data;
  },

  deleteService: async (id: number): Promise<void> => {
    await api.delete(`/services/items/${id}`);
  }
};
