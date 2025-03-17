@app.put("/hotels/{hotel_id}")
def update_hotel(
    hotel_id: int,
    title: str = Body(embed=True),
    name: str = Body(embed=True)
):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            hotel['title'] = title
            hotel['name'] = name
    return {'status': 'OK'}


@app.patch("/hotels/{hotel_id}")
def update_patch_hotel(
    hotel_id: int,
    title: str | None = Body(None, embed=True),
    name: str | None = Body(None, embed=True)
):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            if title != 'string':
                hotel['title'] = title
            if hotel != 'string':
                hotel['name'] = name
    return {'status': 'OK'}