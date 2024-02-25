"""
Please, full explain this function: document iterations, conditionals, and the
function as a whole
"""


def fn(main_plan, obj, extensions=[]):
    """
    Process items. Handle main plan, obj items and extensions.
    Mark items to be deleted if there is no quantity or if the item is not on
    the main plan nor extensions.
    Include the main plan id with the qty of 1 if it's not processed.

    :param main_plan: main plan.
    :param obj: items.
    :param extensions: extensions, defaults to [].

    :return: list of processed items.
    """
    # List to store processed items.
    items = []
    # Flag to evaluate to include main plan data into the processed items.
    sp = False
    # Flag to evaluate if a product is marked for deletion.
    # TODO: Consider to remove this variable. Even though the value is updated,
    #  the variable is not evaluated in the implemented method.
    cd = False
    # Dict to store price id and quantities.
    ext_p = {}

    # Process extensions (if exists) to extract into a dictionary price id and
    # quantity. e.g.
    # ext_p = {'500': 20, '501', 50, '502': 100}
    for ext in extensions:
        ext_p[ext['price'].id] = ext['qty']

    # Process the items data to get a filtered list of products.
    # e.g.
    # items = [{'id': 10, 'qty': 150}, {'id': 11, 'deleted': True}]
    for item in obj['items'].data:
        product = {
            'id': item.id
        }

        if item.price.id != main_plan.id and item.price.id not in ext_p:
            # If the item price id is different from the main plain id, and it's
            # not on in processed extension dict; then mark the product to be
            # deleted.
            product['deleted'] = True
            cd = True
        elif item.price.id in ext_p:
            # If the item price id is on the processed extension dict.
            # Mark to be deleted if the quantity is less than 1, otherwise add
            # quantity into the product dict.
            qty = ext_p[item.price.id]
            if qty < 1:
                product['deleted'] = True
            else:
                product['qty'] = qty
            # Remove the register from the processed extension dict.
            del ext_p[item.price.id]
        elif item.price.id == main_plan.id:
            # If the item price id is equal to the main plan id, set sp flag to
            # True.
            sp = True

        items.append(product)

    # If the main plain id is not found in the items, then include it with qty
    # of 1.
    if not sp:
        items.append({
            'id': main_plan.id,
            'qty': 1
        })

    # Process the remaining extensions and include them into the items list only
    # if the qty is greater equal tan 1.
    for price, qty in ext_p.items():
        if qty < 1:
            continue
        items.append({
            'id': price,
            'qty': qty
        })

    # Return the processed item list.
    # e.g.
    # items = [{'id': 10, 'qty': 150}, {'id': 11, 'deleted': True}]
    return items
