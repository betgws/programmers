#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


long long solution(int n, vector<int> times){

    long long left = 1;
    long long right = *max_element(times.begin(),times.end()) * (long long)n;
    long long answer = right;

    while (left <= right){

        long long mid = (left+right) / 2;

        long long people= 0;


        for(int time: times){
            people = mid / time;

            if(people >= n){
                break;
            }

        }
        if(people >= n){
            answer = mid;
            right = mid - 1;  
        }
        else{
            left = mid + 1;
        }
    }

    return answer;

}