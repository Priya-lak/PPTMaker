import React from 'react';
import { AppProvider, useApp } from '../contexts/AppContext';
import ProgressIndicator from '../components/ProgressIndicator';
import ContentGeneratorForm from '../components/ContentGeneratorForm';
import ContentPreview from '../components/ContentPreview';
import PPTSettings from '../components/PPTSettings';
import DownloadPage from '../components/DownloadPage';

const AppContent: React.FC = () => {
  const { state } = useApp();

  const renderCurrentStep = () => {
    switch (state.currentStep) {
      case 1:
        return <ContentGeneratorForm />;
      case 2:
        return <ContentPreview />;
      case 3:
        return <PPTSettings />;
      case 4:
        return <DownloadPage />;
      default:
        return <ContentGeneratorForm />;
    }
  };

  return (
    <div className="min-h-screen py-8 px-4 bg-gray-900">
      <div className="container mx-auto max-w-6xl">
        <ProgressIndicator />
        {renderCurrentStep()}
      </div>
    </div>
  );
};

const Index: React.FC = () => {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
};

export default Index;
