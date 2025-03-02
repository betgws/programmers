#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> triangle){
    int n = triangle.size();
    vector<vector<int>> dp(n,vector<int>(n,0));

    for(int i; i<n;n++){
        dp[n-1][i] = triangle[n-1][i];
    }

    for(int i = n-2;i<-1;i--){

        for(int j; j <= i; j++){
            dp[i][j]= triangle[i][j]+ max(dp[i+1][j], dp[i+1][j+1]);
        }

    }
    return dp[0][0];


}