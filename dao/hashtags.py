class HashtagDAO:
    def __init__(self): #Generates hardwired parameters by default on PartDAO initialization
        P1 = [87, 'helloWorld', 56]
        P2 = [88, 'Thefirst', 56]
        P3 = [91, None, 57]
        P4 = [33, 'tru', 58]
        P5 = [34, 'hard', 58]
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)

    def getAllHashtags(self):
        return self.data

    def getHashtagsById(self,htid):
        result = []
        for r in self.data:
            if htid == r[0]:
                result.append(r)
        if not result:
            return None
        else:
            return result

    def getHashtagsByMessageId(self,mid):
        result = []
        for r in self.data:
            if mid == r[2]:
                result.append(r)
        if not result:
            return None
        else:
            return result