
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
    <div className="w-full max-w-4xl mx-auto mb-8">
      <div className="flex items-center justify-between">
        {steps.map((step, index) => (
          <div key={step.number} className="flex items-center">
            <div className="flex flex-col items-center">
              <div
                className={`w-12 h-12 rounded-full flex items-center justify-center text-sm font-bold transition-all duration-300 ${
                  state.currentStep === step.number
                    ? 'gradient-purple text-white scale-110 shadow-lg'
                    : state.currentStep > step.number
                    ? 'bg-purple-600 text-white'
                    : 'bg-purple-900/50 text-purple-300 border-2 border-purple-600/30'
                }`}
              >
                {state.currentStep > step.number ? '✓' : step.number}
              </div>
              <div className="mt-2 text-center">
                <div className={`text-sm font-medium ${
                  state.currentStep >= step.number ? 'text-white' : 'text-purple-300'
                }`}>
                  {step.title}
                </div>
                <div className={`text-xs ${
                  state.currentStep >= step.number ? 'text-purple-200' : 'text-purple-400'
                }`}>
                  {step.description}
                </div>
              </div>
            </div>
            {index < steps.length - 1 && (
              <div
                className={`flex-1 h-1 mx-4 rounded transition-all duration-300 ${
                  state.currentStep > step.number
                    ? 'bg-purple-600'
                    : 'bg-purple-900/30'
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
