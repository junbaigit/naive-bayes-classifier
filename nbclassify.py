import math


"""
NB classfier 
"""
class nbclassify:

    def __init__(self,hamPost,spamPost,hamProTable,spamProTable):
        """

        :param hamPost: P(ham)
        :param spamPost: P(spam)
        :param hamProTable: p(word|ham)
        :param spamProTable: P(word|spam)
        """
        self._hamPost = hamPost
        self._spamPost = spamPost
        self._hamProTable = hamProTable
        self._spamProTable = spamProTable

        self.hamTotal = 0
        self.spamTotal = 0

        # self.predictY = []

        self.precentHam = 0
        self.precentSpam =0
        self.FP =0
        self.TP =0
        self.FN =0
        self.TN=0
        self.accuracy =0

    def predict(self,x,y):
        """

        :param x: testing data
        :param y: testing ground truth
        :return: accuracy
        """

        predictY =[]
        for sentence in x:
            ham = 0
            spam =0

            """
            sum of log over all P(word|ham) and P(word|spam)
            """
            for word in sentence:

                if word in self._hamProTable and word in self._spamProTable:
                    ham+=  math.log(self._hamProTable[word])
                    spam += math.log(self._spamProTable[word])

            """
            sum log P(ham) 
            sum log P(spam)
            """
            ham +=math.log(self._hamPost)
            spam +=math.log(self._spamPost)


            """
            classify
            """
            if ham > spam:
                predictY.append(1)
            else:
                predictY.append(0)
        """
        get precentage of correct ham, spam prediction
        """
        self.precentOFham(y,predictY)

        """
        get false positive rate
        """
        self.falasPostive(y,predictY)

        return self.accuracy


    def precentOFham(self,y_true, y_pred):
        """

        :param y_true: ground truch
        :param y_pred: prediction
        :return:
        """
        totalHam = 0
        totalSpam =0
        totalPreHam =0
        totalPreSpam=0

        for i in range(len(y_true)):
            if y_true[i] ==1:
                totalHam+=1
                if y_pred[i] ==1:
                    totalPreHam+=1
            else:
                totalSpam += 1
                if y_pred[i] == 0:
                    totalPreSpam += 1



        self.precentHam = totalPreHam/totalHam
        self.precentSpam = totalPreSpam/totalSpam

    def falasPostive(self,y_true, y_pred):
        """
        get TP,TN,FN,FP and accuracy
        :param y_true:
        :param y_pred:
        :return:
        """


        for i in range(len(y_pred)):
            if y_true[i] == y_pred[i] == 1:
                self.TP += 1
            if y_pred[i] == 1 and y_true[i] != y_pred[i]:
                self.FP += 1
            if y_true[i] == y_pred[i] == 0:
                self.TN += 1
            if y_pred[i] == 0 and y_true[i] != y_pred[i]:
                self.FN += 1
        self.accuracy = (self.TP + self.TN) / (self.TP + self.FP + self.FN + self.TN)



