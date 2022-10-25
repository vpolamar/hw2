from bottle import default_app, route, get, post, template, request, redirect

from dataset_database import get_items, add_item, delete_item, update_item

@route('/')
def get_index():
    redirect('/task2/list/')

@route('/task2/list/')
def get_list():
    items = get_items()
    return template("shopping_list.tpl", name="pvkalyan13", shopping_list=items)

@post('/task2/add/')
def post_add():
    description = request.forms.get("description")
    quantity = request.forms.get("quantity")
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    add_item(description, quantity)
    redirect('/task2/list/')

@route("/task2/delete/<id>")
def get_delete(id):
    delete_item(id)
    redirect('/task2/list/')

@get("/task2/edit/<id>")
def get_edit(id):
    items = get_items(id)
    if len(items) != 1:
        redirect('/task2/list/')
    item_id, description = items[0]['id'], items[0]['description']
    assert item_id == int(id)
    return template("edit_item.tpl", id=id, description=description)

@post("/task2/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    update_item(id, description)
    redirect('/task2/list/')

application = default_app()

