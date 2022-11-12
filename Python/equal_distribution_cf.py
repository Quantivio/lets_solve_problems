class EqualDistribution:
    @staticmethod
    def solution():
        total_test_cases: int = int(input())
        for _ in range(total_test_cases):
            bob, alice = map(int, input().split())
            total = bob + alice
            if total % 2 == 0:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    EqualDistribution.solution()
