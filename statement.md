# Project Statement

## Project Title

Product Review & Price Analyzer

## Problem Statement

Online shopping platforms contain a large number of product reviews and changing prices. Some reviews may contain exaggerated or suspicious patterns also sometimes companies just to sell their defective items add false or fake reviws about that product ., while product prices may change over time.

Users may find it difficult to evaluate a review and understand recent price changes before purchasing a product.

This project provides a simple system that analyzes product reviews for potentially suspicious patterns and displays recent product price history to support better purchase evaluation.

## Target Users

The system is intended for:
- Online shoppers
- Students and general users who want to evaluate product reviews
- Users who want to observe recent price changes before purchasing a product

## Project Scope

The current prototype focuses on:
- Review text analysis using predefined rules
- Suspicion score calculation
- Product rating consideration
- Local price-history analysis
- Price trend visualization
- Basic purchase guidance

The current prototype does not connect to live Amazon, Flipkart, or other marketplace data.

## High-Level Features

1. Product Details Input
2. Product Review Analysis
3. Suspicion Score Calculation
4. Review Result Classification
5. Product Price History Analysis
6. Price Trend Graph
7. Before You Buy Guidance
8. Input Validation

## Input

The system accepts:
- Product name
- Source / Platform
- Product category
- Colour
- Product rating
- Review text

## Output

The system provides:
- Review analysis result
- Suspicion score
- Recent price history
- Current/recent price information
- Price trend graph
- Basic purchase guidance

## Data Used

The prototype uses locally stored review and price-history data.

The current price-history data is sample/demo data created for testing and demonstration purposes. It does not represent live marketplace prices.

## Technology Used

- Python
- Streamlit
- CSV files
- Rule-based text analysis