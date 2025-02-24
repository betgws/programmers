#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <cmath>

using namespace std;

int solution(int N, int number){

    if(number == 1){
        return 1;
    }

    vector<unordered_set<int>> dp(9);

    for(int i=1; i<=8; i++){
        int num = 0;

        for(int k =1; k<=8; k++){
            num = num*10 + N;
        }
        dp[i].insert(num);


        for(int j= 1; j <i; j++){
            for(int num1: dp[j]){
                for(int num2: dp[i-j]){
                    dp[i].insert(num1 + num2);
                    dp[i].insert(num1 - num2);
                    dp[i].insert(num1 * num2);

                    if(num2 != 0){
                        dp[i].insert(num1 / num2)  ;
                    }
                }
            }

        }

        if(dp[i].count(number)){
            return i;
        }

    }

    return -1;




}