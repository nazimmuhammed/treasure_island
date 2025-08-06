pprint('''       
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')
print("Welcome to the world of mystery and adventure - Treasure Island!")
print("Your mission, if you choose to accept it, is to find the treasure without dying! Good luck, soldier!")

choice = input('''You have entered the murky waters of Wild Stone Island.
Choose your move - would you prefer to move left or right?
Type 'l' for left or 'r' for right: ''').lower()

if choice == "l":
    print('''Good choice! You have reached the dungeons of the dead skeletons - spooky!
You have two choices: wait for the boat to cross the lake of fire, or swim across the pool.''')

    dchoice = input("Your turn to either wait for the boat or swim across the unknown water. Enter 'b' for boat or 's' for swim: ").lower()

    if dchoice == "b":
        print("Lucky save! You have crossed the fire of doom and are one step ahead to get your treasure!")

        # Continue to final chamber
        print('''🕯️ The final chamber glows dimly as you approach three ancient doors —
each whispering secrets from a time long forgotten.

You stand before:
- A door painted **Red**, glowing like a furnace's breath.
- A door tinted **Blue**, colder than a widow's last tear.
- A door bathed in **Yellow**, faded like time's forgotten sun.

The voice of the island speaks:

"Three paths await the brave and bold,
But only one holds glittering gold.
One hides flame that dances bright,
Another guards in silent night.
The last, where hunger slept for years,
Holds no teeth, no claws, no fears.

Choose with wit, not strength or brawn,
Lest your tale be dead and gone."

So, adventurer… what door shall you open?
Type 'red', 'blue', or 'yellow' to decide your fate.''')

        final_choice = input().lower()

        if final_choice == "red":
            print("🔥 The fire roared to life — your journey ends in ashes. Fate was unkind.")
        elif final_choice == "blue":
            print("⚔️ Silent shadows strike — the assassins were patient. And deadly. You fall.")
        elif final_choice == "yellow":
            print("🌟 Your mind was sharp as your blade — the lion, long starved, is no more. The treasure is yours!")
        else:
            print("Enter the correct choice!")

    elif dchoice == "s":
        print("You are dead! The water was poisonous. Better luck next time!")
    else:
        print("Enter the correct choice!")

elif choice == "r":
    print("☠️ You have chosen right, but right is not always right! You came across hungry cannibals. You're dead!")
else:
    print("Enter the right choice, young man! The island doesn't wait for delayers!")