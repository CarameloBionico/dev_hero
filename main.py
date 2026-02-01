"""
Dev Hero - A typing game for developers!
Main entry point for the game.
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import DevHeroGame
from codes import get_available_categories, get_category_display_name


def print_header():
    """Print the game header."""
    print("\n" + "=" * 60)
    print(" " * 15 + "🚀 DEV HERO 🚀")
    print(" " * 10 + "Type Hero for Developers")
    print("=" * 60)
    print()

def print_footer():
    """Print the game footer."""
    print("\n" + "=" * 60)
    print(" " * 15 + "🚀 DEV HERO 🚀")
    print(" " * 10 + "Type Hero for Developers")
    print("=" * 60)
    print()

def print_challenge(challenge):
    """Print the challenge to type."""
    print("\n" + "-" * 60)
    print("Type this:")
    print(f"\n  {challenge}")
    print("\n" + "-" * 60)
    print("Start typing (press Enter when done):\n")


def print_stats(stats):
    """Print statistics for a round."""
    print("\n" + "=" * 60)
    print("📊 ROUND STATS")
    print("=" * 60)
    print(f"⏱️  Time:        {stats['time']}s")
    print(f"⚡ WPM:          {stats['wpm']}")
    print(f"🎯 Accuracy:     {stats['accuracy']:.1f}%")
    print(f"✅ Correct:      {stats['correct_chars']}/{stats['total_chars']} chars")
    print("=" * 60)
    
    if stats['accuracy'] == 100.0:
        print("\n🎉 PERFECT! 🎉\n")
    elif stats['accuracy'] >= 95.0:
        print("\n✨ Great job! ✨\n")
    elif stats['accuracy'] >= 80.0:
        print("\n👍 Good! 👍\n")
    else:
        print("\n💪 Keep practicing! 💪\n")


def show_category_menu():
    """Display category selection menu.
    
    Returns:
        None (prints menu to console)
    """
    categories = get_available_categories()
    
    print("\n" + "=" * 60)
    print(" " * 15 + "SELECT CATEGORY")
    print("=" * 60)
    print("\nChoose a category to practice:\n")
    
    for i, category in enumerate(categories, 1):
        display_name = get_category_display_name(category)
        print(f"  {i}. {display_name}")
    
    print("\n" + "=" * 60)


def select_category():
    """Get category selection from user.
    
    Returns:
        str: Selected category key, or 'all' if invalid input
    """
    categories = get_available_categories()
    
    while True:
        try:
            choice = input(f"Enter your choice (1-{len(categories)}): ").strip()
            
            if not choice:
                print(f"Invalid choice. Please enter a number between 1 and {len(categories)}.")
                continue
            
            choice_num = int(choice)
            
            if 1 <= choice_num <= len(categories):
                selected = categories[choice_num - 1]
                display_name = get_category_display_name(selected)
                print(f"\n✓ Selected: {display_name}\n")
                return selected
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(categories)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\n\nSelection cancelled.")
            return 'all'


def print_category_stats(game):
    """Print statistics for each category that has been played.
    
    Args:
        game: DevHeroGame instance
    """
    all_cat_stats = game.get_all_category_stats()
    
    if not all_cat_stats:
        return
    
    print("\n" + "=" * 60)
    print("📊 STATISTICS BY CATEGORY")
    print("=" * 60)
    
    for category, stats in all_cat_stats.items():
        display_name = get_category_display_name(category)
        print(f"\n{display_name}:")
        print(f"  🎮 Rounds:      {stats['rounds']}")
        print(f"  ⚡ Avg WPM:      {stats['avg_wpm']}")
        print(f"  🎯 Avg Accuracy: {stats['avg_accuracy']:.1f}%")
        print(f"  🌟 Best WPM:      {stats['best_wpm']}")
    
    print("=" * 60)


def print_game_stats(game):
    """Print overall game statistics."""
    avg_stats = game.get_average_stats()
    
    print("\n" + "=" * 60)
    print("🏆 GAME STATISTICS")
    print("=" * 60)
    print(f"🎮 Rounds played:  {avg_stats['rounds']}")
    print(f"⚡ Average WPM:    {avg_stats['avg_wpm']}")
    print(f"🎯 Avg Accuracy:   {avg_stats['avg_accuracy']:.1f}%")
    print(f"🌟 Best WPM:       {avg_stats['best_wpm']}")
    print("=" * 60)
    
    # Also show category statistics
    print_category_stats(game)


def show_character_comparison(target, user_input):
    """Show character-by-character comparison."""
    print("\n" + "-" * 60)
    print("Character comparison:")
    print("-" * 60)
    print(f"Target:  {target}")
    print(f"Your:    {user_input}")
    
    # Show differences
    diff_line = "Diff:    "
    max_len = max(len(target), len(user_input))
    
    for i in range(max_len):
        if i < len(target) and i < len(user_input):
            if target[i] == user_input[i]:
                diff_line += "✓"
            else:
                diff_line += "✗"
        elif i < len(target):
            diff_line += "✗"
        else:
            diff_line += "✗"
    
    print(diff_line)
    print("-" * 60)


def main():
    """Main game loop."""
    print_header()
    
    # Show category menu and get selection
    show_category_menu()
    selected_category = select_category()
    
    # Initialize game with selected category
    game = DevHeroGame(category=selected_category)
    
    display_name = get_category_display_name(selected_category)
    print("Welcome to Dev Hero!")
    print(f"Practice mode: {display_name}")
    print("Type the code snippets, keywords, or memes as fast as you can!")
    print("\nCommands:")
    print("  - Just type and press Enter to submit")
    print("  - Type 'quit' or 'exit' to end the game")
    print("  - Type 'stats' to see your statistics")
    print()
    
    try:
        while True:
            # Get challenge
            challenge = game.start_round()
            print_challenge(challenge)
            
            # Get user input
            user_input = input().strip()
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() == 'stats':
                print_game_stats(game)
                game.timer.reset()
                continue
            
            # Finish round and show stats
            stats = game.finish_round(challenge, user_input)
            print_stats(stats)
            
            # Show comparison if not perfect
            if not game.is_perfect_match(challenge, user_input):
                show_character_comparison(challenge, user_input)
            
            # Ask if continue
            print("\nPress Enter to continue, or type 'quit' to exit...")
            choice = input().strip().lower()
            if choice in ['quit', 'exit', 'q']:
                break
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user.")
    
    finally:
        # Show final statistics
        if game.rounds_played > 0:
            print_game_stats(game)
        print("\n👋 Thanks for playing Dev Hero! 👋\n")


if __name__ == '__main__':
    main()

