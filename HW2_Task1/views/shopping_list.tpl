<html>
<body>
<h2>Shopping List - Task 1</h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['desc'])}}</td>
    <td><a href="/task1/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/task1/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/task1/add/" method="post">
  <p>Add new item: <input name="description"/></p>
  <p><button type="submit">Submit</button>
</form>
</body>
</html>
