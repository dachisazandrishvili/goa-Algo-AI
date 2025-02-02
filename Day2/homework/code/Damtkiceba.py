def damtkiceba(arr):
    # საშუალო არითმეტიკული
    def arit_mean(arr):
        num = 0
        for i in arr:
            num += i
        # return round(num / len(arr))
        return num / len(arr)
    
    #საშუალო გეომეტრიული
    def geo_mean(arr):
        num = 1
        for i in arr:
            num *= i
        # root = 
        return num ** (1/len(arr))
    # print(geo_mean([1.1,1.2,1.3]))

    def harmo_mean(arr):
        arr2 = []
        for i in arr:
            arr2.append(1 / i)
        num = 0
        for i in arr2:
            num += i
        return (num / len(arr)) ** -1

    # print(harmo_mean([3,2]))
    
    #დამტკიცება

    true_false_arr = []
    if min(arr) <= arit_mean(arr) <= max(arr):
        true_false_arr.append(True)
    else:
        if min(arr) <= geo_mean(arr) <=max(arr):
            true_false_arr.append(True)
        else:
            if min(arr) <= harmo_mean(arr) <= max(arr):
                true_false_arr.append(True)
            else:
                return False
    return true_false_arr[0]

print(damtkiceba([10,11,22]))
