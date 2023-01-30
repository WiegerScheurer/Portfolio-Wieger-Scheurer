#Install and load the package that includes getSymbols and chartSeries
install.packages("quantmod")
library(quantmod)

#Get the stock price as an xts file of Amicus Therapeutics, an American
#biopharma company from Philadelphia (FOLD)
getSymbols("FOLD", env = NULL)

#Chart the data for the year 2022 using chartSeries
chartSeries(FOLD["2022"])

#Function that takes 3 arguments, a stock name that has a OHLC object available
#followed by the year to be viewed, and the name of the file to be exported.
#There can only be one year entered, and there cannot be any spaces in the title
#The stock argument has to be entered as a string.

plotstock = function(stock_str, year, filename){
  
  #Request the data of the input stock
  stock_df = getSymbols(stock_str, env = NULL)
  
  #Turn the input arguments into strings
  filename_str = deparse(substitute(filename))
  filename_strpng = paste(filename_str, ".png")
  year_str = deparse(substitute(year))
  
  #Create a .png file of the requested data
  png(file = filename_strpng)
  chartSeries(stock_df[year_str])
  
  #Save the created plot in the directory
  dev.off()
}
#Trial run of the function
plotstock("AAPL",2022,AAPL_stock2022)



