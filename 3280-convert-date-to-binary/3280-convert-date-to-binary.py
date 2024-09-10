class Solution:
    def convertDateToBinary(self, date: str) -> str:
        dl = date.split('-')
        dl_bin = [str(bin(int(dl[i]))[2:]) for i in range(len(dl))]
        return '-'.join(dl_bin)