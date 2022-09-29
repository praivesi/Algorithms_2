#include <string>
#include <vector>
#include <iostream>
#include <stack>
#include <cmath>

using namespace std;

typedef struct Node
{
    string name;
    string referral;
    int x;
    int y;
    int refX;
    int refY;
    int earn;

    Node()
    {
        name = "";
        referral = "";
        x = -1;
        y = -1;
        refX = -1;
        refY = -1;
        earn = 0;
    }
} Node;

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount);

int main()
{
    vector<string> enroll, referral, seller;
    vector<int> amount;

    enroll.push_back("john");
    enroll.push_back("mary");
    enroll.push_back("edward");
    enroll.push_back("sam");
    enroll.push_back("emily");
    enroll.push_back("jaimie");
    enroll.push_back("tod");
    enroll.push_back("young");

    referral.push_back("-");
    referral.push_back("-");
    referral.push_back("mary");
    referral.push_back("edward");
    referral.push_back("mary");
    referral.push_back("mary");
    referral.push_back("jaimie");
    referral.push_back("edward");

    seller.push_back("young");
    seller.push_back("john");
    seller.push_back("tod");
    seller.push_back("emily");
    seller.push_back("mary");

    amount.push_back(12);
    amount.push_back(4);
    amount.push_back(2);
    amount.push_back(5);
    amount.push_back(10);

    vector<int> answer = solution(enroll, referral, seller, amount);

    for (int a : answer)
    {
        cout << a << " ";
    }
    cout << endl;
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount)
{
    vector<int> answer;
    vector<vector<Node>> hash(26);

    for (int i = 0; i < enroll.size(); i++)
    {
        cout << "enroll : " << enroll[i] << endl;

        Node n;
        n.name = enroll[i];
        n.referral = referral[i];
        n.x = enroll[i][0] - 'a';
        n.y = hash[enroll[i][0] - 'a'].size();

        hash[enroll[i][0] - 'a'].push_back(n);
    }

    for (vector<Node> v : hash)
    {
        for (Node &n : v)
        {
            cout << "default Node : name => " << n.name << ", referral => " << n.referral << ", earn => " << n.earn << ", x => " << n.x
                 << ", y => " << n.y << ")" << endl;
        }
    }

    stack<Node> travel;

    for (int i = 0; i < seller.size(); i++)
    {
        cout << "seller: " << seller[i] << endl;
        
        for (Node &node : hash[seller[i][0] - 'a'])
        {

            if (node.name != seller[i])
            {
                continue;
            }

            travel.push(node);
            int curAmount = amount[i] * 100;
            int nextAmount = -1;

            while (!travel.empty())
            {
                Node curNode = travel.top();
                travel.pop();

                cout << "cur node: name => " << curNode.name << ", referral => " << curNode.referral << ", earn => " << curNode.earn << ")" << endl;

                nextAmount = (curAmount - curAmount % 10)  * 0.1;
                
                cout << "nextAmount: " << nextAmount << endl;

                if (nextAmount < 1)
                {
                    hash[curNode.x][curNode.y].earn += curAmount;
                }
                else
                {
                    if (curNode.referral == "-")
                    {
                        hash[curNode.x][curNode.y].earn += curAmount - nextAmount;
                    }
                    else
                    {

                        hash[curNode.x][curNode.y].earn += curAmount - nextAmount;
                        curAmount = nextAmount;

                        if (curNode.refX != -1 && curNode.refY != -1)
                        {
                            travel.push(hash[curNode.refX][curNode.refY]);

                            cout << "travel pushed." << endl;

                            continue;
                        }

                        for (int j = 0; j < hash[curNode.referral[0] - 'a'].size(); j++)
                        {
                            Node refNode = hash[curNode.referral[0] - 'a'][j];

                            if (refNode.name != curNode.referral)
                            {
                                continue;
                            }

                            curNode.refX = curNode.referral[0] - 'a';
                            curNode.refY = j;

                            travel.push(refNode);

                            cout << "travel pushed." << endl;

                            break;
                        }
                    }
                }

                Node finalCurNode = hash[curNode.x][curNode.y];
                cout << "after cur node: name => " << finalCurNode.name << ", referral => " << finalCurNode.referral << ", earn => " << finalCurNode.earn << ")" << endl;
            }
        }
    }

    for (string &e : enroll)
    {
        for (Node &n : hash[e[0] - 'a'])
        {
            if (n.name != e)
            {
                continue;
            }

            answer.push_back(n.earn);
            break;
        }
    }

    return answer;
}