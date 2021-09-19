class Solution(object):
    def restoreString(self, s, indices):
        aux = ""
        
        for i in range(len(indices)):
            aux += s[indices.index(i)]
        
        return aux