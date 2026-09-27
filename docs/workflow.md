# System Workflow

## 1. Start Application

The user starts the Product Review & Price Analyzer through the Streamlit application.

## 2. Enter Product Details

The user enters:
- Product name
- Source / Platform
- Product type / category
- Colour
- Product rating

## 3. Enter Review

The user enters or pastes the product review that they want to analyze.

## 4. Validate Input

The system checks whether the required information, especially product name, source, and review, has been provided.

If required information is missing, the system displays a warning.

## 5. Preprocess Review

The review text is cleaned before analysis.

The preprocessing includes:
- Converting text to lowercase
- Removing unnecessary special characters
- Removing extra spaces

## 6. Analyze Review

The cleaned review is passed to the review analyzer.

The system checks predefined suspicious patterns such as:
- Excessive promotional words
- Repeated exaggerated words
- Excessive exclamation marks
- Very short reviews
- Certain rating and review combinations

A suspicion score is calculated based on the detected patterns.

## 7. Display Review Result

Based on the calculated score, the system displays one of three results:

- 🟢 Review looks relatively trustworthy
- 🟡 Review needs a closer look
- 🔴 Review is potentially suspicious

The result is an indication of suspicious patterns and is not a definite claim that a review is fake.

## 8. Retrieve Price History

The system searches the local `price_history.csv` file using:
- Product name
- Source / Platform

If matching records are found, the available price history is retrieved.

## 9. Analyze Price

The system compares the recent prices and identifies whether:
- The price is at a recent low
- The price has decreased
- The price has increased
- The price has remained stable

## 10. Display Price Trend

The system displays the available price history and a line graph showing the price trend.

## 11. Provide Before You Buy Guidance

The system displays general suggestions such as comparing different reviews, checking both positive and negative feedback, and considering more than one review before making a purchase decision.

## 12. End

The user can review the analysis and make their own purchase decision based on the information provided.