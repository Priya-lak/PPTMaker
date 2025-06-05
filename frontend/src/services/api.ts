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
  private getAuthHeaders(): Record<string, string> {
    const token = localStorage.getItem('access_token');
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
    };

    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

    return headers;
  }

  private async makeRequest<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        headers: {
          ...this.getAuthHeaders(),
          ...options.headers,
        },
        ...options,
      });

      if (!response.ok) {
        if (response.status === 401) {
          // Token expired or invalid, redirect to login
          localStorage.removeItem('access_token');
          window.location.reload();
        }
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
        headers: this.getAuthHeaders(),
        body: JSON.stringify({ filepath }),
      });

      if (!response.ok) {
        if (response.status === 401) {
          localStorage.removeItem('access_token');
          window.location.reload();
        }
        throw new Error(`Download failed! status: ${response.status}`);
      }

      return await response.blob();
    } catch (error) {
      console.error('Download failed:', error);
      throw error;
    }
  }

  getPreviewUrl(filepath: string): string {
    try {
      const token = localStorage.getItem('access_token');
      const encodedFilepath = encodeURIComponent(filepath);

      // Construct the preview URL - no validation needed, just return the URL
      const previewUrl = `${API_BASE_URL}/chatbot/preview/${encodedFilepath}${token ? `?token=${token}` : ''}`;

      return previewUrl;
    } catch (error) {
      console.error('Preview URL generation failed:', error);
      throw error;
    }
  }

  async validatePreview(filepath: string): Promise<boolean> {
    try {
      const previewUrl = this.getPreviewUrl(filepath);

      // Make a simple GET request to check if the file exists
      // We'll catch the response but not process the content
      const response = await fetch(previewUrl, {
        method: 'GET',
        headers: this.getAuthHeaders(),
      });

      return response.ok;
    } catch (error) {
      console.warn('Preview validation failed:', error);
      return false;
    }
  }
  getGoogleDocsPreviewUrl(filepath: string): string {
    try {
      // Get the direct URL to the file
      const directUrl = this.getPreviewUrl(filepath);

      // Construct Google Docs viewer URL
      const googleDocsUrl = `https://docs.google.com/gview?url=http://0.0.0.0:9898/chatbot/preview/temp/Deep-Learning-Basics.pptx&embedded=true`;

      return googleDocsUrl;
    } catch (error) {
      console.error('Google Docs preview URL generation failed:', error);
      throw error;
    }
  }

  async getPreviewBlob(filepath: string): Promise<string> {
    try {
      const response = await fetch(`${API_BASE_URL}/chatbot/download`, {
        method: 'POST',
        headers: this.getAuthHeaders(),
        body: JSON.stringify({ filepath }),
      });

      if (!response.ok) {
        if (response.status === 401) {
          localStorage.removeItem('access_token');
          window.location.reload();
        }
        throw new Error(`Preview blob failed! status: ${response.status}`);
      }

      const blob = await response.blob();

      // Create a blob URL for the file
      const blobUrl = URL.createObjectURL(blob);

      return blobUrl;
    } catch (error) {
      console.error('Preview blob generation failed:', error);
      throw error;
    }
  }

}

export const apiService = new ApiService();
