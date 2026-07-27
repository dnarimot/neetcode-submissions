class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        index = 0
        start = 0
        while index < len(s):
            if s[index] == "#":
                lenS = int(s[start:index])
                start = index + 1 + lenS
                decoded_list.append(s[index + 1:start])
                index += lenS
            index += 1
        return decoded_list
                