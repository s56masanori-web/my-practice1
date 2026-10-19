# 簡単な四則演算プログラム

def calculate():
    print("=== 簡単な計算機プログラム ===")
    
    # 数字の入力
    num1 = float(input("1つ目の数字を入力してください: "))
    num2 = float(input("2つ目の数字を入力してください: "))
    
    print("\n--- 計算結果 ---")
    print(f"足し算 (+): {num1} + {num2} = {num1 + num2}")
    print(f"引き算 (-): {num1} - {num2} = {num1 - num2}")
    print(f"掛け算 (*): {num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        print(f"割り算 (/): {num1} / {num2} = {num1 / num2}")
    else:
        print("割り算 (/): 0で割ることはできません")

if __name__ == "__main__":
    calculate()