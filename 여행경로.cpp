#include <iostream>
#include <vector>
#include<unordered_map>
#include<algorithm>

using namespace std;

unordered_map<string, vector<string>> graph;
vector<string> answer;

vector<string> solution(vector<pair<string, string>> tickets){


    sort(tickets.begin(), tickets.end());
    
    for(auto& ticket: tickets ){
        graph[ticket.first].push_back(ticket.second);
    }

}
void dfs(const string& start){
    while()
    
}
