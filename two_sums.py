nums = [3,3]
target = 6

#hallar dos numeros que sumados den target
#hallar el index de esos dos numeros
#retornar esos index


def twoSum(nums, target):
  for i in range (len(nums)):
    for j in range  (i+1,len(nums)):
      if  (nums[i] + nums[j]) == target:
         print(i,j)
twoSum(nums, target)
      
