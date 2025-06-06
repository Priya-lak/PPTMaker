import React, { useState, useEffect } from 'react';
import { useApp } from '../contexts/AppContext';
import { apiService } from '../services/api';

const DownloadPage: React.FC = () => {
  const { state, setLoading, setError, resetState } = useApp();
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [previewLoading, setPreviewLoading] = useState(true);
  const [previewError, setPreviewError] = useState<string | null>(null);
  const [previewMethod, setPreviewMethod] = useState<'google' | 'blob' | 'direct'>('google');

  useEffect(() => {
    const loadPreview = async () => {
      if (state.outputFile) {
        setPreviewLoading(true);
        setPreviewError(null);

        try {
          if (previewMethod === 'google') {
            // Try Google Docs viewer first
            const googleUrl = apiService.getGoogleDocsPreviewUrl(state.outputFile);
            setPreviewUrl(googleUrl);
          } else if (previewMethod === 'blob') {
            // Fallback to blob method
            const blobUrl = await apiService.getPreviewBlob(state.outputFile);
            setPreviewUrl(blobUrl);
          } else {
            // Direct URL method
            const directUrl = apiService.getPreviewUrl(state.outputFile);
            setPreviewUrl(directUrl);
          }
        } catch (error) {
          console.error('Failed to load preview:', error);
          setPreviewError('Preview not available');
        } finally {
          setPreviewLoading(false);
        }
      }
    };

    loadPreview();

    // Cleanup blob URL when component unmounts or outputFile changes
    return () => {
      if (previewUrl && previewUrl.startsWith('blob:')) {
        URL.revokeObjectURL(previewUrl);
      }
    };
  }, [state.outputFile, previewMethod]);

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

  const handlePreviewMethodChange = (method: 'google' | 'blob' | 'direct') => {
    setPreviewMethod(method);
  };

  const renderPreview = () => {
    if (previewLoading) {
      return (
        <div className="flex items-center justify-center h-[600px] text-gray-400">
          <div className="text-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500 mx-auto mb-4"></div>
            <p>Loading presentation preview...</p>
            <p className="text-sm mt-2">Using {previewMethod === 'google' ? 'Google Docs Viewer' : previewMethod === 'blob' ? 'Blob Method' : 'Direct Method'}</p>
          </div>
        </div>
      );
    }

    if (previewError) {
      return (
        <div className="flex items-center justify-center h-[600px] text-gray-400">
          <div className="text-center">
            <div className="text-4xl mb-4">⚠️</div>
            <p className="text-red-300 mb-2">{previewError}</p>
            <p className="text-sm mb-4">Try a different preview method:</p>
            <div className="flex gap-2 justify-center">
              <button
                onClick={() => handlePreviewMethodChange('google')}
                className={`px-3 py-1 text-xs rounded ${previewMethod === 'google' ? 'bg-blue-600' : 'bg-gray-600'}`}
              >
                Google Viewer
              </button>
              <button
                onClick={() => handlePreviewMethodChange('blob')}
                className={`px-3 py-1 text-xs rounded ${previewMethod === 'blob' ? 'bg-blue-600' : 'bg-gray-600'}`}
              >
                Blob Method
              </button>
              <button
                onClick={() => handlePreviewMethodChange('direct')}
                className={`px-3 py-1 text-xs rounded ${previewMethod === 'direct' ? 'bg-blue-600' : 'bg-gray-600'}`}
              >
                Direct
              </button>
            </div>
          </div>
        </div>
      );
    }

    if (previewUrl) {
      return (
        <div className="relative">
          <iframe
            src={previewUrl}
            className="w-full h-[600px] border-0 rounded-lg"
            title="PowerPoint Preview"
            sandbox="allow-same-origin allow-scripts allow-popups allow-forms"
            onError={() => {
              setPreviewError('Failed to load preview iframe');
            }}
            onLoad={() => {
              console.log('Preview loaded successfully');
            }}
          />
          {previewMethod === 'google' && (
            <div className="absolute top-2 right-2 bg-black bg-opacity-50 text-white text-xs px-2 py-1 rounded">
              Google Docs Viewer
            </div>
          )}
        </div>
      );
    }

    return (
      <div className="flex items-center justify-center h-[600px] text-gray-400">
        <div className="text-center">
          <div className="text-4xl mb-4">📋</div>
          <p>Preview not available</p>
          <p className="text-sm mt-2">You can still download your presentation</p>
        </div>
      </div>
    );
  };

  if (!state.outputFile) {
    return (
      <div className="max-w-2xl mx-auto text-center">
        <div className="card-dark rounded-xl p-8">
          <div className="text-4xl mb-4">❌</div>
          <h2 className="text-2xl font-bold text-white mb-2">No Presentation Found</h2>
          <p className="text-gray-400 mb-6">Please create a presentation first.</p>
          <button
            onClick={handleCreateNew}
            className="button-primary px-6 py-3 rounded-lg"
          >
            🆕 Create New Presentation
          </button>
        </div>
      </div>
    );
  }

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
              <div className="flex items-center gap-2">
                <select
                  value={previewMethod}
                  onChange={(e) => handlePreviewMethodChange(e.target.value as 'google' | 'blob' | 'direct')}
                  className="text-xs bg-gray-700 text-white px-2 py-1 rounded border border-gray-600"
                >
                  <option value="google">Google Docs Viewer</option>
                  <option value="blob">Blob Method</option>
                  <option value="direct">Direct Method</option>
                </select>
                <div className="text-sm text-gray-400">
                  Preview Method
                </div>
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
                <p><span className="font-medium text-gray-300">Theme:</span> {state.layoutCustomization.theme.replace(/[-_]/g, ' ')}</p>
                <p><span className="font-medium text-gray-300">Slides:</span> {state.layoutCustomization.slide_range}</p>
                <p><span className="font-medium text-gray-300">Style:</span> {state.layoutCustomization.visual_preference.replace(/[-_]/g, ' ')}</p>
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
              <p className="mt-1">Thank you for using AI PPT Maker!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DownloadPage;
