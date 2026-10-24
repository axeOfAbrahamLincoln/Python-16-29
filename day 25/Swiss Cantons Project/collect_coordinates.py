import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Swiss Canton Game")
image = "/Volumes/Macintosh HD Data/Coding/Python 2.0/day 25/Swiss Cantons Project/suisse68.gif"
screen.addshape(image)
screen.setup(width=1040, height=697)
turtle.shape(image)

# answer_canton = screen.textinput(title="Guess the Canton", prompt="What's another Canton name?")



import turtle
import pandas as pd

# DataFrame with Swiss cantons
df = pd.DataFrame({
    "cantons": [
        "Aargau","Appenzell Ausserrhoden","Appenzell Innerrhoden",
        "Basel Landschaft","Basel Stadt","Bern","Fribourg","Geneva",
        "Glarus","Graubünden","Jura","Lucerne","Neuchâtel","Nidwalden",
        "Obwalden","Schaffhausen","Schwyz","Solothurn","St. Gallen",
        "Thurgau","Tessin","Uri","Wallis","Waadt","Zug","Zurich"
    ],
    "shorts": [
        "AG", "AR", "AI", "BL", "BS", "BE", "FR", "GE", "GL", "GR", "JU", "LU", "NE", "NW", "OW", "SH", "SZ", "SO", "SG", "TG", "TI", "UR", "VA", "VS", "ZG", "ZH"]
})

coords = []
counter = 0

t = turtle.Turtle()
t.hideturtle()
t.penup()

def get_mouse_click_coor(x, y):
    global counter

    if counter < len(df):
        coords.append((int(x), int(y)))

        # write number on map
        t.goto(x, y)
        t.write(counter, align="center", font=("Arial", 8, "normal"))

        counter += 1

    # when all 26 clicks are done
    if counter == len(df):
        turtle.bye()

        # add coordinates to dataframe
        df["x"], df["y"] = zip(*coords)


        # save to csv
        df.to_csv("swiss_canton_coordinates1.csv", index=False)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()