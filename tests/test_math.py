import subprocess
import pytest
import os


class TestMathFunctions:
    """独立的数学函数测试类"""

    @classmethod
    def setup_class(cls):
        """测试类初始化：编译C程序"""
        print("编译C程序...")
        result = subprocess.run(
            ["gcc", "-o", "math_program", "src/main.c"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            pytest.fail(f"编译失败: {result.stderr}")
        print("✅ C程序编译成功")

    def test_addition_output(self):
        """测试加法输出"""
        result = subprocess.run(["./math_program"], capture_output=True, text=True)
        output = result.stdout

        assert "3 + 4 = 7" in output, f"加法输出不正确。实际输出:\n{output}"
        print("✅ 加法测试通过")

    def test_multiplication_output(self):
        """测试乘法输出"""
        result = subprocess.run(["./math_program"], capture_output=True, text=True)
        output = result.stdout

        assert "3 * 4 = 12" in output, f"乘法输出不正确。实际输出:\n{output}"
        print("✅ 乘法测试通过")

    def test_greeting_message(self):
        """测试问候语"""
        result = subprocess.run(["./math_program"], capture_output=True, text=True)
        output = result.stdout

        assert "Hello, CI/CD World!" in output, f"问候语缺失。实际输出:\n{output}"
        print("✅ 问候语测试通过")

    def test_program_exit_code(self):
        """测试程序退出码"""
        result = subprocess.run(["./math_program"], capture_output=True, text=True)
        assert result.returncode == 0, f"程序异常退出，退出码: {result.returncode}"
        print("✅ 程序退出码测试通过")


def test_standalone_function():
    """独立的测试函数示例"""
    # 编译程序
    subprocess.run(["gcc", "-o", "math_program", "src/main.c"], check=True)

    # 运行并验证
    result = subprocess.run(["./math_program"], capture_output=True, text=True)
    output = result.stdout

    # 综合验证
    expected_lines = [
        "Hello, CI/CD World!",
        "3 + 4 = 7",
        "3 * 4 = 12"
    ]

    for expected in expected_lines:
        assert expected in output, f"缺少预期输出: '{expected}'"

    print("✅ 独立函数测试通过")


if __name__ == "__main__":
    # 可以直接运行这个文件进行测试
    pytest.main([__file__, "-v"])