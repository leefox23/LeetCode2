class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        for i in symbols:
            paragraph = paragraph.replace(i, " ")
        hashMap = defaultdict(int)
        paragraph = paragraph.lower()
        list1 = paragraph.split()
        for i in list1:
            if i not in banned:
                hashMap[i] = hashMap[i] + 1
        maximum = max(hashMap.values())
        for key, value in hashMap.items():
            if value == maximum:
                return key
