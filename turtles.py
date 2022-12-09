turtles = {
    'donatello': {'username':'donatello', 'password': 'pepperoni'},
    'leonardo': {'username':'leonardo', 'password': 'meatlovers'},
    'michelangelo': {'username':'michelangelo', 'password': 'anchovies'},
    'raphael': {'username':'raphael', 'password': 'pineapple'},
    'splinter': {'username': 'splinter', 'password': 'jalapeno'}
}

def get_by_username(username):
    return turtles.get(username)