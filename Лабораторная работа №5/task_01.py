from pprint import pprint
dict_translator = [{'bin':bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)]

pprint(dict_translator)