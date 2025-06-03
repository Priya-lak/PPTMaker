
import React from 'react';
import { useApp } from '../contexts/AppContext';
import { apiService } from '../services/api';

const DownloadPage: React.FC = () => {
  const { state, setLoading, setError, resetState } = useApp();

  const handleDownload = async () => {
    setLoading(true);
    setError(null);

    try {
      const blob = await apiService.downloadFile(state.outputFile);

      // Create download link
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `${state.topic.replace(/[^a-z0-9]/gi, '_').toLowerCase()}_presentation.pptx`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(url);

    } catch (error) {
      setError('Failed to download file. Please try again.');
      console.error('Download error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateNew = () => {
    resetState();
  };

  return (
    <div className="max-w-2xl mx-auto text-center">
      <div className="glass-effect rounded-3xl p-8 hover-lift">
        <div className="mb-8">
          <div className="text-6xl mb-4 cute-bounce">🎉</div>
          <h2 className="text-3xl font-bold gradient-text mb-4">
            Your Presentation is Ready!
          </h2>
          <p className="text-purple-200 text-lg">
            Your PowerPoint presentation has been generated successfully
          </p>
        </div>

        {state.error && (
          <div className="bg-red-500/20 border border-red-500/50 rounded-lg p-4 mb-6">
            <p className="text-red-200">{state.error}</p>
          </div>
        )}

        <div className="bg-purple-800/30 rounded-lg p-6 border border-purple-600/30 mb-8">
          <h3 className="text-lg font-semibold text-white mb-3">Presentation Details</h3>
          <div className="space-y-2 text-purple-200 text-left">
            <p><span className="font-medium">Topic:</span> {state.topic}</p>
            <p><span className="font-medium">Theme:</span> {state.layoutCustomization.theme.replace('-', ' ')}</p>
            <p><span className="font-medium">Slides:</span> {state.layoutCustomization.slide_range}</p>
            <p><span className="font-medium">Style:</span> {state.layoutCustomization.visual_preference.replace('_', ' ')}</p>
            {state.outputFile && (
              <p><span className="font-medium">File:</span> {state.outputFile}</p>
            )}
          </div>
        </div>

        <div className="space-y-4">
          <button
            onClick={handleDownload}
            disabled={state.isLoading}
            className={`w-full py-4 px-6 rounded-xl font-semibold text-lg transition-all duration-300 ${
              state.isLoading
                ? 'bg-purple-700/50 text-purple-300 cursor-not-allowed'
                : 'gradient-purple hover:shadow-lg hover:shadow-purple-500/25 hover:scale-105 text-white'
            }`}
          >
            {state.isLoading ? (
              <span className="flex items-center justify-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                Preparing Download...
              </span>
            ) : (
              '📥 Download PowerPoint'
            )}
          </button>

          <button
            onClick={handleCreateNew}
            className="w-full px-6 py-3 bg-purple-700/50 hover:bg-purple-700 text-purple-200 hover:text-white rounded-lg transition-all duration-300 border border-purple-600/30"
          >
            🆕 Create New Presentation
          </button>
        </div>

        <div className="mt-8 text-purple-300 text-sm">
          <p>💝 Thank you for using AI PPT Maker!</p>
          <p>Your presentation will be downloaded as a .pptx file</p>
        </div>
      </div>
    </div>
  );
};

export default DownloadPage;
