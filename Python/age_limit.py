class AgeLimit:
    @staticmethod
    def solution():
        total_test_cases = int(input().strip())

        for _ in range(total_test_cases):
            min_age, max_age, current_age = map(int, input().split())
            if min_age <= current_age < max_age:
                print("yes")
            else:
                print("no")
