from mail_system import parse_int, parse_pack
from subprocess import run
from pathlib import Path

def test_parse():
  assert parse_int("6") == 6
  assert parse_int("0") == 0
  assert parse_pack("PACK 0") == ('PACK', 0)

def test_main():
  test_input = Path('test_input.txt').read_text()
  test_output = Path('test_output.txt').read_text()
  completed_process = run(('python3', './main.py'), input=test_input, text=True, capture_output=True)
  completed_process.check_returncode()
  assert test_output == completed_process.stdout