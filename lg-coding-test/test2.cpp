#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

stack<char> st;

const char ALIAS = '&';
string angel = "";

void decomp(char c)
{
    // cout << "insert ' " << c << " '" << endl;

    if (c == ')')
    {
        char popC = ' ';
        char buf[10000] = {
            0,
        };

        int pos = 0;
        popC = st.top();
        st.pop();

        while (popC != '(')
        {
            cout << "insert buf c : " << popC << endl;
            cout << "while st size => " << st.size() << endl;
            cout << "st top => " << st.top() << endl;
            cout << "& = " << angel << endl;
            buf[pos] = popC;
            pos++;

            popC = st.top();

            
            st.pop();

             if (popC == '(')
            {
                break;
            }

           
        }

        string str = "";

        for (int i = 0; i < pos; i++)
        {
            cout << "c : " << buf[pos - i - 1] << ", ";
            // str.append(buf[pos - i - 1] + "");
            if (buf[pos - i - 1] == '&')
            {
                str += angel;
            }
            else
            {
                str += buf[pos - i - 1];
            }
            // str += (buf[pos - i - 1] == '&') ? angel : buf[pos - i - 1];
        }

        cout << "appended str => " << str << endl;

        char numBuf[10000] = {
            0,
        };
        int numPos = 0;

        // cout << "normal st size => " << st.size() << endl;
        // cout << "st top => " << st.top() << endl;
        popC = st.top();
        st.pop();
        // cout << "start mult popC => " << popC << endl;

        while (popC != ')')
        {
            cout << "====================== ))))))) =============" << endl;
            cout << "popC: " << popC << endl;
            // cout << "insert numBuf c : " << popC << endl;
            numBuf[numPos] = popC;
            numPos++;

            if (st.empty())
            {
                break;
            }

            popC = st.top();
            if (popC == '(' || popC == '&')
            {
                break;
            }
            st.pop();
        }


        int multNum = 0;
        for (int i = 0; i < numPos; i++)
        {
            cout << "calc multNum : " << multNum << endl;
            multNum *= 10;
            multNum += numBuf[numPos - i - 1] - '0';
        }

        string final = "";

        cout << "decomped string => " << str << endl;
        cout << "******************************* multNum : " << multNum << endl;

        for (int i = 0; i < multNum; i++)
        {
            angel += str;
        }

        st.push(ALIAS);

        // for (int i = 0; i < multNum; i++)
        // {
        //     for (int j = 0; j < str.length(); j++)
        //     {
        //         st.push(ALIAS);
        //         // cout << "final push " << str[j] << endl;
        //         // st.push(str[str.length() - j - 1]);
        //     }
        // }
    }
    else
    {
        st.push(c);
        // cout << "push " << c << endl;
    }
}

string solution(string compressed)
{
    const char *chars = compressed.c_str();
    int compLength = compressed.length();

    for (int i = 0; i < compLength; i++)
    {
        // cout << 'compressed[' << i << "] : " << compressed[i] << endl;
        decomp(compressed[i]);
    }

    vector<char> finalChars;
    while (!st.empty())
    {
        // cout << "top() : " << st.top() << endl;

        finalChars.insert(finalChars.begin(), st.top());
        st.pop();
    }

    for (int i = 0; i < finalChars.size(); i++)
    {
        cout << "final char => " << finalChars[i] << endl;
    }

    // string finalStr(finalChars.begin(), finalChars.end());

    string finalStr = "";

    for (int i = 0; i < finalChars.size(); i++)
    {
        char c = finalChars[finalChars.size() - i - 1];
        // finalStr += finalChars[finalChars.size() - i - 1];

        if (c == '&')
        {
            finalStr += angel;
        }
        else
        {
            finalStr += c;
        }
    }

    return finalStr;
}

int main()
{
    string compressed = "2(2(hi)2(co))x2(bo)";
    string ans = solution(compressed);

    cout << "ans : " << ans << endl;
}