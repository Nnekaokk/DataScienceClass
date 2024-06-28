# #write a function that adds its argument to the end of a list
# # def adding_list(my_list,new_list):
# #     my_list.append(new_list)
# #     return my_list
# # my_list=[1,2,3,4]
# # new_list=5
# # adding_list=adding_list(my_list,new_list)
# print(adding_list) 
# function that takes list of numbers as strings

# goods=['2000kg','50kg','40kg']
# def change_numbers_into_strings (string_list):
  #case 1 not modifiying the content of the list
  
# def add_weights(weights):
#     total=0
#     for weight in weights:
#      string_value= weight.strip('kg')
#      numval=int(string_value)
#      total= total + numval
#      #total+=numval
#      return total
# # return total

# goods=['2000kg','50kg','40kg']
# ans= add_weights(goods)
# print(ans)
# print('average is:',ans/3)
# print(f'averageis:{ans/3}')

# #calculate the average of the numbers [2,3,5,6,4,8]
# def average_numbers(numbers):
#    ans=average_numbers(numbers)
#    numbers=[2,3,5,6,4,8]
#    print(ans)

values=[2,3,5,6,4,8]
def totalsum(values):
   total=0
   for val in values:
      total=total + val

      return total
      ans2=totalsum(values)
      print(ans2)




