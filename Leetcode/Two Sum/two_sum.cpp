/*
Test C++ program
*/

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector <int> twoSum(vector<int> nums, int target){
    unordered_map<int, int> hash_map;
    vector <int> ans;
    for (int i = 0; i < nums.size(); i++){
        int numberToFind = target - nums[i];
        auto it = hash_map.find(numberToFind);
        if (it != hash_map.end()){
            ans.push_back(it -> second);
            ans.push_back(i);
        }
        hash_map[nums[i]] = i;
    }
    return ans;
}