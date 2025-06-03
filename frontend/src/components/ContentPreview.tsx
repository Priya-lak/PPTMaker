
import React from 'react';
import { useApp } from '../contexts/AppContext';

const ContentPreview: React.FC = () => {
  const { state, updateEditedContent, setCurrentStep } = useApp();

  const handleContinue = () => {
    setCurrentStep(3);
  };

  const handleBack = () => {
    setCurrentStep(1);
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="glass-effect rounded-3xl p-8 hover-lift">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold gradient-text mb-4">
            📝 Review Your Content
          </h2>
          <p className="text-purple-200 text-lg">
            Feel free to edit the generated content before creating your presentation
          </p>
        </div>

        <div className="space-y-6">
          <div>
            <label htmlFor="content" className="block text-sm font-medium text-purple-200 mb-3">
              Generated Content for: <span className="text-white font-semibold">"{state.topic}"</span>
            </label>
            <textarea
              id="content"
              value={state.editedContent}
              onChange={(e) => updateEditedContent(e.target.value)}
              rows={20}
              className="w-full px-4 py-3 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white placeholder-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all resize-none"
              placeholder="Your generated content will appear here..."
            />
            <p className="text-purple-300 text-sm mt-2">
              💡 Tip: You can edit this content to better match your needs
            </p>
          </div>

          <div className="flex gap-4">
            <button
              onClick={handleBack}
              className="px-6 py-3 bg-purple-700/50 hover:bg-purple-700 text-purple-200 hover:text-white rounded-lg transition-all duration-300 border border-purple-600/30"
            >
              ← Back to Topic
            </button>
            <button
              onClick={handleContinue}
              disabled={!state.editedContent.trim()}
              className={`flex-1 py-3 px-6 rounded-lg font-semibold transition-all duration-300 ${
                !state.editedContent.trim()
                  ? 'bg-purple-700/50 text-purple-300 cursor-not-allowed'
                  : 'gradient-purple hover:shadow-lg hover:shadow-purple-500/25 hover:scale-105 text-white'
              }`}
            >
              Continue to Design Settings 🎨
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContentPreview;
