class Solution:

    def recurse(self,image, r, c, start_color, color):
        if  r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != start_color or image[r][c] == color:
            return
        image[r][c] = color
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for dx,dy in directions:
            self.recurse(image, r+dx, c+ dy, start_color, color)
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            self.recurse(image,sr,sc,image[sr][sc],color)
            return image