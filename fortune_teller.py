def display_welcome():
    name = "Ravneet Singh"
    admission_number = "21je0756"
    print(f"\nWelcome to {name}'s Fortune Teller ({admission_number}) ")

def get_mood():
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
    return mood

def tell_fortune(mood):
    name = "Ravneet"
    if mood == "happy":
        print(f"Your fortune: Great things await you, {name}! Keep shining.")
    elif mood == "sad":
        print(f"Your fortune: Tough times never last, {name}, but tough people do.")
    elif mood == "neutral":
        print(f"Your fortune: A balanced mind brings clarity, {name}. Trust yourself.")
    elif mood == "stressed":
        print(f"Your fortune: Breathe, {name}. Storms pass and strength remains.")
    elif mood == "excited":
        print(f"Your fortune: The universe is aligning for you, {name}. Ride the wave of greatness!")
    elif mood == "angry":
        print(f"Your fortune: Anger can cloud judgment, {name}. Take a deep breath and let go.")
    else:
        print("Invalid mood. Please enter happy, sad, or neutral.")


if __name__ == "__main__":
    display_welcome()
    mood = get_mood()
    tell_fortune(mood)
