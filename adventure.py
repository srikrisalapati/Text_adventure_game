import time

def get_player_choice(prompt, options):
    """
    Displays a prompt and a list of options, and safely gets the player's choice.

    Args:
        prompt (str): The question to ask the player.
        options (list): A list of strings, where each string is an option.

    Returns:
        int: The user's chosen option number (1-based).
    """
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"  {i + 1}. {option}")

    while True:
        try:
            choice = int(input("> "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please pick a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_scary_game():
    """Handles the logic for the 'Scary Game' path."""
    print("\n--- The Scary Game ---")
    time.sleep(1)
    prompt = "You find yourself drawn to a place of fear. Where do you go?"
    options = [
        "A dense, dark forest.",
        "An old, abandoned cinema playing a scary movie.",
        "The empty city streets in the middle of the night.",
        "A vast, misty lake with a single rowboat."
    ]
    choice_layer_2 = get_player_choice(prompt, options)

    if choice_layer_2 == 1:
        prompt = "You are deep in the forest. A strange sound echoes. What do you do?"
        options = ["Venture deeper to find the source.", "Build a fire and wait till morning."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You can take up brave challenges head-on."
        else:
            result = "You are brave, but temper it with caution and practicality."
    
    elif choice_layer_2 == 2:
        prompt = "You are alone watching the film. You hear a door creak behind you. What do you do?"
        options = ["Turn around quickly to confront the noise.", "Pretend you heard nothing and focus on the movie."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are confrontational and face your fears directly."
        else:
            result = "You like to appear daring, but you prefer your thrills to be controlled."

    elif choice_layer_2 == 3:
        prompt = "You are walking down a deserted street. A shadowy figure appears far ahead. What do you do?"
        options = ["Continue walking towards it, staying aware.", "Cross the street and take a different route."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are brave and perhaps a bit reckless, trusting in your ability to handle risk."
        else:
            result = "You are street-smart and prioritize safety over unnecessary risk."

    elif choice_layer_2 == 4:
        prompt = "You are rowing on the misty lake. The shore disappears from view. What do you do?"
        options = ["Keep rowing into the mist, enjoying the solitude.", "Use a compass to immediately row back."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You have a high tolerance for the unknown and find peace in solitude."
        else:
            result = "You are a prepared navigator who doesn't like to leave things to chance."
            
    print("\n--- Personality Assessment ---")
    print(result)


def play_fun_game():
    """Handles the logic for the 'Fun Game' path."""
    print("\n--- The Fun Game ---")
    time.sleep(1)
    prompt = "You have a completely free day! What is your ideal source of fun?"
    options = [
        "Socializing with a large group of friends.",
        "Engaging in a creative or skill-based hobby.",
        "Exploring the outdoors and nature.",
        "Relaxing at home with movies or video games."
    ]
    choice_layer_2 = get_player_choice(prompt, options)

    if choice_layer_2 == 1:
        prompt = "You decide to host a party. What is your main role?"
        options = ["The energetic host, making sure everyone is having fun.", "The relaxed guest, enjoying conversations in a smaller circle."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are an extrovert who thrives in social situations and loves being the center of energy."
        else:
            result = "You are a social person who prefers deep connections over large crowds."
    
    elif choice_layer_2 == 2:
        prompt = "You pick up your hobby. What kind of project do you choose?"
        options = ["A challenging one that will push your skills to the limit.", "A familiar one that you find calming and enjoyable."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are a disciplined and ambitious person who finds fun in self-improvement and mastery."
        else:
            result = "You are a creative person who uses hobbies as a way to relax and express yourself."
            
    elif choice_layer_2 == 3:
        prompt = "You head outdoors. What is your destination?"
        options = ["A challenging mountain trail you've never hiked before.", "A quiet, beautiful park to relax and people-watch."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are an adventurous spirit who seeks challenges and finds joy in physical accomplishment."
        else:
            result = "You are a calm individual who finds peace and rejuvenation in the beauty of nature."

    elif choice_layer_2 == 4:
        prompt = "You're relaxing at home. What's on the screen?"
        options = ["An exciting, action-packed blockbuster movie.", "A nostalgic comfort show you've seen many times."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You seek excitement and escapism in your entertainment."
        else:
            result = "You are a comfortable introvert who values personal time and finds relaxation in the familiar."

    print("\n--- Personality Assessment ---")
    print(result)


def play_mental_game():
    """Handles the logic for the 'Mental Game' path."""
    print("\n--- The Mental Game ---")
    time.sleep(1)
    prompt = "You are presented with a complex puzzle box that has stumped others. What is your first approach?"
    options = [
        "Analyze its design meticulously before making a single move.",
        "Immediately start trying different combinations and ideas.",
        "Collaborate and ask a friend for their perspective.",
        "Set it aside to think about it subconsciously."
    ]
    choice_layer_2 = get_player_choice(prompt, options)
    
    if choice_layer_2 == 1:
        prompt = "After analyzing, you find a tiny, almost invisible seam. What do you do?"
        options = ["Try to pry it open carefully.", "Look for a hidden button that might open it."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are a direct problem-solver who takes action once a path is clear."
        else:
            result = "You are a patient and analytical thinker who believes every problem has a hidden, elegant solution."

    elif choice_layer_2 == 2:
        prompt = "Your random attempts are failing. What is your next step?"
        options = ["Keep trying, but in a more systematic, brute-force way.", "Stop and try a different approach, like analysis."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are a persistent and determined individual who believes in the power of sheer effort and resilience."
        else:
            result = "You are adaptable, willing to change strategies when one isn't working."

    elif choice_layer_2 == 3:
        prompt = "Your friend suggests an idea you already dismissed. How do you react?"
        options = ["Explain why it won't work.", "Try their idea anyway, just in case you missed something."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are a confident and logical thinker who trusts your own analysis."
        else:
            result = "You are a true collaborator who values teamwork and is open to being wrong."

    elif choice_layer_2 == 4:
        prompt = "While doing something else, a solution suddenly pops into your head. What do you do?"
        options = ["Rush back to the puzzle to try it immediately.", "Write the idea down to try later when you are ready."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are driven by flashes of inspiration and act on them with passion."
        else:
            result = "You are an intuitive but methodical thinker, capturing ideas to explore in a structured way."
            
    print("\n--- Personality Assessment ---")
    print(result)
    
    
def play_luck_game():
    """Handles the logic for the 'Luck Game' path."""
    print("\n--- The Luck Game ---")
    time.sleep(1)
    prompt = "You are offered a choice of three mysterious doors. Which do you choose?"
    options = [
        "The plain wooden door that seems humble and safe.",
        "The ornate golden door that promises great riches.",
        "The shimmering, ethereal door that hums with strange energy."
    ]
    choice_layer_2 = get_player_choice(prompt, options)

    if choice_layer_2 == 1:
        prompt = "Behind the door is a simple, home-cooked meal. How do you feel?"
        options = ["Content and grateful for the simple pleasure.", "Slightly disappointed, wondering what was behind the other doors."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are a grounded person who finds happiness in simple, reliable comforts."
        else:
            result = "You have an ambitious heart and are always curious about the greater possibilities."

    elif choice_layer_2 == 2:
        prompt = "Behind the door is a pile of gold, but it's guarded by a sleeping dragon. What do you do?"
        options = ["Try to sneak some gold without waking it.", "Leave empty-handed, valuing your life over riches."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are an ambitious risk-taker, willing to face danger for a great reward."
        else:
            result = "You are a wise and pragmatic person who can accurately assess risk versus reward."

    elif choice_layer_2 == 3:
        prompt = "Behind the door is a portal to an unknown world. What do you do?"
        options = ["Jump through immediately, eager for adventure.", "Observe it from a distance, too cautious to enter."]
        choice_layer_3 = get_player_choice(prompt, options)
        if choice_layer_3 == 1:
            result = "You are a true explorer, driven by curiosity and a desire for new experiences above all else."
        else:
            result = "You are an imaginative but cautious soul, fascinated by the unknown but valuing your safety."

    print("\n--- Personality Assessment ---")
    print(result)


def main():
    """Main function to run the game loop."""
    print("Welcome to the Personality Assessment Game!")
    print("Your choices will reveal a glimpse of your personality.")

    while True:
        prompt = "Which realm of choice do you want to enter?"
        options = ["A scary scenario", "A fun scenario", "A mental challenge", "A test of luck"]
        main_choice = get_player_choice(prompt, options)

        if main_choice == 1:
            play_scary_game()
        elif main_choice == 2:
            play_fun_game()
        elif main_choice == 3:
            play_mental_game()
        elif main_choice == 4:
            play_luck_game()

        print("\n" + "="*40 + "\n")
        
        # --- MODIFIED SECTION ---
        play_again = input("Do you want to play again? (y/n): ").lower()
        if not play_again.startswith('y'):
            print("Thank you for playing!")
            break


# This line ensures the main() function runs when the script is executed
if __name__ == "__main__":
    main()
