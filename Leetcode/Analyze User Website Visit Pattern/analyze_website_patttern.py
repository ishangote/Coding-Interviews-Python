"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

Example 1:
Input: 
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
timestamp = [1,2,3,4,5,6,7,8,9,10], 
website = ["home","about","career","home","cart","maps","home","home","about","career"]

Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 

Note:
3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.
"""

"""
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]

per_user_websites = 
{
    joe: [home, about, career]
    james: [home, cart, maps, home]
    mary: [home, about, career]
}

count_of_combinations = 
{
    (home, about, career): 2
    (home, cart, maps): 1
    (cart, maps, home): 1
    ...: 1

}

NOTE:
>>> from itertools import combinations
>>> x = ["home", "cart", "maps", "home"]
>>> set(combinations(x,3))
{('home', 'cart', 'maps'), ('cart', 'maps', 'home'), ('home', 'maps', 'home'), ('home', 'cart', 'home')}

"""
from collections import defaultdict
from collections import Counter
from itertools import combinations
def analyze_website_pattern(username, timestamp, website):
    packed_tuple = sorted(zip(timestamp, username, website))

    per_user_websites = defaultdict(list)
    for time, user, web in packed_tuple:
        per_user_websites[user].append(web)
    
    three_sequences_count = defaultdict(int)
    for websites in per_user_websites.values():
        three_sequences = set(combinations(websites, 3))
        for ts in three_sequences:
            three_sequences_count[ts] += 1
            
    sorted_three_sequences_count = sorted(three_sequences_count, key = lambda x: (-three_sequences_count[x], x))
        
    return list(sorted_three_sequences_count[0])

import unittest
class TestAnalyzeUserWebsiteVisitPattern(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(analyze_website_pattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"]), ["home","about","career"])

if __name__ == "__main__": unittest.main()