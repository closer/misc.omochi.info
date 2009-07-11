#!/opt/local/bin/js 

print("Content-Type: text/html");
print("");

var v = readline().toString();
var a = v.split('&');

print("<p>" + v.length + "</p>");
print("<p>" + v + "</p>");
print("<p>" + a + "</p>");

print(
	
<form action="post.js" method="post">
	<input type="hidden" name="a" value="1"/>
	<input type="text" name="b" value=""/>
	<input type="submit" value="go"/>
</form>	

);