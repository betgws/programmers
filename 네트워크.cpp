#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int solution(int n , vector<vector<int>> computers){

    int answer = 0;
    vector<bool> visited(n,false)

    auto bfs = [&](int index) {
        queue<int> q;
        q.push(index);
        visited[index] = True

        while(!q.empty()){
            int v = q.front();
            q.pop();
            for(int i, i < n, ++ i){
                if(computers[v][i] == 1 && visited[i] == false){
                    q.push(i);
                    visited[i] == true
                }
            }
        }


    }

}