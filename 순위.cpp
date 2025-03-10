#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> results){

    vector<vector<int>> winList(n+1);
    vector<vector<int>> loseList(n+1);

    int answer = 0;

    for(auto &i: results ){

        winList[i[0]].push_back(i[1]);
        loseList[i[1]].push_back(i[0]);

    }

    for(int i; i<n; i++){

        vector<bool> visited(n, false);
        visited[i] = true;

        queue<int> winQueue;
        winQueue.push(i+1);

        queue<int> loseQueue;
        loseQueue.push(i);

        int c = 1;
        int t = 0;

        while(!winQueue.empty()){
            if(c == n){
                answer = answer +1;
                t = 1;
                break;
            }

            int a = winQueue.front();
            winQueue.pop();

            for(auto &i : winList[a]){
                if(!visited[i-1]){
                    visited[i-1] = true;
                    c = c + 1;
                    winQueue.push(i);
                }
            }

        }


    }




}