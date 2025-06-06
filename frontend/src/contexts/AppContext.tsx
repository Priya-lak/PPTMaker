
import React, { createContext, useContext, useState, ReactNode } from 'react';

export interface ContentCustomization {
  detail_level: 'overview' | 'intermediate' | 'deep_dive'| "expert_level";
  engagement_level: 'informational' | 'interactive' | 'highly_engaging';
  include_examples: 'none' | 'minimal' | 'moderate'|'extensive';
  industry: string;
  length: 'brief' | 'moderate' | 'descriptive'|'comprehensive';
  presentation_purpose: 'sales_pitch' | 'conference_talk' | 'educational' | 'training'|"meeting_presentation"|'workshop'|'pitch_deck';
  target_audience: 'general' | 'students' | 'technical_experts' | 'executives';
  tone: 'casual' | 'friendly' | 'professional'|'academic'|'persuasive'|'technical';
}

export interface LayoutCustomization {
  slide_range: "3-5"|"6-9"|"10-15"|"16+";
  visual_preference: 'minimal' | 'visual_heavy' | 'balanced';
  theme: string;
}

export interface AppState {
  currentStep: number;
  topic: string;
  contentCustomization: ContentCustomization;
  generatedContent: string;
  editedContent: string;
  layoutCustomization: LayoutCustomization;
  outputFile: string;
  isLoading: boolean;
  error: string | null;
}

interface AppContextType {
  state: AppState;
  updateTopic: (topic: string) => void;
  updateContentCustomization: (customization: Partial<ContentCustomization>) => void;
  updateGeneratedContent: (content: string) => void;
  updateEditedContent: (content: string) => void;
  updateLayoutCustomization: (customization: Partial<LayoutCustomization>) => void;
  updateOutputFile: (file: string) => void;
  setCurrentStep: (step: number) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  resetState: () => void;
}

const initialState: AppState = {
  currentStep: 1,
  topic: '',
  contentCustomization: {
    detail_level: 'intermediate',
    engagement_level: 'informational',
    include_examples: 'moderate',
    industry: 'general',
    length: 'moderate',
    presentation_purpose: 'conference_talk',
    target_audience: 'general',
    tone: 'professional'
  },
  generatedContent: '',
  editedContent: '',
  layoutCustomization: {
    slide_range: '10-15',
    visual_preference: 'balanced',
    theme: 'madison-lilac'
  },
  outputFile: '',
  isLoading: false,
  error: null
};

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, setState] = useState<AppState>(initialState);

  const updateTopic = (topic: string) => {
    setState(prev => ({ ...prev, topic }));
  };

  const updateContentCustomization = (customization: Partial<ContentCustomization>) => {
    setState(prev => ({
      ...prev,
      contentCustomization: { ...prev.contentCustomization, ...customization }
    }));
  };

  const updateGeneratedContent = (content: string) => {
    setState(prev => ({ ...prev, generatedContent: content, editedContent: content }));
  };

  const updateEditedContent = (content: string) => {
    setState(prev => ({ ...prev, editedContent: content }));
  };

  const updateLayoutCustomization = (customization: Partial<LayoutCustomization>) => {
    setState(prev => ({
      ...prev,
      layoutCustomization: { ...prev.layoutCustomization, ...customization }
    }));
  };

  const updateOutputFile = (file: string) => {
    setState(prev => ({ ...prev, outputFile: file }));
  };

  const setCurrentStep = (step: number) => {
    setState(prev => ({ ...prev, currentStep: step }));
  };

  const setLoading = (loading: boolean) => {
    setState(prev => ({ ...prev, isLoading: loading }));
  };

  const setError = (error: string | null) => {
    setState(prev => ({ ...prev, error }));
  };

  const resetState = () => {
    setState(initialState);
  };

  return (
    <AppContext.Provider value={{
      state,
      updateTopic,
      updateContentCustomization,
      updateGeneratedContent,
      updateEditedContent,
      updateLayoutCustomization,
      updateOutputFile,
      setCurrentStep,
      setLoading,
      setError,
      resetState
    }}>
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};
