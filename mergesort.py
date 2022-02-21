# for future references

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left_l = lst[:mid]
        right_l = lst[mid:]

        merge_sort(left_l)
        merge_sort(right_l)

        a = b = c = 0

        while (a < len(left_l) and b < len(right_l)):
            if (left_l[a] < right_l[b]):
                lst[c] = left_l[a]
                a+=1
            else:
                lst[c] = right_l[b]
                b+=1
            c+=1
        
        while (a < len(left_l)):
            lst[c] = left_l[a]
            a+=1
            c+=1
        while (b < len(right_l)):
            lst[c] = right_l[b]
            b+=1
            c+=1

a = [315,1,6,23,-12,12,135,13012,-213,56,231,-23,653,90,2]
print(a)
merge_sort(a)
print(a)