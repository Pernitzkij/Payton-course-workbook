def calc(f_int_str):
    for i in str(f_int_str):

        if i.isdigit():
            yield i


with open('in.txt', 'r') as f_in, open('out.txt', 'w') as f_out:
    str1 = sum(int(i) for i in calc(*f_in))
    f_out.write(str(str1))
