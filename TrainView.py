from tkinter import *
import os
from PIL import Image, ImageTk
from tkinter import messagebox

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score,recall_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold
import random
# import tensorflow as tf
import tensorflow
from keras import layers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import warnings
import os
import shutil
from PIL import ImageFile
import tkinter as tk
from tkinter import *
from tkinter import ttk


from joblib import Parallel, delayed
import joblib
  

ImageFile.LOAD_TRUNCATED_IMAGES = True
from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
root_path = ''
datasetFolderName = root_path+'data'
sourceFiles = []
MODEL_FILENAME=root_path+"model_cv.h5"
classLabels = []
path = 'data/train'
for _, dirnames, filenames in os.walk(path):
    classLabels=dirnames
    break
X=[]
Y=[]
img_rows, img_cols = 100, 100
train_path=datasetFolderName+'/train/'
test_path=datasetFolderName+'/test/'
validation_path=datasetFolderName+'/validation/'
batch_size = 36
epoch=10
activationFunction='elu'
def transferBetweenFolders(source, dest, splitRate): 
    global sourceFiles
    sourceFiles=os.listdir(source)
    if(len(sourceFiles)!=0):
        transferFileNumbers=int(len(sourceFiles)*splitRate)
        transferIndex=random.sample(range(0, len(sourceFiles)), transferFileNumbers)
        for eachIndex in transferIndex:
            shutil.move(source+str(sourceFiles[eachIndex]), dest+str(sourceFiles[eachIndex]))
    else:
        print("No file moved. Source empty!")
        
def transferAllClassBetweenFolders(source, dest, splitRate):
    for label in classLabels:
        transferBetweenFolders(datasetFolderName+'/'+source+'/'+label+'/', 
                               datasetFolderName+'/'+dest+'/'+label+'/', 
                               splitRate)

def my_metrics(y_true, y_pred):
    accuracy=accuracy_score(y_true, y_pred)
    precision=precision_score(y_true, y_pred,average='weighted')
    recall = recall_score(y_true, y_pred,average='weighted')
    f1Score=f1_score(y_true, y_pred, average='weighted') 
    print("Accuracy  : {}".format(accuracy))
    print("Precision : {}".format(precision))
    print("Recall : {}".format(recall))
    print("f1Score : {}".format(f1Score))
    cm=confusion_matrix(y_true, y_pred)
    print(cm)
    return accuracy


def prepareNameWithLabels(folderName, X, Y):
    sourceFiles=os.listdir(datasetFolderName+'/train/'+folderName)
    for val in sourceFiles:
        X.append(val)
        for i in range(len(classLabels)):
          if(folderName==classLabels[i]):
              Y.append(i)
              
#chuan bi data
def preprocess(X, Y):
    transferAllClassBetweenFolders('test', 'train', 1.0)
    transferAllClassBetweenFolders('train', 'test', 0.3)
    for i in range(len(classLabels)):
        prepareNameWithLabels(classLabels[i], X, Y)


#Model
# Note that, this model structure is a very basic one. To achieve better performance, you should change the model structure and hyperparameters according to your needs and data.
def getModel():
    model = Sequential()
    model.add(Conv2D(64, (3, 3), padding='same', activation=activationFunction, input_shape=(img_rows, img_cols, 3)))
    model.add(Conv2D(64, (3, 3), activation=activationFunction))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
 
    model.add(Conv2D(32, (3, 3), padding='same', activation=activationFunction))
    model.add(Conv2D(32, (3, 3), activation=activationFunction))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
 
    model.add(Conv2D(16, (3, 3), padding='same', activation=activationFunction))
    model.add(Conv2D(16, (3, 3), activation=activationFunction))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
 
    model.add(Flatten())
    model.add(Dense(64, activation=activationFunction))
    model.add(Dropout(0.1))                  
    model.add(Dense(32, activation=activationFunction))
    model.add(Dropout(0.1))
    model.add(Dense(16, activation=activationFunction))
    model.add(Dropout(0.1))
    model.add(Dense(len(classLabels), activation='softmax')) 
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model




#======================Train
def train():
    
    global test_datagen
    model=getModel()
    X=[]
    Y=[]
    preprocess(X, Y)
    X=np.asarray(X)
    Y=np.asarray(Y)
    skf = StratifiedKFold(n_splits=10, shuffle=True)
    skf.get_n_splits(X, Y)
    foldNum=0
    for train_index, val_index in skf.split(X, Y):
    #First cut all images from validation to train (if any exists)
        transferAllClassBetweenFolders('validation', 'train', 1.0)
        foldNum+=1
        print("Results for fold",foldNum)
        X_train, X_val = X[train_index], X[val_index]
        Y_train, Y_val = Y[train_index], Y[val_index]
    # Move validation images of this fold from train folder to the validation folder
        for eachIndex in range(len(X_val)):
            classLabel=''
            for i in range(len(classLabels)):
                if(Y_val[eachIndex]==i):
                    classLabel=classLabels[i]
        #Then, copy the validation images to the validation folder
            shutil.move(datasetFolderName+'/train/'+classLabel+'/'+X_val[eachIndex], 
                    datasetFolderName+'/validation/'+classLabel+'/'+X_val[eachIndex])
        
        train_datagen = ImageDataGenerator(
                      rescale=1./255,
                      zoom_range=0.20,
                      fill_mode="nearest")
        validation_datagen = ImageDataGenerator(rescale=1./255)
        test_datagen = ImageDataGenerator(rescale=1./255)
        
    #Start ImageClassification Model
        train_generator = train_datagen.flow_from_directory(
            train_path,
            target_size=(img_rows, img_cols),
            batch_size=batch_size,
            class_mode='categorical',
            subset='training')

        validation_generator = validation_datagen.flow_from_directory(
            validation_path,
            target_size=(img_rows, img_cols),
            batch_size=batch_size,
            class_mode=None,  # only data, no labels
            shuffle=False)   
   
    # fit model
        history=model.fit_generator(train_generator, 
                        epochs=10)
        
    print("==============TEST RESULTS============")
    test_generator = test_datagen.flow_from_directory(
            test_path,
            target_size=(img_rows, img_cols),
            batch_size=batch_size,
            class_mode=None,
            shuffle=False) 
    predictions = model.predict(test_generator, verbose=1)
    yPredictions = np.argmax(predictions, axis=1)
    true_classes = test_generator.classes

    testAcc = my_metrics(true_classes, yPredictions)
    model.save(MODEL_FILENAME)
    # joblib.dump(model, 'Model_trained.pkl')
    
    
    
    messagebox.showinfo("Thông báo", "Train dữ liệu thành công", parent=root)
    lb = Label(root, text=f"Test accuracy : {testAcc}",  font=("times new roman", 13, "bold"))
    lb.place(x=130, y=100)


class Train():
    def __init__(self, root) :
        self.root = root
        self.root.geometry("600x400+300+50")  # kích thước và vị trí hiển thị giao diện
        self.root.title("Train data")
        self.root.iconbitmap('Image\\gaming.ico')
        
    

        train_btn=Button(root,text="Train",command=train,font=("times new roman",13,"bold"),bg="#000000", fg="white",width=17)
        train_btn.place(x=200,y=200)
    
       
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Train(root)
    root.mainloop()# cua so hien len