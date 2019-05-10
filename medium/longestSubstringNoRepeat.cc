#include <iostream>
#include <string>
#include <vector>

using namespace std;

int lengthOfLongestSubstring(string s) {
  int longest = 0;
  vector<char> substring;

  for (int i = 0; i < s.size(); i++) {
    char c = s[i];

    substring.push_back(c);

    for (int j = 0; j < substring.size(); j++) {
      if (substring[j] == c) {
        if (substring.size() > longest) {
          longest = substring.size();
        }
        substring.clear();
        break;
      } else {
        if (substring.size() > longest) {
          longest = substring.size();
        }
      }
    }

  }

  return longest;
}

int main() {
  string s = "aab";
  int res = lengthOfLongestSubstring(s);

  cout << res << endl;
}