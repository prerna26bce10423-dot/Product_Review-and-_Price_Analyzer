import streamlit as st

from price_analyzer import get_price_history, analyze_price
from review_analyzer import analyze_review

st.set_page_config(
    page_title="Product Review Analyzer",
    page_icon="🛍️",
    layout="centered"
)


st.title("🛍️ Product Review & Price Analyzer")

st.write(
    "Analyze product reviews and recent price trends before making a purchase."
)

st.divider()


st.header("📦 Product Details")

product_name = st.text_input("Product Name")

source = st.text_input("Source / Platform")

product_type = st.text_input("Product Type / Category")

colour = st.text_input("Colour")

rating = st.slider(
    "⭐ Product Rating",
    1,
    5,
    3
)


st.header("📝 Write Your Review")

review = st.text_area(
    "Enter the product review",
    placeholder="Write or paste the review here..."
)


if st.button("🔍 Analyze Product"):

    if product_name and source and review:

        st.success(
            f"Product received from {source}!"
        )


       

        st.subheader(
            f"🛍️ Your Today's Pick on {source}"
        )

        st.write(
            "Product:",
            product_name
        )

        st.write(
            "Type:",
            product_type
        )

        st.write(
            "Colour:",
            colour
        )

        st.write(
            "Rating:",
            "⭐" * rating
        )




        st.divider()

        st.header("🔍 Review Analysis")

        review_result = analyze_review(
            review,
            rating
        )

        st.subheader(
            review_result["result"]
        )

        st.write(
            f"Suspicion Score: {review_result['score']}"
        )


    

        st.divider()

        st.header(
            f"📊 {source} Price History"
        )

        prices = get_price_history(
            product_name,
            source
        )


        if prices:

            result = analyze_price(prices)


           

            for item in prices:

                st.write(
                    f"📅 {item['date']} → ₹{item['price']:,.0f}"
                )


            

            st.subheader("📈 Price Trend")

            price_values = {
                      item["date"]: item["price"]
                      for item in prices
            }

            st.line_chart(
                        price_values
            )


        
            st.metric(
                  "Current Price",
                  f"₹{result['current_price']:,.0f}"
            )


           
            st.info(
                result["message"]
            )


        else:

            st.warning(
                "No price history found for this product and source."
            )


        

        st.divider()

        st.header("🛒 Before You Buy")

        st.write(
                  "* Compare reviews from different users."
        )

        st.write(
                 "* Read both positive and negative reviews."
        )

        st.write(
                  "* Look for specific product-use experiences."
        )

        st.write(
                  "* Check whether the reviewer explains why they liked or disliked the product."
        )

        st.write(
                  "* Look for both advantages and limitations."
        )

        st.warning(
                    "⚠️ Don't make a purchase decision based on a single review alone."
        )


    else:

        st.warning(
                    "Please enter the product name, source and review."
        )

        