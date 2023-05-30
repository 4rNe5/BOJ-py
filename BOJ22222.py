def round_float(float_number, n_digits):
  """
  입력받은 실수를 소수점 아래 n_digits 자리까지 반올림하여 반환합니다.

  Args:
    float_number: 반올림할 실수.
    n_digits: 반올림할 소수점 아래 자리 수.

  Returns:
    반올림된 실수.
  """

  float_number_str = str(float_number)
  float_number_str_without_decimal = float_number_str[:float_number_str.find(".") + 1 + n_digits]
  return float(float_number_str_without_decimal)


def main():
  """
  입력받은 실수를 소수점 아래 222자리까지 반올림하여 출력합니다.
  """

  float_number = float(input("실수를 입력하세요: "))
  rounded_float_number = round_float(float_number, 222)
  print("반올림된 실수:", rounded_float_number)


if __name__ == "__main__":
  main()
