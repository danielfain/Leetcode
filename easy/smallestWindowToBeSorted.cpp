#include <vector>

using namespace std;

vector<int> smallestWindowToBeSorted(vector<int>& nums) {

    vector<int> bounds {};

    int right = INT32_MAX;
    int left = INT32_MIN;

    for (int i = nums.size()-1; i >= 0; i--) {
        if (nums[i] < right) {
            right = nums[i];
        } else {
            bounds.insert(bounds.begin(), i);
        }
    }

    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] > left) {
            left = nums[i];
        } else {
            bounds.insert(bounds.begin()+1, i);
        }
    }

    return bounds;
}
