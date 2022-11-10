from time import perf_counter


class RemoveAdjacentDuplicates:
    @staticmethod
    def solution(base_string: str) -> str:
        stack = []
        for character in base_string:
            if stack and stack[-1] == character:
                stack.pop()
            else:
                stack.append(character)
        return "".join(stack)


if __name__ == "__main__":
    start_time = perf_counter()
    print(RemoveAdjacentDuplicates.solution("abbaca"))
    end_time = perf_counter()
    print(f"The time taken {end_time - start_time}")
