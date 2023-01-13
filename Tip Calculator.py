from math import ceil
def calculate_tip(amount, rating):
    rating = rating.lower()
    match rating:
        case "terrible":
            rating = 0
        case "poor":
            rating = 5
        case 'good':
            rating = 10
        case 'great':
            rating = 15
        case 'excellent':
            rating = 20
            
    return ceil(amount * (rating / 100)) if type(rating) == int else "Rating not recognised"