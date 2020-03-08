from .utils import say_goodbye, say_hello, create_dics, load_files, save_to_audio, save_and_say, change_the_mean
from flask import current_app
import os 
import random


def getData(prefix):
    path_to_eng = os.path.join(current_app._static_folder,'data','{}e.txt'.format(prefix))
    path_to_vie = os.path.join(current_app._static_folder,'data','{}v.txt'.format(prefix))
    engs, viets = load_files(path_to_eng, path_to_vie)
    save_to_audio(engs, 'en')
    data = []
    for i,w in enumerate(engs):
        data.append({
            'eng' : engs[i],
            'vn' : viets[i],
            'audio' :  'data/audio/{}.mp3'.format(engs[i])
        })
    random.shuffle(data)
    return data #[(engs[i], viets[i],  os.path.join(current_app._static_folder,'data','audio','{}.mp3'.format(engs[i])))]
