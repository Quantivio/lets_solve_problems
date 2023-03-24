class Weights:
    @staticmethod
    def solution():
        total_test_cases = int(input().strip())
        for _ in range(total_test_cases):
            weight, x_weight, y_weight, z_weight = map(int, input().split())
            stack = []
            weight_list = [x_weight, y_weight, z_weight]
            for s_weight in weight_list:
                if weight in weight_list:
                    print("YES")
                    break
                if len(stack) > 0 and (weight - s_weight) in stack:
                    print("YES")
                    break
                else:
                    stack.append(s_weight)
            else:
                print("NO")


Weights.solution()
