from bottle import default_app, route, get, post, template, request, redirect

from peewee_database import get_items, add_item, delete_item, update_item

@route('/')
def get_index():
    redirect('/task3/list/')

@route('/task3/list/')
def get_list():
    items = get_items()
    return template("shopping_list.tpl", name="pvkalyan13", shopping_list=items)

@post('/task3/add/')
def post_add():
    description = request.forms.get("description")
    # quantity = request.forms.get("quantity")
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    # add_item(description, quantity)
    add_item(description)
    redirect('/task3/list/')

@route("/task3/delete/<id>")
def get_delete(id):
    delete_item(id)
    redirect('/task3/list/')

@get("/task3/edit/<id>")
def get_edit(id):
    items = get_items(id)
    if len(items) != 1:
        redirect('/list')
    item_id, description = items[0]['id'], items[0]['description']
    assert item_id == int(id)
    return template("edit_item.tpl", id=id, description=description)

@post("/task3/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    update_item(id, description)
    redirect('/task3/list/')

application = default_app()

