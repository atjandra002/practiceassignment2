library(rvest)
read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
csv_wiki <- read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
csv_tables <- csv_wiki %>% html_nodes(xpath='//*[@id="mw-content-text"]/div[1]/pre[1]') %>% html_text()
csv_tables
csv_table <- csv_tables[1]
write.table(csv_table, file="car.csv", quote=FALSE, col.names=FALSE, row.names=FALSE)
read.csv("car.csv")
