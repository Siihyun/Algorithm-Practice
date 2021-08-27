class Solution:
    def makeGraph(self, digits):
        graph = {}
        graph['2'] = 'abc'
        graph['3'] = 'def'
        graph['4'] = 'ghi'
        graph['5'] = 'jkl'
        graph['6'] = 'mno'
        graph['7'] = 'pqrs'
        graph['8'] = 'tuv'
        graph['9'] = 'wxyz'
        
        return graph
        
    def dfs(self, graph, cur_string, length, digits, output):
        if length == len(digits):
            output.append(cur_string)
            return
        
        for letter in graph[digits[length]]:
            self.dfs(graph, cur_string + letter, length +1, digits, output)
            
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        graph = self.makeGraph(digits)
        output = []
        self.dfs(graph,'',0,digits,output)
        
        return output