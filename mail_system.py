def parse_int(to_parse: str) -> int:
  #if to_parse.isdigit():
  #  return int(to_parse)
  return int(to_parse)

def parse_pack(line: str) -> tuple:
  line = line.split()
  assert len(line) == 2
  # (name, weight)
  return (line[0], parse_int(line[1]))

class Office:
  __slots__ = ('min_pack_w', 'max_pack_w', 'queue')

  def __init__(self, pack_count: int, min_pack_w: int, max_pack_w: int):
    # TODO: add error recovery mechanism
    assert all(x is not None for x in (pack_count, min_pack_w, max_pack_w))
    self.min_pack_w = min_pack_w
    self.max_pack_w = max_pack_w
    # WARNING: split may not be 2 length
    self.queue = tuple(parse_pack(input()) for _ in range(pack_count))
  
  def __len__(self):
    return len(self.queue)
  
  # does pack fit in this office
  def fit(self, pack: tuple) -> bool:
    return self.min_pack_w <= pack[1] <= self.max_pack_w

  def transfer_from (self, source):
    assert isinstance(source, Office)
    fit_packs = tuple(pack for pack in source.queue if self.fit(pack))
    unfit_packs = tuple(pack for pack in source.queue if not self.fit(pack))
    self.queue += fit_packs
    source.queue = unfit_packs


def create_city(office_count: int) -> tuple:
  # TODO: add error recovery mechanism
  assert office_count is not None
  return tuple(
            # WARNING: split may not be 3 length
            Office(*map( parse_int, input().split() ))
            for _ in range(office_count)
          )


def create_cities(city_count: int) -> dict:
  # dict[city_name] = city_dict
  return {
        input() : create_city(parse_int(input()))
        for _ in range(city_count)
      }

def parse_all_system() -> dict:
  return create_cities(parse_int(input()))