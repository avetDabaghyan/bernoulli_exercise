#using matplotlib.pyplot
import matplotlib.pyplot as plt
import bernoulli

##Tutorial example below.

result1 = bernoulli.all_bernoulli(0.22,70)
##result1 = bernoulli.at_least(0.71,30,10)
x = result1[0]
y = result1[1]


plt.plot(x,y)
plt.xlabel("x - k. ")
plt.ylabel("y - probability of k number of successes.")

plt.show()



# todo:
#make functions for each all_bernoulli and at_least.


##------
#This is from a tutorial.
# # x axis values
# x = [1,2,3]
# # corresponding y axis values
# y = [2,4,1]
#
# # plotting the points
# plt.plot(x, y)
#
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
#
# # giving a title to my graph
# plt.title('My first graph!')
#
# # function to show the plot
# plt.show()
