class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #(target - position) / speed = time it takes to reach
        #if time it takes to reach is less than cars in fleets, add to that fleet
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: #sorted list in reverse order
            time = (target - p) / s 
            stack.append(time) #append time of each car

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if there are more than 2 cars in stack, see if time of 2nd last element is greater than last element
                stack.pop() #if so, pop
        
        return len(stack)
        