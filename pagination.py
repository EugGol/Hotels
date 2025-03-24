
def pagination(hotels_, page, der_page):
    start = (page - 1) * der_page
    end = start + der_page
    return hotels_[start: end]
