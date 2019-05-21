def second_repeated_word(char_str):
    result = {}
    words = char_str.split()
    for word in words:
        result.setdefault(word, 0)
        result[word] += 1

    return sorted(result.items(), key=lambda obj: obj[1], reverse=True)[1]


if __name__ == '__main__':
    print(second_repeated_word("Both of these issues are fixed by postponing the evaluation of annotations. \
    Instead of compiling code which executes expressions in annotations at their definition time, \
    the compiler stores the annotation in a string form equivalent to the AST of the expression in question. \
    If needed, annotations can be resolved at runtime using typing.get_type_hints(). \
    In the common case where this is not required, the annotations are cheaper to store \
    (since short strings are interned by the interpreter) and make startup time faster."))
