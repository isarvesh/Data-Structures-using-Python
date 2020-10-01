def check_cheese(cheese):
    """ return true if the cheese is in stock
    """
    if cheese == "Gouda":
        logging.info("ooh we have that one")
        return True
    logging.info(f"we don't have any {cheese}")
    return False

def find_first_available_cheese():
    """iterates over preferred cheeses, returns the first one that is available"""
    for cheese in ['Emmental','Gouda']:
        if check_cheese(cheese):
            return cheese
    logging.error("and you call yourself a cheeseshop!")

find_first_available_cheese()   ### start