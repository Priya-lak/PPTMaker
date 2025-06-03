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
    <div className="max-w-5xl mx-auto">
      <div className="card-dark rounded-xl p-8 hover-lift">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-white mb-2">
            Review Your Content
          </h2>
          <p className="text-gray-400 text-lg">
            Feel free to edit the generated content before creating your presentation
          </p>
        </div>

        <div className="space-y-6">
          <div>
            <label htmlFor="content" className="block text-sm font-medium text-gray-300 mb-3">
              Generated Content for: <span className="text-white font-semibold">"{state.topic}"</span>
            </label>
            <textarea
              id="content"
              value={state.editedContent}
              onChange={(e) => updateEditedContent(e.target.value)}
              rows={20}
              className="w-full px-4 py-3 input-dark rounded-lg text-white placeholder-gray-500 focus:outline-none transition-all resize-none font-mono text-sm leading-relaxed"
              placeholder="Your generated content will appear here..."
            />
            <p className="text-gray-500 text-sm mt-2">
              💡 Tip: You can edit this content to better match your needs
            </p>
          </div>

          <div className="flex gap-4">
            <button
              onClick={handleBack}
              className="px-6 py-3 button-secondary rounded-lg transition-all duration-200"
            >
              ← Back to Topic
            </button>
            <button
              onClick={handleContinue}
              disabled={!state.editedContent.trim()}
              className={`flex-1 py-3 px-6 rounded-lg font-semibold transition-all duration-200 ${
                !state.editedContent.trim()
                  ? 'bg-gray-700 text-gray-500 cursor-not-allowed'
                  : 'button-primary hover:scale-[1.02]'
              }`}
            >
              Continue to Design Settings →
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ContentPreview;
