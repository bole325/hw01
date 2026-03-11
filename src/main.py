"""
计算器主程序
提供命令行交互界面
"""

from calculator import Calculator

def get_number_input(prompt):
    """获取用户输入的数字，包含错误处理"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("错误：请输入有效的数字！")

def display_menu():
    """显示操作菜单"""
    print("\n" + "="*30)
    print("       简单计算器")
    print("="*30)
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 退出")
    print("="*30)

def perform_operation(choice, a, b):
    """执行选中的运算"""
    calc = Calculator()
    
    operations = {
        '1': ('+', calc.add),
        '2': ('-', calc.subtract),
        '3': ('*', calc.multiply),
        '4': ('/', calc.divide)
    }
    
    if choice in operations:
        symbol, operation = operations[choice]
        try:
            result = operation(a, b)
            print(f"\n结果：{a} {symbol} {b} = {result}")
        except ValueError as e:
            print(f"错误：{e}")
    else:
        print("错误：无效的选择！")

def main():
    """主程序入口"""
    while True:
        display_menu()
        choice = input("请选择操作 (1-5): ")
        
        if choice == '5':
            print("感谢使用计算器，再见！")
            break
        
        if choice in ['1', '2', '3', '4']:
            print("\n--- 输入数字 ---")
            a = get_number_input("请输入第一个数字: ")
            b = get_number_input("请输入第二个数字: ")
            perform_operation(choice, a, b)
        else:
            print("错误：请选择1-5之间的选项！")

if __name__ == "__main__":
    main()