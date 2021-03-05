import pickle
data_game={
    'position': 'North23 East45',
    'pocket':['thing1','thing2','thing3'],
    'backpack':['thing4','thing5','thing6'],
    'money': 200
}

file=open('save.dat','wb')
pickle.dump(data_game,file)
file.close()