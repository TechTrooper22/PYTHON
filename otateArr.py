def rotateArr(A,D,N):
    a = A[D:]
    b = A[:D]
    ans = a + b
    print(ans)


rotateArr([1,2,3,4,5], 2, 5)