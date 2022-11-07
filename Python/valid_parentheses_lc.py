from time import perf_counter

PARENTHESES_MAPPING = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


class ValidParentheses:
    @staticmethod
    def valid_parentheses(string: str) -> bool:
        bracket_list = []
        bracket_mapping = dict(zip('([{', ')]}'))
        for char in string:
            if char in "({[":  # change to '([{' for better performance
                bracket_list.append(char)
            elif not bracket_list or bracket_mapping[bracket_list.pop()] != char:
                return False

        return not bracket_list


if __name__ == "__main__":
    start_timer = perf_counter()
    print(ValidParentheses.valid_parentheses("{[]}"))
    end_timer = perf_counter()
    print(f"Time taken {end_timer - start_timer}")
