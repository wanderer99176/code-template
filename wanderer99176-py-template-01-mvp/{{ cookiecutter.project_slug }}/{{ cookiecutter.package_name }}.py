#!/usr/bin/env python3
"""
{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

这是你的主脚本文件。在这里开始编码！
"""

import requests


def main():
    """主函数 - 脚本入口点。"""
    print("Hello from {{ cookiecutter.project_name }}!")
    print("这是你的MVP脚本。在这里开始编码！")
    
    # 示例：发起一个简单的HTTP请求
    try:
        response = requests.get("https://httpbin.org/json")
        if response.status_code == 200:
            print("✅ Successfully made HTTP request!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ HTTP request failed with status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error making HTTP request: {e}")


if __name__ == "__main__":
    main()
