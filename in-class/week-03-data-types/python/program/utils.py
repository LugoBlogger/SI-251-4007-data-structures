

def check_file(file_path):
  is_exist = False
  try:
    with open(file_path, 'r') as file:
      print(f"'{file_path}' exists and is readable.")
      is_exist = True

  except FileNotFoundError:
    print(f"'{file_path}' does not exist.")

  except IOError:
    print(f"'{file_path}' exists but is not accessible.")

  return is_exist