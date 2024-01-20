# This is a "Choose your own adventure" kind of story, where you will be given a short story in The Enchanted Forest
# and depending on your decisions, you will see the outcome!

name = input("Enter your name: ")
print("Welcome to this adventure", name)

answer = input("Once upon a time, you find yourself standing at the edge of an enchanted forest. The trees are tall and ancient, their branches forming a dense canopy that blocks out most of the sunlight. You hear a mysterious melody in the air, beckoning you to explore the magical realm within. On the other hand, you also notice a weird path that may lead to someone, or something, as well as a humungous tree that looks majestic. You... (follow the melody/take the unmarked path/climb the ancient tree) ").lower()

if answer == "follow the melody":
    answer = input("Intrigued by the enchanting music, you decide to follow the melodic notes deeper into the forest. As you venture further, the trees seem to come alive with shimmering lights. You soon find a clearing where a group of friendly woodland creatures is gathered, dancing to the magical tune. They invite you to join them. Do you: (join the dance/politely decline) ")

    if answer == "join the dance":
        print("You decide to join the lively dance of the woodland creatures. As you twirl and sway to the magical melody, you become infused with the enchanting energy of the forest. The creatures, grateful for your participation, offer you a special token of their appreciation—a small, glowing crystal that enhances your senses. With this newfound gift, you can navigate the forest more easily and even communicate with the creatures, gaining their assistance on your journey.")
    elif answer == "politely decline":
        print("Choosing not to join the dance, you politely thank the woodland creatures and continue on your way deeper into the forest. As you explore, you stumble upon a hidden pathway that leads to a forgotten emblem. The emblem holds a mystical curse. You really don't know what it does, nor that it holds the power of a curse, but you read it aloud anyway. It ends up trapping you inside the emblem, and now, you will spend the rest of your life incarcerated within it.")
    else:
        print("This is not a valid option. The story ends here!")


elif answer == "take the unmarked path":
    answer = input("Noticing a less traveled path to your right, you decide to explore the unknown. The air becomes thick with magic as you walk, and you stumble upon a hidden grove. In the center, there's a sparkling pool with a mysterious glow. You sense that it holds a secret. Do you: (dip your hand into the glowing pool/observe from a distance and move on) ")
    if answer == "dip your hand into the glowing pool":
        print("As your hand touches the magical pool, a surge of energy courses through you. You feel a connection with the ancient magic of the forest, gaining a newfound ability to communicate with the woodland creatures. They guide you to a hidden path leading to the heart of the forest, where you discover a treasure chest filled with enchanted artifacts. The creatures express their gratitude, and you leave the forest with newfound friends and magical items!")
    elif answer == "observe from a distance and move on":
        print("Deciding not to interfere with the mysterious glow, you continue your journey through the forest. As you explore, you come across a wise old tree that imparts ancient knowledge about the secrets of the enchanted realm. With this newfound wisdom, you navigate through the forest with ease, avoiding potential dangers and discovering hidden wonders. Your respect for the natural magic of the forest earns you the trust of the woodland creatures, and they guide you to the exit, ensuring a safe passage out of the enchanted realm.")
    else:
        print("This is not a valid option. The story ends here!")


elif answer == "climb the ancient tree":
    answer = input("Spotting a massive ancient tree with sturdy branches, you decide to climb to get a better view of the forest. As you ascend, you notice a majestic bird perched at the top. It seems to be waiting for someone. Do you: (climb down and explore the forest floor/attempt to communicate with the majestic bird) ")
    if answer == "climb down and explore the forest floor":
        print("You carefully descend the ancient tree and explore the forest floor. As you wander, you come across a wounded creature. Using your kindness, you tend to its injuries and gain its trust. In gratitude, the creature leads you to a hidden glade where a rare flower blooms, possessing healing properties. You gather some of these flowers, leaving the forest with a newfound friend and a token of nature's gratitude.")
    elif answer == "attempt to communicate with the majestic bird":
        print("You attempt to communicate with the majestic bird at the top of the ancient tree. Sadly, you realize it's a guardian spirit, bound to the tree, unable to leave. The spirit imparts ancient wisdom but expresses a longing for freedom. While you gain profound knowledge, there's a bittersweet feeling as you leave the enchanted forest, knowing the majestic bird spirit remains bound to the ancient tree, watching over the magical realm.")
    else:
        print("This is not a valid option. The story ends here!")

else:
    print("This is not a valid option. The story ends here!")

print("Thank you for playing", name, "!")
