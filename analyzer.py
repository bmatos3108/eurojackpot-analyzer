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
