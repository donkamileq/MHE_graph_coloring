#include <iostream>
#include <list>
#include <time.h>
#include <vector>

using namespace std;

class Graph
{
    int V;
    list<int> *adj;

public:
    Graph(int V)   { this->V = V; adj = new list<int>[V];}
    ~Graph()       { delete [] adj; }

    void addEdge(int v, int w);
    void colorVertices();
    int getBadConnections(int *result);
    int scoreOfAlgorithm(int result[]);
    int getUniqueColor(int *arr);
    void HillClimbing(int iteration);
    void whiteout(int result[]);


};

void Graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
    adj[w].push_back(v);
}

void Graph::whiteout(int result[]) {
    for (int u = 0; u < V; u++)
        result[u] = 0;

}

void Graph::colorVertices(){
    srand (time(NULL));
    int result[V];
    int colors[4] = {0, 1, 2, 3};

    for(int i=0; i<50; i++){
        int RanIndex = rand() % 4;
        int color = colors[RanIndex];
        result[i] = color;
    }

    cout << "-----Start Algorithm-----" << endl;
    printf("Number of different colors: %d", getUniqueColor(result));
    cout << "\nWrong connection happend " << getBadConnections(result) << endl;
    cout << "Score of Algorithm: " << scoreOfAlgorithm(result) << endl;
}

int Graph::getBadConnections(int result[]) {
    int bad_connect = 0;

    for(int i=0; i<V; i++){
        list<int>::iterator it;
        for(it=adj[i].begin(); it!=adj[i].end(); ++it){
            if(result[i] == result[*it]){
                bad_connect++;
            }
        }
    }
    return bad_connect;
}

int Graph::scoreOfAlgorithm(int result[]) {
    int score = (getBadConnections(result) + getUniqueColor(result));
    return score;
}

int Graph::getUniqueColor(int arr[]) {
    int color_counter = 0;
    int results_backup[V];

    for (int i = 0; i < V; i++) {
        results_backup[i] = arr[i];
    }
    sort(results_backup, results_backup + V);

    for (int i = 0; i < V; i++) {
        if (results_backup[i] == results_backup[i + 1]) {
            continue;
        } else {
            color_counter++;
        }
    }
    return color_counter;
}

void Graph::HillClimbing(int iteration) {
    int result[V];
    int results_backup[V];
    int state;
    whiteout(result);
    std::vector<int> vector_result;

    for (int i = 0; i < iteration; i++) {
        for (int j = 0; j < V; j++) {
            results_backup[j] = result[j];
        }
        state = scoreOfAlgorithm(result);

        int random_vert = (rand() % 51);
        result[random_vert] = (rand() % 4);

        if (state < scoreOfAlgorithm(result)) {
            for (int j = 0; j < V; j++) {
                result[j] = results_backup[j];
            }
        } else {
            vector_result.push_back(scoreOfAlgorithm(result));
        }
    }

    cout << "\n-----Start Algorithm-----" << endl;
    printf("Number of different colors: %d", getUniqueColor(result));
    cout << "\nWrong connection happend " << getBadConnections(result) << endl;
    cout << "Score of Algorithm: " << scoreOfAlgorithm(result) << endl;
}

int main(){
    Graph g1(50);
    g1.addEdge(0,21);
    g1.addEdge(1,0);
    g1.addEdge(2,25);
    g1.addEdge(2,31);
    g1.addEdge(3,25);
    g1.addEdge(4,17);
    g1.addEdge(5,41);
    g1.addEdge(6,27);
    g1.addEdge(7,9);
    g1.addEdge(7,16);
    g1.addEdge(9,29);
    g1.addEdge(9,5);
    g1.addEdge(10,6);
    g1.addEdge(10,38);
    g1.addEdge(13,0);
    g1.addEdge(14,11);
    g1.addEdge(15,4);
    g1.addEdge(15,45);
    g1.addEdge(16, 6);
    g1.addEdge(17, 49);
    g1.addEdge(18, 44);
    g1.addEdge(19, 37);
    g1.addEdge(20, 18);
    g1.addEdge(21, 35);
    g1.addEdge(21, 20);
    g1.addEdge(22, 26);
    g1.addEdge(22, 16);
    g1.addEdge(23, 17);
    g1.addEdge(23, 40);
    g1.addEdge(24, 31);
    g1.addEdge(25, 15);
    g1.addEdge(26, 32);
    g1.addEdge(27, 47);
    g1.addEdge(28, 24);
    g1.addEdge(29, 43);
    g1.addEdge(30, 13);
    g1.addEdge(30, 33);
    g1.addEdge(32, 23);
    g1.addEdge(32, 27);
    g1.addEdge(33, 1);
    g1.addEdge(34, 28);
    g1.addEdge(34, 11);
    g1.addEdge(35, 34);
    g1.addEdge(36, 28);
    g1.addEdge(36, 42);
    g1.addEdge(37, 5);
    g1.addEdge(37, 2);
    g1.addEdge(38, 4);
    g1.addEdge(39, 1);
    g1.addEdge(39, 30);
    g1.addEdge(40, 44);
    g1.addEdge(40, 14);
    g1.addEdge(41, 10);
    g1.addEdge(41, 3);
    g1.addEdge(42, 20);
    g1.addEdge(42, 38);
    g1.addEdge(43, 13);
    g1.addEdge(44, 43);
    g1.addEdge(45, 36);
    g1.addEdge(45, 18);
    g1.addEdge(47, 19);
    g1.addEdge(47, 31);
    g1.addEdge(49, 39);

    g1.colorVertices();
    g1.HillClimbing(100);
    return 0;
}
