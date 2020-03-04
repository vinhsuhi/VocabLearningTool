import numpy as np
from tqdm import tqdm
import argparse
from gtts import gTTS
from playsound import playsound
import time
import os
from datetime import datetime
from utils import say_goodbye, say_hello, create_dics, load_files, save_to_audio, save_and_say, change_the_mean


def english_test(eng_path, viet_path, engs, viets, words, dictionary, use_audio, lang='en'):
    print("Number of words in dictionary: {}".format(len(dictionary)))

    np.random.shuffle(words)
    for worde in tqdm(list(set(words))):
        print("(Press 0 to exit, 1 to see answer, 2 to fix the mean)")
        if use_audio:
            print("Write the meaning of this word...")
        else:
            print("Write the meaning of this word: '{}'".format(worde))
        if lang == 'en':
            playsound("statics/data/audio/{}.mp3".format(worde))
        if use_audio:
            word = input("It means (Press 0 to exit, 1 to see answer, 2 to fix the mean): ".format(worde))
        else:
            word = input("'{}' means (Press 0 to exit, 1 to see answer, 2 to fix the mean): ".format(worde))
        succ = False
        if word == "0":
            say_goodbye(Silent)
        if word == "1":
            print("'{}' means: '{}'".format(worde, dictionary[worde][0]))
            if lang == 'vi':
                for word_answer in dictionary[worde]:
                    playsound("statics/data/audio/{}.mp3".format(word_answer))
                    time.sleep(0.5)
            continue
        if word == "2":
            if lang == 'vi':
                exit()
            change_the_mean(dictionary[worde][0], engs, viets, eng_path, viet_path)

        if word.lower().strip() in dictionary[worde]:
            print("You are RIGHT!")
            if lang == 'vi':
                for word_answer in dictionary[worde]:
                    playsound("statics/data/audio/{}.mp3".format(word_answer))
                    time.sleep(0.5)
            succ = True
        while not succ:
            print("WRONG!, try again!")
            if use_audio:
                print("Write the meaning of this word...")
            else:
                print("Write the meaning of this word: '{}'".format(worde))            
            if lang == 'en':
                playsound("statics/data/audio/{}.mp3".format(worde))
            if use_audio:
                word = input("It means (Press 0 to exit, 1 to see answer, 2 to fix the mean): ".format(worde))
            else:
                word = input("'{}' means (Press 0 to exit, 1 to see answer, 2 to fix the mean): ".format(worde))
            if word == "0":
                say_goodbye(Silent)
            if word == "1":
                print("'{}' means: '{}'".format(worde, dictionary[worde]))
                if lang == 'vi':
                    for word_answer in dictionary[worde]:
                        playsound("statics/data/audio/{}.mp3".format(word_answer))
                        time.sleep(0.5)
                succ = True
            if word == "2":
                if lang == 'vi':
                    exit()
                change_the_mean(dictionary[worde][0], engs, viets, eng_path, viet_path)
            if word.lower().strip() in dictionary[worde]:
                print("You are RIGHT!")
                if lang == 'vi':
                    for word_answer in dictionary[worde]:
                        playsound("statics/data/audio/{}.mp3".format(word_answer))
                        time.sleep(0.5)
                succ = True
        # print("{}".format())
    print("THE TEST IS FINISHED!")



if __name__ == "__main__":

    Silent = input("Do you want this to be silent??? ('yes' or 'no'): ")
    while Silent not in ['yes', 'no', '0']:
        Silent = input("Do you want this to be silent??? ('yes' or 'no'): ")
        
    if Silent == '0':
        print("bye")
        exit()
    
    if Silent == 'yes':
        Silent = True
    else:
        Silent = False

    ########################### Welcome #################################
    save_and_say("statics/data/audio/suhi_intro.mp3", "welcome to Suhi's English test", silent=Silent)
    #############################LOAD DATA###############################

    # eng_path = "english.txt"
    # vet_path = "vietnamese.txt"

    eng_path = "statics/data/Destination_B2_unit2e.txt"
    vet_path = "statics/data/Destination_B2_unit2v.txt"

    # eng_path = "statics/data/Destination_B2_unit4e.txt"
    # vet_path = "statics/data/Destination_B2_unit4v.txt"

    engs, viets = load_files(eng_path, vet_path)

    print("Saving audio files...")
    save_to_audio(engs, 'en')
    print("DONE!")

    dictionary_ev, dictionary_ve = create_dics(engs, viets)
    
    #########################################################################


    USE_AUDIO = 'suhi'
    type_of_test_text = "Please choose to use listen and guess test or not, type yes or no and enter"
    print(type_of_test_text)
    save_and_say("statics/data/audio/suhi_1.mp3", type_of_test_text, silent=Silent)

    while USE_AUDIO not in ['yes', 'no']:
        USE_AUDIO = input("Whether to use listen and guess test??? ('yes' or 'no'): ")
    
    if USE_AUDIO:
        start_text = "Starting listen and guess test"
        print(start_text)
        save_and_say("statics/data/audio/suhi_1USE_AUDIO.mp3", start_text, silent=Silent)
    else:
        start_text = "Starting look at word and guess meaning test"
        save_and_say("statics/data/audio/suhi_1NOT_USE_AUDIO.mp3", start_text, silent=Silent)
    
    
    MODE = "suhi"

    text1 = "Please input the type of test, type e v to enter the english to vietnamese test, v e to enter the vietnamese to english test, or just type both to simultaneously enter the two tests."
    
    print(text1)
    save_and_say("statics/data/audio/suhi_rules.mp3", text1, silent=Silent)

    while MODE not in ['ev', 've', 'both', '0']:
        MODE = input("Input the mode of the test: 'ev', 've', 'both' or '0' to exit: ")

    if MODE == '0':
        say_goodbye(Silent)
    
    text2 = "You will hear or see a word or a phrase once, then type the answer as the meaning of it. Notice that you can exit while doing the test by pressing 0 and enter. To pass the question and see the answer, press 1 and enter. Thank you"
    print(text2)
    save_and_say("statics/data/audio/suhi_detail_rule.mp3", text2, True, silent=Silent)

    if MODE in ['ev', 'both']:
        ev_text =  "This is English to Vietnamese test"
        print(ev_text)
        save_and_say("statics/data/audio/suhi_eng_viet.mp3", ev_text, silent=Silent)
        english_test(eng_path, vet_path, engs, viets, engs, dictionary_ev, USE_AUDIO, lang='en')

    if MODE in ['ve', 'both']:
        ve_text = "This is Vietnamese to English test"
        print(ve_text)
        save_and_say("statics/data/audio/suhi_viet_eng.mp3", ve_text, silent=Silent)
        english_test(eng_path, vet_path, engs, viets, viets, dictionary_ve, False, lang='vi')





    