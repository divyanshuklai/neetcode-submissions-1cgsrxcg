class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            if aster > 0:
                st.append(aster)
            elif st:
                while st and st[-1] > 0 and st[-1] < abs(aster):
                    st.pop()
                if st and st[-1] > 0 and st[-1] == abs(aster):
                    st.pop()
                    continue
                if st and st[-1] > abs(aster):
                    continue 
                st.append(aster)
            else:
                st.append(aster)
        return st
                    