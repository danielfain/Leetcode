#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> hm;

    for (int i = 0; i < nums.size(); i++) {
        auto dif = hm.find(target - nums[i]);

        if (dif != hm.end()) {
            return vector<int> {min(i, dif->second), max(i, dif->second)};
        } else {
            hm.insert({nums[i], i});
        }
    }
    return vector<int> {0, 0};
}

int main() {
    vector<int> nums {1, 4, 5, 2, 4, 99, 13, 7};
    int target = 18;

    vector<int> res = twoSum(nums, target);

    cout << res[0] << ", " << res[1] << endl;
}