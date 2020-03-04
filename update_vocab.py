import os
from utils import load_files, save_and_say

def save_to_file(eng_path, vie_path, engs, viets):
    print("Saving data to files...")
    with open(eng_path, 'w', encoding='utf-8') as file:
        for word in engs:
            file.write("{}\n".format(word))
    file.close()

    with open(vie_path, 'w', encoding='utf-8') as file:
        for word in viets:
            file.write("{}\n".format(word))
    file.close()
    print("DONE!, goodbye")
    exit()


if __name__ == "__main__":
    prefix = input("Please input the prefix for file name (eg. Destination_B2_unit4): ")
    eng_path = "data/{}e.txt".format(prefix)
    vie_path = "data/{}v.txt".format(prefix)
    if os.path.exists("data/{}e.txt".format(prefix)):
        engs, viets = load_files(eng_path, vie_path)
    else:
        engs, viets = [], []
    
    while True:
        eng_new = input("Type the word that you are learing (0 to finish): ")

        if eng_new == '0':
            save_to_file(eng_path, vie_path, engs, viets)

        mean = input("Type the meaning of '{}' (0 to finish): ".format(eng_new))

        save_and_say("data/audio/{}.mp3".format(eng_new), eng_new)
        
        if mean == "0":
            save_to_file(eng_path, vie_path, engs, viets)

        if eng_new not in engs:
            engs.append(eng_new)
            viets.append(mean)
