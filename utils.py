import numpy as np
from tqdm import tqdm
import argparse
from gtts import gTTS
from playsound import playsound
import time
import os
from datetime import datetime


def create_dics(engs, viets):
    dictionary_ev = dict()
    for i in range(len(engs)):
        eng_word = engs[i]
        vie_word = viets[i]
        if eng_word in dictionary_ev:
            dictionary_ev[eng_word].append(vie_word)
        else:
            dictionary_ev[eng_word] = [vie_word]

    dictionary_ve = dict()

    for i in range(len(engs)):
        eng_word = engs[i]
        vie_word = viets[i]
        if vie_word in dictionary_ve:
            dictionary_ve[vie_word].append(eng_word)
        else:
            dictionary_ve[vie_word] = [eng_word]
    return dictionary_ev, dictionary_ve


def load_files(eng_path, vet_path):
    engs = []
    viets = []

    with open(eng_path, "r", encoding="utf-8") as file:
        for line in file:
            engs.append(line.strip().lower())
    file.close()

    with open(vet_path, "r", encoding="utf-8") as file:
        for line in file:
            viets.append(line.strip().lower())
    file.close()
    return engs, viets


def save_to_audio(list_words, lang='en'):
    for word in list_words:
        if not os.path.exists("data/audio/{}.mp3".format(word)):
            speech = gTTS(text=word, lang=lang)
            speech.save("data/audio/{}.mp3".format(word))


def part_of_this_day():
    hour = datetime.now().hour
    if 0 < hour < 4:
        return 'midnight'
    if 4 <= hour < 11:
        return 'morning'
    if 11 <= hour < 13:
        return 'noon'
    if 13 <= hour < 18:
        return 'afternoon'
    if 18 <= hour < 21:
        return 'night'
    if 21 <= hour:
        return 'late'

def say_goodbye(silent):
    print("bye!")
    part_of_day = part_of_this_day()
    if part_of_day == 'midnight':
        save_and_say("data/audio/suhi_goodbye_midnight.mp3", "It's late, take a rest, good night", silent=silent)
    if part_of_day == 'morning':
        save_and_say("data/audio/suhi_goodbye_morning.mp3", "weldone, have a nice day", silent=silent)
    if part_of_day == 'noon':
        save_and_say("data/audio/suhi_goodbye_noon.mp3", "feel hungry?, let's get something to eat", silent=silent)
    if part_of_day == 'afternoon':
        save_and_say("data/audio/suhi_goodbye_afternoon.mp3", "you've done it so well, take some rest", silent=silent)
    if part_of_day == 'night':
        save_and_say('data/audio/suhi_goodbye_night.mp3', "It's soon, but goodnight", silent=silent)
    if part_of_day == 'late':
        save_and_say("data/audio/suhi_goodbye_late.mp3", "it's hard to say goodbye, anyway, have a sweet dream!", silent=silent)
    exit()


def say_hello():
    part_of_day = part_of_this_day()
    if part_of_day == 'midnight':
        save_and_say("data/audio/suhi_hello_midnight.mp3", "Hello, it's late, take it easy.")
    if part_of_day == 'morning':
        save_and_say("data/audio/suhi_hello_morning.mp3", "Good morning, Let's have some English")
    if part_of_day == 'noon':
        save_and_say("data/audio/suhi_hello_noon.mp3", "Well, take it fast, you have your lunch waiting")
    if part_of_day == 'afternoon':
        save_and_say("data/audio/suhi_hello_afternoon.mp3", "Good afternoon.")
    if part_of_day == 'night':
        save_and_say("data/audio/suhi_hello_night.mp3", "Hello, Is candy next to you, let's review what we have learnt")
    if part_of_day == 'late':
        save_and_say("data/audio/suhi_hello_late.mp3", "Hello, Is candy next to you, let's review what we have learnt")
    


def save_and_say(path, text, just_save=False, silent=False):
    if not os.path.exists(path) or just_save:
        speech = gTTS(text=text)
        speech.save(path)
    if not silent:
        playsound(path)




def change_the_mean(old, ori_list, target_list, file_ori, file_target):
    new = input("Enter the new meaning (or 0 to ignore): ")
    if new == '0':
        return
    for i in range(len(target_list)):
        ele = target_list[i]
        if ele.strip().lower() == old.strip().lower():
            target_list[i] = new.strip().lower()
            break
    with open(file_ori, 'w', encoding="utf-8") as file:
        for ele in ori_list:
            file.write("{}\n".format(ele))
    file.close()

    with open(file_target, 'w', encoding="utf-8") as file:
        for ele in target_list:
            file.write("{}\n".format(ele))
    file.close()
    print("Successfully update the mean!")


