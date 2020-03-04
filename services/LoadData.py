from utils import say_goodbye, say_hello, create_dics, load_files, save_to_audio, save_and_say, change_the_mean

def getData(path_to_eng, path_to_vie):
    engs, viets = load_files(path_to_eng, path_to_vie)
    save_to_audio(engs, 'en')

    return [(engs[i], viets[i], 'statics/data/audio/{}.mp3'.format(engs[i]))]