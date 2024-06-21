class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        mapping = defaultdict(list)
        my_list = text.split()

        for i in range(len(my_list)-2):
            key = (my_list[i], my_list[i+1])
            mapping[key].append(my_list[i+2])

        find_key = (first, second)
        return mapping[find_key]