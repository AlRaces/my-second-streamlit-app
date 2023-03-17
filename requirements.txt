import pickle

filename = 'model.pickle'

pickle.dump(model, open(filename, "wb"))
model = pickle.load(open(filename, "rb"))
