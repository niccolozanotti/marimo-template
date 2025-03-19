import marimo

__generated_with = "0.11.21"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md("Hello")
    return (mo,)


@app.cell
def test_cell():
    from utils import add

    x = 4
    assert add(1, 2) == 3
    assert 2 == 2
    print(f"x = {x}")
    return add, x


if __name__ == "__main__":
    app.run()
