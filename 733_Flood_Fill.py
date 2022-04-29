class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        color_to_change = image[sr][sc]

        def dfs(r, c):
            nonlocal rows, cols, newColor, image

            if r < 0 or c < 0 or r > rows-1 or c > cols-1 or image[r][c] == newColor or image[r][c] != color_to_change:
                return

            image[r][c] = newColor

			# radiate in four directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr, sc)

        return image
