import pickle
save_file=open('save.dat','rb')
load_game_data=pickle.load(save_file)
save_file.close

print(load_game_data)  