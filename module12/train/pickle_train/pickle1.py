import pickle

some_data = {
    'taxi': 200,
    'restaurant': ['soup', 'tea', 'coffe', 'salad'],
    'home': ('money', 'money', 'money', 'money'),
    'products': {'apple': 2, 'banana': 3, 'ukrop': 'dohuya'}
}


def packing(data_to_pack, f_out_name):
    with open(f_out_name, 'wb') as f_in:
        pickle.dump(data_to_pack, f_in)


packing(some_data, 'some')


def unpacking(file_name):
    with open(file_name, 'rb') as f_out:
        return pickle.load(f_out)


result = unpacking('some')


print(f'result is \n\n{result}')
