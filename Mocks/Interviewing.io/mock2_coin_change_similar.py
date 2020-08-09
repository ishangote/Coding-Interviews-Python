# You want to buy an item that costs some amount from a vending machine that doesn't give change.
# Given the cost and some possible bill sizes, find the minimum amount of money you can waste.
"""
11
[1, 2, 5]
7
[3, 5]
 ^
               7
             /   \
            4     2
          /  \    /  \
         1    -1 -1    -3
        / \
      -2  -4
      
  [3, 5]
  
  5
  3 -> 2 
  3 -> 1
   
  [0 1   2 3 4 5 6 7]
  [0 2   1 0 1 0 0 1]

min(2, 1)
min(2, 0)
min(1, 1)

Pseudo:
c -> bills
for each c:
  if index out of range: memo[i] = min(memo[i], abs(i- c))
  else:
    memo[i] = min(memo[i], memo[i - c])  
  return memo[-1]
"""
# My code during interview
def min_cost(bills, amount):
  #Input Validation
  memo = [0] + [float('inf')] * amount

  for i, v in enumerate(memo):
    for b in bills:
      if i >= b: 
        memo[i] = min(memo[i], memo[i - b])
      else:
        memo[i] = min(memo[i], abs(i - b))

  return memo[-1]

"""
Unittests:

1. 4, [3, 5]
Actual: 1
Expected: 1
               *
       0 1 2 3 4
memo =[0 2 1 0 1]

i    b
0    3
0    5

1    3
1    5

2    3
2    5

3  3
3  5

4  3
4  5  

"""

"""
Interviewers Answer:
    public static int minWaste(int cost, int[] bills) {
        return helper(cost, bills, 0);
    }

    private static int helper(int cost, int[] bills, int i) {
        if (cost <= 0) {
            return -cost;
        } else if (bills.length == i) {
            return Integer.MAX_VALUE;
        }

        return Math.min(
                helper(cost - bills[i], bills, i),
                helper(cost, bills, i + 1));
    }

    public static int minWasteDp(int cost, int[] bills) {
        Map<Integer, Map<Integer, Integer>> cache = new HashMap<>();
        return helper(cost, bills, 0, cache);
    }

    private static int helper(int cost, int[] bills, int i, Map<Integer, Map<Integer, Integer>> cache) {
        if (cache.containsKey(cost) && cache.get(cost).containsKey(i)) {
            return cache.get(cost).get(i);
        }

        if (cost <= 0) {
            return -cost;
        } else if (bills.length == i) {
            return Integer.MAX_VALUE;
        }

        int result = Math.min(
                helper(cost - bills[i], bills, i),
                helper(cost, bills, i + 1));

        if (!cache.containsKey(cost)) {
            cache.put(cost, new HashMap<>());
        }
        cache.get(cost).put(i, result);
        return result;
    }

queue = [5, 6, 8]
visited = {0, 3, 5, 6, 8}
"""