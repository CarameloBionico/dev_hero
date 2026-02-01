"""
Main game logic for Dev Hero typing game.
"""

from codes import get_random_challenge, get_random_challenge_by_category, get_available_categories
from timer import Timer
from score import calculate_stats


class DevHeroGame:
    """Main game class for Dev Hero typing game."""
    
    def __init__(self, category='all'):
        self.timer = Timer()
        self.rounds_played = 0
        self.total_wpm = 0.0
        self.total_accuracy = 0.0
        self.best_wpm = 0.0
        self.category = category.lower() if category else 'all'
        self.category_stats = self._init_category_stats()
    
    def _init_category_stats(self):
        """Initialize statistics dictionary for all categories.
        
        Returns:
            dict: Dictionary with stats for each category
        """
        categories = get_available_categories()
        stats = {}
        for cat in categories:
            if cat != 'all':  # Don't track stats for 'all' category
                stats[cat] = {
                    'rounds': 0,
                    'total_wpm': 0.0,
                    'total_accuracy': 0.0,
                    'best_wpm': 0.0,
                }
        return stats
    
    def get_challenge(self):
        """Get a random challenge to type from the selected category.
        
        Returns:
            str: Random challenge string
        """
        if self.category == 'all':
            return get_random_challenge()
        else:
            return get_random_challenge_by_category(self.category)
    
    def set_category(self, category):
        """Set the category for challenges.
        
        Args:
            category: Category key (e.g., 'python', 'javascript', 'all')
        """
        self.category = category.lower() if category else 'all'
    
    def start_round(self):
        """Start a new typing round.
        
        Returns:
            str: The challenge to type
        """
        challenge = self.get_challenge()
        self.timer.start()
        return challenge
    
    def finish_round(self, target, user_input):
        """Finish a typing round and calculate stats.
        
        Args:
            target: The target string that should have been typed
            user_input: What the user actually typed
        
        Returns:
            dict: Statistics for this round
        """
        self.timer.stop()
        time_elapsed = self.timer.elapsed()
        
        stats = calculate_stats(target, user_input, time_elapsed)
        
        # Update game statistics
        self.rounds_played += 1
        self.total_wpm += stats['wpm']
        self.total_accuracy += stats['accuracy']
        
        if stats['wpm'] > self.best_wpm:
            self.best_wpm = stats['wpm']
        
        # Update category statistics if not 'all'
        if self.category != 'all' and self.category in self.category_stats:
            cat_stats = self.category_stats[self.category]
            cat_stats['rounds'] += 1
            cat_stats['total_wpm'] += stats['wpm']
            cat_stats['total_accuracy'] += stats['accuracy']
            if stats['wpm'] > cat_stats['best_wpm']:
                cat_stats['best_wpm'] = stats['wpm']
        
        self.timer.reset()
        
        return stats
    
    def is_perfect_match(self, target, user_input):
        """Check if user input perfectly matches target.
        
        Args:
            target: The target string
            user_input: The user's input
        
        Returns:
            bool: True if perfect match, False otherwise
        """
        return target == user_input
    
    def get_average_stats(self):
        """Get average statistics across all rounds.
        
        Returns:
            dict: Average WPM and accuracy
        """
        if self.rounds_played == 0:
            return {'avg_wpm': 0.0, 'avg_accuracy': 0.0, 'rounds': 0, 'best_wpm': 0.0}
        
        return {
            'avg_wpm': round(self.total_wpm / self.rounds_played, 2),
            'avg_accuracy': round(self.total_accuracy / self.rounds_played, 2),
            'rounds': self.rounds_played,
            'best_wpm': round(self.best_wpm, 2),
        }
    
    def get_category_stats(self, category):
        """Get statistics for a specific category.
        
        Args:
            category: Category key (e.g., 'python', 'javascript')
        
        Returns:
            dict: Statistics for the category, or None if category not found or has no rounds
        """
        category = category.lower()
        if category not in self.category_stats:
            return None
        
        cat_stats = self.category_stats[category]
        if cat_stats['rounds'] == 0:
            return None
        
        return {
            'rounds': cat_stats['rounds'],
            'avg_wpm': round(cat_stats['total_wpm'] / cat_stats['rounds'], 2),
            'avg_accuracy': round(cat_stats['total_accuracy'] / cat_stats['rounds'], 2),
            'best_wpm': round(cat_stats['best_wpm'], 2),
        }
    
    def get_all_category_stats(self):
        """Get statistics for all categories that have been played.
        
        Returns:
            dict: Dictionary mapping category keys to their statistics
        """
        all_stats = {}
        for category, stats in self.category_stats.items():
            if stats['rounds'] > 0:
                all_stats[category] = {
                    'rounds': stats['rounds'],
                    'avg_wpm': round(stats['total_wpm'] / stats['rounds'], 2),
                    'avg_accuracy': round(stats['total_accuracy'] / stats['rounds'], 2),
                    'best_wpm': round(stats['best_wpm'], 2),
                }
        return all_stats

