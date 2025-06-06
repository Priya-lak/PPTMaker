
import React from 'react';
import { AppProvider, useApp } from '../contexts/AppContext';
import { AuthProvider, useAuth } from '../contexts/AuthContext';
import LoginForm from '../components/LoginForm';
import ProgressIndicator from '../components/ProgressIndicator';
import ContentGeneratorForm from '../components/ContentGeneratorForm';
import ContentPreview from '../components/ContentPreview';
import PPTSettings from '../components/PPTSettings';
import DownloadPage from '../components/DownloadPage';
import { Button } from '../components/ui/button';

const AppContent: React.FC = () => {
  const { state } = useApp();
  const { isAuthenticated, logout } = useAuth();

  if (!isAuthenticated) {
    return null; // Will be handled by AuthWrapper
  }

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
        <div className="flex justify-end mb-4">
          <Button
            onClick={logout}
            variant="outline"
            className="text-slate-300 border-slate-600 hover:bg-slate-700"
          >
            Logout
          </Button>
        </div>
        <ProgressIndicator />
        {renderCurrentStep()}
      </div>
    </div>
  );
};

const AuthWrapper: React.FC = () => {
  const { isAuthenticated, login } = useAuth();

  if (!isAuthenticated) {
    return <LoginForm onLoginSuccess={login} />;
  }

  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
};

const Index: React.FC = () => {
  return (
    <AuthProvider>
      <AuthWrapper />
    </AuthProvider>
  );
};

export default Index;
