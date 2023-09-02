
class Ceremony:
    """
    The :class:`Ceremony` represents a Graduation Ceremony.

    :param no_of_days: An :int:  
    """
    def __init__(self, no_of_days: int)-> None:
        """
        Initializes a ceremony object.

        Raises:
            ValueError: if number of days is less than 1
        """
        if no_of_days < 1:
            raise ValueError("Number of days must be greater than or equal to 1")
        self.no_of_days = no_of_days
        self.m = 4

    def run(self) -> str:
        """
        Calculates the probability to miss the graduation ceremony.
        """
        dp = [1]*(self.m + 1)
        dp[self.m] = 0
        temp = [0]*(self.m + 1)
        for i in range(1, self.no_of_days + 1):
            temp[self.m] = 0
            for j in range(self.m-1, -1, -1):
                temp[j] = dp[0] + dp[j+1]
            temp, dp = dp, temp
        total_valid_ways = dp[0]
        ways_to_miss_last_day = temp[1]
        return f"{ways_to_miss_last_day}/{total_valid_ways}"

if __name__ == "__main__":
    n  = int(input())
    ceremony = Ceremony(n)
    print(ceremony.run()) 
