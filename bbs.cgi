#!/opt/local/bin/js 

load('./cgi.js');

var logfile = "log.txt";

var cgi = new CGI;

print("Content-Type: text/html\n\n");

if(cgi.params.post['text']) {
  var log = new File(logfile);
  var text = cgi.params.post['text'];
  log.writeln(text);
  log.close();
}

var log = new File(logfile);
log.readAll().forEach(function(line){
  print(line + "<br>");
});
log.close();

print(
<form action="bbs.cgi" method="post">
<input type="text" name="text" value=""/>
<input type="submit" value="SEND"/>
</form>
);

