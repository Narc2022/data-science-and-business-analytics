course = " python programming"
print(course.upper());          # PYTHON PROGRAMMING
print(course.lower());          # python programming
print(course.title());          # Python Programming
print(course.rstrip())          #python programming
print(course.find("Pro"))       #-1 means string not found
print(course.find("pro"))       # index
print(course.replace("p","j"))  # jython jrogramming
print("pro" in course);         # True
print("swift" in course);       # False
print("swift" not in course);   # True