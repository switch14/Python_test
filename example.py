#num1
def hello_wprld():
    print("hello world")

#num2
def greet():
    print("こんにちは")

#num3
def print_name(name:str):
    print(f"私の名前は {name} です")

#num4
def get_greet():
    return "おはようございます"

#num5
def add(a:int|float, b:int|float) -> int|float:
    return a + b




if __name__ == "__main__":
    hello_wprld()
    greet()
    print_name("やましん")
    print(get_greet())
    print(add(5, 3))