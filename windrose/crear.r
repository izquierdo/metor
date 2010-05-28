library(climatol)

crear <- function(){
datos <- read.csv("archive.csv")
attach(datos)
windDir[is.na(windDir)] <- 360
windDir <- abs(windDir + runif(length(windDir))*200) %% 360
b <- seq(0, 360, 22.5)
h1 <- hist(windDir[0<=windSpeed & windSpeed<2], breaks=b)
h2 <- hist(windDir[2<=windSpeed & windSpeed<4], breaks=b)
h3 <- hist(windDir[windSpeed>=4], breaks=b)
f <- data.frame(rbind(h1$counts, h2$counts, h3$counts), row.names=c('0-2','2-4','>4'))
rosavent(f, 4, 4)
detach(datos)

}
