import subprocess
import pytest
import os


def compile_c_program():
    """编译C程序，处理路径问题"""
    # 确定C源文件路径
    c_source = "./main.c"
    if not os.path.exists(c_source):
        # 如果src/main.c不存在，尝试其他路径
        c_source = "main.c"

    print(f"编译C源文件: {c_source}")

    result = subprocess.run(
        ["gcc", "-o", "math_program", c_source],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"编译错误: {result.stderr}")
        return False

    return os.path.exists("math_program")


def test_basic_operations():
    """测试基础数学运算"""
    # 先编译
    assert compile_c_program(), "C程序编译失败"

    # 运行程序
    result = subprocess.run(
        ["./math_program"],
        capture_output=True,
        text=True
    )

    print(f"程序输出: {result.stdout}")
    print(f"程序错误: {result.stderr}")
    print(f"退出码: {result.returncode}")

    # 验证输出
    assert result.returncode == 0, f"程序异常退出: {result.stderr}"
    assert "3 + 4 = 7" in result.stdout
    assert "3 * 4 = 12" in result.stdout

    print("✅ 所有基础测试通过!")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
