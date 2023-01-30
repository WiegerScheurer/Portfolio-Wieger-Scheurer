#Create a new dataframe with only the relevant columns, chicks and weight 
#(transformed to the max values within the aggregate function)
weight_max = aggregate(weight ~ Chick, data = ChickWeight, max)

#Reduce the dataframe to a new one only including the chicks of interest
sel_chicks = weight_max[weight_max$Chick %in% c(1, 20, 3, 40, 5),]

#Modify the factor levels of chick numbers using the factor() function to get 
#the right order.
sel_chicks$Chick = factor(sel_chicks$Chick, levels = c(1, 20, 3, 40, 5))

#Plot the dataframe with the updated factor levels, maximized weights, and 
#selected chicks.
chick_weight = ggplot(fat_chicks, aes(x=Chick, y=weight)) + 
  geom_bar(stat = "identity")

#Create another dataframe in which only the relevant variables are present, with 
#average values of the weight variable.
weight_time = aggregate(weight ~ Time, data = ChickWeight, mean)

#Plot the new dataframe using ggplot with the geom_smooth option. set se to true 
#in order to view the standard error envelope.
ggplot(weight_time, aes(Time, weight)) +
  geom_smooth(method = "lm", se = TRUE)

#Install and load the patchwork package for adding plots
install.packages("patchwork")
library(patchwork)

#Steps to create second plot
#Turn the original dataframe into one that solely comprises the chicks of 
#interest, without maximizing the values. 
chick_prog = ChickWeight[ChickWeight$Chick %in% c(1, 20, 3, 40, 5),]

#Modify the factor levels so that the order of the coloured categories within 
#the line plot are the same as the bar graph
chick_prog$Chick = factor(chick_prog$Chick, levels =  c(1, 20, 3, 40, 5))

#Build the second plot, categorizing the 5 chicks per colour. 
progplot = ggplot(chick_prog, aes(x = Time)) +
  geom_line(aes(y = weight, colour = Chick))

#Add the two plots together
chick_weight + progplot
