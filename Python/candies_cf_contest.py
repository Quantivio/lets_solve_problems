class Candies:
    @staticmethod
    def solution():
        # Split the given array into two parts and find both arrays do not have any repeated elements.
        test_cases = int(input().strip())
        for _ in range(test_cases):
            candies = int(input().strip())
            candies_price_list = list(map(int, input().split()))
            if len(candies_price_list) % 2 == 0:
                for number in candies_price_list:
                    if candies_price_list.count(number) > 2:
                        print("NO")
                        break
                else:
                    print("YES")
            else:
                print("NO")


Candies.solution()
