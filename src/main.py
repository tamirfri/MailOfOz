from mail_system import parse_all_system
from mail_ops import parse_all_ops

def main():
  cities = parse_all_system()
  parse_all_ops(cities)

if __name__ == '__main__':
  main()