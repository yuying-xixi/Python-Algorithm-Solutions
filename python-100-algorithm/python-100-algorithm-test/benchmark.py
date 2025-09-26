import timeit
import importlib

def benchmark(module_name, func_names, number=1000, sort_desc=True):
    """
    测试某个模块中多个函数的性能，并排序输出

    :param module_name: 模块名（字符串）
    :param func_names: 函数名列表
    :param number: 每个函数运行次数
    :param sort_desc: True 按耗时从慢到快，False 从快到慢
    """
    module = importlib.import_module(module_name)
    results = []

    for func_name in func_names:
        func = getattr(module, func_name)
        timer = timeit.Timer(func)
        total_time = timer.timeit(number=number)
        avg_time = total_time / number
        results.append((func_name, total_time, avg_time))

    # 排序
    results.sort(key=lambda x: x[2], reverse=sort_desc)

    # 输出结果
    print(f"\n模块: {module_name}, 每个函数运行 {number} 次\n")
    for name, total, avg in results:
        print(f"{name:15s} 总耗时: {total:.6f} 秒 | 平均: {avg:.8f} 秒")


if __name__ == "__main__":
    print("=== Python 代码性能测试工具 ===")

    module_name = input("请输入模块名（不带.py): ").strip()
    funcs_input = input("请输入要测试的函数名（多个用逗号分隔）: ").strip()
    func_names = [f.strip() for f in funcs_input.split(",")]
    benchmark(module_name, func_names, number=10000, sort_desc=True)
