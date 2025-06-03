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
      <div className="card-dark rounded-xl p-8 hover-lift">
        <div className="mb-8">
          <div className="text-6xl mb-4 cute-bounce">🎉</div>
          <h2 className="text-3xl font-bold text-white mb-2">
            Your Presentation is Ready!
          </h2>
          <p className="text-gray-400 text-lg">
            Your PowerPoint presentation has been generated successfully
          </p>
        </div>

        {state.error && (
          <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-4 mb-6">
            <p className="text-red-300">{state.error}</p>
          </div>
        )}

        <div className="card-dark rounded-lg p-6 border border-gray-700 mb-8">
          <h3 className="text-lg font-semibold text-white mb-3">Presentation Details</h3>
          <div className="space-y-2 text-gray-400 text-left">
            <p><span className="font-medium text-gray-300">Topic:</span> {state.topic}</p>
            <p><span className="font-medium text-gray-300">Theme:</span> {state.layoutCustomization.theme.replace('-', ' ')}</p>
            <p><span className="font-medium text-gray-300">Slides:</span> {state.layoutCustomization.slide_range}</p>
            <p><span className="font-medium text-gray-300">Style:</span> {state.layoutCustomization.visual_preference.replace('_', ' ')}</p>
            {state.outputFile && (
              <p><span className="font-medium text-gray-300">File:</span> {state.outputFile}</p>
            )}
          </div>
        </div>

        <div className="space-y-4">
          <button
            onClick={handleDownload}
            disabled={state.isLoading}
            className={`w-full py-4 px-6 rounded-xl font-semibold text-lg transition-all duration-200 ${
              state.isLoading
                ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                : 'button-primary hover:scale-[1.02]'
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
            className="w-full px-6 py-3 button-secondary rounded-lg transition-all duration-200"
          >
            🆕 Create New Presentation
          </button>
        </div>

        <div className="mt-8 text-gray-500 text-sm">
          <p>Thank you for using AI PPT Maker!</p>
          <p>Your presentation will be downloaded as a .pptx file</p>
        </div>
      </div>
    </div>
  );
};

export default DownloadPage;
