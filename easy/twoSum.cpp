#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> hm {};

    for (int i = 0; i < nums.size(); i++) {
        auto dif = hm.find(target - nums[i]);

        if (dif != hm.end()) {
            return std::vector<int> {std::min(i, dif->second), std::max(i, dif->second)};
        } else {
            hm.insert({nums[i], i});
        }
    }
    return std::vector<int> {0, 0};
}
