h=[1,8,6,2,5,4,8,3,7]
max_area=0
left=0
right=len(h)-1
area=0
while left<right:
    area=(right-left)*min(h[left],h[right])
    max_area=max(max_area,area)
    if h[left]<h[right]:
        left+=1
    else:
        right-=1
print(max_area)
