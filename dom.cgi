#!/opt/local/bin/js 

print("Content-Type: text/html");
print("");

var hoge = "aiueo";

print(

<html>
<head>
<title>{hoge}</title>
</head>
<body>
<h1>{hoge}</h1>
</body>
</html>

);

for (var i in this) {
  print(i + ' : ' + this[i] + "<br>\n");
}

var aa = "aa";