def maxArea(height: list[int]) -> int:
        lp = 0
        rp = len(height)-1
        m = 0
        while lp < rp:
            if height[lp] > height[rp]:
                area = height[rp] * (rp - lp)
                rp-=1
            else:
                area = height[lp] * (rp - lp)
                lp+=1
            if m < area:
                m = area 
        return m
