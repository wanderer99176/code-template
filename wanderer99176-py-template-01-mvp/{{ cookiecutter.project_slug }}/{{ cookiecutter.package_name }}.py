#!/usr/bin/env python3
"""
{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}

This is your main script file. Start coding here!
"""

import requests


def main():
    """Main function - your script entry point."""
    print("Hello from {{ cookiecutter.project_name }}!")
    print("This is your MVP script. Start coding here!")
    
    # Example: Make a simple HTTP request
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
