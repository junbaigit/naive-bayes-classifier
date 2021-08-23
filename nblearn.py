
"""
NB training
"""

class nblearn():

    def __init__(self):

        self.numOfham = 0
        self.numOfspam =0
        self.vocabHAM = []
        self.vocabSPAM =[]

        self.hamWordCount = {}     # ham word frequence
        self.spamWordCount = {}    # spam word frequence

        self.hamProTable ={}       # p(word|ham) table
        self.spamProTable = {}     # P(word|spam) table

        self.totalSpamS =0
        self.totalHamS = 0

        self.hamPost = 0
        self.spamPost = 0

    def train(self, x,y):
        """
        :param x: training input
        :param y: label
        :return: P(word|ham),P(word|spam) table
        """

        """
        buiding up the word frequence 
        """
        for sentence,label in zip(x,y):

            if label ==1:
                self.vocabHAM.append(sentence)
                for word in sentence:
                    if word in self.hamWordCount:

                        self.hamWordCount[word]+= 1
                    else:
                        self.hamWordCount[word]= 1
            else:
                self.vocabSPAM.append(sentence)
                for word in sentence:
                    if word in self.spamWordCount:
                        self.spamWordCount[word]+= 1
                    else:
                        self.spamWordCount[word]= 1

        """
        total number of words of ham and spam
        """

        self.numOfham = len(self.hamWordCount)
        self.numOfspam =len(self.spamWordCount)


        """
        total number of ham message and spam message
        """

        self.totalHamS = len(self.vocabHAM)
        self.totalSpamS = len(self.vocabSPAM)


        """
        P(ham) = totalham message / total message
        P(spam) = totalspam message / total message
        """

        self.hamPost = self.totalHamS/len(x)
        self.spamPost = self.totalSpamS/len(x)


        """
        updating P(word|ham) table
        """
        for key in self.hamWordCount:

            self.hamProTable[key] = self.hamWordCount[key]/self.numOfham

        """
        updating P(word|spam) table
        """
        for key in self.spamWordCount:


            self.spamProTable[key] = self.spamWordCount[key]/self.numOfspam


        return self.hamProTable,self.spamProTable
