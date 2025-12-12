// Capy UI Theme Demo - TypeScript/JavaScript

/**
 * Welcome to Capy UI Theme! 🦫
 * This file demonstrates the syntax highlighting capabilities.
 */

import { useState, useEffect } from 'react';
import type { UserProfile } from './types';

// Constants and configuration
const API_BASE_URL = 'https://api.example.com';
const MAX_RETRIES = 3;

/**
 * Interface definitions
 */
interface CapyConfig {
  theme: 'light' | 'dark';
  accentColor: string;
  enableAnimations: boolean;
}

/**
 * Class demonstrating object-oriented features
 */
class ThemeManager {
  private config: CapyConfig;
  
  constructor(config: CapyConfig) {
    this.config = config;
  }
  
  public applyTheme(): void {
    console.log(`Applying theme: ${this.config.theme}`);
  }
  
  static getDefaultConfig(): CapyConfig {
    return {
      theme: 'dark',
      accentColor: '#1e80c7',
      enableAnimations: true
    };
  }
}

/**
 * Async function with error handling
 */
async function fetchUserData(userId: number): Promise<UserProfile | null> {
  try {
    const response = await fetch(`${API_BASE_URL}/users/${userId}`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    return null;
  }
}

/**
 * React component example
 */
export const CapyButton: React.FC<{ onClick: () => void }> = ({ onClick }) => {
  const [count, setCount] = useState(0);
  const [isLoading, setIsLoading] = useState(false);
  
  useEffect(() => {
    console.log(`Count changed to: ${count}`);
  }, [count]);
  
  const handleClick = () => {
    setCount(prev => prev + 1);
    onClick();
  };
  
  return (
    <button 
      onClick={handleClick}
      disabled={isLoading}
      className="capy-button"
    >
      Clicks: {count}
    </button>
  );
};

// Array methods and functional programming
const numbers = [1, 2, 3, 4, 5];
const squared = numbers
  .filter(n => n % 2 === 0)
  .map(n => n ** 2)
  .reduce((acc, n) => acc + n, 0);

// Regular expressions
const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const isValidEmail = emailRegex.test('user@example.com');

// Template literals
const greeting = `Hello, ${name}! 
Welcome to Capy UI Theme.
Electric blue accent: #1e80c7`;

// Object destructuring and spread
const { theme, accentColor, ...rest } = ThemeManager.getDefaultConfig();
const newConfig = { ...rest, theme: 'light' };

// Export
export { ThemeManager, fetchUserData };
export default CapyButton;
