from views import get_all_product, add_product, get_by_id, get_filtered_data

def setup_routes(app):
    app.router.add_get('/', get_all_product)
    app.router.add_post('/filter', get_filtered_data)
    app.router.add_post('/create', add_product)
    app.router.add_post('/id', get_by_id)


    
