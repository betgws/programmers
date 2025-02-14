#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <set>

using namespace std;

// 동, 서, 남, 북 방향을 정의
int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int bfs(vector<vector<int>>& maps) {
    int n = maps.size();
    int m = maps[0].size();
    queue<tuple<int, int, int>> q;  // (x, y, 이동 거리) 저장하는 큐
    q.push({0, 0, 1});  // 시작점과 초기 거리 1을 큐에 추가

    while (!q.empty()) {
        auto [x, y, dist] = q.front();
        q.pop();

        // 상대 팀 진영에 도착한 경우
        if (x == n - 1 && y == m - 1) {
            return dist;
        }

        // 동서남북 네 방향으로 이동
        for (int i = 0; i < 4; ++i) {
            int nx = x + directions[i][0];
            int ny = y + directions[i][1];

            // 맵 범위 내에서 벽이 아닌 곳으로 이동
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1) {
                maps[nx][ny] = 0;  // 방문 처리 (재방문 방지)
                q.push({nx, ny, dist + 1});
            }
        }
    }

    // 상대 팀 진영에 도달할 수 없는 경우
    return -1;
}

int solution(vector<vector<int>>& maps) {
    return bfs(maps);
}

int main() {
    vector<vector<int>> maps = {
        {1, 0, 1, 1, 1},
        {1, 0, 1, 0, 1},
        {1, 0, 1, 1, 1},
        {1, 1, 1, 0, 1},
        {0, 0, 0, 0, 1}
    };

    int result = solution(maps);
    cout << "최단 거리: " << result << endl;

    return 0;
}







bool isOneLetterdiff(const string& word1, const string& word2){
    int diff = 0;
    for(int i = 0; i < word1.length(); i ++){
        if(word1[i] != word2[i]){
            diff++; 
        }
        if(diff > 1){
            return false;
        }
    }
    return diff == 1;
}

int dfs(const string& start, const string& target, unordered_map<string, vector<string>> &graph){
    queue<pair<string, int>> q;
    set<string> visited;

    q.push({start, 0});
    visited.insert(start);

    while(!q.empty()){
        auto [current, steps] = q.front();
        q.pop();

        if(current == target){
            return steps;
        }

        for(const string& )

    }



}