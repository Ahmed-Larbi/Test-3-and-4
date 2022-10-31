def Test3(a, b, m, n):
 
    if ((m == 0 and n == 0) or n == 0):
        return 1
    if (m == 0):
        return 0
 
    if (a[m - 1] == b[n - 1]):
        return (Test3(a, b, m - 1, n - 1) +
                Test3(a, b, m - 1, n))
    else:
        return Test3(a, b, m - 1, n)
 
# Driver code
a = input("please Enter Sentence 1")
b = input("please Enter Sentence 2")
 
print(Test3(a, b, len(a),len(b)))