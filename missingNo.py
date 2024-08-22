def check(arr,n):
        sum = 0
        sumA = 0
        for i in range(1, n+1, 1):
            sum = sum + i
        for j in range(0,n-1,1):
            sumA = sumA + arr[j]
        print(sum)
        print(sumA)
        print(sum - sumA)

arr1 = [1,2,3,5]
n = 5
check(arr1,n)
