#include <string>
#include <vector>
#include <iostream>

using namespace std;

int** map;
int minNum = 10001;

void minCheck(int n){
    minNum = n < minNum ? n : minNum;
}

void turn(vector<int> & query){
    int x1 =  query[0];
    int y1 =  query[1];
    int x2 =  query[2];
    int y2 =  query[3];

    int cx = x1;
    int cy = y1;

    int stash = map[x1][y1];

    for(; cx < x2; cx++){
        minCheck(map[cx][cy]);
        map[cx][cy] = map[cx + 1][cy];
    }

    for(; cy < y2; cy++){
        minCheck(map[cx][cy]);
        map[cx][cy] = map[cx][cy + 1];
    }

    for(; cx > x1; cx--){
        minCheck(map[cx][cy]);
        map[cx][cy] = map[cx - 1][cy];
    }

    for (; cy > y1; cy--)
    {
        minCheck(map[cx][cy]);

        if (cy == y1 + 1)
        {
            map[cx][cy] = stash;
        }
        else
        {
            map[cx][cy] = map[cx][cy - 1];
        }
    }
}

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;

    map = new int*[rows + 1];

    for(int i = 1; i < rows + 1; i++){
        map[i] = new int[columns + 1];
        for(int j = 1; j < columns + 1; j++){
            map[i][j] = j + columns * (i - 1);
        }
    }

    for(vector<int> & query : queries){
        minNum = 10001;
        turn(query);
        answer.push_back(minNum);
    }

    return answer;
}