from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for _str in strs:
            cnt = [0] * 26
            for _chr in _str:
                cnt[ord('a') - ord(_chr)] += 1

            d[tuple(cnt)].append(_str)

        return list(d.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
