#!/opt/local/bin/js 

load('cgi.js');

print("Content-Type: text/html\n\n");

var cgi = new CGI();

print("<h2>GET Query</h2>");
for(var i in cgi.params.get) print(i + " = " + cgi.params.get[i] + "<br>");

print("<h2>POST Query</h2>");
for(var i in cgi.params.post) print(i + " = " + cgi.params.post[i] + "<br>")

print(
<div>
<h2>GET</h2>
<form action="./jscgi.cgi" method="get">
get1:<input name="get1" type="text" value=""/>
<input type="submit" value="get"/>
</form>
<h2>POST</h2>
<form action="./jscgi.cgi" method="post">
post1:<input name="post1" type="text" value=""/><br/>
post2:<input name="post2" type="text" value=""/>
<input type="submit" value="post"/>
</form>
</div>
);

