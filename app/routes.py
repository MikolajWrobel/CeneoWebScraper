from pstats import Stats
from app import app
from flask import render_template, redirect, url_for
import requests
from bs4 import BeautifulSoup
import json
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from app.models.product import Product

@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods=["POST", "GET"])
def extract():
    if requests.models == "POST":
        product_id = requests.form.get("product_id")
        product = Product(product_id)
        product.extract_product()

        return redirect(url_for("product", product_id=product_id))
    else:
        return render_template("extract.html.jinja")

@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("./app/opinions")]
    return render_template("products.html.jinja", products=products)

@app.route('/author')
def author():
    return render_template("author.html.jinja")


@app.route('/product/<product_id>')
def product(product_id):
    opinions = pd.read_json(f"app/opinions/{id}.json")
    opinions.stars = opinions.stars.map(lambda x: float(x.split("/")[0].replace(",",".")))

    recommendation = opinions.recommendation.value_counts(dropna = False).sort_index().reindex(["Polecam", None, "Nie Polecam"])
    recommendation.plot.pie(
        label="", 
        autopct="%1.1f%%", 
        colors=["forestgreen", "lightskyblue", "crimson"],
        labels=["Polecam", "Nie mam zdania", "Nie polecam"]
    )

    plt.title("Rekomendacja")
    plt.savefig(f"plots/{id}_recommendations.png")
    plt.close()

    stars = opinions.stars.value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
    stars.plot.bar()
    plt.title("Oceny produktu")
    plt.xlabel("Liczba gwiazdek")
    plt.ylabel("Liczba opinii")
    plt.grid(True)
    plt.xticks(rotation=0)
    plt.savefig(f"plots/{id}_stars.png")
    plt.close()

    return render_template("product.html.jinja", stats=stats, product_id=product_id, opinions=opinions)
