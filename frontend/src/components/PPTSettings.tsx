
import React from 'react';
import { useApp } from '../contexts/AppContext';
import { apiService } from '../services/api';

const themes = [
  { id: 'madison-lilac', name: 'Madison Lilac', color: 'bg-gradient-to-r from-purple-400 to-pink-400' },
  { id: 'classic-blue', name: 'Classic Blue', color: 'bg-gradient-to-r from-blue-500 to-blue-700' },
  { id: 'modern-dark', name: 'Modern Dark', color: 'bg-gradient-to-r from-gray-700 to-gray-900' },
  { id: 'sunset-orange', name: 'Sunset Orange', color: 'bg-gradient-to-r from-orange-400 to-red-500' },
  { id: 'forest-green', name: 'Forest Green', color: 'bg-gradient-to-r from-green-500 to-green-700' }
];

const PPTSettings: React.FC = () => {
  const {
    state,
    updateLayoutCustomization,
    updateOutputFile,
    setCurrentStep,
    setLoading,
    setError
  } = useApp();

  const handleCreatePPT = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await apiService.createPPT({
        content: state.editedContent,
        layout_customization: state.layoutCustomization,
        theme: state.layoutCustomization.theme
      });

      updateOutputFile(response.output_file);
      setCurrentStep(4);
    } catch (error) {
      setError('Failed to create PowerPoint. Please try again.');
      console.error('PPT creation error:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleBack = () => {
    setCurrentStep(2);
  };

  return (
    <div className="max-w-3xl mx-auto">
      <div className="glass-effect rounded-3xl p-8 hover-lift">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold gradient-text mb-4">
            🎨 Customize Your Presentation
          </h2>
          <p className="text-purple-200 text-lg">
            Choose the perfect theme and layout for your slides
          </p>
        </div>

        {state.error && (
          <div className="bg-red-500/20 border border-red-500/50 rounded-lg p-4 mb-6">
            <p className="text-red-200">{state.error}</p>
          </div>
        )}

        <div className="space-y-8">
          <div>
            <label className="block text-lg font-medium text-purple-200 mb-4">
              Theme Selection
            </label>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {themes.map((theme) => (
                <button
                  key={theme.id}
                  onClick={() => updateLayoutCustomization({ theme: theme.id as any })}
                  className={`p-4 rounded-lg border-2 transition-all duration-300 hover:scale-105 ${
                    state.layoutCustomization.theme === theme.id
                      ? 'border-purple-400 bg-purple-600/20'
                      : 'border-purple-600/30 hover:border-purple-400/50'
                  }`}
                >
                  <div className={`w-full h-16 rounded-md ${theme.color} mb-3`}></div>
                  <p className="text-white font-medium">{theme.name}</p>
                </button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium text-purple-200 mb-2">
                Number of Slides
              </label>
              <select
                value={state.layoutCustomization.slide_range}
                onChange={(e) => updateLayoutCustomization({slide_range: e.target.value })}
                className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="5-8">5-8 slides</option>
                <option value="10-15">10-15 slides</option>
                <option value="15-20">15-20 slides</option>
                <option value="20+">20+ slides</option>
              </select>
            </div>

            <div>
              <label className="block text-sm font-medium text-purple-200 mb-2">
                Visual Style
              </label>
              <select
                value={state.layoutCustomization.visual_preference}
                onChange={(e) => updateLayoutCustomization({ visual_preference: e.target.value as any })}
                className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
              >
                <option value="minimal">Minimal & Clean</option>
                <option value="balanced">Balanced</option>
                <option value="visual_heavy">Visual Heavy</option>
              </select>
            </div>
          </div>

          <div className="bg-purple-800/30 rounded-lg p-6 border border-purple-600/30">
            <h3 className="text-lg font-semibold text-white mb-3">Preview Settings</h3>
            <div className="space-y-2 text-purple-200">
              <p><span className="font-medium">Theme:</span> {themes.find(t => t.id === state.layoutCustomization.theme)?.name}</p>
              <p><span className="font-medium">Slides:</span> {state.layoutCustomization.slide_range}</p>
              <p><span className="font-medium">Style:</span> {state.layoutCustomization.visual_preference.replace('_', ' ')}</p>
              <p><span className="font-medium">Topic:</span> {state.topic}</p>
            </div>
          </div>

          <div className="flex gap-4">
            <button
              onClick={handleBack}
              className="px-6 py-3 bg-purple-700/50 hover:bg-purple-700 text-purple-200 hover:text-white rounded-lg transition-all duration-300 border border-purple-600/30"
            >
              ← Back to Content
            </button>
            <button
              onClick={handleCreatePPT}
              disabled={state.isLoading}
              className={`flex-1 py-3 px-6 rounded-lg font-semibold transition-all duration-300 ${
                state.isLoading
                  ? 'bg-purple-700/50 text-purple-300 cursor-not-allowed'
                  : 'gradient-purple hover:shadow-lg hover:shadow-purple-500/25 hover:scale-105 text-white'
              }`}
            >
              {state.isLoading ? (
                <span className="flex items-center justify-center">
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                  Creating PowerPoint...
                </span>
              ) : (
                '✨ Create PowerPoint'
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PPTSettings;
