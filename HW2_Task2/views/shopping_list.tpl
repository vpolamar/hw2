<html>
<body>
<h2>Shopping List - Task 2</h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['description'])}}</td>
    <td><a href="/task2/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/task2/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/task2/add/" method="post">
  <p>New item: <input name="description"/></p>
  <p><button type="submit">Submit</button>
</form>
</body>
</html>
