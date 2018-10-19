#include <iostream>
#include <vector>
#include <map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    map<int, int> hm;
    vector<int> ans;
    for (int i = 0; i < nums.size(); i++) {
        int dif = target - nums[i];
        if (hm.find(dif) == hm.end()) {
            hm[nums[i]] = i;
        } else {
            if (i < hm[dif]) {
                ans.push_back(i);
                ans.push_back(hm[dif]);
            } else {
                ans.push_back(hm[dif]);
                ans.push_back(i);
            }
            return ans;
        }
    }
    return ans;
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    twoSum(nums, target);
    return 0;
}