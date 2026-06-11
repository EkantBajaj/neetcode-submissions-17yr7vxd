class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def generate(i):
            if i == len(nums):
                return True

            for bucket in range(k):

                if buckets[bucket] + nums[i] <= target:
                    buckets[bucket] += nums[i]

                    if generate(i + 1):
                        return True

                    buckets[bucket] -= nums[i]

                # symmetry pruning
                if buckets[bucket] == 0:
                    break

            return False

        return generate(0)