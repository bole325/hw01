"""
计算器单元测试
使用 pytest 运行测试
"""

import pytest
from src.calculator import Calculator

class TestCalculator:
    """计算器测试类"""
    
    def setup_method(self):
        """每个测试方法执行前的设置"""
        self.calc = Calculator()
    
    # 加法测试
    def test_add_positive_numbers(self):
        """测试正数加法"""
        assert self.calc.add(3, 5) == 8
        assert self.calc.add(10.5, 20.3) == 30.8
    
    def test_add_negative_numbers(self):
        """测试负数加法"""
        assert self.calc.add(-3, -5) == -8
        assert self.calc.add(-10, 5) == -5
    
    def test_add_zero(self):
        """测试加0"""
        assert self.calc.add(10, 0) == 10
        assert self.calc.add(0, 0) == 0
    
    # 减法测试
    def test_subtract_positive_numbers(self):
        """测试正数减法"""
        assert self.calc.subtract(10, 3) == 7
        assert self.calc.subtract(20.5, 10.2) == 10.3
    
    def test_subtract_negative_numbers(self):
        """测试负数减法"""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(5, -3) == 8
    
    # 乘法测试
    def test_multiply_positive_numbers(self):
        """测试正数乘法"""
        assert self.calc.multiply(4, 5) == 20
        assert self.calc.multiply(2.5, 3) == 7.5
    
    def test_multiply_negative_numbers(self):
        """测试负数乘法"""
        assert self.calc.multiply(-4, 5) == -20
        assert self.calc.multiply(-4, -5) == 20
    
    def test_multiply_by_zero(self):
        """测试乘以0"""
        assert self.calc.multiply(10, 0) == 0
        assert self.calc.multiply(0, 10) == 0
    
    # 除法测试
    def test_divide_positive_numbers(self):
        """测试正数除法"""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(7.5, 2) == 3.75
    
    def test_divide_negative_numbers(self):
        """测试负数除法"""
        assert self.calc.divide(-10, 2) == -5
        assert self.calc.divide(-10, -2) == 5
    
    def test_divide_by_zero(self):
        """测试除以0的情况"""
        with pytest.raises(ValueError, match="除数不能为0"):
            self.calc.divide(10, 0)
    
    # 边界测试
    def test_large_numbers(self):
        """测试大数运算"""
        large_num = 1e15
        assert self.calc.add(large_num, large_num) == 2e15
        assert self.calc.multiply(large_num, 2) == 2e15
    
    def test_small_numbers(self):
        """测试小数运算"""
        small_num = 1e-15
        assert self.calc.add(small_num, small_num) == 2e-15
        assert self.calc.multiply(small_num, 2) == 2e-15