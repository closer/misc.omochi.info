#!/opt/local/bin/js 

print("Content-Type: text/html");
print("");

print("<h2>arguments</h2>");
for(var i in arguments) print(i + ' - ' + arguments[i] + "<br>");

print("<h2>environment</h2>")
for(var i in environment) print(i + " - " + environment[i] + "<br>");

print("<h2>Post Form</h2>");
print(
<form action="./arguments.cgi" method="post">
<input type="text" name="arg1" value="" />
<input type="submit" value="send" />
</form>
);

