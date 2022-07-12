from datetime import date, datetime


class helper:

    @classmethod
    def ListofDict2ListofList(self,ListofDict:list):
        headers=list(ListofDict[0])
        ListofList=[]
        for i in range(len(ListofDict)):
            List2=[]
            for key in headers:
                List2.append(ListofDict[i].get(key))
            ListofList.append(List2)
        return ListofList

    @classmethod
    def StrDate(self,Date:date):
        now=Date
        return now.strftime("%m/%d/%Y")
    @classmethod
    def calculate_age(self,born:date):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))