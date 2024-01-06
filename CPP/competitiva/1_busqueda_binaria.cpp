#include <iostream>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
};

int main() {
    // Aquí puedes probar tu función search.
    std::vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 9;

    Solution solution;
    int result = solution.search(nums, target);

    std::cout << "Resultado: " << result << std::endl;

    return 0;
}
