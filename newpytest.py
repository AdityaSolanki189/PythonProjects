num_arr = list(map(int, input().split()))
ind_arr = list(map(int, input().split()))

ans = []
for i in range(len(num_arr)):
    ans.insert(ind_arr[i], num_arr[i])
print(ans)