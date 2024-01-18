#include <iostream>
#include <vector>

class Solution {
public:
    int search(std::vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            std::cout << "Comprobando elemento en el indice " << mid << std::endl;

            if (nums[mid] == target) {
                std::cout << "Objetivo encontrado en el indice " << mid << std::endl;
                return mid;
            } else if (nums[mid] < target) {
                std::cout << "El objetivo es mayor, buscando en la mitad derecha" << std::endl;
                low = mid + 1;
            } else {
                std::cout << "El objetivo es menor, buscando en la mitad izquierda" << std::endl;
                high = mid - 1;
            }
        }

        std::cout << "Objetivo no encontrado" << std::endl;
        return -1;
    }
};

int main() {
    std::vector<int> nums1 = {1, 3, 5, 7, 9};
    int target1 = 5;
    Solution solution1;
    int result1 = solution1.search(nums1, target1);
    std::cout << "Result 1: " << result1 << std::endl;

    std::vector<int> nums2 = {2, 4, 6, 8, 10};
    int target2 = 7;
    Solution solution2;
    int result2 = solution2.search(nums2, target2);
    std::cout << "Result 2: " << result2 << std::endl;

    return 0;
}
