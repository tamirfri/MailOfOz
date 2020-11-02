from mail_system import Office, parse_int

def describe_city(name:str, cities: dict):
  name = name.strip()
  assert name in cities
  print(f"{name}:")
  for i, office in enumerate(cities[name]):
    print(f"\t{i}:")
    for pack in office.queue:
      print(f"\t\t{pack[0]}")

def transfer(source: Office, target: Office):
  target.transfer_from(source)

def loadest_city(cities: dict):
  def calc_city_load(name: str):
    return sum(map(len, cities[name]))
  arg_max = max(cities, key=calc_city_load)
  print("Town with the most number of packages is", arg_max)

def do_op(op_id: int, op_params: tuple, cities: dict):
  if op_id == 1:
    describe_city(op_params[0], cities)
  elif op_id == 2:
    src_city = op_params[0]
    src_offi = parse_int(op_params[1])
    tgt_city = op_params[2]
    tgt_offi = parse_int(op_params[3])
    # WARNING: input check is needed
    transfer(cities[src_city][src_offi],
            cities[tgt_city][tgt_offi])
  elif op_id == 3:
    loadest_city(cities)
  else:
    raise ValueError("op_id is not 1, 2, or 3")

def do_all_ops(op_count: int, cities: dict):
  for _ in range(op_count):
    params = input().split()
    op_id, params = params[0], params[1:]
    do_op(parse_int(op_id), params, cities)

def parse_all_ops(cities:dict):
  do_all_ops(parse_int(input()), cities)
