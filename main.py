import nbclassify
import nblearn
from project import dataLoader
import sys



def outPut( outFile,nblearn,nbclassify,prediction,train = False,):

    """

    :param outFile: file name
    :param nblearn: training model
    :param nbclassify: classify model
    :param prediction: accuracy
    :param train: bool of check if output in training or test
    :return:
    """

    with open(outFile, 'a') as file:
        """
        Size of ham training set: XXXX
        Size of spam training set: XXXX
        Percentage of ham classified correctly: XX.X
        Percentage of spam classified correctly: XX.X
        Total accuracy: XX.XX
        False Positive: XX.XX
        """
        if train:
            file.write("Training on training, test on training set: \n\n")
        else:
            file.write("Training on training, test on test set: \n\n")
        file.write("Size of ham training set: " + str(nblearn.totalHamS) + "\n")
        file.write("Size of spam training set: " + str(nblearn.totalSpamS) + "\n")
        file.write("Percentage of ham classified correctly: " + str((nbclassify.precentHam * 100)) + ' %' + "\n")
        file.write("Percentage of spam classified correctly: " + str((nbclassify.precentSpam * 100)) + ' %' + "\n")
        file.write("Total accuracy: " + str(prediction * 100) + '%' + "\n")
        file.write("False Positive: " + str(nbclassify.FP) + "\n")
        file.write('*********************************************************\n\n')

if __name__=='__main__':
    TESTRATIO = 0.2

    """
    load the cleaned whole dataset 
    """
    data, classes, vocabularyList = dataLoader.loadData(sys.argv[1])
    # data,classes,vocabularyList = dataLoader.loadData('SMSSpamCollection')

    if TESTRATIO !=0:

        """
        split data to training and test, default is 80 train 20 test
        TESTRATIO will change train and test ratio
        """
        x_train,y_train,x_test,y_test = dataLoader.splitData(data, classes, TESTRATIO)

        """
        training model
        """
        nblearn = nblearn.nblearn()
        hamProTable,spamProTable = nblearn.train(x_train,y_train)

        """
        P(ham)
        P(spam)
        """
        hamPost, spamPost = nblearn.hamPost,nblearn.spamPost


        """
        classify on training set
        """
        nbclassify = nbclassify.nbclassify(hamPost,spamPost,hamProTable,spamProTable)
        prediction = nbclassify.predict(x_train,y_train)
        # print(prediction)

        outFile = 'aa.txt'

        outPut(outFile,nblearn,nbclassify,prediction,True)

        """
        classify on testing set
        """


        prediction2 = nbclassify.predict(x_test, y_test)

        outPut(outFile,nblearn,nbclassify,prediction2,False)






