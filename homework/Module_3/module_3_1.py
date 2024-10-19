

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(st: str):
    re = (f'{len(st)}', st.upper(), st.lower())
    count_calls()
    return re


find_list = ['mem','KeK','mang', 'lbL']
def is_contains(stt, f_list):
    count_calls()
    res = False
    for i in f_list:
        if i.lower() == stt.lower():
            res = True
            break
        else:
            res = False
    return res


print(string_info('local'))
print(is_contains('MEm', find_list))
print(is_contains('mangs', find_list))

print(calls)