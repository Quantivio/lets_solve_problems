from time import perf_counter


class MakeTheStringGreat:
    @staticmethod
    def solution_with_conditioning(base_string: str) -> str:
        string_list: list[str] = [char for char in base_string]
        index = 0
        while index < len(string_list):
            if (
                (index + 1) < len(string_list)
                and string_list[index].lower() == string_list[index + 1].lower()
                and (
                    (string_list[index].isupper() and string_list[index + 1].islower())
                    or (
                        string_list[index].islower()
                        and string_list[index + 1].isupper()
                    )
                )
            ):
                string_list.pop(index)
                string_list.pop(index)
                index = 0
            else:
                index += 1
        return "".join(string_list)

    @staticmethod
    def solution_with_stack(base_string: str) -> str:
        stack: list[str] = []
        index = 0
        while index < len(base_string):
            if len(stack) == 0:
                stack.append(base_string[index])
            elif (
                stack[-1].lower() == base_string[index].lower()
                and stack[-1] != base_string[index]
            ):
                stack.pop()
            else:
                stack.append(base_string[index])
            index += 1
        return "".join(stack)

    @staticmethod
    def solution_with_for_stack(base_string: str) -> str:
        stack: list[str] = []
        for character in base_string:
            if (
                stack
                and stack[-1].lower() == character.lower()
                and stack[-1] != character
            ):
                stack.pop()
            else:
                stack.append(character)
        return "".join(stack)


if __name__ == "__main__":
    start_counter = perf_counter()
    print(MakeTheStringGreat.solution_with_conditioning("leEeetcode"))
    end_counter = perf_counter()
    print(f"Time taken: {end_counter - start_counter}")

    start_counter = perf_counter()
    print(MakeTheStringGreat.solution_with_stack("leEeetcode"))
    end_counter = perf_counter()
    print(f"Time taken: {end_counter - start_counter}")

    start_counter = perf_counter()
    print(MakeTheStringGreat.solution_with_for_stack("leEeetcode"))
    end_counter = perf_counter()
    print(f"Time taken: {end_counter - start_counter}")
