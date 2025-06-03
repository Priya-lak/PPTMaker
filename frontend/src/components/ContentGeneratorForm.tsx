
import React, { useState } from 'react';
import { useApp } from '../contexts/AppContext';
import { apiService } from '../services/api';
import { ChevronDown, ChevronUp } from 'lucide-react';

const ContentGeneratorForm: React.FC = () => {
  const { state, updateTopic, updateContentCustomization, updateGeneratedContent, setCurrentStep, setLoading, setError } = useApp();
  const [showAdvanced, setShowAdvanced] = useState(false);

  const handleGenerateContent = async () => {
    if (!state.topic.trim()) {
      setError('Please enter a topic for your presentation');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await apiService.generateContent({
        topic: state.topic,
        content_customization: state.contentCustomization
      });

      updateGeneratedContent(response.content);
      setCurrentStep(2);
    } catch (error) {
      setError('Failed to generate content. Please try again.');
      console.error('Content generation error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto">
      <div className="glass-effect rounded-3xl p-8 hover-lift">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold gradient-text mb-4">
            ✨ AI PPT Maker
          </h1>
          <p className="text-purple-200 text-lg">
            Let's create an amazing presentation together!
          </p>
        </div>

        {state.error && (
          <div className="bg-red-500/20 border border-red-500/50 rounded-lg p-4 mb-6">
            <p className="text-red-200">{state.error}</p>
          </div>
        )}

        <div className="space-y-6">
          <div>
            <label htmlFor="topic" className="block text-sm font-medium text-purple-200 mb-2">
              What's your presentation topic? *
            </label>
            <input
              type="text"
              id="topic"
              value={state.topic}
              onChange={(e) => updateTopic(e.target.value)}
              placeholder="e.g., Introduction to Machine Learning"
              className="w-full px-4 py-3 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white placeholder-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all"
            />
          </div>

          <div className="border-t border-purple-600/30 pt-6">
            <button
              type="button"
              onClick={() => setShowAdvanced(!showAdvanced)}
              className="flex items-center justify-between w-full text-left text-purple-200 hover:text-white transition-colors"
            >
              <span className="font-medium">Advanced Customization (Optional)</span>
              {showAdvanced ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
            </button>

            {showAdvanced && (
              <div className="mt-6 space-y-4 animate-in slide-in-from-top duration-300">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-purple-200 mb-2">
                      Detail Level
                    </label>
                    <select
                      value={state.contentCustomization.detail_level}
                      onChange={(e) => updateContentCustomization({ detail_level: e.target.value as any })}
                      className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    >
                      <option value="overview">Overview</option>
                      <option value="intermediate">Intermediate</option>
                      <option value="deep_dive">Deep Dive</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-purple-200 mb-2">
                      Engagement Level
                    </label>
                    <select
                      value={state.contentCustomization.engagement_level}
                      onChange={(e) => updateContentCustomization({ engagement_level: e.target.value as any })}
                      className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    >
                      <option value="informational">informational</option>
                      <option value="interactive">interactive</option>
                      <option value="highly_engaging">Highly Engaging</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-purple-200 mb-2">
                      Include Examples
                    </label>
                    <select
                      value={state.contentCustomization.include_examples}
                      onChange={(e) => updateContentCustomization({ include_examples: e.target.value as any })}
                      className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    >
                      <option value="none">None</option>
                      <option value="few">Few</option>
                      <option value="extensive">Extensive</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-purple-200 mb-2">
                      Target Audience
                    </label>
                    <select
                      value={state.contentCustomization.target_audience}
                      onChange={(e) => updateContentCustomization({ target_audience: e.target.value as any })}
                      className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    >
                      <option value="general">General</option>
                      <option value="students">Students</option>
                      <option value="technical_experts">Technical Experts</option>
                      <option value="executives">Executives</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-purple-200 mb-2">
                      Presentation Purpose
                    </label>
                    <select
                      value={state.contentCustomization.presentation_purpose}
                      onChange={(e) => updateContentCustomization({ presentation_purpose: e.target.value as any })}
                      className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    >
                      <option value="conference_talk">Conference Talk</option>
                      <option value="sales_pitch">Sales Pitch</option>
                      <option value="educational">Educational</option>
                      <option value="business_proposal">Business Proposal</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-purple-200 mb-2">
                      Tone
                    </label>
                    <select
                      value={state.contentCustomization.tone}
                      onChange={(e) => updateContentCustomization({ tone: e.target.value as any })}
                      className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
                    >
                      <option value="professional">Professional</option>
                      <option value="formal">Formal</option>
                      <option value="casual">Casual</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-purple-200 mb-2">
                    Industry (Optional)
                  </label>
                  <input
                    type="text"
                    value={state.contentCustomization.industry}
                    onChange={(e) => updateContentCustomization({ industry: e.target.value })}
                    placeholder="e.g., healthcare, finance, technology"
                    className="w-full px-3 py-2 bg-purple-900/50 border border-purple-600/30 rounded-lg text-white placeholder-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
                  />
                </div>
              </div>
            )}
          </div>

          <button
            onClick={handleGenerateContent}
            disabled={state.isLoading || !state.topic.trim()}
            className={`w-full py-4 px-6 rounded-xl font-semibold text-lg transition-all duration-300 ${
              state.isLoading || !state.topic.trim()
                ? 'bg-purple-700/50 text-purple-300 cursor-not-allowed'
                : 'gradient-purple hover:shadow-lg hover:shadow-purple-500/25 hover:scale-105 text-white'
            }`}
          >
            {state.isLoading ? (
              <span className="flex items-center justify-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
                Generating Content...
              </span>
            ) : (
              '🚀 Generate Content'
            )}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ContentGeneratorForm;
