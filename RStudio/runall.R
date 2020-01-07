#before start :install.packages("PerformanceAnalytics")
#rm(list = ls())清除所有
library("PerformanceAnalytics")

library(quantmod)


charts.PerformanceSummary(rdata,Rf)
#set current directory as working directory
rdata=read.csv("portfolio_op_annr.csv",row.names = 1)
rdata=data.matrix(rdata)
rf=read.csv("rf.csv",row.names = 1)
rf=data.matrix(rf)
Rf=mean(rf)
#以下计算完毕后在table中要annualized by 250

#Cumulated PnL or Return
C_r=Return.cumulative(rdata, geometric = TRUE)
return_cumulative <- (sqrt(cumprod(1+rdata))-1)*250#没开根号

#chart.CumReturns(rdata,geometric = TRUE,main="Cumulative Returns",begin="first")

#Daily Mean Arithmetic / Geometric Return, Daily Min Return
mean_Ar=mean(rdata)
mean_Gr=mean.geometric(rdata)
min_r=min(rdata)

#Max 10 days Drawdown

Max_DD=t(round(maxDrawdown(rdata),10))#不是10天好像
chart.Drawdown(rdata[,c(1,1)], main="Drawdown")

#Volatility
vol=StdDev(rdata)*sqrt(250)

#SharpeRatio
sp=SharpeRatio(rdata,Rf,annualized=TRUE)#rf用sp算

#Skewness, Kurtosis
sk=skewness(rdata*250)
ku=kurtosis(rdata*250)

#Modified VaR, CVaR
m_var=VaR(rdata,p=0.95,"modified")
c_var=CVaR(rdata,p=0.95)


rf_cumulative <- cumprod(1+rf)-1
plot((return_cumulative+1)*100+(rf_cumulative+1)*100)
plot(rdata*250)#annualized

