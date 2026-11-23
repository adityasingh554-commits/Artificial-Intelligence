def is_variable(x):
  return isinstance(x, str) and x[0].islower()


def is_compound(x):
  return isinstance(x, tuple) and len(x) == 2 and isinstance(x[1], list)


def occur_check(var, x, theta):
  if var == x:
    return True
  elif is_variable(x) and x in theta:
    return occur_check(var, theta[x], theta)
  elif is_compound(x):
    return occur_check(var, x[0], theta) or occur_check(var, x[1], theta)
  elif isinstance(x, list):
    return any(occur_check(var, item, theta) for item in x)
  return False


def unify_var(var, x, theta):
  if var in theta:
    return unify(theta[var], x, theta)
  elif is_variable(x) and x in theta:
    return unify(var, theta[x], theta)
  elif occur_check(var, x, theta):
    return None
  else:
    new_theta = theta.copy()
    new_theta[var] = x
    return new_theta


def unify(x, y, theta=None):
  if theta is None:
    theta = {}
  if theta == 'FAILURE':
    return 'FAILURE'
  elif x == y:
    return theta
  elif is_variable(x):
    res = unify_var(x, y, theta)
    return 'FAILURE' if res is None else res
  elif is_variable(y):
    res = unify_var(y, x, theta)
    return 'FAILURE' if res is None else res
  elif is_compound(x) and is_compound(y):
    return unify(x[1], y[1], unify(x[0], y[0], theta))
  elif isinstance(x, list) and isinstance(y, list):
    if len(x) != len(y):
      return 'FAILURE'
    return unify(x[1:], y[1:], unify(x[0], y[0], theta))
  else:
    return 'FAILURE'


expr1 = ('Knows', ['John', 'x'])
expr2 = ('Knows', ['y', ('Mother', ['y'])])

print(unify(expr1, expr2))
