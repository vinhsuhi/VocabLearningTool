from utils import say_goodbye, say_hello, create_dics, load_files, save_to_audio, save_and_say, change_the_mean
from playsound import playsound
import numpy as np


def load_synonyms(data_path, path_v):
    datas = []
    words = []
    with open(data_path, 'r', encoding='utf-8') as file:
        for line in file:
            this = []
            data_lines = line.split(',')
            for ele in data_lines:
                this.append(ele.strip().lower())
                words.append(ele.strip().lower())
            datas.append(this)
    file.close()

    means = []
    with open(path_v, 'r', encoding='utf-8') as file:
        for line in file:
            means.append(line.strip().lower())
    file.close()
    return datas, words, means


if __name__ == "__main__":
    sound_prefix_path = "statics/data/audio/"
    path = "statics/data/PreIELTS/synonyms.txt"
    path_v = 'statics/data/PreIELTS/synonyms_v.txt'
    datas_total, words, means_total = load_synonyms(path, path_v)
    shuffle_index = list(range(len(datas_total)))
    np.random.shuffle(shuffle_index)
    datas_total = [datas_total[index] for index in shuffle_index]
    means_total = [means_total[index] for index in shuffle_index]
    print("Saving audio files...")
    save_to_audio(words, 'en')
    print("DONE!")

    BatchSize = 10
    NumBatch = int(len(datas_total) / BatchSize)
    if len(datas_total) % NumBatch == 0:
        NumBatch += 1
    for i in range(NumBatch):
        datas = datas_total[i * BatchSize : (i+1) * BatchSize]
        means = means_total[i * BatchSize : (i+1) * BatchSize]
        shuffle_index_i = list(range(len(datas)))
        np.random.shuffle(shuffle_index_i)

        datas = [datas[ele] for ele in shuffle_index_i]
        means = [means[ele] for ele in shuffle_index_i]
        while True:
            for k, group in enumerate(datas):
                first = group[0]
                last = group[1:]
                word = "suhi"
                while len(last) > 0:
                    print("You have {} words to list!".format(len(last)))
                    word = input("Which words can be used to paraphrase for '{}' (0 to exit, 1 to pass, 2 to show mean, 3 to pronounce it): ".format(first))
                    if word == '0':
                        say_goodbye(False)
                    if word == '1':
                        print("Those words are: ")
                        print(last)
                        print("MEAN: {}".format(means[k]))
                        for ans in last:
                            print(ans)
                            playsound("{}{}.mp3".format(sound_prefix_path, ans))
                        break

                    if word == '2':
                        print("MEAN: {}".format(means[k]))
                    
                    if word == '3':
                        playsound("{}{}.mp3".format(sound_prefix_path, first))
                        
                    if word in last:
                        playsound("{}{}.mp3".format(sound_prefix_path, word))
                        last.remove(word)
                
                if word != '1':
                    print("MEAN: {}".format(means[k]))
                    print("You are totally right!")
                print()
            Conti = 'suhi'
            while Conti not in ['yes', 'no', '0']:
                Conti = input("Do you want to study one more time ('yes' or 'no' or '0' to exit): ")
            if Conti == '0':
                say_goodbye(False)
            elif Conti == 'yes':
                continue
            elif Conti == 'no':
                break
            
        




