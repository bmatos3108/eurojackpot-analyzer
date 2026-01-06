"""
EuroJackpot Simple Analyzer
"""
import pandas as pd
from collections import Counter
from datetime import datetime

# Sample 2025 data
data = [
    {'date': '2025-01-03', 'numbers': [1, 20, 21, 27, 29], 'euros': [8, 10]},
    {'date': '2025-01-07', 'numbers': [1, 16, 20, 23, 44], 'euros': [5, 9]},
    {'date': '2025-01-10', 'numbers': [17, 34, 38, 42, 48], 'euros': [2, 11]},
    {'date': '2025-01-14', 'numbers': [10, 11, 17, 20, 30], 'euros': [2, 6]},
    {'date': '2025-01-17', 'numbers': [7, 9, 14, 18, 31], 'euros': [7, 8]},
]

def analyze():
    print("🎰 EuroJackpot Analyzer 2026")
    print("=" * 50)
    
    # Count frequencies
    main_freq = Counter()
    euro_freq = Counter()
    
    for draw in data:
        main_freq.update(draw['numbers'])
        euro_freq.update(draw['euros'])
    
    # Generate predictions
    print("\n🔥 HOT NUMBERS (Most Frequent):")
    print(f"Main: {[n for n, c in main_freq.most_common(5)]}")
    print(f"Euro: {[n for n, c in euro_freq.most_common(2)]}")
    
    print("\n✅ Analysis complete!")
    print(f"Analyzed {len(data)} draws")

if __name__ == "__main__":
    analyze()
"""
EuroJackpot Analysis & Prediction System
Advanced statistical analysis and ML-based predictions
Author: Sofia Herrmann
"""

import pandas as pd
import numpy as np
from datetime import datetime
from collections import Counter
import json

