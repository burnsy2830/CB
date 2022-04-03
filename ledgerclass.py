import pickle
from datetime import datetime


class ledger:
    """
    The class that holds the ledger of people, the amounts they payed, new ledger can be genorated for each year.
    """

    def __init__(self):
        """
        Initalize backing data structure of a dictionary
        """
        self.dict = {}

    def __repr__(self):
        repstring =""
        for x in self.dict:
            repstring+= x + str((self.dict[x]))

        return repstring
    def getter(self):
        return self.dict

    def sum_total(self):
        """
        Sum the total of each person returns a list of tuples
        """
        ret_list = []
        for x in self.dict:
            name = x
            total =0
            for i in self.dict[x]:
                total+= i[1]
            ret_list.append((x,total))
        return ret_list

    def sum_individual(self,name):
        if name  not in self.dict:
            return "Name Not in list"

        total = 0
        for x in self.dict[name]:
            total+= x[1]
        return total

    def add(self,name,ammount,number):
        if name in self.dict:
            self.dict[name].append((datetime.today().strftime('%Y-%m-%d'),ammount,number))
        else:
            self.dict[name] = [(datetime.today().strftime('%Y-%m-%d'),ammount,number)]


    def gen_string(self,name):
        ret_array = []
        for i in self.dict:
            print(i)
            the_string = ""
            the_string += str(self.dict[i][2]) + str(self.dict[i][1])
            ret_array.append(the_string)

