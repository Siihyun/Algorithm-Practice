class Solution:
    def dfs(self,x,y,x_len,y_len,grid,visited):
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]
        
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= x_len or ny >= y_len:
                continue
            if grid[nx][ny] == '1' and visited[nx][ny] == 0:
                self.dfs(nx,ny,x_len,y_len,grid,visited)
        
        return 0
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        
        if grid is None:
            return 0
        x_len = len(grid)
        y_len = len(grid[0])
        
        visited = [[0]*y_len for i in range(x_len)]
        
        for i in range(x_len):
            for j in range(y_len):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    answer += 1
                    self.dfs(i,j,x_len,y_len,grid,visited)
        return answer
                    