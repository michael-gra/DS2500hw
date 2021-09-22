'''
Grace Michael
DS2500: Programming with Data
Lab 4
'''


from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import random
import numpy as np

if __name__ == "__main__":


    # Load the digits dataset and print its shape (number of samples,
    # number of features per sample)
    digits = load_digits()
    print(digits.data.shape)

    ''' TODO: Split data into training/testing, and instantiate a classifier'''
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

    knn =KNeighborsClassifier()
    knn.fit(X = X_train, y = y_train)


    # Try out one number image at a time, just to see what we get
    which = random.randint(0, 1796)
    plt.imshow(digits.images[which], cmap = plt.cm.gray_r)
    plt.show()
    predicted = knn.predict(X = digits.data[which].reshape(1, -1))
    print("Predicted for data......", predicted)
    print("Were we right??? .....", digits.target[which])


    ##### Testing our own hand-written image
    # Convert to the correct format (2d instead of 3d) and
    # put the values within the expected range

    ''' TODO: Create an image file and read it in here '''
    img = plt.imread("IMG-1222.jpg")

    img = np.dot(img[...,:3], [1, 1, 1])
    img = (16 - img * 16).astype(int)
    plt.figure(2)
    plt.imshow(img, cmap = plt.cm.gray_r)

    predicted = knn.predict(img.flatten().reshape(1, -1))
    print("Predicted for my hand-drawn image.....", predicted)

    # It took me like 10 tries to get this to work... I had to make the numbers very thick and dark...
    # If numbers were too skinny, they were automatically 1, if too wide, automatically zero
