class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)      # O(1) lookup
        memo = {}                    # start_index -> all valid sentences from here

        def build(start):
            if start == len(s):
                return [""]          # one valid way to finish

            if start in memo:
                return memo[start]   # reuse already computed suffix

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]  # current word candidate

                if word not in wordSet:
                    continue

                suffix_sentences = build(end)  # solve remaining string

                for suffix in suffix_sentences:
                    if suffix == "":
                        sentences.append(word)  # last word in sentence
                    else:
                        sentences.append(word + " " + suffix)

            memo[start] = sentences
            return sentences

        return build(0)