

class Bill ():
    def __init__(self, amount):
        if isinstance(amount, int):
            if amount >= 0:
                self.amount = amount
            else:
                raise ValueError("Cannot give a negative number")
        else:
            raise TypeError ("The amount is not an integer!!!")



    def __str__(self):
        return "A {}$ bill".format(str(self.amount))

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __repr__(self):
        return "{}".format(self.amount)

    def __hash__(self):
        return self.amount

    def total (self):
        return self.amount

    def get_list(self):
        return [self]



class BatchBill () :

    def __init__(self, batch):
        self.batch = batch

    def __len__(self):
        return len(self.batch)

    def total(self):
        all = 0
        for el in self.batch:
            all += int(el)
        return all

    def __getitem__(self, index):

        return self.batch[index]

    def __int__(self):
        return sum([int(x) for x in self.batch])

    def get_list (self):
        return [self.batch]

class CashDesk ():



    def __init__(self):
        self.desk_money = []

    def take_money (self,money):
        self.desk_money.append(money)

    def total(self):

        x = sum([int(m) for m in self.desk_money])
        return x

    def inspect (self):

        insp_dict = {}
        for elem in self.desk_money:
            for n in elem.get_list():
                if n in insp_dict:
                    insp_dict[n] += 1
                else:
                    insp_dict[n] = 1
        print (insp_dict)
        return insp_dict

if __name__ == "__main__":

    '''
    a = Bill(10)
    b = Bill(5)
    c = Bill(10)
    #z = Bill(-1)
    print (int(a)) # 10
    print (str(a)) # "A 10$ bill"
    print(a) # A 10$ bill

    print(a == b) # False
    print (a == c) # True

    money_holder = {}

    money_holder[a] = 1

    if c in money_holder:
        money_holder[c] += 1

    print(money_holder)  # { "A 10$ bill": 2 }

    values = [10, 20, 50, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)
    sum = 0
    for bill in batch:
        print(bill)

    print ("total sum: ",batch.total())
    '''

    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    print(desk.total())
    desk.inspect()