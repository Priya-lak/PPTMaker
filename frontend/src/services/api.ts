import { ContentCustomization, LayoutCustomization } from '../contexts/AppContext';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://0.0.0.0:9898';

export interface GenerateContentRequest {
  topic: string;
  content_customization?: ContentCustomization;
}

export interface CreatePPTRequest {
  content: string;
  layout_customization: LayoutCustomization;
  theme: string;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

class ApiService {
  private async makeRequest<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDg5NTU2OTMsInVzZXJuYW1lIjoidXNlciJ9.k7tBBhLBcwjO_mSzk4Fmq6zcGZHRgZpd_CnySF8ZrNU',
          ...options.headers,
        },
        ...options,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('API request failed:', error);
      throw error;
    }
  }

  async generateContent(request: GenerateContentRequest): Promise<{ content: string }> {
    return this.makeRequest<{ content: string }>('/chatbot/generate-content', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async createPPT(request: CreatePPTRequest): Promise<{ output_file: string }> {
    return this.makeRequest<{ output_file: string }>('/chatbot/create-ppt', {
      method: 'POST',
      body: JSON.stringify(request),
    });
  }

  async downloadFile(filepath: string): Promise<Blob> {
    try {
      const response = await fetch(`${API_BASE_URL}/chatbot/download`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ filepath }),
      });

      if (!response.ok) {
        throw new Error(`Download failed! status: ${response.status}`);
      }

      return await response.blob();
    } catch (error) {
      console.error('Download failed:', error);
      throw error;
    }
  }
}

export const apiService = new ApiService();
