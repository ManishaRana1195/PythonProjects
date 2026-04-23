import random

def code_madlib():
    body_part = input("Body part: ")
    verb = input("Verb: ")
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun(Plural): ")

    return f"I love computer programming because it's {adj1}! The journey to becoming a \
good programmer starts with hope in your mind and a dream in your {body_part}. Through blood, \
sweat, and {noun2}, hopefully it never ends. Yes, once you learn to {verb}, it becomes \
a part of your life identity and you can become a super {adj2} hacker. Knowledge of programming \
lets you take control of your {noun1}."

def hp_madlib():
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    body_part = input("Body part: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    spell1 = input("Spell: ")
    verb_past = input("Verb(past): ")
    noun_plural = input("Noun(plural):")

    return f"A {adj1} glow burst suddenly across the enchanted sky above them as an edge of \
dazzling sun appeared over the sill of the nearest {noun1}. The light hit both of their {body_part} \
at the same time, so that Voldemort's was suddenly a flaming {noun2}. Harry heard the high voice \
shriek as he too {verb_past} his best hope to the heavens, pointing Draco's {noun3}:\n\
\"{spell1}!\"\n\
The bang was like a cannon blast, and the {adj2} flames that erupted between them, \
at the dead center of the circle they had been treading, marked the point where the \
{noun_plural} collided."

def hunger_games_madlib():
    number = input("Number: ")
    verb = input("Verb: ")
    noun = input("Noun: ")
    noun_plural = input("Noun(plural): ")
    sound_important = input("Sound: ")
    adj = input("Adjective: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")

    return f"{number} seconds. That's how long we're required to {verb} on our metal circles before \
the sound of a {noun} releases us. Step off before the {number} seconds is up, and {noun_plural} blow your \
legs off. {number} seconds to take in the ring of tributes all equidistant from the {sound_important}, a giant \
{adj} {noun2} shaped like a {noun3} with a curved tail, the mouth of which is at least twenty feet \
high, spilling over with the things that will give us life here in the arena."
    


def zombie_madlib():
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    time_of_day = input("Time of day: ")
    body_part_plural = input("Body part(plural): ")
    food = input("Food: ")
    noun_plural_1 = input("Noun(plural)")

    return f"It was a {adj1} summer {time_of_day} when we realized that the vaccine to stop \
spread of the disease did not work. Instead, it produced ZOMBIES!!! They were thirsty for {body_part_plural} \
and the streets were lined with these monsters holding {noun_plural_1} in their hands. \
Their eyes were red with hunger as they roamed around the city looking for {food}. \
They were {adj2} and {adj3}, unknowing how to act in this human world... except eat {body_part_plural}!!!!"
    
   


if __name__ == "__main__":
    random_madlib = random.choice([zombie_madlib, hunger_games_madlib, hp_madlib, code_madlib])()
    print(random_madlib)
