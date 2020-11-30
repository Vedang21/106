import plotly.express as px
import csv 

with open("Data2.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Marks In PercentageDays Present",y="Days Present")
    fig.show()