import React, { useState, useEffect } from 'react';

const DownloadPage: React.FC = () => {
  // Mock state for demonstration
  const [state, setState] = useState({
    outputFile: 'sample_presentation.pptx',
    topic: 'Machine Learning Fundamentals',
    layoutCustomization: {
      theme: 'modern-dark',
      slide_range: '8-10',
      visual_preference: 'professional_clean'
    },
    isLoading: false,
    error: null
  });

  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [previewType, setPreviewType] = useState<'pdf' | 'images' | 'office'>('pdf');
  const [slideImages, setSlideImages] = useState<any[]>([]);
  const [currentSlide, setCurrentSlide] = useState(0);

  const setLoading = (loading: boolean) => {
    setState(prev => ({ ...prev, isLoading: loading }));
  };

  const setError = (error: string | null) => {
    setState(prev => ({ ...prev, error }));
  };

  const resetState = () => {
    setState({
      outputFile: '',
      topic: '',
      layoutCustomization: {
        theme: '',
        slide_range: '',
        visual_preference: ''
      },
      isLoading: false,
      error: null
    });
  };

  useEffect(() => {
    if (state.outputFile) {
      const baseUrl = 'http://0.0.0.0:9898/chatbot'; // You can make this configurable
      const token = localStorage.getItem('access_token');

      // Use your existing preview route for all preview types
      setPreviewUrl(`${baseUrl}/preview/${encodeURIComponent(state.outputFile)}?token=${token}`);
    }
  }, [state.outputFile, previewType]);

  const handleDownload = async () => {
    setLoading(true);
    setError(null);

    try {
      const baseUrl = 'http://0.0.0.0:9898'; // You can make this configurable
      const response = await fetch(`${baseUrl}/download`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('access_token')}` // If you need auth
        },
        body: JSON.stringify({ filepath: state.outputFile })
      });

      if (!response.ok) {
        throw new Error('Failed to download file');
      }

      const blob = await response.blob();

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

  const renderPreview = () => {
    if (previewUrl) {
      return (
        <iframe
          src={previewUrl}
          className="w-full h-[600px] border-0"
          title="PowerPoint Preview"
          sandbox="allow-same-origin allow-scripts"
        />
      );
    }

    return (
      <div className="flex items-center justify-center h-[600px] text-gray-400">
        <div className="text-center">
          <div className="text-4xl mb-4">📋</div>
          <p>Loading presentation preview...</p>
        </div>
      </div>
    );
  };

  return (
    <div className="max-w-7xl mx-auto">
      <div className="text-center mb-8">
        <div className="text-6xl mb-4 cute-bounce">🎉</div>
        <h2 className="text-3xl font-bold text-white mb-2">
          Your Presentation is Ready!
        </h2>
        <p className="text-gray-400 text-lg">
          Preview your PowerPoint presentation and download when ready
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Preview Section */}
        <div className="lg:col-span-3">
          <div className="card-dark rounded-xl p-6 hover-lift">
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-xl font-semibold text-white flex items-center">
                📊 PowerPoint Preview
              </h3>
              <div className="text-sm text-gray-400">
                Using your existing preview route
              </div>
            </div>
            <div className="bg-slate-800 rounded-lg overflow-hidden">
              {renderPreview()}
            </div>
          </div>
        </div>

        {/* Download & Info Section */}
        <div className="lg:col-span-1">
          <div className="card-dark rounded-xl p-6 hover-lift sticky top-4">
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-white mb-3">Presentation Details</h3>
              <div className="space-y-2 text-gray-400 text-sm">
                <p><span className="font-medium text-gray-300">Topic:</span> {state.topic}</p>
                <p><span className="font-medium text-gray-300">Theme:</span> {state.layoutCustomization.theme.replace('-', ' ')}</p>
                <p><span className="font-medium text-gray-300">Slides:</span> {state.layoutCustomization.slide_range}</p>
                <p><span className="font-medium text-gray-300">Style:</span> {state.layoutCustomization.visual_preference.replace('_', ' ')}</p>
                {state.outputFile && (
                  <p><span className="font-medium text-gray-300">File:</span> {state.outputFile.split('/').pop()}</p>
                )}
              </div>
            </div>

            {state.error && (
              <div className="bg-red-500/10 border border-red-500/30 rounded-lg p-4 mb-6">
                <p className="text-red-300 text-sm">{state.error}</p>
              </div>
            )}

            <div className="space-y-4">
              <button
                onClick={handleDownload}
                disabled={state.isLoading}
                className={`w-full py-3 px-4 rounded-lg font-semibold transition-all duration-200 ${
                  state.isLoading
                    ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                    : 'button-primary hover:scale-[1.02]'
                }`}
              >
                {state.isLoading ? (
                  <span className="flex items-center justify-center">
                    <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                    Downloading...
                  </span>
                ) : (
                  <>
                    📥 Download
                    <br />
                    <span className="text-xs opacity-75">PowerPoint File</span>
                  </>
                )}
              </button>

              <button
                onClick={handleCreateNew}
                className="w-full px-4 py-3 button-secondary rounded-lg transition-all duration-200 text-sm"
              >
                🆕 Create New Presentation
              </button>
            </div>

            <div className="mt-6 text-gray-500 text-xs text-center">
              <p>Your presentation will be downloaded as a .pptx file</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DownloadPage;
