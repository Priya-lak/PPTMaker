import React from 'react';
import { useApp } from '../contexts/AppContext';

const steps = [
  { number: 1, title: 'Topic & Settings', description: 'Tell us what you want to present' },
  { number: 2, title: 'Review Content', description: 'Edit your generated content' },
  { number: 3, title: 'Customize Design', description: 'Choose theme and layout' },
  { number: 4, title: 'Download', description: 'Get your PowerPoint file' }
];

const ProgressIndicator: React.FC = () => {
  const { state } = useApp();

  return (
    <div className="w-full max-w-4xl mx-auto mb-12">
      <div className="flex items-center justify-between">
        {steps.map((step, index) => (
          <div key={step.number} className="flex items-center">
            <div className="flex flex-col items-center">
              <div
                className={`w-12 h-12 rounded-full flex items-center justify-center text-sm font-semibold transition-all duration-300 ${
                  state.currentStep === step.number
                    ? 'gradient-purple text-white scale-110 shadow-lg'
                    : state.currentStep > step.number
                    ? 'bg-purple-600 text-white'
                    : 'bg-gray-700 text-gray-400 border-2 border-gray-600'
                }`}
              >
                {state.currentStep > step.number ? '✓' : step.number}
              </div>
              <div className="mt-3 text-center">
                <div className={`text-sm font-medium ${
                  state.currentStep >= step.number ? 'text-gray-200' : 'text-gray-500'
                }`}>
                  {step.title}
                </div>
                <div className={`text-xs ${
                  state.currentStep >= step.number ? 'text-gray-400' : 'text-gray-600'
                }`}>
                  {step.description}
                </div>
              </div>
            </div>
            {index < steps.length - 1 && (
              <div
                className={`flex-1 h-0.5 mx-8 rounded transition-all duration-300 ${
                  state.currentStep > step.number
                    ? 'bg-purple-600'
                    : 'bg-gray-700'
                }`}
              />
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProgressIndicator;
