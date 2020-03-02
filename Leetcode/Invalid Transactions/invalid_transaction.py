# A transaction is possibly invalid if:

# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

# Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.
# Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

# Constraints:

# transactions.length <= 1000
# Each transactions[i] takes the form "{name},{time},{amount},{city}"
# Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
# Each {time} consist of digits, and represent an integer between 0 and 1000.
# Each {amount} consist of digits, and represent an integer between 0 and 2000.
""" 
Example 1:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

Example 2:
Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Example 3:
Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]

Optimized Solution Explanation

Create a transaction data structure so the attributes can easily be queried and store it in a transactions array
Sort the transactions array based on time
Iterate through the transactions array and create a hash table/dictionary with name as the key, and an array of transaction indexes as the value.
Iterate through the dictionary and loop through the name specific transaction indexes array.
Over 1000 dollars check: If the current transaction amount is greater than 1000, then add to the res and continue to the next transaction.
Within 60 minutes check: Use left, and right pointers to represent the possible neighbor transactions that are within the 60 minutes. This window can be represented here:
If 886 is the current transaction time:
only increment left if it is to the left of 826 (exclusive) (886-60) (represented by x's)
xxxx
|---|-----------|-----------|---|
   826   -60   886   +60  946

only increment right if the right+1 time is less than 946 (inclusive) (886+60) (represented by x's)
                xxxxxxxxxxxxx
|---|-----------|-----------|---|
   826   -60   886   +60  946
If the current transaction has any neighbors within the 60 minutes then check if the city is different. If so, add to the res and continue to the next transactions.
Time Complexity
O(nlogn + 2n) -> O(nlogn)

Space Complexity
O(n)

Code
"""

class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions):
        transactions = [Transaction(*transaction.split(',')) for transaction in transactions]
        transactions.sort(key=lambda t: t.time) # O(nlogn) time

        trans_indexes = defaultdict(list)
        for i, t in enumerate(transactions): # O(n) time
            trans_indexes[t.name].append(i)

        res = []
        for name, indexes in trans_indexes.items(): # O(n) time
            left = right = 0
            for i, t_index in enumerate(indexes):
                t = transactions[t_index]
                if (t.amount > 1000):
                    res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                    continue
                while left <= len(indexes)-2 and transactions[indexes[left]].time < t.time - 60: # O(60) time
                    left += 1
                while right <= len(indexes)-2 and transactions[indexes[right+1]].time <= t.time + 60: # O(60) time
                    right += 1
                for i in range(left,right+1): # O(120) time
                    if transactions[indexes[i]].city != t.city:
                        res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                        break

        return res