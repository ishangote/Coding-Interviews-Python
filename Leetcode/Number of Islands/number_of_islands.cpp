#include <iostream>
#include <vector>
#include <string>

using namespace std;

//Recursive DFS
void numIslandsHelper(vector<vector<char>>& grid, int i, int j){
    int m = grid.size(), n = grid[0].size();
    if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == '0')
        return;
    
    grid[i][j] = '1';
    numIslandsHelper(grid, i + 1, j);
    numIslandsHelper(grid, i - 1, j);
    numIslandsHelper(grid, i, j + 1);
    numIslandsHelper(grid, i, j - 1);
}

int numIslands(vector<vector<char>>& grid){
    int ans = 0, m = grid.size(), n = grid[0].size();
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if (grid[i][j] == '1'){
                ans++;
                numIslandsHelper(grid, i, j);
            }
        }
    }
}