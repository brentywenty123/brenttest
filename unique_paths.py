class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        
        if m < 1 or n < 1:
            return 0
        
        if m == 1 and n == 1:
            return 1
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


def main():
    s = Solution()
    m = 23
    n = 12
    print(s.uniquePaths(m, n))



if __name__ == "__main__":
    main()