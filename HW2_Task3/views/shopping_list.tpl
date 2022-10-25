<html>
<body>
<h2>Shopping List - Task 3</h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['description'])}}</td>
    <td><a href="/task3/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/task3/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<form action="/task3/add/" method="post">
  <p>New item: <input name="description"/></p>
  <p><button type="submit">Submit</button>
</form>
</body>
</html>
