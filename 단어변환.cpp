#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;

// Helper function to check if two words differ by exactly one letter
bool isOneLetterDiff(const string& word1, const string& word2) {
    int diffCount = 0;
    for (int i = 0; i < word1.length(); ++i) {
        if (word1[i] != word2[i]) {
            diffCount++;
        }
        if (diffCount > 1) return false;  // Early termination if more than one letter differs
    }
    return diffCount == 1;
}

// Function to find the shortest transformation path
int bfs(const string& start, const string& target, unordered_map<string, vector<string>>& graph) {
    queue<pair<string, int>> q;  // (current word, steps)
    set<string> visited;         // To track visited words

    q.push({start, 0});
    visited.insert(start);

    while (!q.empty()) {
        auto [current, steps] = q.front();
        q.pop();

        if (current == target) return steps;

        for (const string& neighbor : graph[current]) {
            if (visited.find(neighbor) == visited.end()) {
                visited.insert(neighbor);
                q.push({neighbor, steps + 1});
            }
        }
    }

    return 0;  // No transformation path found
}

int solution(string begin, string target, vector<string> words) {
    if (find(words.begin(), words.end(), target) == words.end()) {
        return 0;  // Target word is not in the list
    }

    // Build the graph using adjacency list
    unordered_map<string, vector<string>> graph;
    words.push_back(begin);
    for (const string& word : words) {
        for (const string& nextWord : words) {
            if (isOneLetterDiff(word, nextWord)) {
                graph[word].push_back(nextWord);
            }
        }
    }

    // Perform BFS to find the shortest transformation path
    return bfs(begin, target, graph);
}

int main() {
    vector<string> words = {"hot", "dot", "dog", "lot", "log", "cog"};
    string begin = "hit";
    string target = "cog";

    int result = solution(begin, target, words);
    cout << "Result: " << result << endl;  // Output: 4

    return 0;
}
