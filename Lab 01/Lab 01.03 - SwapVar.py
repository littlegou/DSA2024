"""Lab 01.03 - SwapVar"""
def convert_string_to_tuples(text_in):
    values = text_in.strip('()').split(', ')
    values = tuple(map(float, values))
    print((values[1],values[0]))
convert_string_to_tuples(input())
