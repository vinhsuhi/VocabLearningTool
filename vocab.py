import numpy as np

if __name__ == "__main__":
    eng_path = "english.txt"
    vet_path = "vietnamese.txt"

    engs = []
    viets = []

    with open(eng_path, "r", encoding="utf-8") as file:
        for line in file:
            engs.append(line.strip().lower())
    file.close()

    with open(vet_path, "r", encoding="utf-8") as file:
        for line in file:
            viets.append(line.strip().lower())

    dictionary = dict(zip(engs, viets))

    print("Number of words in dictionary: {}".format(len(dictionary)))

    print("Start Test")

    np.random.shuffle(engs)
    # print(dictionary)
    for eng in engs:
        print("(Press 0 and Enter to exit, Press 1 and Enter to pass)")
        print("Write the vietnamese meaning of this word: '{}'".format(eng))
        succ = False
        word = input("'{}' means (Press 0 and Enter to exit, Press 1 and Enter to pass): ".format(eng))
        if word == "0":
            print("bye")
            exit()
        if word == "1":
            print("'{}' means: '{}'".format(eng, dictionary[eng]))
            continue
        if word.lower().strip() == dictionary[eng]:
            print("You are RIGHT!")
            succ = True
        while not succ:
            print("WRONG!, try again!")
            word = input("'{}' means (Press 0 and Enter to exit, Press 1 and Enter to pass): ".format(eng))
            if word == "0":
                print("bye")
                exit() 
            if word == "1":
                print("'{}' means: '{}'".format(eng, dictionary[eng]))
                succ = True
            if word.lower().strip() == dictionary[eng]:
                print("You are RIGHT!")
                succ = True
        # print("{}".format())
    print("THE TEST IS FINISHED!")