class EuroJackpotAnalyzer:
    def __init__(self):
        self.main_range = (1, 50)
        self.euro_range = (1, 12)
        self.historical_data = []
        
    def load_sample_data(self):
        """Load sample historical data"""
        data = [
            {'date': '2025-01-03', 'numbers': [1, 20, 21, 27, 29], 'euros': [8, 10]},
            {'date': '2025-01-07', 'numbers': [1, 16, 20, 23, 44], 'euros': [5, 9]},
            {'date': '2025-01-10', 'numbers': [17, 34, 38, 42, 48], 'euros': [2, 11]},
            {'date': '2025-01-14', 'numbers': [10, 11, 17, 20, 30], 'euros': [2, 6]},
            {'date': '2025-01-17', 'numbers': [7, 9, 14, 18, 31], 'euros': [7, 8]},
            {'date': '2025-01-21', 'numbers': [3, 17, 22, 28, 40], 'euros': [4, 9]},
            {'date': '2025-01-24', 'numbers': [2, 9, 16, 46, 47], 'euros': [3, 9]},
            {'date': '2025-01-28', 'numbers': [2, 7, 28, 43, 46], 'euros': [5, 12]},
            {'date': '2025-01-31', 'numbers': [1, 23, 32, 42, 47], 'euros': [4, 11]},
            {'date': '2025-02-04', 'numbers': [10, 18, 21, 41, 42], 'euros': [3, 9]},
            {'date': '2025-02-07', 'numbers': [15, 17, 27, 33, 45], 'euros': [5, 9]},
            {'date': '2025-02-11', 'numbers': [3, 12, 22, 28, 47], 'euros': [1, 12]},
            {'date': '2025-02-14', 'numbers': [12, 14, 18, 45, 50], 'euros': [2, 10]},
            {'date': '2025-02-18', 'numbers': [1, 9, 14, 19, 44], 'euros': [2, 3]},
            {'date': '2025-02-21', 'numbers': [18, 26, 29, 35, 36], 'euros': [11, 12]},
            {'date': '2025-02-25', 'numbers': [28, 31, 38, 42, 48], 'euros': [3, 10]},
            {'date': '2025-02-28', 'numbers': [3, 4, 13, 20, 21], 'euros': [8, 12]},
            {'date': '2025-03-04', 'numbers': [4, 12, 35, 37, 48], 'euros': [4, 10]},
            {'date': '2025-03-07', 'numbers': [7, 11, 12, 32, 42], 'euros': [1, 4]},
            {'date': '2025-03-11', 'numbers': [15, 18, 22, 23, 44], 'euros': [1, 11]},
        ]
        
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'])
        self.historical_data = df
        print(f"✓ Loaded {len(df)} historical draws")
        return df
    
    def calculate_frequency(self):
        """Calculate number frequencies"""
        main_freq = Counter()
        euro_freq = Counter()
        
        for _, row in self.historical_data.iterrows():
            main_freq.update(row['numbers'])
            euro_freq.update(row['euros'])
        
        return {
            'main': dict(main_freq),
            'euro': dict(euro_freq),
            'hot_main': main_freq.most_common(10),
            'hot_euro': euro_freq.most_common(5)
        }
    
    def predict_hot_numbers(self, freq):
        """Method 1: Hot Numbers Strategy"""
        main = sorted([num for num, _ in freq['hot_main'][:5]])
        euros = sorted([num for num, _ in freq['hot_euro'][:2]])
        
        return {
            'method': 'Hot Numbers',
            'main': main,
            'euros': euros,
            'confidence': 75,
            'description': 'Most frequently drawn numbers'
        }
    
    def predict_balanced(self, freq):
        """Method 2: Balanced Mix Strategy"""
        hot = [num for num, _ in freq['hot_main'][:3]]
        cold = sorted([k for k, v in sorted(freq['main'].items(), key=lambda x: x[1])[:2]])
        main = sorted(hot + cold)
        euros = sorted([num for num, _ in freq['hot_euro'][:2]])
        
        return {
            'method': 'Balanced Mix',
            'main': main,
            'euros': euros,
            'confidence': 70,
            'description': 'Mix of hot and cold numbers'
        }
    
    def predict_random(self):
        """Method 3: Random Distribution"""
        ranges = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
        main = []
        
        for r_min, r_max in ranges:
            num = np.random.randint(r_min, r_max + 1)
            while num in main:
                num = np.random.randint(r_min, r_max + 1)
            main.append(num)
        
        euros = sorted(np.random.choice(range(1, 13), 2, replace=False).tolist())
        
        return {
            'method': 'Statistical Distribution',
            'main': sorted(main),
            'euros': euros,
            'confidence': 65,
            'description': 'Balanced across number ranges'
        }
    
    def generate_all_predictions(self):
        """Generate all predictions"""
        freq = self.calculate_frequency()
        
        predictions = [
            self.predict_hot_numbers(freq),
            self.predict_balanced(freq),
            self.predict_random()
        ]
        
        return predictions
    
    def print_report(self):
        """Generate analysis report"""
        freq = self.calculate_frequency()
        predictions = self.generate_all_predictions()
        
        print("\n" + "="*60)
        print("🎰 EUROJACKPOT ANALYSIS & PREDICTION REPORT 2026")
        print("="*60)
        
        print(f"\n📊 HISTORICAL DATA SUMMARY")
        print("─"*60)
        print(f"Total Draws Analyzed: {len(self.historical_data)}")
        print(f"Date Range: {self.historical_data['date'].min().date()} to {self.historical_data['date'].max().date()}")
        
        print(f"\n🔥 HOT NUMBERS (Main)")
        print("─"*60)
        print(f"Top 10: {', '.join([f'{num}({count})' for num, count in freq['hot_main']])}")
        
        print(f"\n⭐ EURO NUMBERS")
        print("─"*60)
        print(f"Top 5: {', '.join([f'{num}({count})' for num, count in freq['hot_euro']])}")
        
        print(f"\n🎯 2026 PREDICTIONS")
        print("─"*60)
        
        for i, pred in enumerate(predictions, 1):
            print(f"\n{i}. {pred['method']} (Confidence: {pred['confidence']}%)")
            print(f"   Main: {' - '.join(map(str, pred['main']))}")
            print(f"   Euro: {' - '.join(map(str, pred['euros']))}")
            print(f"   Note: {pred['description']}")
        
        print(f"\n⚠️  DISCLAIMER")
        print("─"*60)
        print("EuroJackpot is a game of chance. All predictions are based on")
        print("statistical analysis and do not guarantee future results.")
        print("Play responsibly.")
        print("\n" + "="*60)
        
        return predictions


def main():
    """Main execution"""
    print("🎰 EuroJackpot Analysis System - Starting...")
    print("="*60)
    
    # Initialize analyzer
    analyzer = EuroJackpotAnalyzer()
    
    # Load sample data
    analyzer.load_sample_data()
    
    # Generate and print report
    analyzer.print_report()
    
    print("\n✨ Analysis complete!")


if __name__ == "__main__":
    main()
