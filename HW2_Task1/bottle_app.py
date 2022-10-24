from bottle import default_app, route, get, post, template, request, redirect

import database

@route('/')
def get_index():
    redirect('/task1/list/')

@route('/task1/list/')
def get_list():
    items = database.get_items()
    return template("shopping_list.tpl", name="pvkalyan13", shopping_list=items)

@post('/task1/add/')
def post_add():
    description = request.forms.get("description")
    database.add_item(description)
    redirect('/task1/list/')

@route("/task1/delete/<id>")
def get_delete(id):
    database.delete_item(id)
    redirect('/task1/list/')

@get("/task1/edit/<id>")
def get_edit(id):
    items = database.get_items(id)
    if len(items) != 1:
        redirect('/task1/list/')
    item_id, description = items[0]['id'], items[0]['desc']
    assert item_id == int(id)
    return template("edit_item.tpl", id=id, description=description)

@post("/task1/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    database.update_item(id, description)
    redirect('/task1/list/')

application = default_app()

