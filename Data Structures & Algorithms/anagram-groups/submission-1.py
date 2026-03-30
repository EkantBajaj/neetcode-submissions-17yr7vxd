class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = defaultdict(list)
        for each in strs:
            a = 26*[0]
            for char in each:
                a[ord(char)-ord("a")]+=1
            result_dict[tuple(a)].append(each)
        
        return list(result_dict.values())

            