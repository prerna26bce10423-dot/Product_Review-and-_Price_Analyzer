# Product Review & Price Analyzer

## Overview

- Product Review & Price Analyzer is a Python-based application designed to help users evaluate product reviews and observe recent price changes before making a purchase decision.

- The system analyzes review text using predefined patterns and calculates a suspicion score. It also uses product-specific price records to identify recent price changes and display a price trend.

## Objectives

- Analyze product reviews for potentially suspicious patterns.
- Use product ratings along with review text for analysis.
- Calculate a review suspicion score.
- Analyze recent product price changes.
- Display price trends in an easy-to-understand format.
- Provide useful guidance before purchasing a product.

## Key Features

- Product details input
- Review text analysis
- Rating-based analysis
- Suspicion score calculation
- Three-level review classification
- Product price history analysis
- Price increase and decrease detection
- Price trend visualization
- Before You Buy guidance
- Input validation

## Major Modules

1. Product Input & Validation Module
2. Review Preprocessing & Analysis Module
3. Suspicion Scoring Module
4. Price Analysis & Visualization Module
5. Result Reporting Module

## Technologies Used

- Python
- Streamlit
- CSV
- Regular Expressions
- Rule-based Text Analysis

## Project Structure

```text
product_review_analyzer/
│
├── app.py
├── review_analyzer.py
├── text_preprocessor.py
├── scoring.py
├── price_analyzer.py
├── result_report.py
│
├── data/
│   ├── reviews.csv
│   └── price_history.csv
│
└── docs/
    ├── requirements.md
    ├── testing.md
    └── workflow.md


How the System Works:

1)The user enters product details.
2)The user enters a product review and rating.
3)The system validates the required input.
4)The review text is cleaned and processed.
5)Suspicious patterns are analyzed.
6)A suspicion score and review result are generated.
7)Matching product price records are retrieved.
8)Recent price changes are analyzed.
9)The price trend is displayed as a graph.
10)The system provides general Before You Buy guidance.
Input

The system accepts:

Product name
Source / Platform
Product category
Colour
Product rating
Review text
Output

The system provides:

Review analysis result
Suspicion score
Price history
Current price
Price change information
Price trend graph
Before You Buy guidance
Data Storage

The application uses local CSV files for data storage.

- Installation

Install Python and Streamlit, then run:

pip install streamlit
Running the Application

Open the project folder in the terminal and run:

streamlit run app.py

The application will open in the browser.

- sample run:

Example 1 — Redmi Note 14

Input:

Product Name: Redmi Note 14
Source: Amazon
Category: electronics
Colour: Green
Rating: 3
Review: battery and processor is good .

Expected Output:

Review Result → 🟡/🔴 based on detected patterns
Price → ₹15,999
Price Status → 🔥 Price is at the recent low
Price Trend → Price decreased over the recorded dates

Example 2 — Women Cotton Kurti

Input:

Product Name: Women Cotton Kurti
Source: Flipkart
Category: Clothes
Colour: Yellow
Rating: 4
Review: Absolutely perfect product. Everyone should buy this immediately!

Expected Output:

Review Result → based on analysis of review given by the user 
Price → ₹749
Price Status → 🔥 Price is at the recent low / high
Price Trend → Price decreased / increased over the recorded dates

Example 3 — Men Hoodie

Input:

Product Name: Men Hoodie
Source: Amazon
Category: Clothes
Colour: white
Rating: 4
Review: good quality and useful for everyday use .

Expected Output:

Review Result → based on analysis of review given by the user.
Price → ₹1,199
Price Status → 🔥 Price is at the recent low / high
Price Trend → Price increased and then decreased over the recorded dates

Limitations

Review analysis is based on predefined patterns and does not guarantee that a review is fake.
Price information is based on the available local price records.
The application does not currently fetch live prices directly from shopping platforms.


Future Enhancements


Integration with larger review datasets
Improved machine-learning-based review analysis
Additional price-history sources
More detailed review comparison
Improved reporting and visualization

Conclusion

Product Review & Price Analyzer combines review analysis and price analysis in a single Python application. It provides users with a simple way to examine potentially suspicious review patterns and recent price movements before making a purchase decision.