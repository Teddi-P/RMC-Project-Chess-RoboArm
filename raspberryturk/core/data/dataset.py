import numpy as np


class Dataset(object):
    def __init__(self, X_train, X_val, y_train, y_val, zca=None, metadata=""):
        self.X_train = X_train
        self.X_val = X_val
        self.y_train = y_train
        self.y_val = y_val
        self.zca = zca
        self.metadata = metadata

    def save_file(self, filename):
        with open(filename, 'wb') as f:
            np.savez(f, X_train=self.X_train,
                        X_val=self.X_val,
                        y_train=self.y_train,
                        y_val=self.y_val,
                        zca=self.zca,
                        metadata=self.metadata)
