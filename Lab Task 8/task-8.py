import math as mt

val = [3, 5, 2, 9, 3, 5, 2, 9]
n = len(val)
lvl = mt.log2(n)
level = int(lvl)

def minimaxi_code(crr_dpt,nd_index,min_turn,item,total_depth):
    if crr_dpt == total_depth:
        return val[nd_index]
    
    if min_turn:
        return min(minimaxi_code(crr_dpt+1,nd_index*2,False,item,total_depth),
                   minimaxi_code(crr_dpt+1,nd_index*2+1,False,item,total_depth))
    
    return max(minimaxi_code(crr_dpt+1,nd_index*2,True,item,total_depth),
                minimaxi_code(crr_dpt+1,nd_index*2+1,True,item,total_depth))


res = minimaxi_code(0,0,True,val,level)
print("The Result value is : ",res)