"""
https://www.interviewbit.com/problems/pick-from-both-sides/

"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        prefix_arr, suffix_arr = [], []
        last_pre, last_suff = None, None
        for i in range(B):
            j = len(A) - i - 1

            if last_pre is None:
                prefix_arr.append(A[i])
                last_pre = A[i]
            else:
                prefix_arr.append(A[i] + last_pre)
                last_pre += A[i]

            if last_suff is None:
                suffix_arr.append(A[j])
                last_suff = A[j]
            else:
                suffix_arr.append(A[j] + last_suff)
                last_suff += A[j]

        result = max(suffix_arr[-1], prefix_arr[-1])
        for i in range(B-1):
            pre_n = i+1
            post_n = B - pre_n
            result = max(result, prefix_arr[pre_n-1] + suffix_arr[post_n-1])

        return result


def test_func():
    assert Solution().solve([5, -2, 3, 1, 2], 3) == 8
    assert Solution().solve([1, 2, 3, -1], 3) == 6
    assert Solution().solve(
        [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ],
        48
    ) == 6253
    assert Solution().solve(
        [ -584, -714, -895, -512, -718, -545, 734, -886, 701, 316, -329, 786, -737, -687, -645, 185, -947, -88, -192, 832, -55, -687, 756, -679, 558, 646, 982, -519, -856, 196, -778, 129, -839, 535, -550, 173, -534, -956, 659, -708, -561, 253, -976, -846, 510, -255, -351, 186, -687, -526, -978, -832, -982, -213, 905, 958, 391, -798, 625, -523, -586, 314, 824, 334, 874, -628, -841, 833, -930, 487, -703, 518, -823, 773, -730, 763, -332, 192, 985, 102, -520, 213, 627, -198, -901, -473, -375, 543, 924, 23, 972, 61, -819, 3, 432, 505, 593, -275, 31, -508, -858, 222, 286, 64, 900, 187, -640, -587, -26, -730, 170, -765, -167, 711, 760, -104, -333 ],
        32
    ) == 727
    assert Solution().solve(
        [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ],
        48
    ) == 6253