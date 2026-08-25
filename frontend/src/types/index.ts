export type UserRole = 'CUSTOMER' | 'TECHNICIAN' | 'ADMIN';

export interface User {
  id: number;
  email: string;
  full_name: string;
  phone?: string;
  role: UserRole;
  is_active: boolean;
  is_verified: boolean;
  avatar_url?: string;
  specialization?: string;
  experience_years?: number;
  bio?: string;
  hourly_rate?: string;
  rating?: string;
  created_at: string;
  updated_at: string;
}

export interface AuthToken {
  access_token: string;
  token_type: string;
  user_id: number;
  email: string;
  role: UserRole;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterPayload {
  email: string;
  password: string;
  full_name: string;
  phone?: string;
  role: UserRole;
  specialization?: string;
  experience_years?: number;
  bio?: string;
}
