import sys
import django

sys.path = sys.path[1:]
print(django.__path__)
