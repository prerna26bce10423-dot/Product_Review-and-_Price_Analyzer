import csv


def get_price_history(product_name, source):

    prices = []

    entered_product = product_name.strip().lower()
    entered_source = source.strip().lower()

    with open(
        "data/price_history.csv",
        "r",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            csv_product = row["product_name"].strip().lower()
            csv_source = row["source"].strip().lower()

            if (
                csv_product == entered_product
                and csv_source == entered_source
            ):

                prices.append({
                    "date": row["date"].strip(),
                    "price": float(row["price"].strip())
                })

    return prices




def analyze_price(prices):

    if len(prices) < 2:

        return {
            "status": "NOT ENOUGH DATA",
            "message": "Not enough price history available."
        }


    current_price = prices[-1]["price"]

    previous_price = prices[-2]["price"]

    lowest_price = min(
        item["price"]
        for item in prices
    )


    

    if current_price == lowest_price:

        status = "GREAT DEAL"

        message = "🔥 Price is at the recent low!"


    elif current_price < previous_price:

        status = "PRICE DROP"

        message = "🟢 Price has decreased recently."


    elif current_price > previous_price:

        status = "PRICE INCREASE"

        message = "📈 Price has increased recently."


    else:

        status = "PRICE STABLE"

        message = "Price has remained stable."


    return {
        "status": status,
        "message": message,
        "current_price": current_price,
        "previous_price": previous_price,
        "lowest_price": lowest_price
    }