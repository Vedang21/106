import plotly.express as px
import csv 

with open("DATA1.csv")as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="sleep in hours",y="Coffee in ml")
    fig.show()