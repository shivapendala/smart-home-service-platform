export type UserRole = 'CUSTOMER' | 'TECHNICIAN' | 'ADMIN';

export type BookingStatus = 'PENDING' | 'ASSIGNED' | 'IN_PROGRESS' | 'COMPLETED' | 'CANCELLED';

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

export interface Category {
  id: number;
  name: string;
  slug: string;
  icon: string;
  description?: string;
  created_at: string;
}

export interface ServiceItem {
  id: number;
  category_id: number;
  name: string;
  slug: string;
  description: string;
  base_price: number;
  duration_minutes: number;
  image_url?: string;
  is_active: boolean;
  category?: Category;
  created_at: string;
  updated_at: string;
}

export interface Booking {
  id: number;
  customer_id: number;
  technician_id?: number;
  service_id: number;
  scheduled_date: string;
  scheduled_time_slot: string;
  address_line: string;
  city: string;
  zip_code: string;
  notes?: string;
  status: BookingStatus;
  total_amount: number;
  created_at: string;
  updated_at: string;
  customer?: User;
  technician?: User;
  service?: ServiceItem;
}

export interface BookingCreatePayload {
  service_id: number;
  scheduled_date: string;
  scheduled_time_slot: string;
  address_line: string;
  city: string;
  zip_code: string;
  notes?: string;
}

export interface ServiceCreatePayload {
  category_id: number;
  name: string;
  description: string;
  base_price: number;
  duration_minutes: number;
  image_url?: string;
  is_active?: boolean;
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
