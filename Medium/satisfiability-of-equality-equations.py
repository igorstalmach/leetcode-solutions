class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent, not_equal = {}, []

        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])

        for eq in equations:
            if eq[1] == '=':
                a, b = find(eq[0]), find(eq[3])

                if a != b: 
                    parent[b] = a
            
            else:
                not_equal.append((eq[0], eq[3]))

        for a, b in not_equal:
            if find(a) == find(b):
                return False
        
        return True