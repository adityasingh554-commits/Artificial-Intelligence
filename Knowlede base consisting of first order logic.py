import itertools


def entails(kb_func, query_func, symbols):
  for values in itertools.product([False, True], repeat=len(symbols)):
    model = dict(zip(symbols, values))
    if kb_func(model) and not query_func(model):
      return False
  return True


symbols = ['P', 'Q']


def kb(model):
  return ((not model['P']) or model['Q']) and model['P']


def query(model):
  return model['Q']


print(entails(kb, query, symbols))
