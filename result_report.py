

def create_review_report(review_result):

    return {
        "title": "Review Analysis Result",
        "result": review_result["result"],
        "score": review_result["score"],
        "message": (
            "This result indicates potentially suspicious patterns "
            "and does not confirm that the review is fake."
        )
    }




def create_price_report(price_result):

    return {
        "title": "Price Analysis Result",
        "status": price_result["status"],
        "message": price_result["message"]
    }