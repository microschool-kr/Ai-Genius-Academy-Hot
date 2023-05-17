def main():
    n_input = input("라벨 개수(숫자만 입력하세요.): ")
    if not n_input.isdigit():
        print("숫자만 입력하세요.")
        return
    n = int(n_input)
    if n < 1:
        print("0 이상의 숫자를 입력하세요.")
        return
    content = ""
    for i in range(1, n+1):
        label = input(f"label {i}: ")
        content += f"""item {{
  id: {i}
  name: '{label}'
}}\n"""
    with open("./label_map.pbtxt", "w") as f:
        f.write(content)

main()