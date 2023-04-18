# pip install pythonnet


def small_test():
    from pythonnet import load

    runtimeconfig_path = r"C:\git\pythonnet_test\cs\testlib\out\testlib.runtimeconfig.json"
    load("coreclr", runtime_config=runtimeconfig_path)

    import clr
    import sys

    sys.path.append(r"C:\git\pythonnet_test\cs\testlib\out")
    clr.AddReference("testlib")

    from testlib import Class1
    n = Class1().CountDevices()

    print(f"Found {n} devices")


if __name__ == "__main__":
    small_test()
