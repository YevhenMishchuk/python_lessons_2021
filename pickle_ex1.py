import pickle
my_items=['one','ten','rock','valve']

my_file=open('favorites.dat','wb')
pickle.dump(my_items, my_file)
my_file.close()


save_file=open('favorites.dat','rb')
load_data=pickle.load(save_file)
save_file.close()
print (load_data)