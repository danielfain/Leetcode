def string_compression(string):             # O(n) time and O(n) space
    compressed_string_list = []
    num_row = 1

    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            num_row += 1
        else:
            compressed_string_list.append(string[i])
            compressed_string_list.append(str(num_row))
            num_row = 1

    compressed_string_list.append(string[len(string) - 1])
    compressed_string_list.append(str(num_row))

    compressed_string = "".join(compressed_string_list)

    if len(compressed_string) >= len(string): 
        return string

    return compressed_string

string = "aabcccccaaazx"
print(string_compression(string))