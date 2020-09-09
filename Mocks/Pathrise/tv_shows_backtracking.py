"""
We have to quarantine for k days, so we are planning to watch a TV show episode every day. There are n shows to choose from. 
Each show has (1) a number of episodes and (2) an average rating per episode. Our goal is to choose what TV shows to watch so that 
(1) if we watch an episode from a show, we watch them all, (2) we have something to watch every day, 
(3) we maximize the average rating of the episodes we watch. 
It is guaranteed that there is at least one way to watch something every day.

Input: 
k: the number of days to quarantine
episodes: an array of length n where episodes[i] is the number of episodes of show i
ratings: an array of length n where ratings[i] is the average rating of the episodes of show i

Output:
The average rating of the episodes you will watch if you choose optimally.

Examples:
k = 2
            0. 1. 2. 3
episodes = [2, 1, 1, 1]
ratings = [8, 10, 5, 4]
Solution: 8, by watching show 0.


k = 2
            0. 1. 2  3
episodes = [2, 1,  1, 1]
ratings = [7, 10, 5, 4]
               ^
Solution: 7.5, by watching shows 1 and 2.


            k = 2
            (0, 0)
           /     \
     k=0 (2, 7)  (1, 10) k = 1
                  \
               (1, 7.5) k = 0

            0. 1. 2. 3
episodes = [2, 1, 1, 1]
ratings =  [8, 10, 5, 4]
            
k = 2
                         (rating = 0, curr_k = 2)
    (rating = 8, curr_k = 0) (rating = 10, curr_k = 1) (rating = 5 curr_k = 1) (rating = 4, curr_k = 1)
                            (rating = , curr_k = )

"""
def average(prev_rating, curr_rating):

def util(prev_rating, curr_rating, cur_k):
    if cur_k == 0: return average(prev_rating, curr_rating)
    

def max_rating(k, episodes, ratings):
    #input validations   
     
    prev_rating = {}
    
    max_rating = 0
    if k == 0: return max_rating
    
    for i in episodes: