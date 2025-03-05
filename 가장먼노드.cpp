#include <iostream>;
#include <vector>;
#include <queue>;


using namespace std;

int solution(int n, vector<vector<int>> edge){

    vector<vector<int>> graph(n+1);
    vector<bool> visited(n+1, false);
    
    for(const auto& next : edge ){
        graph[next[0]].push_back(next[1]);
        graph[next[1]].push_back(next[0]); 
    }

}

int bfs(vector<vector<int>>&  graph, vector<bool> visited, int start){
    queue<pair<int,int>> q;
    visited[1] = true;

    int answer = 0;
    int lef = 0;
    int max = 0;

    for(const auto& next : graph[start]){
        q.push({next,1});
        visited[next] = true;
    }

    while(!q.empty()){
        auto [node, dist] = q.front();
        q.pop();

        for(const auto& a : graph[node]){
            if(visited[a] != true){
                visited[a] = true;
                q.push({a,dist+1});
            }
        }

        if (dist > max) {
            max = dist;
            answer = 1;
        } else if (dist == max) {
            answer++;
        }
    }

    return answer;


}