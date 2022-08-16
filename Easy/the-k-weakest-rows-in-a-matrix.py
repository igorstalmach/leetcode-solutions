class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        ppl = {}
        index = 0

        for inner in mat:
            for j in inner:
                if index in ppl:
                    ppl[index] += j
                else:
                    ppl[index] = j
            index += 1
        
        ppl = dict(sorted(ppl.items(), key=lambda item: item[1]))

        out = []

        for key, val in ppl.items():
            out.append(key)

        return out[:k]