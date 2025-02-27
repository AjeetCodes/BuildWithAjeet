import sys

print(f"📌 Python Version: {sys.version}")
print(f"📌 Platform: {sys.platform}")
print(f"📌 Recursion Limit: {sys.getrecursionlimit()}")
print(f"📌 System Path: {sys.path[:3]} ...")  # Display first 3 paths
args = sys.argv[1:] if len(sys.argv) > 1 else 'None'
print(f"📌 Command-line Args: {args}")
sys.stdout.write("✅ Standard Output Example\n")
sys.stderr.write("❌ Error Message Example\n")
# Uncomment to exit the script
# sys.exit("Program Terminated!")

