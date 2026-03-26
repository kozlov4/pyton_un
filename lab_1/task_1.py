import turtle
import time


def draw_koch_curve(depth, length):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        draw_koch_curve(depth - 1, length)
        turtle.left(60)
        draw_koch_curve(depth - 1, length)
        turtle.right(120)
        draw_koch_curve(depth - 1, length)
        turtle.left(60)
        draw_koch_curve(depth - 1, length)


def draw_koch_snowflake(depth, length):
    for _ in range(3):
        draw_koch_curve(depth, length)
        turtle.right(120)


def measure_execution_times(max_depth, length):
    times = []

    turtle.tracer(0, 0)

    for current_depth in range(max_depth + 1):
        turtle.clear()
        turtle.penup()
        turtle.goto(-length / 2, length / 3)
        turtle.pendown()

        start_time = time.perf_counter()

        draw_koch_snowflake(current_depth, length)
        turtle.update()

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        print(f"Глибина {current_depth}: {elapsed_time:.5f} секунд")

    return times


def draw_graph(times):
    turtle.clear()
    turtle.tracer(1, 10)
    turtle.speed(5)

    start_x, start_y = -200, -200
    max_time = max(times) if max(times) > 0 else 1
    graph_width = 400
    graph_height = 300

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.forward(graph_width)
    turtle.write("  Глибина рекурсії", align="left")

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(graph_height)
    turtle.write("Час (сек)  ", align="right")

    turtle.setheading(0)
    turtle.penup()
    turtle.color("red")
    turtle.pensize(2)

    x_step = graph_width / (len(times) - 1) if len(times) > 1 else graph_width

    for i, t in enumerate(times):
        x = start_x + i * x_step
        y = start_y + (t / max_time) * (graph_height - 50)

        turtle.goto(x, y)
        turtle.pendown()
        turtle.dot(8, "blue")

        turtle.penup()
        turtle.color("black")
        turtle.goto(x, start_y - 25)
        turtle.write(str(i), align="center", font=("Arial", 10, "normal"))

        turtle.goto(x, y + 10)
        turtle.write(f"{t:.4f}s", align="center", font=("Arial", 8, "normal"))
        turtle.color("red")


def main():
    screen = turtle.Screen()
    screen.title("Лабораторна робота №1 - Черепахова графіка (Сніжинка Коха)")

    max_recursion_depth = 8
    size = 300

    print("Починаємо вимірювання часу...")
    times = measure_execution_times(max_recursion_depth, size)

    print("\nМалюємо графік...")
    draw_graph(times)

    turtle.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()