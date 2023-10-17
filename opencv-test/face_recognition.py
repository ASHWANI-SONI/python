'''
    Recognise faces using some classification algo like
    Logisitic, KNN , SVM etc.

    1. Read a video stream using opencv
    2. extract faces out of it
    3. load the training data (numpy arrays of all the persons)
        # x - values are stores in the numpy arrays
        # y - values we ned to assign for each person

    4. use knn to find the prediciton of face (int)
    5. map the predicted id to name of the user 
    6. Display the prediction on the screen - bounding box and name
'''

