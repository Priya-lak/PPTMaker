import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import { useApp } from '../contexts/AppContext';

const ContentPreview: React.FC = () => {
  const { state, updateEditedContent, setCurrentStep } = useApp();
  const [isEditing, setIsEditing] = useState(false);

  const handleContinue = () => {
    setCurrentStep(3);
  };

  const handleBack = () => {
    setCurrentStep(1);
  };

  const toggleMode = () => {
    setIsEditing(!isEditing);
  };

  return (
    <div className="max-w-6xl mx-auto">
      <div className="card-dark rounded-xl p-8 hover-lift">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-white mb-2">
            Review Your Content
          </h2>
          <p className="text-slate-400 text-lg">
            {isEditing ? 'Edit your content' : 'Preview the rendered markdown'}
          </p>
        </div>

        {/* Toggle Buttons */}
        <div className="flex justify-center mb-6">
          <div className="bg-slate-800 rounded-lg p-1 flex">
            <button
              onClick={() => setIsEditing(false)}
              className={`px-4 py-2 rounded-md text-sm font-medium transition-all duration-200 ${
                !isEditing
                  ? 'bg-purple-600 text-white shadow-lg'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              👁️ Preview
            </button>
            <button
              onClick={() => setIsEditing(true)}
              className={`px-4 py-2 rounded-md text-sm font-medium transition-all duration-200 ${
                isEditing
                  ? 'bg-purple-600 text-white shadow-lg'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              ✏️ Edit
            </button>
          </div>
        </div>

        {/* Single Content Pane */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-300 mb-3">
              {isEditing ? (
                <>Content Editor - <span className="text-purple-400 font-semibold">"{state.topic}"</span></>
              ) : (
                'Markdown Preview'
              )}
            </label>

            {isEditing ? (
              // Editor Mode
              <div>
                <textarea
                  id="content"
                  value={state.editedContent}
                  onChange={(e) => updateEditedContent(e.target.value)}
                  rows={20}
                  className="w-full px-4 py-3 input-dark rounded-lg text-white placeholder-slate-400 focus:outline-none transition-all resize-none font-mono text-sm leading-relaxed"
                  placeholder="Your generated content will appear here..."
                />
                <p className="text-slate-500 text-sm mt-2">
                  💡 Tip: Content is in markdown format - edit as needed
                </p>
              </div>
            ) : (
              // Preview Mode
              <div className="w-full px-4 py-3 input-dark rounded-lg text-white min-h-[500px] overflow-y-auto">
                <div className="prose prose-invert prose-purple max-w-none">
                  <ReactMarkdown
                    components={{
                      h1: ({children}) => <h1 className="text-2xl font-bold text-white mb-4">{children}</h1>,
                      h2: ({children}) => <h2 className="text-xl font-semibold text-purple-300 mb-3">{children}</h2>,
                      h3: ({children}) => <h3 className="text-lg font-medium text-slate-200 mb-2">{children}</h3>,
                      p: ({children}) => <p className="text-slate-300 mb-3 leading-relaxed">{children}</p>,
                      ul: ({children}) => <ul className="list-disc list-inside text-slate-300 mb-3 space-y-1">{children}</ul>,
                      ol: ({children}) => <ol className="list-decimal list-inside text-slate-300 mb-3 space-y-1">{children}</ol>,
                      li: ({children}) => <li className="text-slate-300">{children}</li>,
                      strong: ({children}) => <strong className="text-purple-300 font-semibold">{children}</strong>,
                      em: ({children}) => <em className="text-purple-200 italic">{children}</em>,
                      code: ({children}) => <code className="bg-slate-800 text-purple-300 px-2 py-1 rounded text-sm">{children}</code>,
                      pre: ({children}) => <pre className="bg-slate-800 p-4 rounded-lg overflow-x-auto mb-4">{children}</pre>,
                      blockquote: ({children}) => <blockquote className="border-l-4 border-purple-500 pl-4 italic text-slate-400 mb-4">{children}</blockquote>,
                    }}
                  >
                    {state.editedContent || '*No content to preview*'}
                  </ReactMarkdown>
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="flex gap-4 mt-8">
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
                ? 'bg-slate-700 text-slate-500 cursor-not-allowed'
                : 'button-primary hover:scale-[1.02]'
            }`}
          >
            Continue to Design Settings →
          </button>
        </div>
      </div>
    </div>
  );
};

export default ContentPreview;
