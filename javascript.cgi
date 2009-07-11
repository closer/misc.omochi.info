#!/opt/local/bin/js 

print("Content-Type: text/html");
print("");


// Title
print("<h1>Test</h1>");

// List
print("<ul>");
var array = "One,Two,Three".split(',');
array.forEach(function(i){
  print("<li>" + i + "</li>");
});
print("</ul>");

try {
  if(File.exists('./hoge.as')) {
    print("aruyo");
  } else {
    print("naiyo");
  }
} catch(e) {
  print(e);
}
/*
  var a = new File("./hoge.as");
  a.writeln("hoge.as dayo"); 
  a.close();
*/